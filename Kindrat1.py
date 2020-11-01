from matplotlib import pyplot as plt


def build_schedule(data_frame, name_list, by_sett):
    for name in name_list:
        if type(data_frame[name][1]) is str:
            plt.scatter(data_frame[by_sett], data_frame[name], label=name + ' direction', color='green')
            plt.xlabel(by_sett, fontsize=20)
            plt.ylabel(name, fontsize=20)
            plt.title(name + " graph by " + by_sett)
            plt.grid()
            plt.show()
        else:
            plt.scatter(data_frame[by_sett], data_frame[name])
            plt.xlabel(by_sett, fontsize=20)
            plt.ylabel(name, fontsize=20)
            plt.title(name + " graph by " + by_sett)
            plt.grid()
            plt.legend()
            plt.show()