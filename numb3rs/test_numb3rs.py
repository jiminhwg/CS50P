from numb3rs import validate

def main():
    test_validate()

def test_validate():
    assert validate("255.255.255.255") == True
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
    assert validate("127.0.0.1") == True
    assert validate("512.512.512.512") == False
    assert validate("20.30") == False
    assert validate("30.30.30.30.30") == False
    assert validate("30") == False
    assert validate("30.500.400.500") == False
    assert validate("300.12.123.123") == False

if __name__ == "__main__":
    main()
