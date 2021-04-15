import matplotlib.pyplot as plt


def plot_function(plot_dictionary_list, path_to_save = 0):
    for plot_dictionary in plot_dictionary_list:
        plt.rc('font', size=5)
        keys = list(plot_dictionary.keys())
        values = list(plot_dictionary.values())
        fig = plt.figure(figsize=(10, 5))
        plt.bar(keys, values, color='maroon', width=0.1)
        plt.xlabel("Combinations of reported symptoms")
        plt.ylabel("Occurrence frequency in percentage")
        plt.title("Occurrence frequency static by symptom combination")
        if not path_to_save:
            plt.show()
        else:
            fig.savefig(path_to_save)