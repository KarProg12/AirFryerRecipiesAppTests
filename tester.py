import textwrap

<<<<<<< HEAD
recipies = {}
recipies_table = []
=======
recipes = {}
>>>>>>> ea61f6cc8ce35a710465643cc289e41ec668a8d0

prompt = f"""\n-----------------------------------------------------
Enter the recipe in this order:
  'KEY: recipe_name' : 'VALUE: recipe_content'
Type ['/man'] to show user manual.
-----------------------------------------------------
[~! REMEMBER ABOUT CORRECT recipe FORMAT !~]
\n>>>"""

# List of app's commands
commands = ['/help', '/shall', '/end', '/exit']

<<<<<<< HEAD
def show_recipies_in_table():
    """Display nice-formatted recipies"""
    list_index = len(recipies_table)

    for name, recipie in recipies.items():
        name.append()
        recipie.append()

    for index in range(list_index):
        if index % 2 == 0:
            print(f"{recipie_name}: <15")
=======
def nothing_to_add() -> None:
    print("!!! Nothing to add !!!")

>>>>>>> ea61f6cc8ce35a710465643cc289e41ec668a8d0

def add_recipe(name, content) -> None:
    recipes[name] = content


<<<<<<< HEAD

while app_is_running:
    user_input = input(prompt)
=======
# Print all recipes in table
def print_all_recipes_in_table() -> None:
    """Display table-formatted recipes"""
    if not recipes:
        print("\n!!! There's no recipes yet !!!")
        return
>>>>>>> ea61f6cc8ce35a710465643cc289e41ec668a8d0

    for name, recipe in recipes.items():
        formatted_recipe = recipe.replace(',', ',\n')
        formatted_recipe = textwrap.indent(formatted_recipe, '  ')
        print(f"\n{name.capitalize()}:\n"
              f"{formatted_recipe}\n--------------------------")

<<<<<<< HEAD
    if user_input == 'showInTable':
        show_recipies_in_table()

    elif (user_input == 'end') or (user_input == 'exit'):
        print('>> Escaped program <<')
        app_is_running = False
=======
user_help_menu = """
> Type ['/end'] or ['/exit'] to escape the program.
> Type ['/shall'] to display all recipes in table."""

def print_user_manual() -> None:
    print(user_help_menu)
>>>>>>> ea61f6cc8ce35a710465643cc289e41ec668a8d0

def format_error() -> None:
    format_communicate = """\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
!!! ERROR: Read the prompt above !!!"""
    print(format_communicate)


# Main app loop
while True:

    try:
        # .strip() deletes unwanted spaces at the beginning and at the end
        user_cmd = input(prompt).strip().lower()
    # If user's input is Ctrl + C or Ctr + D escape the program without any errors and print summary of recipes
    except(EOFError, KeyboardInterrupt):
        print('\n---------------------\n>> Escaped program <<\n---------------------')
        print(f"\n@| You've added {len(recipes)} recipe/s |@")
        break


    # ---COMMANDS-CHECKS---
    # Check for program exiting command
    if user_cmd == '/end' or user_cmd == '/exit':
        print('\n---------------------\n>> Escaped program <<\n---------------------')
        print(f"\n@| You've added {len(recipes)} recipe/s |@")
        break

    # Display all recipes in table (for now it is primitive)
    elif user_cmd == '/shall':
        print_all_recipes_in_table()
        continue

    # Check for /man (user manual command)
    elif user_cmd == '/man':
        print_user_manual()
        continue

    # ---ERRORS-PREDICTING---
    # Check for white spaces
    if user_cmd == '':
        nothing_to_add()
        continue

    # If ":" is not in user's input print error about incorrect recipe format
    if ":" not in user_cmd:
        format_error()
        continue

    # if everything's ok add recipe
    # split user_cmd after ":"
    recipe_name, recipe_content = user_cmd.split(':', maxsplit=1)

    # Check if user typed recipe without name or only recipe name without content and display communicate
    if not recipe_name.strip() or not recipe_content.strip():
        nothing_to_add()
        continue

    # After all validations above if everything is ok add recipe to dict
    add_recipe(recipe_name.strip(), recipe_content.strip())
    print(f'\n> Saved <\n{recipe_name.strip().capitalize()}:\n  {recipe_content.strip()}')
