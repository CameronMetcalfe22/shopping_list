from dataclasses import dataclass
from typing import List


@dataclass
class Ingredient:
    name: str
    qty: int
    unit: str


@dataclass
class Recipe:
    id: str
    name: str
    ingredients: List[Ingredient]
