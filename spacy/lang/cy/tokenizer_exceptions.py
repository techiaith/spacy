# encoding: utf8
from typing import Dict, List

from ..tokenizer_exceptions import BASE_EXCEPTIONS
from ...util import update_exc
from ...symbols import ORTH, NORM


_exc: Dict[str, List[Dict]] = {}

_exc_datums = [
    {ORTH: "tua.", NORM: "tua"},
    {ORTH: "ion.", NORM: "ionawr"},
    {ORTH: "chw.", NORM: "chwefror"},
    {ORTH: "abr.", NORM: "abrill"},
    {ORTH: "maw.", NORM: "mawrth"},
    {ORTH: "mai.", NORM: "mai"},
    {ORTH: "meh.", NORM: "mehefin"},
    {ORTH: "gor.", NORM: "gorffenaf"},
    {ORTH: "aw.", NORM: "awst"},
    {ORTH: "med.", NORM: "medi"},
    {ORTH: "hyd.", NORM: "hydref"},
    {ORTH: "tac.", NORM: "tachwedd"},
    {ORTH: "rha.", NORM: "rhagfyr"},
    {ORTH: "St.", NORM: "Sant"},
    {ORTH: "dr.", NORM: "doctor"},
    {ORTH: "Sen.", NORM: "Senedd"},
    {ORTH: "a.", NORM: "ac"},
    {ORTH: "e.", NORM: "er"},
    {ORTH: "y.", NORM: "y"},
    {ORTH: "y.", NORM: "yn"},
    {ORTH: "y.", NORM: "yw"},
]

for exc_data in _exc_datums:
    _exc[exc_data[ORTH]] = [exc_data]


for pron in ["fi", "ti", "e", "fe", "hi", "ni", "chi", "chdi", "nhw"]:
    for orth in [pron, pron.title()]:
        _exc[orth + "'n"] = [
            {ORTH: orth, NORM: pron},
            {ORTH: "'n", NORM: ""}
        ]



# Times

for h in range(1, 12 + 1):
    for period in ["y.b.", "yb"]:
        _exc[f"{h}{period}"] = [
            {ORTH: f"{h}"},
            {ORTH: period, NORM: "y.b."},
        ]
    for period in ["p.m.", "pm"]:
        _exc[f"{h}{period}"] = [
            {ORTH: f"{h}"},
            {ORTH: period, NORM: "y.p."},
        ]

_orth_datums = [
    "A.C.",
    "A.S.",
    "A.S.E.",
    "a.y.b",
    "a.y.y.b",
    "Bnr.", # Mr. 
    "Bns.", # Mrs.
    "Cyf.",
    "yb.",
    "yp."
    "Parch.",
    "c'ath",
    "e.e",
    "g'ath",
    "h.y.",
]

for orth in _orth_datums:
    _exc[orth] = [{ORTH: orth}]

TOKENIZER_EXCEPTIONS = update_exc(BASE_EXCEPTIONS, _exc)
