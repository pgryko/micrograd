from typing import Union


class Value:
    def __init__(self, data: Union[float, int]) -> None:
        """
        Initialize a new Value instance.

        Args:
            data (float): The numeric value to be wrapped.
        """
        self.data = data

    def __add__(self, other: Union["Value", float, int]) -> "Value":
        """
        Add another Value instance or a numeric value to this instance.

        Args:
            other (Value or float): The value to add.

        Returns:
            Value: The result of the addition.
        """
        if isinstance(other, Value):
            return Value(self.data + other.data)
        return Value(self.data + other)

    def __radd__(self, other: float) -> "Value":
        """
        Add this instance to another value (right-hand addition).

        Args:
            other (float): The value to add.

        Returns:
            Value: The result of the addition.
        """
        return self.__add__(other)

    def __sub__(self, other: Union["Value", float, int]) -> "Value":
        """
        Subtract another Value instance or a numeric value from this instance.

        Args:
            other (Value or float): The value to subtract.

        Returns:
            Value: The result of the subtraction.
        """
        if isinstance(other, Value):
            return Value(self.data - other.data)
        return Value(self.data - other)

    def __rsub__(self, other: float) -> "Value":
        """
        Subtract this instance from another value (right-hand subtraction).

        Args:
            other (float): The value to subtract from.

        Returns:
            Value: The result of the subtraction.
        """
        if isinstance(other, Value):
            return Value(other.data - self.data)
        return Value(other - self.data)

    def __mul__(self, other: Union["Value", float, int]) -> "Value":
        """
        Multiply this instance by another Value instance or a numeric value.

        Args:
            other (Value or float): The value to multiply by.

        Returns:
            Value: The result of the multiplication.
        """
        if isinstance(other, Value):
            return Value(self.data * other.data)
        return Value(self.data * other)

    def __rmul__(self, other: float) -> "Value":
        """
        Multiply another value by this instance (right-hand multiplication).

        Args:
            other (float): The value to multiply by.

        Returns:
            Value: The result of the multiplication.
        """
        return self.__mul__(other)

    def __truediv__(self, other: Union["Value", float, int]) -> "Value":
        """
        Divide this instance by another Value instance or a numeric value.

        Args:
            other (Value or float): The value to divide by.

        Returns:
            Value: The result of the division.
        """
        if isinstance(other, Value):
            return Value(self.data / other.data)
        return Value(self.data / other)

    def __rtruediv__(self, other: float) -> "Value":
        """
        Divide another value by this instance (right-hand division).

        Args:
            other (float): The value to divide.

        Returns:
            Value: The result of the division.
        """
        if isinstance(other, Value):
            return Value(other.data / self.data)
        return Value(other / self.data)

    def __pow__(self, power: float, modulo: int = None) -> "Value":
        """
        Raise this instance to the power of another value.

        Args:
            power (float): The power to raise to.

        Returns:
            Value: The result of the exponentiation.
        """
        return Value(self.data**power)

    def __iadd__(self, other: Union["Value", float, int]) -> "Value":
        """
        In-place addition of another Value instance or a numeric value.

        Args:
            other (Value or float): The value to add.

        Returns:
            Value: This instance after the addition.
        """
        if isinstance(other, Value):
            self.data += other.data
        else:
            self.data += other
        return self

    def __isub__(self, other: Union["Value", float, int]) -> "Value":
        """
        In-place subtraction of another Value instance or a numeric value.

        Args:
            other (Value or float): The value to subtract.

        Returns:
            Value: This instance after the subtraction.
        """
        if isinstance(other, Value):
            self.data -= other.data
        else:
            self.data -= other
        return self

    def __imul__(self, other: Union["Value", float, int]) -> "Value":
        """
        In-place multiplication by another Value instance or a numeric value.

        Args:
            other (Value or float): The value to multiply by.

        Returns:
            Value: This instance after the multiplication.
        """
        if isinstance(other, Value):
            self.data *= other.data
        else:
            self.data *= other
        return self

    def __itruediv__(self, other: Union["Value", float, int]) -> "Value":
        """
        In-place division by another Value instance or a numeric value.

        Args:
            other (Value or float): The value to divide by.

        Returns:
            Value: This instance after the division.
        """
        if isinstance(other, Value):
            self.data /= other.data
        else:
            self.data /= other
        return self

    def relu(self) -> "Value":
        """
        Apply the ReLU (Rectified Linear Unit) operation.

        Returns:
            Value: The result of applying ReLU.
        """
        return Value(max(0, self.data))

    def __repr__(self) -> str:
        """
        Return a string representation of the Value instance.

        Returns:
            str: String representation of the instance.
        """
        return f"Value({self.data})"
