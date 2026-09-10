prompt = "\n-----------------------------------------------------"
prompt += "\nEnter the recipie in this order:\n"
prompt += "  'KEY: recipie_name' : 'VALUE: recipie_content'\n"
prompt += "If you want to exit the program type 'end' or 'exit'."
prompt += "\n-----------------------------------------------------"
prompt += "\n>>>"

recipies = {}


def add_recipie(name, content):
    recipies[recipie_name] = recipie_content

app_is_running = True

while app_is_running:
    user_input = input(prompt)

    user_input = user_input.lower()
    user_input = str(user_input)

    if (user_input == 'end') or (user_input == 'exit'):
        print('>> Escaped program <<')
        app_is_running = False

    elif (user_input != 'end') or (user_input != 'exit'):
        recipie_name, recipie_content = user_input.split(':', maxsplit=1)

        add_recipie(recipie_name, recipie_content)

        print(f'\n> Saved <\n{recipie_name.capitalize()}:\n  {recipie_content}')
