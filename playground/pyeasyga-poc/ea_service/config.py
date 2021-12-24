import string

EXPECTED_RESULT = [c for c in "hello world"]
LETTERS = list(string.ascii_lowercase) + \
    list(string.whitespace)  # list(string.printable)
