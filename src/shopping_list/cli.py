from shopping_list.recipes import load_recipes


def main() -> None:
    recipes = load_recipes()

    for recipe in recipes:
        print(recipe)


if __name__ == "__main__":
    main()
