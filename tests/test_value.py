from micrograd.nn import Value  # Assuming the class is in a module named value_module


def test_value_initialization():
    v = Value(5)
    assert v.data == 5

    v = Value(3.14)
    assert v.data == 3.14


def test_addition():
    v1 = Value(5)
    v2 = Value(3)
    result = v1 + v2
    assert result.data == 8

    result = v1 + 2
    assert result.data == 7

    result = 2 + v1
    assert result.data == 7


def test_subtraction():
    v1 = Value(5)
    v2 = Value(3)
    result = v1 - v2
    assert result.data == 2

    result = v1 - 2
    assert result.data == 3

    result = 7 - v1
    assert result.data == 2


def test_multiplication():
    v1 = Value(5)
    v2 = Value(3)
    result = v1 * v2
    assert result.data == 15

    result = v1 * 2
    assert result.data == 10

    result = 2 * v1
    assert result.data == 10


def test_division():
    v1 = Value(6)
    v2 = Value(3)
    result = v1 / v2
    assert result.data == 2

    result = v1 / 2
    assert result.data == 3

    result = 12 / v1
    assert result.data == 2


def test_exponentiation():
    v = Value(2)
    result = v**3
    assert result.data == 8


def test_inplace_addition():
    v = Value(5)
    v += 3
    assert v.data == 8

    v += Value(2)
    assert v.data == 10


def test_inplace_subtraction():
    v = Value(5)
    v -= 3
    assert v.data == 2

    v -= Value(2)
    assert v.data == 0


def test_inplace_multiplication():
    v = Value(5)
    v *= 3
    assert v.data == 15

    v *= Value(2)
    assert v.data == 30


def test_inplace_division():
    v = Value(6)
    v /= 3
    assert v.data == 2

    v /= Value(2)
    assert v.data == 1


def test_relu():
    v = Value(-5)
    result = v.relu()
    assert result.data == 0

    v = Value(5)
    result = v.relu()
    assert result.data == 5


def test_repr():
    v = Value(5)
    assert repr(v) == "Value(5)"

    v = Value(3.14)
    assert repr(v) == "Value(3.14)"
