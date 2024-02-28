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
        compliment = get_compliment(sequence)
        if compliment in freq.keys():
            freq[compliment] += 1
        else:
            freq[compliment] = 1
        i += 1
    freq_filtered = {k: v for k, v in freq.items() if v >= threshold}
    return OrderedDict(sorted(freq_filtered.items(), key=lambda item: item[1], reverse=True))


def get_compliment(string):
    if string == '':
        return ''

    s = []
    i = len(string) - 1
    while i >= 0:
        symbol = string[i]
        if symbol == 'A':
            s.append('T')
        elif symbol == 'T':
            s.append('A')
        elif symbol == 'G':
            s.append('C')
        elif symbol == 'C':
            s.append('G')
        else:
            s.append('A')
        i -= 1
    return "".join(s)