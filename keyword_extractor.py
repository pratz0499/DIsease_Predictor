import re
from symptoms_and_diagnoses import *


def keyword_list_generator(keyword_string):
    sublist = []
    for symptom in symptom_dictionary:
        if re.findall(symptom_dictionary[symptom], keyword_string.lower()):
            sublist.append(symptom)
    return sublist
