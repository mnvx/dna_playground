from . import dna
from dna_utils import utils

MIN_BLOCK_SIZE = 500
MAX_BLOCK_SIZE = MIN_BLOCK_SIZE * 2
BLOCK_SIZE_STEP = (MAX_BLOCK_SIZE - MIN_BLOCK_SIZE) / 5
SHIFT_SIZE = 500


class Ori:

    def __init__(self, dna: dna.Dna):
        self._dna = dna

    def find_ori(self, minimums, block_size):
        class BreakIt(Exception):
            pass
        freqs = []
        for i in minimums:

            try:
                ori_len = 14
                while ori_len >= 5:
                    extra_size = 0
                    if block_size < MIN_BLOCK_SIZE:
                        extra_size = int((MIN_BLOCK_SIZE - block_size) / 2)
                    size = block_size + extra_size * 2
                    while size < MAX_BLOCK_SIZE:
                        shift = -SHIFT_SIZE
                        while shift <= SHIFT_SIZE:
                            dna = self._dna.as_string(i - extra_size + shift, i + block_size + extra_size + shift)
                            freq = utils.get_frequent_sequences(dna, ori_len, 3)
                            if len(freq.items()) != 0:
                                freqs.append({
                                    'position': [i - extra_size + shift, i + block_size + extra_size + shift],
                                    'sequence': freq,
                                })
                                print(i - extra_size, i + block_size + extra_size)
                                raise BreakIt
                            shift += max(1, int(SHIFT_SIZE/50))
                        extra_size += int(BLOCK_SIZE_STEP / 2)
                        size = block_size + extra_size * 2
                    ori_len -= 1
            except BreakIt:
                pass

        print(self._dna.as_string(151913, 151913 + 9))
        print(self._dna.as_string(152013, 152013 + 9))
        print(self._dna.as_string(152394, 152394 + 9))
        return freqs
