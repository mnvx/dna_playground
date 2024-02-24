def is_dna(s):
    if not s:
        return False
    dna_str_characters = 'ATGCatgc \n'
    if all(c in dna_str_characters for c in s):
        return True
    return False
