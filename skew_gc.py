from dna import dna, skew, ori

dna_file_name = 'examples/Salmonella_enterica.txt'
# dna_file_name = 'examples/Salmonella_enterica_ATCC_9239.fasta'
# dna_file_name = 'examples/Salmonella_enterica_subsp_enterica_ATCC_39183.fasta'
# dna_file_name = 'examples/Salmonella_enterica_subsp_enterica_ATCC_700931.fasta'
# dna_file_name = 'examples/E_coli.txt'
block_size = 5000
chart_x_points = 20

dna = dna.Dna(dna_file_name)
skews = skew.Skew(dna)
skews.read_skews(block_size)
skews.calc_increasing_diff('G', 'C')
min_indices = skews.find_minimums()

ori = ori.Ori(dna)
ori_res = ori.find_ori(min_indices, block_size)
for ori in ori_res:
    print(ori)

skews.build_chart(chart_x_points, min_indices)

