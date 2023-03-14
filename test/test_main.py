from .main import suma


#test unitarios
def test_suma_enteros():
    assert suma(1, 2) == 3


def test_suma_text():
    assert suma("1", "2") == "Error"


def test_suma_vacio():
    assert suma() == 0
