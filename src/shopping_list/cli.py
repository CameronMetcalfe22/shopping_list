def main() -> None:
    print("shopping_list: it works!")


if __name__ == "__main__":
    main()

from shopping_list.recipes import load_recipes


def main() -> None:
    recipes = load_recipes()
    print(recipes)


if __name__ == "__main__":
    main()
