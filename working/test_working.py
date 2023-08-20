from working import convert
import pytest

def test_convert():
    assert convert("9 AM to 5 PM")=="09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM")=="09:00 to 17:00"
    assert convert("9 PM to 5 AM")=="21:00 to 05:00"
    assert convert("9:30 AM to 5:30 PM")=="09:30 to 17:30"

def test_valid_type():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("13 AM to 20 PM")