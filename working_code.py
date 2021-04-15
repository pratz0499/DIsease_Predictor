import csv
import re
import pandas
from mlxtend.frequent_patterns import apriori
from mlxtend.preprocessing import TransactionEncoder

file1 = open('Major-Project-main/encounter.csv')
file2 = open('Major-Project-main/encounter_dx.csv')
reader1 = csv.reader(file1)
reader2 = csv.reader(file2)

table1 = []
table2 = []

for row in reader1:
    table1.append(row)
for row in reader2:
    table2.append(row)

final_table = []

for i in table1:
    for j in table2:
        if i[1] == j[5]:
            new_row = [i[1], i[2], i[8], i[25], j[3]]
            final_table.append(new_row)

symptom_dictionary = {'Vertigo': r'vertigo',
           'Headaches': r'headaches?',
           'Lightheadedness': r'lightheadedness',
           'Edema': r'(?<!no\s)edema',
           'Clubbing': r'(?<!or\s)clubbing',
           'Rales': r'(?<!no\s)rales?',
           'Wheezing': r'(?<!or\s)wheez(e|ing)',
           'Hypertension': r'hypertension',
           'Dyspnea': r'dyspnea',
           'Cough': r'cough(ing)?',
           'Heart murmurs': r'murmurs?',
           'Ringing in the ears': r'ringing in( the)? ears?',
           'Shortness of breath': r'short(ening|ness|ened)( of)? breath(ing)?',
           'Sputum production': r'sputum production|production of sputum',
           'Pyelonephritis': r'pyelonephritis',
           'Hemorrhagic stroke': r'ha?emorrhagic stroke',
           'Lumps': r'lumps?',
           'Diabetes': r'diabet(es|ic)',
           'Weight loss': r'weight loss|loss of weight',
           'Foot pain': r'foot pain',
           'Paresthesia': r'paresthesia',
           'Foamy urine': r'foamy urine',
           'Tingling of the feet': r'tingling of( the)? (foot|feet)',
           'Atherosclerotic calcification': r'atherosclerotic calcification|atherosclerosis',
           'Frequent urination': r'frequent urinati(on|ng)',
           'Increased thirst': r'increase(d| in) thirst',
           'Weak urinary stream': r'weak urinary stream',
           'Chest pain': r'chest pain|pain in( the?) chest',
           'Hemorrhage': r'ha?emorrhage',
           'Trauma': r'trauma',
           'Lethargy': r'letharg(y|ic)',
           'Swollen ankles': r'(swollen|swelling (of|at)( the)?) ankles?',
           'Palpitations': r'palpitations?',
           'Stump pain': r'stump pain|pain (in|at) (the )?(stump|amputation site)',
           'Discomfort with movement': r'discomfort (with|in) mov(ement|ing)',
           'Distress': r'distress',
           'Urinary dribbling': r'urinary (dribbling|incontinence)',
           'Fever': r'fever',
           'Myocardial infarction': r'myocardial infarction|heart attack',
          'Swelling at the amputation site': r'(swelling|swollen) (at|in )?(the )?(amputation site|stump)',
           'Disarticulation of the right shoulder': r'disarticulat(ion|ed) ((of|at|in)( the )? )?right shoulder',
           'Erythema': r'erythem(a|ic)',
           'Burned shoulder': r'burn(ed)? ((at|to|in) (the )?)?shoulder',
           'Disarticulation of the right hip': r'disarticulat(ion|ed) ((of|at|in)( the )? )?right hip',
           'Limb pain': r'limb pain|pain (in|at) (the )?limb'}

diagnosis_list = ['Hemorrhagic Stroke', 'Pyelonephritis', 'Embolic Stroke', 'Type 2 Diabetes', 'Chronic Congestive Heart Failure', 'Type 1 Diabetes', 'Chronic Renal Failure', 'Chronic Obstructive Pulmonary Disease', 'Kidney Stones', 'Hypertension', 'Acute Renal Failure', 'Myocardial Infarction']
data_list = []

for row in final_table:
    sublist = []
    for i in symptom_dictionary:
        if re.findall(symptom_dictionary[i], row[3].lower()):
            sublist.append(i)
    sublist.append(row[4])
    data_list.append(sublist)

te = TransactionEncoder()
te_ary = te.fit(data_list).transform(data_list)
data_frame = pandas.DataFrame(te_ary, columns=te.columns_)
apriori_result = apriori(data_frame, min_support=0.001, use_colnames=True)

input_symptoms = input("Enter the description of symptoms: ")

input_symptom_list = []

for i in symptom_dictionary:
    if re.findall(symptom_dictionary[i], input_symptoms.lower()):
        input_symptom_list.append(i)

table_size = apriori_result.size

row_dict = {}
count_list = []

for i in range(0, int(table_size/2)):
    symptom_ctr = 0
    for j in (apriori_result.at[i, 'itemsets']):
        if j in input_symptom_list:
            symptom_ctr = symptom_ctr + 1
    row_dict[i] = symptom_ctr
    count_list.append(symptom_ctr)

print("\nPossible diagnoses are as follows:\n")
for i in row_dict:
    if row_dict[i] == max(count_list):
        for j in diagnosis_list:
            if j in (apriori_result.at[i, 'itemsets']):
                print(j+" accompanied with the following symptoms:")
                for k in (apriori_result.at[i, 'itemsets']):
                    if k != j:
                        print(k)
                print('\n')