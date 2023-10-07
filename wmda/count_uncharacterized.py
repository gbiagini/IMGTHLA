from collections import defaultdict
import pyard

ard = pyard.init('3530')

loc_counts = defaultdict(int)
visited = []

loci = ['A*', 'B*', 'C*', 'DQB1*', 'DRB1*']

with open("rel_dna_ser.txt", "r") as handle:
    for line in handle:
        if line.startswith('#'):
            continue
        
        line = line.strip()
        locus, allele, unamb, *_ = line.split(';')
        
        if locus not in loci:
            continue
        
        if unamb == "":
            allele = ard.redux(f"{locus}{allele}","U2")
            if allele not in visited:
                visited.append(allele)
                loc_counts[locus] += 1
            else:
                continue

for locus, count in loc_counts.items():
    print(f"{locus}\t{count}")