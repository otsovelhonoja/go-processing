# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 15:15:58 2019

@author: Otso
"""

from collections import Counter


def read_go_ids(filename):

    go_ids_dict = {}

    with open(filename) as file_obj:

        for line in file_obj:

            if line.startswith('!'):
                continue

            line = line.split()
            db_id = line[1]

            for word in line:
                if word.startswith('GO:'):
                    go_id = word[3:]

            go_ids_dict.setdefault(db_id, set()).add(go_id)

    return go_ids_dict


def read_go_parents(filename):
    go_parents_dict = {}

    with open(filename) as file_obj:
        for line in file_obj:
            line = line.split(sep='\t')
            if line[4]:
                go_id = line[2]
                go_parents = line[4].split(sep=',')
                go_parents_dict[go_id] = go_parents

    return go_parents_dict


def read_go_classes(filename):
    go_classes_dict = {}

    with open(filename) as file_obj:
        for line in file_obj:
            line = line.split(sep='\t')
            go_id = line[2]
            go_class = line[3]
            go_classes_dict[go_id] = go_class

    return go_classes_dict


def add_go_ids(to_dict, from_dict):

    for gene, go_ids in to_dict.items():

        new_ids = set()

        for go_id in go_ids:

            if go_id in from_dict.keys():

                for p in from_dict[go_id]:
                    new_ids.add(p)

        to_dict[gene] = to_dict[gene].union(new_ids)

    return to_dict


def count_go_classes(id_dict):

    count_dict = Counter()

    for id_list in id_dict.values():
        count_dict.update(Counter(id_list))

    return count_dict
