from . import dna
from dna_utils import utils

MIN_BLOCK_SIZE = 5000
MAX_BLOCK_SIZE = MIN_BLOCK_SIZE * 2
BLOCK_SIZE_STEP = (MAX_BLOCK_SIZE - MIN_BLOCK_SIZE) / 5


class Ori:

    def __init__(self, dna: dna.Dna):
        self._dna = dna

    def find_ori(self, minimums, block_size):
        class BreakIt(Exception):
            pass
        freqs = []
        for i in minimums:
            extra_size = 0
            if block_size < MIN_BLOCK_SIZE:
                extra_size = int((MIN_BLOCK_SIZE - block_size) / 2)
            size = block_size + extra_size*2

            try:
                while size < MAX_BLOCK_SIZE:
                    dna = self._dna.as_string(i - extra_size, i + block_size + extra_size)
                    ori_len = 14
                    while ori_len >= 5:
                        freq = utils.get_frequent_sequences(dna, ori_len, 3)
                        if len(freq.items()) != 0:
                            freqs.append(freq)
                            raise BreakIt
                        ori_len -= 1
                    extra_size += int(BLOCK_SIZE_STEP/2)
                    size = block_size + extra_size*2
            except BreakIt:
                pass

        return freqs
