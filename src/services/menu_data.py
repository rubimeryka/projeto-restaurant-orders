import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.load_file(source_path)

    def load_file(self, source_path: str) -> None:
        with open(source_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                dish_name = row['dish']
                dish_price = float(row['price'])
                ingredient_name = row['ingredient']
                recipe_amount = int(row['recipe_amount'])

                # Find or create the dish instance
                dish = next(
                    (d for d in self.dishes if d.name == dish_name),
                    None
                )
                if dish is None:
                    dish = Dish(dish_name, dish_price)
                    self.dishes.add(dish)

                # Create and add ingredient dependency
                ingredient = Ingredient(ingredient_name)
                dish.add_ingredient_dependency(ingredient, recipe_amount)
