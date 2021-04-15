import itertools


def common_data(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result
    return result


def apriori_function(original_database, minimum_support_count):
    transient_database = []
    original_item_list = []
    transient_item_list = []
    support_dictionary = {}

    for i in original_database:
        for j in i:
            if j not in original_item_list:
                original_item_list.append(j)

# The 1-frequent items have been collected

    for i in original_item_list:
        support_counter = 0
        found_list = []
        for j in original_database:
            if set([i]).issubset(j):
                support_counter = support_counter + 1
                found_list.append(j)
        support_dictionary[frozenset([i])] = [support_counter, found_list]

# The support counts of the 1-frequent items have been calculated

    index_found_list = []

    for i in support_dictionary:
        if support_dictionary[i][0] >= minimum_support_count:
            for j in i:
                if j not in transient_item_list:
                    transient_item_list.append(j)
            for j in range(0, len(original_database)):
                if original_database[j] in support_dictionary[i][1]:
                    if j not in index_found_list:
                        index_found_list.append(j)

    for i in index_found_list:
        transient_database.append(original_database[i])

# End of first iteration

    combinations_list = []
    for i in (itertools.combinations(range(len(transient_item_list)), 2)):
        combination_item = []
        for j in i:
            combination_item.append(transient_item_list[j])
        combinations_list.append(combination_item)

    transient_item_list = combinations_list
    iteration_counter = 2

    while True:
        for i in transient_item_list:
            frozen_item = frozenset(i)
            found_list = []
            support_counter = 0
            for j in transient_database:
                if set(frozen_item).issubset(set(j)):
                    support_counter = support_counter + 1
                    found_list.append(j)
            support_dictionary[frozen_item] = [support_counter, found_list]

        transient_item_list = []
        index_found_list = []

        for i in support_dictionary:
            if len(i) == iteration_counter:
                if support_dictionary[i][0] >= minimum_support_count:
                    if i not in transient_item_list:
                        transient_item_list.append(i)
                    for j in range(0, len(transient_database)):
                        if transient_database[j] in support_dictionary[i][1]:
                            if j not in index_found_list:
                                index_found_list.append(j)

        new_transient_database = []

        for i in index_found_list:
            new_transient_database.append(transient_database[i])

        transient_database = new_transient_database

        new_transient_item_list = []

        for i in itertools.combinations(range(len(transient_item_list)), iteration_counter + 1):
            for j in i:
                for k in i:
                    if j != k:
                        if common_data(transient_item_list[j], transient_item_list[k]):
                            union_element = transient_item_list[j].union(transient_item_list[k])
                            if union_element not in new_transient_item_list:
                                new_transient_item_list.append(union_element)

        transient_item_list = new_transient_item_list

        deletion_list = []

        for i in transient_database:
            indicator = 0
            for j in transient_item_list:
                if j.issubset(set(i)):
                    indicator = 1
                    break
            if indicator == 0:
                deletion_list.append(i)

        for i in deletion_list:
            for j in transient_database:
                if i == j:
                    transient_database.remove(j)

        iteration_counter = iteration_counter + 1

        if not transient_item_list:
            break

    counter = 0
    for i in support_dictionary:
        if support_dictionary[i][0] > 0:
            counter = counter + 1
            print(counter, i, support_dictionary[i])
