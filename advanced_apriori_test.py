from advanced_apriori import *
from create_large_input_file import *
from data_preparation import *
import time


# test_database = [('1', '2', '5'), ('2', '4'), ('2', '3'), ('1', '2', '4'), ('1', '3'), ('2', '3'), ('1', '3'), ('1', '2', '3', '5'), ('1', '2', '3')]
# apriori_function(test_database, 2)

# new_input_list = create_large_input()
# new_input_set_list = []
#
# for list_entry in new_input_list:
#     new_input_set_list.append(set(list_entry))
#
# st = time.time()
# result_dict = apriori_function(new_input_set_list, 3)
# ft = time.time()
# for item_key in result_dict:
#     print(item_key, ":", result_dict[item_key])
# print("Time taken:", ft-st)

# word_database = []
#
# for set_item in test_database:
#     word_set_item = set([])
#     for string_item in set_item:
#         if string_item == '1':
#             word_set_item.add('one')
#         elif string_item == '2':
#             word_set_item.add('two')
#         elif string_item == '3':
#             word_set_item.add('three')
#         elif string_item == '4':
#             word_set_item.add('four')
#         elif string_item == '5':
#             word_set_item.add('five')
#     word_database.append(word_set_item)

# result_dictionary = apriori_function(word_database, 2)
#
# for item_key in result_dictionary:
#     print(item_key, ":", result_dictionary[item_key])

# for item in new_input_list:
#     print(item)
st = time.time()
new_test_input = create_input_list()
result_dictionary = apriori_function(new_test_input, 100)
ft = time.time()
set_of_one_counter = 0
set_of_two_counter = 0
set_of_three_counter = 0
set_of_four_counter = 0
set_of_five_counter = 0
set_of_six_counter = 0
for item_key in result_dictionary:
    print(item_key, result_dictionary[item_key])
    if len(item_key) == 1:
        set_of_six_counter = set_of_one_counter + 1
    elif len(item_key) == 2:
        set_of_six_counter = set_of_two_counter + 1
    elif len(item_key) == 3:
        set_of_three_counter = set_of_three_counter + 1
    elif len(item_key) == 4:
        set_of_four_counter = set_of_four_counter + 1
    elif len(item_key) == 5:
        set_of_five_counter = set_of_five_counter + 1
    elif len(item_key) == 6:
        set_of_six_counter = set_of_six_counter + 1
print("Time taken:", ft-st)
print("Total number of combinations:", len(result_dictionary))
print("Number of sets of one:", set_of_one_counter)
print("Number of sets of two:", set_of_two_counter)
print("Number of sets of three:", set_of_three_counter)
print("Number of sets of four:", set_of_four_counter)
print("Number of sets of five:", set_of_five_counter)
print("Number of sets of six:", set_of_six_counter)

test_list = [2, [frozenset({'Rales', 'Heart murmurs'}), 393], [frozenset({'Cough', 'Rales', 'Heart murmurs'}), 355], [frozenset({'Rales', 'Heart murmurs', 'Chronic Obstructive Pulmonary Disease'}), 361], [frozenset({'Rales', 'Lumps', 'Heart murmurs'}), 38], [frozenset({'Shortness of breath', 'Rales', 'Heart murmurs'}), 358], [frozenset({'Dyspnea', 'Rales', 'Heart murmurs'}), 350], [frozenset({'Cough', 'Rales', 'Heart murmurs', 'Chronic Obstructive Pulmonary Disease'}), 331], [frozenset({'Cough', 'Rales', 'Lumps', 'Heart murmurs'}), 36], [frozenset({'Shortness of breath', 'Cough', 'Rales', 'Heart murmurs'}), 335], [frozenset({'Cough', 'Dyspnea', 'Rales', 'Heart murmurs'}), 335], [frozenset({'Shortness of breath', 'Rales', 'Heart murmurs', 'Chronic Obstructive Pulmonary Disease'}), 326], [frozenset({'Dyspnea', 'Rales', 'Heart murmurs', 'Chronic Obstructive Pulmonary Disease'}), 326], [frozenset({'Shortness of breath', 'Rales', 'Lumps', 'Heart murmurs'}), 38], [frozenset({'Rales', 'Dyspnea', 'Lumps', 'Heart murmurs'}), 36], [frozenset({'Shortness of breath', 'Dyspnea', 'Rales', 'Heart murmurs'}), 335], [frozenset({'Shortness of breath', 'Cough', 'Dyspnea', 'Rales', 'Heart murmurs'}), 335], [frozenset({'Chronic Obstructive Pulmonary Disease', 'Shortness of breath', 'Cough', 'Rales', 'Heart murmurs'}), 311], [frozenset({'Shortness of breath', 'Cough', 'Rales', 'Lumps', 'Heart murmurs'}), 36], [frozenset({'Chronic Obstructive Pulmonary Disease', 'Cough', 'Dyspnea', 'Rales', 'Heart murmurs'}), 311], [frozenset({'Cough', 'Rales', 'Dyspnea', 'Lumps', 'Heart murmurs'}), 36], [frozenset({'Chronic Obstructive Pulmonary Disease', 'Shortness of breath', 'Dyspnea', 'Rales', 'Heart murmurs'}), 311], [frozenset({'Shortness of breath', 'Rales', 'Dyspnea', 'Lumps', 'Heart murmurs'}), 36], [frozenset({'Shortness of breath', 'Cough', 'Dyspnea', 'Rales', 'Lumps', 'Heart murmurs'}), 36], [frozenset({'Chronic Obstructive Pulmonary Disease', 'Shortness of breath', 'Cough', 'Dyspnea', 'Rales', 'Heart murmurs'}), 311]]

for item in test_list:
    print(item)