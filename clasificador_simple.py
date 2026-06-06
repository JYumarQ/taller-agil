import unittest

# Función a desarrollar (HU02)
def limpiar_texto(texto):
    return texto

# Función a desarrollar (HU03 y HU06)
def clasificar_sentimiento(texto):
    return "Neutral"

# Pruebas Unitarias (HU04)
class TestClasificador(unittest.TestCase):
    def test_clasificacion_positiva(self):
        texto_limpio = limpiar_texto("¡El hotel es MARAVILLOSO y excelente!")
        resultado = clasificar_sentimiento(texto_limpio)
        self.assertEqual(resultado, "Positiva")

if __name__ == '__main__':
    unittest.main()
