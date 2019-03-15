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

    print('Analysing...')

    ids = go.read_go_ids(file1)
    parents = go.read_go_parents(file2)
    classes = go.read_go_classes(file2)

    new_ids = go.add_go_ids(ids, parents)
    counts = go.count_go_classes(new_ids)

    go.output_most_common_classes(counts, classes, 50)

    print('\nFinished!')


if __name__ == '__main__':
    main()
