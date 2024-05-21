from fuel import convert, gauge
import pytest

def main():
    test_convert()
    test_gauge()


def test_convert():
    assert convert("1/2") == 50
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ZeroDivisionError):
        convert("4/0")


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"


if __name__ == "__main__":
    main()