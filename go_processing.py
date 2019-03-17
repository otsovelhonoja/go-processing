# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 15:47:10 2019

@author: Otso Velhonoja
"""

from sys import argv
import go_processing_functions as go


def main():

    file1 = 'data/gene_association.mgi'
    file2 = 'data/mergeGO.out'

    if len(argv) == 1:
        n = 50
    elif len(argv) == 2:
        n = int(argv[1])
    else:
        file1 = argv[1]
        file2 = argv[2]
        n = int(argv[3])

    print('\nAnalysing...')

    # Part 1
    ids = go.read_go_ids(file1)
    # Part 2
    parents = go.read_go_parents(file2)
    # Part 3
    classes = go.read_go_classes(file2)
    # Part 4
    new_ids = go.add_go_ids(ids, parents)
    # Part 5
    counts = go.count_go_classes(new_ids)
    # Part 6
    go.output_most_common_classes(counts, classes, n)

    print('\nFinished!')


if __name__ == '__main__':
    main()
