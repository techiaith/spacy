from typing import List, Tuple

from ...pipeline import Lemmatizer
from ...tokens import Token


class WelshLemmatizer(Lemmatizer):
    @classmethod
    def get_lookups_config(cls, mode: str) -> Tuple[List[str], List[str]]:
        if mode == "lookup":
            required = [
                "lemma_lookup_adj",
                "lemma_lookup_adp",
                "lemma_lookup_adv",
                "lemma_lookup_aux",
                "lemma_lookup_det",
                "lemma_lookup_noun",
                "lemma_lookup_num",
                "lemma_lookup_pron",
                "lemma_lookup_propn",
                "lemma_lookup_verb",
                # "lemma_lookup_other",
                # "lemma_lookup",
            ]
            return (required, [])
        else:
            return super().get_lookups_config(mode)

    def lookup_lemmatize(self, token: Token) -> List[str]:
        string = token.text
        univ_pos = token.tag_
        lookup_pos = univ_pos.lower()
        lookup_table = self.lookups.get_table("lemma_lookup_" + lookup_pos, {})
        if univ_pos == "NOUN":
            lemma = self.lemmatize_noun(string, univ_pos, lookup_table)
        else:
            if univ_pos != "PROPN":
                string = string.lower()
            if univ_pos in {"DET", "PRON", "ADP", "ADJ"}:
                lemma = lookup_table.get(string, string)
            else:
                lemma = lookup_table.get(string, "")
        if not lemma:
            lemma = token.text
        return [lemma]
