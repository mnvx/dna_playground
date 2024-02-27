from collections import OrderedDict


def is_dna(s):
    if not s:
        return False
    dna_str_characters = 'ATGCatgc \n'
    if all(c in dna_str_characters for c in s):
        return True
    return False


def get_frequent_sequences(string, length, threshold=2):
    i = 0
    freq = {}
    while i < len(string) - length:
        sequence = string[i:i + length]
        if sequence in freq.keys():
            freq[sequence] += 1
        else:
            freq[sequence] = 1
        i += 1
    freq_filtered = {k: v for k, v in freq.items() if v >= threshold}
    return OrderedDict(sorted(freq_filtered.items(), key=lambda item: item[1], reverse=True))
