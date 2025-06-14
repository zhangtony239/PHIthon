import math

class pyrange:
    """
    A range-like object that uses 1-based indexing and inclusive stops.
    It supports start, stop, and step arguments.
    pyrange(stop) -> 1, 2, ..., stop
    pyrange(start, stop) -> start, start + 1, ..., stop
    pyrange(start, stop, step) -> start, start + step, ..., stop
    """
    def __init__(self, *args):
        if len(args) == 1:
            self.start = 1
            self.stop = args[0]
            self.step = 1
        elif len(args) == 2:
            self.start = args[0]
            self.stop = args[1]
            self.step = 1
        elif len(args) == 3:
            self.start = args[0]
            self.stop = args[1]
            self.step = args[2]
        else:
            raise TypeError(f"pyrange expected at most 3 arguments, got {len(args)}")

        if self.step == 0:
            raise ValueError("pyrange() arg 3 must not be zero")

        self._len = self._calculate_len()

    def _calculate_len(self):
        """Calculates the length of the range."""
        if self.step > 0 and self.start > self.stop:
            return 0
        if self.step < 0 and self.start < self.stop:
            return 0
        return (self.stop - self.start) // self.step + 1

    def __len__(self):
        """Return the number of items in the range."""
        return self._len

    def __getitem__(self, index):
        """Return item at 1-based index `index`."""
        if not isinstance(index, int):
            raise TypeError("range indices must be integers")
        
        if index == 0:
            raise IndexError("pyrange object index cannot be zero in 1-based system")

        if index < 0:
            # Convert negative index to positive 1-based index
            # -1 is the last element, -2 is the second to last, etc.
            index = self._len + index + 1

        if not (1 <= index <= self._len):
            raise IndexError("pyrange object index out of range")
        
        return self.start + (index - 1) * self.step

    def __iter__(self):
        self._count = 0
        return self

    def __next__(self):
        if self._count < self._len:
            result = self.start + self._count * self.step
            self._count += 1
            return result
        else:
            raise StopIteration

    def __repr__(self):
        if self.step == 1:
            return f"pyrange({self.start}, {self.stop})"
        return f"pyrange({self.start}, {self.stop}, {self.step})"

    def __contains__(self, value):
        """Return True if `value` is in the range."""
        if not isinstance(value, int):
            return False
        
        # Check if value is within the start/stop bounds
        if self.step > 0 and (value < self.start or value > self.stop):
            return False
        if self.step < 0 and (value > self.start or value < self.stop):
            return False
            
        # Check if value is on a valid step
        return (value - self.start) % self.step == 0