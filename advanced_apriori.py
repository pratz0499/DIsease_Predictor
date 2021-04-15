from apriori_utils import *


def apriori_function(database, minimum_support_count):

    original_database = database
    support_dictionary_list = []
    original_item_list = flatten_to_unique(database)

    current_database = original_database
    current_item_list = original_item_list
    iteration_counter = 1

    while True:
        if iteration_counter > 1:
            next_item_list = set_builder(current_item_list, iteration_counter + 1)
            if not next_item_list:
                break

        current_support_dictionary = support_calculator(current_item_list, current_database)
        support_dictionary_list.append(current_support_dictionary)

        current_pruned_item_list = item_list_prune(current_item_list, current_support_dictionary, minimum_support_count)
        current_pruned_database = database_prune(current_database, current_pruned_item_list)

        stopping_condition = 1

        for item_key in current_support_dictionary:
            if current_support_dictionary[item_key][0] >= minimum_support_count:
                stopping_condition = 0
                break

        if stopping_condition:
            break

        current_database = current_pruned_database
        next_item_list = set_builder(current_pruned_item_list, iteration_counter + 1)
        current_item_list = next_item_list
        iteration_counter = iteration_counter + 1

        if iteration_counter >= 7:
            break

    result_dictionary = {}

    for dictionary in support_dictionary_list:
        for item_key in dictionary:
            if dictionary[item_key][0] >= minimum_support_count:
                result_dictionary[item_key] = dictionary[item_key]

    return result_dictionary
