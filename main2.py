from advanced_apriori import *
from data_preparation import *
from keyword_extractor import *
from working_utilities import *
import matplotlib.pyplot as plt
from main import * 
import sys
 
def print_result(input_subset_dictionary,maximal_combination_size,symptom_power_set_list,data_list):
    print("\nThe following diagnoses are possible:\n")

    diagnosis_collector = maximal_diagnosis_collector(getvalue.input_subset_dictionary, getvalue.maximal_combination_size)

    diagnosis_dictionary = diagnosis_dictionary_builder(diagnosis_collector)


    for diagnosis_item in diagnosis_dictionary:
        plot_dictionary = {}
        print(diagnosis_item, "associated with the following symptoms:\n")

        for symptom_item in diagnosis_dictionary[diagnosis_item][0]:
            print(symptom_item)
        print("\n")

        occurrence_frequency_dictionary = occurrence_frequency_calculator(diagnosis_item, getvalue.symptom_power_set_list,getvalue.data_list)

        for item_key in occurrence_frequency_dictionary:
            symptom_list = []
            for symptom_item in item_key:
                symptom_list.append(symptom_item)

            print("This diagnosis occurs in association with the following symptoms:")

            symptom_combination_string = ""

            for item in symptom_list:
                symptom_combination_string = symptom_combination_string + item + ", "

            print(symptom_combination_string[:-2])

            print("with an occurrence frequency of", occurrence_frequency_dictionary[item_key],
                    "percent among the patients surveyed who reported those symptoms.\n")

            plot_dictionary[symptom_combination_string[:-2]] = occurrence_frequency_dictionary[item_key]

        plt.rc('font', size=5)
        keys = list(plot_dictionary.keys())
        values = list(plot_dictionary.values())
        fig = plt.figure(figsize=(10, 5))
        plt.bar(keys, values, color='maroon', width=0.1)
        plt.xlabel("Combinations of reported symptoms")
        plt.ylabel("Occurrence frequency in percentage")
        plt.title("Occurrence frequency graph for " + diagnosis_item + " by symptom combination")
        image=plt.show()