from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1 commit
def test_ingredient():
    ingrediente_um = Ingredient('acucar')
    ingrediente_dois = Ingredient('ovo')
    ingrediente_tres = Ingredient('farinha')

    assert ingrediente_tres != ingrediente_dois
    assert ingrediente_tres == ingrediente_tres

    assert hash(ingrediente_dois) != hash(ingrediente_tres)
    assert hash(ingrediente_dois) != hash(ingrediente_um)
    assert hash(ingrediente_dois) == hash(ingrediente_dois)

    assert repr(ingrediente_dois) == "Ingredient('ovo')"
    assert ingrediente_dois.name == 'ovo'

    assert ingrediente_tres.restrictions == {Restriction.GLUTEN}
