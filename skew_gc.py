from dna import dna, skew, ori

# dna_file_name = 'examples/Salmonella_enterica.txt'
# dna_file_name = 'examples/Salmonella_enterica_ATCC_9239.fasta'
# dna_file_name = 'examples/Salmonella_enterica_subsp_enterica_ATCC_39183.fasta'
# dna_file_name = 'examples/Salmonella_enterica_subsp_enterica_ATCC_700931.fasta'
# dna_file_name = 'examples/Avian_coronavirus_ATCC_VR_841.fasta'
# dna_file_name = 'examples/E_coli.txt'
# dna_file_name = 'examples/Vibrio_cholerae_ATCC_14035.fasta'
dna_file_name = 'examples/Vibrio_cholerae.txt'

block_size = 500
chart_x_points = 20

dna = dna.Dna(dna_file_name)
skews = skew.Skew(dna)
skews.read_skews(block_size)
skews.calc_increasing_diff('G', 'C')
min_indices = skews.find_minimums()

ori = ori.Ori(dna)
ori_res = ori.find_ori([i * block_size for i in min_indices], block_size)
for ori in ori_res:
    print(ori)

skews.build_chart(chart_x_points, min_indices)

