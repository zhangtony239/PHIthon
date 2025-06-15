import gc
import types
from typing import Any, Dict

# --- Cycle Detection Implementation (Remains the same) ---

def check_for_cycles(start_obj: Any):
    # We use a raw id-based path to avoid any magic from __eq__ or __hash__
    path = dict() 
    cycle = _find_cycle_dfs(start_obj, path)
    if cycle:
        try:
            # Attempt to create a readable representation of the cycle path
            path_repr = " -> ".join(repr(p) for p in cycle)
        except Exception:
            path_repr = "Un-representable objects in cycle path"
        raise RecursionError(
            f"A circular reference was detected: {path_repr}"
        )

_IGNORE_TYPES = (
    types.BuiltinFunctionType, types.FunctionType, types.ModuleType,
    types.MethodType, type, str, int, float, bool, tuple,
)

def _find_cycle_dfs(current_obj: Any, path: Dict[int, Any]):
    obj_id = id(current_obj)
    
    # Use type() for direct comparison to avoid overridden isinstance behavior
    if type(current_obj) in _IGNORE_TYPES:
        return None

    if obj_id in path:
        # Cycle detected. Reconstruct the path of the cycle.
        path_list = list(path.values())
        try:
            cycle_start_index = path_list.index(current_obj)
            return path_list[cycle_start_index:] + [current_obj]
        except ValueError:
            # Should not happen if logic is correct, but as a fallback
            return path_list + [current_obj]

    path[obj_id] = current_obj
    
    # gc.get_referents() is the core of the traversal.
    # It finds all objects directly referred to by current_obj.
    for referent in gc.get_referents(current_obj):
        # We must ignore the path dictionary itself to avoid self-reference cycles
        if id(referent) == id(path):
            continue
        
        cycle = _find_cycle_dfs(referent, path)
        if cycle:
            return cycle # Propagate the found cycle up the call stack
            
    # Backtrack: remove current object from path before returning
    del path[obj_id]
    return None


# --- The "var" Factory ---

_created_classes = {}

def var(value: Any) -> Any:
    """
    A factory function that takes a value and returns a new object of the same
    base type (e.g., list, dict) but with added cycle-detection capabilities.
    """
    if isinstance(value, tuple(_IGNORE_TYPES)):
        # Immutable types cannot have cycles introduced, so we return them directly.
        return value

    original_class = value.__class__
    # We cache the dynamically created classes to avoid creating them repeatedly.
    if original_class in _created_classes:
        checked_class = _created_classes[original_class]
        return checked_class(value)

    # 1. Define the Mixin with the checking logic
    class CycleCheckerMixin:
        def __setattr__(self, name, attr_value):
            # Set the attribute first
            super().__setattr__(name, attr_value)
            # Then check for cycles
            check_for_cycles(self)

        def __setitem__(self, key, item_value):
            # Set the item first
            super().__setitem__(key, item_value)
            # Then check
            check_for_cycles(self)

    # 2. Dynamically create the new class by inheriting from the original and the mixin
    # The name is for better debugging and introspection.
    class_name = f"Checked{original_class.__name__}"
    
    # Ensure the mixin's methods are first in the MRO (Method Resolution Order)
    # This is crucial for our __setattr__ to be called.
    checked_class = type(class_name, (CycleCheckerMixin, original_class), {})
    
    _created_classes[original_class] = checked_class

    # 3. Instantiate the new class with the provided value and return it.
    return checked_class(value)