from seasons import get_date
import pytest

def test_get_date():
    assert get_date("2000-01-01") == "Twelve million, twenty-six thousand, eight hundred eighty minutes"
    



