from apriori_utils import *

new_database = [{'1', '2', '5'}, {'2', '4'}, {'2', '3'}, {'1', '2', '4'}, {'1', '3'}, {'2', '3'}, {'1', '3'}, {'1', '2', '3', '5'}, {'1', '2', '3'}]

print("Iteration 1:\n")

first_item_list = flatten_to_unique(new_database)
print("The first item list is:")
print(first_item_list)
print("\n")

first_support_dictionary = support_calculator(first_item_list, new_database)
print("The first support dictionary is:")
print(first_support_dictionary)
print("\n")


first_pruned_item_list = item_list_prune(first_item_list, first_support_dictionary, 2)
print("The first pruned item list is:")
print(first_pruned_item_list)
print("\n")

first_pruned_database = database_prune(new_database, first_pruned_item_list)
print("The first pruned database is:")
print(first_pruned_database)
print("\n")

second_item_list = set_builder(first_pruned_item_list, 2)

print("Iteration 2:\n")

print("The second item list is:")
print(second_item_list)
print("\n")

second_support_dictionary = support_calculator(second_item_list, first_pruned_database)
print("The second support dictionary is:")
print(second_support_dictionary)
print("\n")

second_pruned_item_list = item_list_prune(second_item_list, second_support_dictionary, 2)
print("The second pruned item list is:")
print(second_pruned_item_list)
print("\n")

second_pruned_database = database_prune(first_pruned_database, second_pruned_item_list)
print("The second pruned database is:")
print(second_pruned_database)
print("\n")

third_item_list = set_builder(second_pruned_item_list, 3)

print("Iteration 3:\n")

print("The third item list is:")
print(third_item_list)
print("\n")

third_support_dictionary = support_calculator(third_item_list, second_pruned_database)
print("The third support dictionary is:")
print(third_support_dictionary)
print("\n")

third_pruned_item_list = item_list_prune(third_item_list, third_support_dictionary, 2)
print("The third pruned item list is:")
print(third_pruned_item_list)
print("\n")

third_pruned_database = database_prune(second_pruned_database, third_pruned_item_list)
print("The third pruned database is:")
print(third_pruned_database)
print("\n")

fourth_item_list = set_builder(third_pruned_item_list, 4)

print("Iteration 4:\n")

print("The fourth item list is:")
print(fourth_item_list)
print("\n")

fifth_item_list = set_builder(fourth_item_list, 5)
print(fifth_item_list)

