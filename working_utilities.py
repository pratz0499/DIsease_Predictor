from itertools import combinations
from symptoms_and_diagnoses import *


def power_set_generator(input_symptom_set):
    input_subset_list = []
    for counter in range(1, len(input_symptom_set)):
        iterator_set = combinations(range(len(input_symptom_set)), counter)
        for iterator in iterator_set:
            subset_list = []
            for value in iterator:
                subset_list.append(list(input_symptom_set)[value])
            input_subset_list.append(set(subset_list))
    return input_subset_list


def dictionary_builder(input_subset_dictionary, result_dictionary):
    for subset in input_subset_dictionary:
        item_key_collector = []
        for item_key in result_dictionary:
            if subset.issubset(item_key):
                item_key_collector.append([item_key, result_dictionary[item_key][0]])
        for item in item_key_collector:
            input_subset_dictionary[subset].append(item)


def maximal_combination_size_calculator(input_subset_dictionary):
    valid_combination_sizes = []
    for item_key in input_subset_dictionary:
        if len(input_subset_dictionary[item_key]) > 1:
            valid_combination_sizes.append(input_subset_dictionary[item_key][0])

    valid_combination_sizes_set = set(valid_combination_sizes)
    maximal_combination_size = max(valid_combination_sizes_set)
    return maximal_combination_size


def maximal_diagnosis_collector(input_subset_dictionary, maximal_combination_size):
    diagnosis_collector = []

    for item_key in input_subset_dictionary:
        if input_subset_dictionary[item_key][0] == maximal_combination_size:
            if len(input_subset_dictionary[item_key]) > 1:
                for item in input_subset_dictionary[item_key][1:]:
                    diagnosis = ''
                    for symptom_item in item[0]:
                        if symptom_item in diagnosis_list:
                            diagnosis = symptom_item
                    if diagnosis:
                        diagnosis_collector.append([diagnosis, item[0], item[1]])

    return diagnosis_collector


def diagnosis_dictionary_builder(diagnosis_collector):
    unique_diagnosis_finder = []
    for item in diagnosis_collector:
        unique_diagnosis_finder.append(item[0])
    unique_diagnosis_set = set(unique_diagnosis_finder)

    diagnosis_dictionary = {}

    for diagnosis in unique_diagnosis_set:
        symptom_finder = []
        total_support_calculator = 0
        for item in diagnosis_collector:
            if item[0] == diagnosis:
                total_support_calculator = total_support_calculator + item[2]
                for symptom in item[1]:
                    symptom_finder.append(symptom)
        symptom_list = []
        for symptom in symptom_finder:
            if symptom != diagnosis:
                symptom_list.append(symptom)
        symptom_set = set(symptom_list)
        diagnosis_dictionary[diagnosis] = [symptom_set, total_support_calculator]

    return diagnosis_dictionary


def occurrence_frequency_calculator(diagnosis, diagnosis_subset_list, data_list):
    frequency_dictionary = {}
    for diagnosis_subset in diagnosis_subset_list:
        new_set = {diagnosis}
        for set_item in diagnosis_subset:
            new_set.add(set_item)
        found_count = 0
        not_found_count = 0
        for transaction in data_list:
            if new_set.issubset(transaction):
                found_count += 1
            elif diagnosis_subset.issubset(transaction):
                not_found_count += 1
        if not((found_count == 0) and (not_found_count == 0)):
            frequency_dictionary[frozenset(diagnosis_subset)] = (float(found_count) / (float(not_found_count) +
                                                                                       float(found_count))) * 100
    return frequency_dictionary
