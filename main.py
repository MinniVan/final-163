# This program takes in user input on what features they would like to plot

def main():
    print('There are two level features:')
    print(' 1. High Level')
    print(' 2. Low level')
    print()
    type_level = input('Which level feature are you interested in seeing? Pick 1 or 2: ')
    print('You chose ' + type_level + ' as the level feature')
    print()

    if int(type_level) != (1 or 2):
        type_level = input('Invalid value. Enter either 1 or 2: ')

    if int(type_level) == 1:
        print('Groups of High Level Features:')
        print('     1. Jet Kinematics')
        print('     2. Jet Substructures')
        print('     3. Energy-Correlation Functions')
        print()
        print('Which high level feature are you interested in seeing?')
        user_input = input('Enter the number associated with a high level feature: ')
        print('You picked ' + user_input + ' as the high feature value')
        input_value = {1, 2, 3}
        if int(user_input) not in input_value:
            user_input= input('Invalid value. Enter a new value between 1 and 3 for a high feature: ')
    else:
        print()
        print('Types of Low Level Features:')
        print('     1. Ratio of the pT of each consistent to the pT of the jet') 
        print('     2. Rotated eta of each constituent')  
        print('     3. Rotated phi of each constituent') 
        print('     4. Ratio of the energy of each consistent to the pT of the jet')  
        print('     5. Sqrt((Δeta)2 + (Δphi)2') 
        print('     6. Cos(angle(constituent, jet)')   
        print('     7. PDF ID number of the constituent')
        print()
        print('Which low level feature are you interested in seeing?')
        user_input = input('Enter the number associated with a low level feature' +
                          ' that you are interested in plotting:  ')
        print('You picked ' + user_input + ' as the low feature value')
        print()
        input_value = {1, 2, 3, 4, 5, 6, 7}
        if int(user_input) not in input_value:
            user_input = input('Invalid value. Enter a new value between 1 and 7 for a low feature: ')

if __name__ == '__main__':
    main()
