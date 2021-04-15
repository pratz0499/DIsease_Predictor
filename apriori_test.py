from apriori_function import *
from create_large_input_file import *

myData = create_large_input()[1:8]
#print(myData)
# myData = [['1', '2', '5'], ['2', '4'], ['2', '3'], ['1', '2', '4'], ['1', '3'], ['2', '3'], ['1', '3'], ['1', '2', '3', '5'], ['1', '2', '3']]
apriori_function(myData, 2)
