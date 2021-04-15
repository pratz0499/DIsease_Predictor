import csv
from keyword_extractor import *
from symptoms_and_diagnoses import *


def file_to_list(file_handle):
    table = []
    reader = csv.reader(file_handle)
    for row in reader:
        table.append(row)
    return table


def create_input_list(symptom_data_filename, diagnosis_data_filename):
    file1 = open('encounter.csv')
    file2 = open('encounter_dx.csv')
    table1 = file_to_list(file1)
    table2 = file_to_list(file2)
    combined_table = []
    final_list = []

    for i in table1:
        for j in table2:
            if i[1] == j[5]:
                new_row = [i[25], j[3]]
                combined_table.append(new_row)
    print(combined_table)
    for row in combined_table:
        sublist = keyword_list_generator(row[0])
        if row[1] in diagnosis_list:
            sublist.append(row[1])
        sublist_set = set(sublist)
        final_list.append(sublist_set)

    new_final_list = []

    for item_set in final_list:
        if len(item_set) >= 2:
            new_final_list.append(item_set)

    return new_final_list
