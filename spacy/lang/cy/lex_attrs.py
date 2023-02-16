from ...attrs import LIKE_NUM

# Angen deall sut i drin rhifau aml-air
# Angen rhifau benywaidd
_num_words = (
    'sero', 'un', 'dau', 'tree', 'pedwar', 'pump', 'chwech', 'saith',
    'wyth', 'naw', 'deg', 'deuddeg', 'pymtheg', 'deunaw', 'ugain',
    'deugain', 'trigain',
    'can', 'cant', 'mil', 'miliwn', 'biliwn', 'triliwn', 'cwadriliwn',
    'gajiliwn', 'basiliwn')


def like_num(text):
    text = text.replace(',', '').replace('.', '')
    if text.isdigit():
        return True
    if text.count('/') == 1:
        (num, denom) = text.split('/')
        if num.isdigit() and denom.isdigit():
            return True
    return text in _num_words


LEX_ATTRS = {
    LIKE_NUM: like_num
}
