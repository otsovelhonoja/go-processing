# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 15:15:58 2019

@author: Otso
"""

from collections import Counter


def read_go_ids(filename):
    """PART 1. Returns a dictionary with gene name as key and
    a set of associated GO-ids as value.
    """
    go_ids_dict = {}
    with open(filename) as file_obj:

        for line in file_obj:
            # ignore comments
            if line.startswith('!'):
                continue

            line = line.split()
            db_id = line[1]             # gene name
            # make sure to use only use values starting with 'GO:' as ids
            for word in line:
                if word.startswith('GO:'):
                    go_id = word[3:]    # GO-id without 'GO:'

            go_ids_dict.setdefault(db_id, set()).add(go_id)

    return go_ids_dict


def read_go_parents(filename):
    """PART 2. Returns a dictionary that has GO-id as key and
    list of parent GO-classes as value.
    """
    go_parents_dict = {}

    with open(filename) as file_obj:

        for line in file_obj:
            line = line.split(sep='\t')
            # Check that parents exist for current row
            if line[4]:
                go_id = line[2]
                go_parents = line[4].split(sep=',')
                go_parents_dict[go_id] = go_parents

    return go_parents_dict


def read_go_classes(filename):
    """PART 3. Returns a dictionary that has GO-id as key and
    GO-classname as a value.
    """
    go_classes_dict = {}

    with open(filename) as file_obj:

        for line in file_obj:
            line = line.split(sep='\t')
            go_id = line[2]
            go_class = line[3]      # classname
            go_classes_dict[go_id] = go_class

    return go_classes_dict


def add_go_ids(to_dict, from_dict):
    """PART 4. Returns back the first dictionary with added parent GO-ids
    from the second dictionary.
    """
    # iterate through all the genes in the first dict
    for gene, go_ids in to_dict.items():
        new_ids = set()
        # iterate through all GO-ids for gene
        for go_id in go_ids:
            # check if parent ids exist for GO-id
            if go_id in from_dict.keys():
                # add all parent ids to temporary set of GO-ids
                for parent_id in from_dict[go_id]:
                    new_ids.add(parent_id)
        # merge new GO-ids with the old
        to_dict[gene] = to_dict[gene].union(new_ids)

    return to_dict


def count_go_classes(id_dict):
    """PART 5. Return a dictionary with GO-id as key and
    a count of occurances as value.
    """
    count_dict = Counter()
    # iterate through the list of GO-ids for each gene
    for id_list in id_dict.values():
        # count occurances of each id and
        # merge them with the rest
        count_dict.update(Counter(id_list))

    return count_dict


def output_most_common_classes(count_dict, class_dict, n):
    """PART 6. Outputs a tsv file with n most common GO-classes"""

    with open('most_common_go_classes.tsv', 'w') as out_file:
        out_file.write('id\tcount\tclass\n')

        for c in count_dict.most_common(n):
            out_file.write(f'GO:{c[0]}\t{c[1]}\t{class_dict[c[0]]}\n')
