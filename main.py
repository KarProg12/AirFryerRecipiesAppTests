# ---IMPORTS---
import app_funcs


prompt = """\n---------------------------------------------------------
Enter the recipe in this order:
  'KEY: recipe_name' : 'VALUE: recipe_content'
Type ['/help'] to show available commands.
You can also search in recipes or in recipes ingredients.
---------------------------------------------------------
[~! REMEMBER ABOUT CORRECT recipe FORMAT !~]
\n>>> """

print("\n$$$ WELCOME TO THE AIR FRYER RECIPE APP $$$")


# ---MAIN-APP-LOOP---
while True:
    try:
        # .strip() deletes unwanted spaces at the beginning and at the end
        user_cmd = input(prompt).strip()
    # If user's input is Ctrl + C or Ctr + D escape the program without any errors and print summary of recipes
    except(EOFError, KeyboardInterrupt):
        print('\n---------------------\n>> Escaped program <<\n---------------------')
        print(f"\n@| You've added {len(app_funcs.recipes)} recipe/s |@")
        break

    match user_cmd.split(':', maxsplit=1):
        case ['']:
            app_funcs.nothing_to_add()

        # ---COMMANDS---
        case ['/end'] | ['/exit']:
            print('\n---------------------\n>> Escaped program <<\n---------------------')
            print(f"\n@| You've added {len(app_funcs.recipes)} recipe/s |@")
            break
        case ['/help']:
            app_funcs.print_user_manual()
        case ['/shall']:
            app_funcs.print_all_recipes_in_table()
        case ['/search']:
            app_funcs.search_recipe()
        case ['/del'] | ['/rm']:
            app_funcs.del_recipe()

        # Check if user typed recipe without name or only recipe name without content and display communicate
        case [name, content] if name.strip() and content.strip():
            # After all validations above if everything is ok add recipe to dict
            app_funcs.recipes[name.strip().lower()] = content.strip()
            print(f'\n> Saved <\n{name.strip().capitalize()}:\n  {content}')

        case _:
            app_funcs.print_format_error()