import matplotlib.pyplot as plt
import numpy as np
import math
from dna_utils import utils

DEFAULT_SYMBOL_1 = 'G'
DEFAULT_SYMBOL_2 = 'C'


class Skew:

    def __init__(self, dna_file):
        self._dna_file = dna_file
        self._skews = []
        self._increasing_diff = []
        self._block_size = 0

    def read_skews(self, block_size):
        class BreakIt(Exception):
            pass

        self._skews = []
        self._block_size = block_size

        i = 0
        with open(self._dna_file, 'r') as f:
            try:
                while True:
                    dna = f.readline()
                    if not dna:
                        # eof
                        break
                    if not utils.is_dna(dna):
                        # wrong line format
                        continue

                    for j in range(len(dna)):
                        symbol = dna[j].upper()
                        if symbol not in ['C', 'G', 'T', 'A']:
                            continue

                        block = int(i / self._block_size)

                        if len(self._skews) < block + 1:
                            self._skews.append({
                                'G': 0,
                                'C': 0,
                                'T': 0,
                                'A': 0,
                            })

                        self._skews[block][symbol] += 1
                        i += 1
            except BreakIt:
                pass

        return self._skews

    def calc_increasing_diff(self, symbol1=DEFAULT_SYMBOL_1, symbol2=DEFAULT_SYMBOL_2):
        s1 = symbol1.upper()
        s2 = symbol2.upper()
        self._increasing_diff = [0]
        for k, v in enumerate(self._skews):
            if k > 0:
                self._increasing_diff.append(self._increasing_diff[k - 1] + v[s1] - v[s2])
            else:
                self._increasing_diff[k] = v[s1] - v[s2]
        return self._increasing_diff

    def build_chart(self, chart_x_points_count, min_indices):
        xpoints = np.array([k * self._block_size for k, _ in enumerate(self._increasing_diff)])
        ypoints = np.array(self._increasing_diff)

        min_xpoints = np.array([k * self._block_size for k in min_indices])
        min_ypoints = np.array([self._increasing_diff[k] for k in min_indices])

        m = max(xpoints) - min(xpoints)
        step = 10**int(math.log10(int(m / chart_x_points_count)))
        step *= int(m / step / chart_x_points_count)
        plt.plot(xpoints, ypoints)
        plt.plot(min_xpoints, min_ypoints, 'x')
        plt.xticks(np.arange(min(xpoints), max(xpoints), step))
        plt.show()

    def find_minimums(self, sensitivity: float = 0.01):
        """
        :param sensitivity: from 0 to 1
        :return:
        """
        if not self._increasing_diff:
            return []

        band = max(self._increasing_diff) - min(self._increasing_diff)
        sensitivity_size = band * sensitivity

        # all minimums
        min_indices = []
        for i in range(1, len(self._increasing_diff)-1):
            v = self._increasing_diff[i]
            if v <= self._increasing_diff[i-1] and v <= self._increasing_diff[i+1]:
                is_min = True

                # only sensitive minimums
                class BreakIt(Exception):
                    pass

                try:
                    j = i - 1
                    while abs(v - self._increasing_diff[j]) < sensitivity_size and j >= 0:
                        if v > self._increasing_diff[j]:
                            is_min = False
                            raise BreakIt
                        j -= 1

                    j = i + 1
                    while abs(v - self._increasing_diff[j]) < sensitivity_size and j < len(self._increasing_diff):
                        if v > self._increasing_diff[j]:
                            is_min = False
                            raise BreakIt
                        j += 1
                except BreakIt:
                    pass

                if is_min:
                    min_indices.append(i)

        return min_indices
