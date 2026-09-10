prompt = "\n-----------------------------------------------------"
prompt += "\nEnter the recipie in this order:\n"
prompt += "  'KEY: recipie_name' : 'VALUE: recipie_content'\n"
prompt += "If you want to exit the program type 'end' or 'exit'."
prompt += "\n-----------------------------------------------------"
prompt += "\n>>>"

# Store user input in dict 'recipies'
recipies = {}

def add_recipie(name, content):
    # Assign: '"key:[recipie_name]": "value:recipie"'
    recipies[recipie_name] = recipie_content

# Flag for escaping the while loop with command 'end'
app_is_running = True

while app_is_running:
    # Store user's input in user_input variable
    user_input = input(prompt)

    # Use .lower() method just for clarity
    user_input = user_input.lower()
    user_input = str(user_input)
    
    # if user_input == 'end' escape while loop and print 'goodbye' or something
    if (user_input == 'end') or (user_input == 'exit'):
        print('>> Escaped program <<')
        app_is_running = False

    elif (user_input != 'end') or (user_input != 'exit'):
        # Split user_input after ':' and save name of the recipie in recipie_name key
        # and ingredients of the recipie as value of the key
        recipie_name, recipie_content = user_input.split(':', maxsplit=1)

        add_recipie(recipie_name, recipie_content)

        # Display recipie_name and in new line and recipie_content after tabulator
        print(f'\n> Saved <\n{recipie_name.capitalize()}:\n  {recipie_content}')
