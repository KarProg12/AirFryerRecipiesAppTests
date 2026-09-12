prompt = "\n-----------------------------------------------------"
prompt += "\nEnter the recipie in this order:\n"
prompt += "  'KEY: recipie_name' : 'VALUE: recipie_content'\n"
prompt += "If you want to exit the program type 'end' or 'exit'."
prompt += "\n-----------------------------------------------------"
prompt += "\n>>>"

recipies = {}
recipies_table = []

recipie_name = recipies.keys()
recipie_content = recipies.values()

def add_recipie(name, content):
    recipies[name] = content

def show_recipies_in_table():
    """Display nice-formatted recipies"""
    list_index = len(recipies_table)

    for name, recipie in recipies.items():
        name.append()
        recipie.append()

    for index in range(list_index):
        if index % 2 == 0:
            print(f"{recipie_name}: <15")

        elif index % 2 == 1:
            print(f"{recipie_content}")

app_is_running = True


while app_is_running:
    user_input = input(prompt)

    user_input = user_input.lower()
    user_input = str(user_input)

    if user_input == 'showInTable':
        show_recipies_in_table()

    elif (user_input == 'end') or (user_input == 'exit'):
        print('>> Escaped program <<')
        app_is_running = False

    elif (user_input != 'end') or (user_input != 'exit'):
        recipie_name, recipipe_content = user_input.split(':', maxsplit=1)

        add_recipie(recipie_name, recipipe_content)

        print(f'\n> Saved <\n{recipie_name.capitalize()}:\n  {recipipe_content}')