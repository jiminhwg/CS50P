from twttr import shorten

def main():
    test_shorten()

def test_shorten():
    assert shorten("Twitter") == "Twttr"
    assert shorten("CS50") == "CS50"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("Everyday") == "vrydy"


if __name__ == "__main__":
    main()
