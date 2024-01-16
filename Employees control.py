import os

names = [{'namef': 'Luiz', 'age': 21, 'active': True},
         {'namef': 'Carlos', 'age': 24, 'active': False},
         {'namef': 'Stephanie', 'age': 23, 'active': True}]


# User_invalid
def invalid_option():
    print('Invalid option\n')
    back_menu()

# Main_menu
def layout_main_program():
    print('APP Register')

    # Layout_options


def options_first_layout():
    print('Choose an option ')
    print('1. Register new functionary')
    print('2. Update register')
    print('3. Active/Desactive Register')
    print('4. Show list')
    print('5.Cancel')





    # Return
def back_menu():
    input('Press Enter key to restart\n')
    main()

    # Definitions forms


def subtitle(text):
    os.system('cls')
    line = '*' * (len(text) + 4)
    print(text)
    print(line)
    print()


# Options functions
def new_employee():
    subtitle('New functionary')

    name_funct = input('Name')
    age_funct = int(input(f'Age {name_funct}:'))
    data_funct = {'namef': name_funct, 'age': age_funct, 'active': False}
    names.append(data_funct)
    print(f'- Functionary {name_funct}, was completely registred')
    # print('Functionary Age')
    # age_funct = int(input('Age '))
    # ages.append(age_funct)
    # print(name_funct,'', age_funct)

    print('Confirm?')
    back_menu()


def show_employee():
    subtitle('Show employees')
    print(f" {'Name employees'.ljust(22)} | {'Age'.ljust(20)} | {'Activid'}")
    for name in names:
        names_employee = name['namef']
        age_employee = name['age']
        active_employee = name['ACTIVE' if name['active'] else 'DESACTIVED']
        print(f'- {names_employee.ljust(20)} | {age_employee.ljust(20)} | {active_employee}')
    back_menu()


def active_funct():
    subtitle('Enable/Disable Register')

    names_employee = input('Select employee:')
    found_name = False

    for name in names:
        if names_employee == name['namef']:
            found_name = True
            name['active'] = not name['active']
            notif = f'The employee {names_employee} was activet' if name[
                'active'] else f'The employee {names_employee} was disabled'
            print(notif)
    if not names_employee:
        print('Functionary not found')

    back_menu()


# OptionSelector
def choose_option():
    try:
        number_choose = int(input('Input a number: '))

        # def update_register():
        # def delete_register():

        # Options_def

        if number_choose == 1:
            new_employee()
        elif number_choose == 2:
            print('Upddate register')
        elif number_choose == 3:
            active_funct()
        elif number_choose == 4:
            show_employee()
        elif number_choose == 5:
            print('Cancel')
        else:
            invalid_option()
    except:
        invalid_option()


def main():
    layout_main_program()
    options_first_layout()
    choose_option()


if __name__ == '__main__':
    main()
