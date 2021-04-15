from keyword_extractor import *
from working_utilities import *


def output_generator(input_symptoms, result_dictionary, data_list):
    output_text_list = []
    plot_dictionary_list = []
    input_symptom_list = keyword_list_generator(input_symptoms)
    input_symptom_set = set(input_symptom_list)

    input_subset_list = power_set_generator(input_symptom_set)

    input_subset_dictionary = {frozenset(input_symptom_set): [len(input_symptom_set)]}

    for subset in input_subset_list:
        input_subset_dictionary[frozenset(subset)] = [len(subset)]

    dictionary_builder(input_subset_dictionary, result_dictionary)

    symptom_power_set_list = []

    for item_key in input_subset_dictionary:
        symptom_power_set_list.append(set(item_key))

    maximal_combination_size = maximal_combination_size_calculator(input_subset_dictionary)

    output_text_list.append("\nThe following diagnoses are possible:\n")

    diagnosis_collector = maximal_diagnosis_collector(input_subset_dictionary, maximal_combination_size)

    diagnosis_dictionary = diagnosis_dictionary_builder(diagnosis_collector)

    for diagnosis_item in diagnosis_dictionary:
        plot_dictionary = {}

        output_text_list.append(diagnosis_item + " associated with the following symptoms:\n")

        for symptom_item in diagnosis_dictionary[diagnosis_item][0]:
            output_text_list.append(symptom_item)
        output_text_list.append("\n")

        occurrence_frequency_dictionary = occurrence_frequency_calculator(diagnosis_item, symptom_power_set_list,
                                                                          data_list)

        for item_key in occurrence_frequency_dictionary:
            symptom_list = []
            for symptom_item in item_key:
                symptom_list.append(symptom_item)

            output_text_list.append("This diagnosis occurs in association with the following symptoms:")

            symptom_combination_string = ""

            for item in symptom_list:
                symptom_combination_string = symptom_combination_string + item + ", "

            output_text_list.append(symptom_combination_string[:-2])

            output_text_list.append("with an occurrence frequency of " +
                                    str(occurrence_frequency_dictionary[item_key]) +
                                    " percent among the patients surveyed who reported those symptoms.\n")

            plot_dictionary[symptom_combination_string[:-2]] = occurrence_frequency_dictionary[item_key]

        plot_dictionary_list.append(plot_dictionary)

    return_list = [output_text_list, plot_dictionary_list]
    return return_list