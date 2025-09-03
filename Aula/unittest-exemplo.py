import unittest

def somar(numero1: int, numero2: int) -> int:
    return numero1+numero2

class TestCalculadora(unittest.TestCase):
    def test_somar(self) -> None:
        # Arrange
        val1 = 5
        val2 = 5

        # Act
        resultado = somar(val1,val2)
        print(f"resultado test {resultado}")

        # Assert
        self.assertIsInstance(resultado, int, msg="mensagem")
        self.assertEqual(resultado, 10)

if __name__ == "__main__":
    # print(somar(5,5))

    unittest.main()