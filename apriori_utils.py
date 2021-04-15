from pandas.core.common import flatten
import itertools


def flatten_to_unique(input_list):
    return_list = []
    for item in set(flatten(input_list)):
        return_list.append({item})
    return return_list


def support_calculator(item_list, database):
    support_dictionary = {}
    for item in item_list:
        support_count = 0
        found_list = []
        for transaction in database:
            if item.issubset(transaction):
                found_list.append(transaction)
                support_count = support_count + 1
        support_dictionary[frozenset(item)] = [support_count, found_list]
    return support_dictionary


def item_list_prune(item_list, item_dictionary, minimum_support):
    return_list = []
    for item in item_list:
        if item_dictionary[frozenset(item)][0] >= minimum_support:
            return_list.append(item)
    return return_list


def database_prune(database, item_list):
    result_database = []
    for transaction in database:
        found_flag = 0
        for item in item_list:
            if item.issubset(transaction):
                found_flag = 1
        if found_flag == 1:
            result_database.append(transaction)
    return result_database


def build_sets(item_list, set_size):
    flattened_item_list = list(set(flatten(item_list)))
    combinations = itertools.combinations(range(len(flattened_item_list)), set_size)
    return_list = []
    for i in combinations:
        combination_element = []
        for j in i:
            combination_element.append(flattened_item_list[j])
        return_list.append(set(combination_element))
    return return_list


def sets_generator(item_list, set_size):
    distinct = set.union(*item_list)
    for c in itertools.combinations(distinct, r=set_size):
        yield set(c)


def set_builder(item_list, set_size):
    distinct = set.union(*item_list)
    return [set(c) for c in itertools.combinations(distinct, r=set_size)]