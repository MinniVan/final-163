# This program takes in user input on what features they would like to plot
# Whether it be high level or low level featues


def intro():
    # This method introduces our program and what is that we are working with.
    # It allows user to input their preference for what they would like to be
    # plotted.
    print('In this program we will be exploring a Dense Neural Network (DNN)',
          'algorithm for jet tagging in high energy physics. Specifically',
          'we will analyze two type of features that would be used as input',
          'for the DNN model. We will achieve this by plotting some of these',
          'features in a probability denisty of that feature and 5 labels',
          'used for supervised learning.')
    print()
    print('You, the user, will be prompted to decide which level type you are',
          'interested in, followed by the features you want to see plotted.',
          'There are a total of sixteen high level features and seven total',
          'low level features.')
    print()


def choose_file():
    # This method gives the user two options for data files.
    # First file, is for a very large data set.
    # Second file, is for a relatively smaller data set.
    # If the file input number is not 1 or 2, then user is prompted
    # to retype their preference.
    samples = {'1': 'processed-pythia82-lhc13-all-pt1-50k-r1_h022_e0175_t220_nonu_withPars_truth.z',
               '2': 'processed-pythia82-lhc13-all-pt1-50k-r1_h022_e0175_t220_nonu_withPars_truth_0.z'}
    print('There are two files in here')
    print('     1. Big Sample (aprox (1.3GB)')
    print('     2. Smaller Sample (aprox. 500mb)')
    print()
    print('Specify which sample you would like us to load.')
    print()
    while True:
        user_input = input('Choose the file (Type 1 or 2): ')
        print()
        if user_input == '1' or user_input == '2':
            return samples[user_input]
        else:
            print('INVALID ENTRY')
            print()


def levels():
    # This methods prompts the user to input their prefernce for
    # either high or low level features.
    print('There are two level features:')
    print(' 1. High Level')
    print(' 2. Low Level')
    print()
    while True:
        type_level = input('Which level feature are you interested in',
                           'seeing? (Type 1 or 2): ')
        if type_level == '1' or type_level == '2':
            return int(type_level)
        else:
            print('INVALID ENTRY')
            print()


def hlf():
    # If use chose to see high level features they are then shotly
    # prompted to which features they are interested in seeing
    print('Here are the different types of High Level Features:')
    print('     1. Jet Kinematics')
    print('     2. Jet Substructures')
    print('     3. Energy-Correlation Functions')
    print()
    print('Specify which group of High Level feature you would like ',
          'to look at?')
    print()
    while True:
        user_input = input('Enter the number associated with a High Level',
                           'Feature type: ')
        possible_ins = {'1', '2', '3'}
        if user_input in possible_ins:
            return int(user_input)
        else:
            print('INVALID ENTRY')
            print()


def llf():
    # If user chose to view low level features, they are shortly
    # then prompted to which feature they would like to plot
    print()
    print('Here are the different types of Low Level Features:')
    print('     1. PDF ID number of the constituent')
    print('     2. Ratio of the energy of each consistent to the pT of',
          'the jet')
    print('     3. Ratio of the pT of each consistent to the pT of the jet')
    print('     4. Rotated eta of each constituent')
    print('     5. Rotated phi of each constituent')
    print('     6. Sqrt((Δeta)2 + (Δphi)2')
    print('     7. Cos(angle(constituent, jet)')
    print()
    print('Specify which type of Low Level feature you would like to look at?')
    print()
    while True:
        user_input = input('Enter the number associated with a Low Level',
                           'Feature type: ')
        possible_ins = {'1', '2', '3', '4', '5', '6', '7'}
        if user_input in possible_ins:
            return int(user_input)
        else:
            print('INVALID ENTRY')
            print()


def hl_kinematics():
    # If user chose the kinetmatics feature for high level
    # they are then asked for the specific feature they are
    # wanting to plot
    print()
    print('Jet kinematics:')
    print('     1. Jet mass computed based on modified mass drop tagger')
    print('     2. Jet pT (transverse momentum)')
    while True:
        user_input = input('Enter the number associated with a Low Level',
                           'Feature type: ')
        possible_ins = {'1', '2'}
        if user_input in possible_ins:
            return int(user_input)
        else:
            print('INVALID ENTRY')
            print()


def hl_jetsub():
    # If user chose to see jet subcstructures for high level features,
    # they are then prompted to choose a specific feature to plot
    print('Jet subsctructures')
    print('     1. Jet splitting fraction')
    print('     2. Number of constituents')
    while True:
        user_input = input('Enter the number associated with a Low Level'
                           'Feature type: ')
        possible_ins = {'1', '2'}
        if user_input in possible_ins:
            return int(user_input)
        else:
            print('INVALID ENTRY')
            print()


def hl_energy():
    # If user chose to see energy correlation funcitons for the high level
    # features, they are then prompted for a specific feature
    print('Energy-Correlation functions')
    print('     1. j_c1_b0_mmdt')
    print('     2. j_c1_b1_mmdt')
    print('     3. j_c1_b2_mmdt')
    print('     4. j_c2_b1_mmdt')
    print('     5. j_c2_b2_mmdt')
    print('     6. j_d2_b1_mmdt')
    print('     7. j_d2_b2_mmdt')
    print('     8. j_d2_a1_b1_mmdt')
    print('     9. j_d2_a1_b2_mmdt')
    print('     10. j_m2_b1_mmdt')
    print('     11. j_m2_b2_mmdt')
    print('     12. j_n2_b1_mmdt')
    print('     13. j_n2_b2_mmdt')
    while True:
        user_input = input('Enter the number associated with a Low Level',
                           'Feature type: ')
        possible_ins = {'1', '2', '3', '4', '5', '6', '7',
                        '8', '9', '10', '11', '12', '13'}
        if user_input in possible_ins:
            return int(user_input)
        else:
            print('INVALID ENTRY')
