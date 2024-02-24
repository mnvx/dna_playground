import matplotlib.pyplot as plt
import numpy as np
import math
from dna_utils import utils

dna_file_name = 'examples/Salmonella_enterica.txt'
# dna_file_name = 'examples/Salmonella_enterica_ATCC_9239.fasta'
# dna_file_name = 'examples/Salmonella_enterica_subsp_enterica_ATCC_39183.fasta'
# dna_file_name = 'examples/Salmonella_enterica_subsp_enterica_ATCC_700931.fasta'
# dna_file_name = 'examples/E_coli.txt'
block_size = 5000
chart_x_points = 20


def read_skews(dna_file, block_size):
    class BreakIt(Exception):
        pass

    skews = []

    i = 0
    with open(dna_file, 'r') as f:
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

                    block = int(i / block_size)

                    if len(skews) < block + 1:
                        skews.append({
                            'G': 0,
                            'C': 0,
                            'T': 0,
                            'A': 0,
                        })

                    skews[block][symbol] += 1
                    i += 1
        except BreakIt:
            pass
    print(i)

    return skews


def calc_incr(skews):
    incr = [0]
    # incr = [v['G'] - v['C'] + incr[k-1] - incr[k-1] for k, v in enumerate(skews[1:-1])]
    for k, v in enumerate(skews):
        if k > 0:
            incr.append(incr[k-1] + v['G'] - v['C'])
    return incr


def build_chart(incr, block_size, chart_x_points):
    xpoints = np.array([k * block_size for k, _ in enumerate(incr)])
    # ypoints = np.array([v['G'] - v['C'] + skews[k-1]['G'] - skews[k-1]['C'] for k, v in enumerate(skews[1:-1])])
    ypoints = np.array(incr)
    m = max(xpoints) - min(xpoints)
    step = 10**int(math.log10(int(m / chart_x_points)))
    step *= int(m / step / chart_x_points)
    plt.plot(xpoints, ypoints)
    plt.xticks(np.arange(min(xpoints), max(xpoints), step))
    plt.show()


skews = read_skews(dna_file_name, block_size)
incr = calc_incr(skews)
build_chart(incr, block_size, chart_x_points)
