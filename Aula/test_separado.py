from pyt_exemplo import somar, multiplicar


def test_somar():
    # Arrange
    val1 = 5
    val2 = 5

    # Act
    resultado = somar(val1,val2)
    print(f"resultado test {resultado}")

    # Assert
    assert isinstance(resultado,int), "mensagem de tipo não passou"
    assert resultado == 10

def test_multiplicar():
    # Arrange
    val1 = 5
    val2 = 5

    # Act
    resultado = multiplicar(val1,val2)
    print(f"resultado test {resultado}")

    # Assert
    assert isinstance(resultado,int), "mensagem de tipo não passou"
    assert resultado == 25