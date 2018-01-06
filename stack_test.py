"""Simple tests for the simple stack language."""

import simpleStack


def test_hello_world():
    """Tests hello world."""
    logs = []

    def log_print(val, end=""):
        """Logging print statement."""
        logs.append(val + end)

    with open("examples/hello.ss") as hello:
        simpleStack.run_simple_stack(hello.readlines(), printFun=log_print)

    assert logs[0] == "Hello"
    assert logs[1] == " World!\n"


def test_fizz_buzz():
    """Test fizz buzz."""
    logs = []

    def log_print(val, end=""):
        """Logging print statement. Ignores plain newlines."""
        if (str(val) + end) == "\n":
            return
        logs.append(str(val) + end)

    with open("examples/fizzbuzz.ss") as fizzbuzz:
        simpleStack.run_simple_stack(fizzbuzz.readlines(), printFun=log_print)

    assert(len(logs)) == 100

    for idx, line in enumerate(logs):
        num = idx + 1
        if num % 3 == 0:
            assert "Fizz" in line
        if num % 5 == 0:
            assert "Buzz" in line
        if (num % 3 != 0) and (num % 5 != 0):
            assert str(num) in line
