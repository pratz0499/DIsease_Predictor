import pickle
from output_display import *
from data_preparation import *
from plot_display import *
import time


def diagnose(symptoms):
    data_list = create_input_list('encounter.csv','encounter_dx.csv')
    try:
        apriori_function_file = open('apriori_result', 'rb')
    except:
        raise Exception("Model not found")
    result_dictionary = pickle.load(apriori_function_file)
    output_list = output_generator(symptoms, result_dictionary, data_list)
    plot_function(output_list[1], 'static/plot.png')
    graph_img_src = "static/plot.png" 
    return [output_list[0], graph_img_src]