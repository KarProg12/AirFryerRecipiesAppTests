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
    # .strip() deletes unnessesary spaces at the beginning and at the and
    user_input = input(prompt).strip().lower()

    # Check for program exitting command
    if user_input == 'end()' or user_input == 'exit()':
        is_command = True
        print('\n---------------------\n>> Escaped program <<\n---------------------')
        app_is_running = False
        print(f"\n@| You've added {recipies_count} recipie/s |@")
        continue

    # Display all recipies in table
    elif user_input == 'showall()':
        is_command = True
        show_all_formatted_recipies()
        continue

    # Check for white spaces
    if user_input == '':
        is_command = False
        print('\n!!! Nothing to add !!!')
        continue

    # Check if format of recipie is good
    if ":" not in user_input:
        format_error_comunicate()
        continue

    # if everything's ok add recipie
    # split user_input after ":"
    recipie_name, recipipe_content = user_input.split(':', maxsplit=1)
    add_recipie(recipie_name.strip(), recipipe_content.strip())
    print(f'\n> Saved <\n{recipie_name.strip().capitalize()}:\n  {recipipe_content.strip()}')
