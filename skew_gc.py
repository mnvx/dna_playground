from dna import skew

dna_file_name = 'examples/Salmonella_enterica.txt'
# dna_file_name = 'examples/Salmonella_enterica_ATCC_9239.fasta'
# dna_file_name = 'examples/Salmonella_enterica_subsp_enterica_ATCC_39183.fasta'
# dna_file_name = 'examples/Salmonella_enterica_subsp_enterica_ATCC_700931.fasta'
# dna_file_name = 'examples/E_coli.txt'
block_size = 5000
chart_x_points = 20

skews = skew.Skew(dna_file_name)
skews.read_skews(block_size)
skews.calc_increasing_diff('G', 'C')
min_indices = skews.find_minimums()
skews.build_chart(chart_x_points, min_indices)
