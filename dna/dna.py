from dna_utils import utils

NT_A = 'A'
NT_T = 'T'
NT_C = 'C'
NT_G = 'G'
NT_U = 'U'
NUCLEOTIDES = [NT_A, NT_T, NT_C, NT_G, NT_U]


class Dna:

    def __init__(self, dna_file):
        self._dna_file = dna_file
        self._dna = ""
        self._read_dna()

    def _read_dna(self):
        class BreakIt(Exception):
            pass

        self._dna = ''

        with open(self._dna_file, 'r') as f:
            strs = []
            try:
                while True:
                    dna = f.readline()
                    if not dna:
                        # eof
                        break
                    if not utils.is_dna(dna):
                        # wrong line format
                        continue

                    s = []
                    for j in range(len(dna)):
                        symbol = dna[j].upper()
                        if symbol not in NUCLEOTIDES:
                            continue
                        s.append(symbol)
                    strs.append("".join(s))
            except BreakIt:
                pass
        self._dna += "".join(strs)

    def as_string(self, start: int = None, end: int = None) -> str:
        if start is None and end is None:
            return self._dna
        _start = start if start is not None else 0
        _end = end if end is not None else len(self._dna)
        return self._dna[max(0, _start): min(_end, len(self._dna))]
