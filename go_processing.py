# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 15:47:10 2019

@author: Otso
"""
from sys import argv
import go_processing_functions as go


def main():

    if len(argv) < 2:
        file1 = 'data/gene_association.mgi'
        file2 = 'data/mergeGO.out'

    else:
        file1 = argv[1]
        file2 = argv[2]

    ids = go.read_go_ids(file1)
    parents = go.read_go_parents(file2)
    classes = go.read_go_classes(file2)

    new_ids = go.add_go_ids(ids, parents)
    counts = go.count_go_classes(new_ids)

    with open('most_common_go_classes.txt', 'w') as out_file:

        out_file.write(f'Top 50 most common GO-classes in "{file1}"\n'
                       'id\tcount\tclass\n')

        for c in counts.most_common(50):
            out_file.write(f'GO:{c[0]}\t{c[1]}\t{classes[c[0]]}\n')


if __name__ == '__main__':
    main()
