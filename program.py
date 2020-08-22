import h5py
import math
import pandas as pd
from process_data import Data
import matplotlib.pyplot as plt
import prompt_scripts as prompt



# get the data from Data

# make table
def jet_count_table(data_df, data):
    keys_count = dict()
    keys_count['Total'] = data_df.shape[0]
    labels_k = data.get_labels_truth_table()
    for i in labels_k:
        keys_count[i] = data_df[data_df[i] == 1].shape[0]
    
    
    labels = []
    for label in keys_count.keys():
        if label == 'Total':
            labels.append(label)
        else:
            labels.append(label[2:])
       
    table = {'Label': labels,
        'Number of jets': list(keys_count.values()),
        'Description': ['Total Statistics', 'Gluon jet',
                          'Light-quark jet','W-boson jet', 'Z-boson jet', 
                          'Top-quark jet', 'Undefined jet']
             }

    df = pd.DataFrame(table, columns = ['Label', 'Number of jets', 'Description'])
    return df

    

def plot_feature(data_df, data, feature):
    colors = ['purple', 'red', 'green', 'orange', 'blue']
    legend_labels = ['top', 'X', 'W', 'gluon', 'quark']
    x = dict()
    labels = data.get_labels_truth_table()
    for i in labels:
        if i != 'j_undef':
            x[i] = data_df[feature][data_df[i]==1]
    plt.hist(list(x.values())[::-1], 75, density = 1, histtype='step', color = colors, label=legend_labels)
    plt.legend(bbox_to_anchor=(0, -0.15, 1, 0), loc=2, ncol=2, mode="expand", borderaxespad=0)
    plt.xlabel(feature)
    plt.ylabel('Prob. Density (a.u)')
    plt.show()

def low_level(data):
    all_low = data.get_low_features()
    wanted_low = set(['ptrel', 'etarot', 'phirot', 'erel', 'deltaR', 'costhetarel', 'pdgid'])
    list_ = [i for i in all_low if (i[3:] in wanted_low)]
    result = dict()
    for i in range(len(list_)):
        i = i + 1
        result[i] = list_[i-1]
    return result 

def high_level_kinematics(data):
    all_high = data.get_high_features()
    wanted_high = ['mass_mmdt', 'pt']
    
    list_ = [i for i in all_high if (i[2:] in wanted_high)]
    result = dict()
    for i in range(len(list_)):
        i = i + 1
        result[i] = list_[i-1]
    return result 
    
def high_level_subst(data):
    all_high = data.get_high_features()
    wanted_high = ['zlogz', 'multiplicity']
    
    list_ = [i for i in all_high if (i[2:] in wanted_high)]
    result = dict()
    for i in range(len(list_)):
        i = i + 1
        result[i] = list_[i-1]
    return result 
    
def high_level_energy(data):
    all_high = data.get_high_features()
    wanted_high = ['c1_b0_mmdt', 'c1_b1_mmdt', 'c1_b2_mmdt', 
                    'c2_b1_mmdt', 'c2_b2_mmdt', 'd2_b1_mmdt',
                    'd2_b2_mmdt', 'd2_a1_b1_mmdt', 'd2_a1_b2_mmdt',
                    'm2_b1_mmdt', 'm2_b2_mmdt', 'n2_b1_mmdt',
                    'n2_b2_mmdt']
    list_ = [i for i in all_high if (i[2:] in wanted_high)]
    result = dict()
    for i in range(len(list_)):
        i = i + 1
        result[i] = list_[i-1]
    return result 

    
def main():
    
    prompt.intro()
    file_name = prompt.choose_file()
    print('Hang in there! We are loading your sample...')
    print()
    data = Data(file_name)
    data_df = data.get_data_df()
    print()
    print('For your information, here is a count of each jets',
          'that are in each truth jet label from your selected',
          'sample.')
   
    print()
    print(jet_count_table(data_df, data))
    print()
    print(high_level_energy(data))
    
    ans = 'y'
    while (ans == 'y'):
        
        choose_level = prompt.levels()
        if choose_level == 1:
            l_type = prompt.hlf()
        
            if l_type == 1:
                answer = 'y'
                while (answer == 'y'):
                    p = prompt.hl_kinematics()
                    feature = high_level_kinematics(data)[p]
                    plot_feature(data_df, data, feature)
            
                    answer = ''
                    while not (answer =='y' or answer == 'n'):
                        print()
                        answer = input('Would you like to plot another? (y/n) ')
                        print()


            if l_type == 2:
                answer = 'y'
                while (answer == 'y'):
                    p = prompt.hl_jetsub()
                    feature = high_level_subst(data)[p]
                    plot_feature(data_df, data, feature)
            
                    answer = ''
                    while not (answer =='y' or answer == 'n'):
                        print()
                        answer = input('Would you like to plot another? (y/n) ')
                        print()
                    
            if l_type == 3:
                answer = 'y'
                while (answer == 'y'):
                    p = prompt.hl_energy()
                    feature = high_level_energy(data)[p]
                    plot_feature(data_df, data, feature)
            
                    answer = ''
                    while not (answer =='y' or answer == 'n'):
                        print()
                        answer = input('Would you like to plot another? (y/n) ')
                        print()
        else:
            answer = 'y'
            while (answer == 'y'):
                p = prompt.llf()
                feature = low_level(data)[p]
                plot_feature(data_df, data, feature)
            
                answer = ''
                while not (answer =='y' or answer == 'n'):
                    print()
                    answer = input('Would you like to plot another? (y/n) ')
                    print()
        ans = ''
        while not(ans == 'y' or ans =='q'):
            ans = input('Would you like to change features or quit? (y/q)')
                





    






if __name__ == '__main__':
    main()

