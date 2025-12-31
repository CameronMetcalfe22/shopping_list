from pathlib import Path
import yaml

from shopping_list.models import Recipe, Ingredient


DATA_DIR = Path(__file__).resolve().parents[2] / "data"
RECIPES_FILE = DATA_DIR / "recipes.yaml"


def load_recipes() -> list[Recipe]:
    with RECIPES_FILE.open() as f:
        raw_data = yaml.safe_load(f)

    recipes = []

    for recipe_dict in raw_data["recipes"]:
        ingredients = [
            Ingredient(
                name=ing["name"],
                qty=ing["qty"],
                unit=ing["unit"],
            )
            for ing in recipe_dict["ingredients"]
        ]

        recipe = Recipe(
            id=recipe_dict["id"],
            name=recipe_dict["name"],
            ingredients=ingredients,
        )

        recipes.append(recipe)

    return recipes
