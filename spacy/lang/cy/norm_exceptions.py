# coding: utf8

_exc = {
    # Slang and abbreviations
    # (arbrofi)
    "isho": "eisiau",
    "isio": "eisiau",
    "moen": "moyn",
    "moin": "moyn",
    "pobol": "pobl",

    # Standard variations
    "ydi": "ydy",
    "eisoes": "eisoes",

    # Dehwntify
    "clou" : "cyflym",
    "glou" : "gyflym",
    "fe" : "fo",
    "e" : "o"

}


NORM_EXCEPTIONS = {}

for (string, norm) in _exc.items():
    NORM_EXCEPTIONS[string] = norm
    NORM_EXCEPTIONS[string.title()] = norm
