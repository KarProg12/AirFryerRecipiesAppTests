import textwrap

recipes = {}

prompt = f"""\n-----------------------------------------------------
Enter the recipe in this order:
  'KEY: recipe_name' : 'VALUE: recipe_content'
Type ['/man'] to show user manual.
-----------------------------------------------------
[~! REMEMBER ABOUT CORRECT recipe FORMAT !~]
\n>>>"""

manual_menu = """
> Type ['/end'] or ['/exit'] to escape the program.
> Type ['/shall'] to display all recipes in table."""

def nothing_to_add():
    print("!!! Nothing to add !!!")

def add_recipe(name, content):
    recipes[name] = content

# NOT WORKING 
def print_all_recipes_in_table():
    """Display table-formatted recipes"""
    if not recipes:
        print("\n!!! There's no recipes yet !!!")
        return
    
    for name, recipe in recipes.items():
        formatted_recipe = recipe.replace(',', ',\n')
        formatted_recipe = textwrap.indent(formatted_recipe, '  ')
        print(f"\n{name.capitalize()}:\n"
              f"{formatted_recipe}\n--------------------------")
        
 
def print_user_manual():
    print(manual_menu)


def format_error():
    format_communicate = """\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
!!! ERROR: Read the prompt above !!!"""
    print(format_communicate)
    return

# Main app loop
while True:
    # .strip() deletes unwanted spaces at the beginning and at the end
    user_input = input(prompt).strip()

    # Check for program exiting command
    if user_input.lower() == '/end' or user_input.lower() == '/exit':
        print('\n---------------------\n>> Escaped program <<\n---------------------')
        print(f"\n@| You've added {len(recipes)} recipe/s |@")
        break

    # Display all recipes in table
    elif user_input.lower() == '/shall':
        print_all_recipes_in_table()
        continue

    elif user_input.lower() == '/man':
        print_user_manual()
        continue
    
    # Check for white spaces
    if user_input == '':
        nothing_to_add()
        continue

    if ":" not in user_input:
        format_error()
        continue

    # if everything's ok add recipe
    # split user_input after ":"
    recipe_name, recipe_content = user_input.split(':', maxsplit=1)

    # Check if user typed recipe without name or only recipe name without content and display communicate
    if not recipe_name.strip() or not recipe_content.strip():
        nothing_to_add()
        continue

    add_recipe(recipe_name.strip(), recipe_content.strip())
    print(f'\n> Saved <\n{recipe_name.strip().capitalize()}:\n  {recipe_content.strip()}')
