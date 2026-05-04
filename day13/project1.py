def load_recipes():
    recipes = {}
    try:
        with open("recipes.txt", "r") as f:
            for line in f:
                line = line.strip()
                if ":" in line:
                    name, ingredients = line.split(":", 1)
                    recipes[name.strip()] = ingredients.strip()
    except FileNotFoundError:
        print("Error: recipes.txt not found. Please ensure it is in the same folder you are running from.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return recipes

def show_recipe(recipes):
    print("available recipes: ")
    for r in recipes:
        print("-", r)
    choice = input("enter your recipe name: ")

    if choice in recipes:
        print("ingredients: ", recipes[choice])
    else:
        print("recipe not found")


# Main

recipes = load_recipes()
show_recipe(recipes)