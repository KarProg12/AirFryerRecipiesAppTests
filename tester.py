import textwrap

recipes = {}

prompt = f"""\n-----------------------------------------------------
Enter the recipe in this order:
  'KEY: recipe_name' : 'VALUE: recipe_content'
Type ['/help'] to show available commands.
-----------------------------------------------------
[~! REMEMBER ABOUT CORRECT recipe FORMAT !~]
\n>>> """

def nothing_to_add() -> None:
    print("\n!!! Nothing to add !!!")


def add_recipe(name, content) -> None:
    recipes[name] = content

def del_recipe(recipe_name_to_del) -> None:
    """Deletes the recipe by name"""
    # Check if there are no recipes yet
    if not recipes:
        print("\n!!! There's no recipes yet !!!")
        return

    # Pass the user input to the function's argument
    recipe_name_to_del = input("\n>>>  Enter recipe name to delete\n>>> ").strip().lower()

    # Save the popped recipe do variable to display later
    deleted_recipe = recipes.pop(recipe_name_to_del, None)

    # Check for default value from .pop()
    if deleted_recipe is not None:
        print(f"\n> Successfully removed: {recipe_name_to_del.capitalize()} <")

    else:
        print(f"\n!!! Error 404: Not found: {recipe_name_to_del.capitalize()} !!!")

# Print all recipes in table
def print_all_recipes_in_table() -> None:
    """Display table-formatted recipes"""
    if not recipes:
        print("\n!!! There's no recipes yet !!!")
        return

    for name, recipe in recipes.items():
        formatted_recipe = recipe.replace(',', ',\n')
        formatted_recipe = textwrap.indent(formatted_recipe, '  ')
        print(f"\n{name.capitalize()}:\n"
              f"{formatted_recipe}\n--------------------------")

user_help_menu = """
> Type ['/end'] or ['/exit'] to escape the program.
> Type ['/shall'] to display all recipes in table.
> Type ['/del'], ['/delete'] or ['/rm'] 
   to enter the deleting by name mode 
   (SUGGESTION: first type ['/shall'] to show what's the name of the recipe)."""

def print_user_manual() -> None:
    print(user_help_menu)

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
    match user_cmd:
        case '/end' | '/exit':
            print('\n---------------------\n>> Escaped program <<\n---------------------')
            print(f"\n@| You've added {len(recipes)} recipe/s |@")
            break
        case '/help':
            print_user_manual()
            continue
        case '/shall':
            print_all_recipes_in_table()
            continue
        case '/delete' | '/del' | '/rm':
            del_recipe(user_cmd)
            continue

        # ---ERRORS-PREDICTING---
        # Check for white spaces
        case '':
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
