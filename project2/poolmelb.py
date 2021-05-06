def matching_codons(complements, pool1, pool2):
    rtn = []
    for element in pool1:
        result = "".join([complements[x] for x in element])
        if result in pool2:
            rtn.append((element, result))
    return rtn


complements = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
pool1 = ['AAG', 'TAC', 'CGG', 'GAT', 'TTG', 'GTG', 'CAT', 'GGC', 'ATT', 'TCT']
pool2 = ['TAA', 'CTA', 'AAC', 'TTC', 'AGA', 'CCC', 'CCG', 'GTA']
print(matching_codons(complements, pool1, pool2))
