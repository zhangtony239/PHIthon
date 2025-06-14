class pylist:
    def __init__(self, items=None):
        self._data = list(items) if items else []

    def append(self, item):
        self._data.append(item)

    def index(self, value, start=1, end=None):
        """
        Returns the 1-based index of the first occurrence of a value.
        Raises ValueError if the value is not present.
        """
        start_0_based = start - 1
        if end is not None:
            return self._data.index(value, start_0_based, end) + 1
        else:
            return self._data.index(value, start_0_based) + 1

    def pop(self, index=None):
        """
        Removes and returns the item at the given 1-based index.
        If index is not specified, removes and returns the last item in the list.
        """
        if index is None:
            return self._data.pop()
        else:
            if not 1 <= index <= len(self._data):
                raise IndexError("pylist index out of range")
            return self._data.pop(index - 1)

    def insert(self, index, item):
        """Inserts an item at a given 1-based index."""
        if not 1 <= index <= len(self._data) + 1:
            raise IndexError("pylist index out of range")
        self._data.insert(index - 1, item)

    def remove(self, value):
        """Removes the first occurrence of a value."""
        self._data.remove(value)

    def count(self, value):
        """Returns the number of occurrences of a value."""
        return self._data.count(value)

    def __getitem__(self, index):
        return self._data[index-1]

    def __setitem__(self, index, value):
        self._data[index-1] = value

    def __iter__(self):
        return iter(self._data)

    def sort(self, *, key=None, reverse=False):
        """Sorts the list in-place."""
        self._data.sort(key=key, reverse=reverse)

    def reverse(self):
        """Reverses the list in-place."""
        self._data.reverse()

    def clear(self):
        """Removes all items from the list."""
        self._data.clear()

    def copy(self):
        """Returns a shallow copy of the list."""
        return pylist(self._data.copy())

    def __len__(self):
        return len(self._data)