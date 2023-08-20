from numb3rs import validate

def test_validate():
    assert validate("1.0.0.1")==True
    assert validate("255.255.255.255")==True
    assert validate("257.257.257.257")==False
    assert validate("1000.2000.3000.4000")==False
    assert validate("kitty")==False
    assert validate("157.557.557.557")==False