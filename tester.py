prompt = "\n-----------------------------------------------------"
prompt += "\nEnter the recipie in this order:\n"
prompt += "  'KEY: recipie_name' : 'VALUE: recipie_content'\n"
prompt += "If you want to exit the program type ['end()'] or ['exit()']."
prompt += "\n-----------------------------------------------------"
prompt += "\n[~! REMEMBER ABOUT CORRECT RECIPIE FORMAT !~]"
prompt += "\n\n>>>"

recipies = {}
formatted_recipies = []

recipie_name = recipies.keys()
recipie_content = recipies.values()

recipies_count = 0

app_is_running = True
is_command = False

def add_recipie(name, content):
    global recipies_count
    recipies[name] = content
    recipies_count += 1

# NOT WORKING 
def show_all_formatted_recipies():
    """Display nice-formatted recipies"""
    for name, recipie in recipies.items():
        formatted_recipies.append(name)
        formatted_recipies.append(recipie)
        print(formatted_recipies)

    for index in range(len(formatted_recipies)):
        if index % 2 == 0:
            print(f"{recipie_name}: <15")

        elif index % 2 == 1:
            print(f"{recipie_content}")

def format_error_comunicate():
    syntax_comunicate = "\n!!! Wrong formatted recipie.\n    Read the prompt above !!!"
    print(syntax_comunicate)

# Main app loop
while app_is_running:
    user_input = input(prompt)

    user_input = user_input.lower()
    user_input = str(user_input) 

    # Ignore white spaces
    if user_input == '':
        is_command = False
        print('\n!!! Nothing to add !!!')
        continue

    # Check if user_input DOESN'T HAVE ":" but it IS A COMMAND
    if ":" not in user_input and is_command == True:
        continue

    # Check if user_input DOESN'T HAVE ":" but it IS > NOT < A COMMAND
    if ":" not in user_input and is_command == False:
        format_error_comunicate()
        continue

    # Recognise the recipies adding
    else:
        if (user_input != 'end()') or (user_input != 'exit()'):
            recipie_name, recipipe_content = user_input.split(':', maxsplit=1)

            add_recipie(recipie_name, recipipe_content)

            print(f'\n> Saved <\n{recipie_name.capitalize()}:\n  {recipipe_content}')

    if (user_input == 'end()') or (user_input == 'exit()'):
        is_command = True
        print('\n---------------------\n>> Escaped program <<\n---------------------')
        app_is_running = False
        print(f"\n@| You've added {recipies_count} recipie/s |@")

    elif user_input == 'showAll()':
        is_command = True
        show_all_formatted_recipies()