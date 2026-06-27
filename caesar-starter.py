# ============================================================
# TESTING FRAMEWORK
# ============================================================

def run_tests(tests):
    passed = 0
    for description, run_case, expected in tests:
        try:
            actual = run_case()
        except Exception as error:
            print(f"FAIL: {description}")
            print(f"      crashed with: {error}")
            continue
        if actual == expected:
            print(f"PASS: {description}")
            passed += 1
        else:
            print(f"FAIL: {description}")
            print(f"      expected: {expected!r}")
            print(f"      got:      {actual!r}")
    print(f"\n{passed}/{len(tests)} tests passed")


# ============================================================
# TEST CASES
# ============================================================

shift_letter_tests = [
    ("'a' shifted by 1 should give 'b'",               lambda: shift_letter('a', 1),  'b'),
    ("'z' shifted by 1 should wrap to 'a'",             lambda: shift_letter('z', 1),  'a'),
    ("'a' shifted by -1 should wrap to 'z'",            lambda: shift_letter('a', -1), 'z'),
    ("'Z' shifted by 1 should wrap to 'A' (case kept)", lambda: shift_letter('Z', 1),  'A'),
    ("'a' shifted by 0 should stay 'a'",                lambda: shift_letter('a', 0),  'a'),
    ("'a' shifted by 26 should return to 'a'",          lambda: shift_letter('a', 26), 'a'),
    ("'a' shifted by 27 should behave like shift 1",    lambda: shift_letter('a', 27), 'b'),
]

is_letter_tests = [
    ("lowercase letter",        lambda: is_letter("a"), True),
    ("uppercase letter",        lambda: is_letter("A"), True),
    ("last lowercase letter",   lambda: is_letter("z"), True),
    ("last uppercase letter",   lambda: is_letter("Z"), True),
    ("digit",                   lambda: is_letter("5"), False),
    ("space",                   lambda: is_letter(" "), False),
    ("punctuation",             lambda: is_letter("!"), False),
]

shift_string_tests = [
    ("lowercase word shifts correctly",  lambda: shift_string("abc", 1),        "bcd"),
    ("uppercase is preserved",           lambda: shift_string("ABC", 1),        "BCD"),
    ("wraps at the end of the alphabet", lambda: shift_string("xyz", 1),        "yza"),
    ("non-letters are left unchanged",   lambda: shift_string("Hi, World!", 0), "Hi, World!"),
    ("spaces pass through untouched",    lambda: shift_string("ab cd", 1),      "bc de"),
    ("negative shift moves backwards",   lambda: shift_string("bcd", -1),       "abc"),
]

encrypt_tests = [
    ("encrypt shifts forward by the given amount", lambda: encrypt("abc", 1),    "bcd"),
    ("encrypt wraps correctly",                    lambda: encrypt("xyz", 2),    "zab"),
    ("encrypting by 0 leaves text unchanged",      lambda: encrypt("hello", 0),  "hello"),
]

decrypt_tests = [
    ("decrypt shifts backwards by the given amount",   lambda: decrypt("bcd", 1),                      "abc"),
    ("decrypt undoes a matching encrypt (round trip)", lambda: decrypt(encrypt("hello world", 7), 7),  "hello world"),
    ("decrypting by 0 leaves text unchanged",          lambda: decrypt("hello", 0),                    "hello"),
]


# ============================================================
# SUBPROGRAMS
# ============================================================



# ============================================================
# MAIN PROGRAM
# ============================================================
