from pathlib import Path
import yaml


DATA_DIR = Path(__file__).resolve().parents[2] / "data"
RECIPES_FILE = DATA_DIR / "recipes.yaml"


def load_recipes() -> dict:
    """Load recipes from the YAML file."""
    with RECIPES_FILE.open() as f:
        data = yaml.safe_load(f)
    return data
