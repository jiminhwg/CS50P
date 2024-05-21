from working import convert
import pytest

def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 PM to 5 AM") == "21:00 to 05:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    with pytest.raises(ValueError): #https://docs.pytest.org/en/7.1.x/how-to/assert.html
        assert convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        assert convert("9:00 to 10:00")
    with pytest.raises(ValueError):
        assert convert("10:00 PM to 17:00")
    with pytest.raises(ValueError):
        assert convert("14 AM to 15 PM")
    with pytest.raises(ValueError):
        assert convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        assert convert("9:00 AM 4:00 PM")
