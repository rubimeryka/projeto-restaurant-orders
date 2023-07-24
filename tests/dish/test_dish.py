from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    omelete = Dish("omelete", 15.90)
    lasanha = Dish("lasanha", 30.50)
    omelete_02 = Dish("omelete", 15.90)

    expected_repr = f"Dish('{omelete.name}', R${omelete.price:.2f})"
    assert repr(omelete) == expected_repr

    assert omelete == omelete_02
    assert omelete != lasanha

    assert hash(omelete) == hash(omelete_02)
    assert hash(omelete) != hash(lasanha)

    ovo = Ingredient("ovo")
    omelete.add_ingredient_dependency(ovo, 3)

    assert omelete.recipe.get(ovo) == 3
    assert omelete.get_restrictions() == {Restriction.ANIMAL_DERIVED}
    assert omelete.get_ingredients() == {Ingredient("ovo")}

    with pytest.raises(TypeError):
        Dish("omelete", "churros")

    with pytest.raises(ValueError):
        Dish("omelete", -15.90)
