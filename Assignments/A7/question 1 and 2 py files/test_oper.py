import oper
import pytest

def test_oper():
    assert oper.operate(1, 3, "+") == 4, "failed on addition"
    assert oper.operate(1, 3, "-") == -2, "failed on subtraction"
    assert oper.operate(1, 3, "*") == 3, "failed on multiplication"
    assert oper.operate(1, 3, "/") == 1/3, "failed on division"
    with pytest.raises(TypeError) as excinfo1:
        oper.operate(1, 3, 4)
    assert excinfo1.value.args[0] == "oper must be a string"
    with pytest.raises(ZeroDivisionError) as excinfo2:
        oper.operate(1, 0, "/")
    assert excinfo2.value.args[0] == "division by zero is undefined"
    with pytest.raises(ValueError) as excinfo3:
        oper.operate(1, 3, ">")
    assert excinfo3.value.args[0] == "oper must be one of '+', '/', '-', or '*'"