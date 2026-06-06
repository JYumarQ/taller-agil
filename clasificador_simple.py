import unittest

# Función a desarrollar (HU02)
def limpiar_texto(texto):
    return texto

# Función a desarrollar (HU03 y HU06)
def clasificar_sentimiento(texto):
    positivas = ["excelente", "maravilloso", "bueno", "limpio"]
    negativas = ["malo", "sucio", "roto", "horrible"]
    texto_limpio = texto.lower()
    
    if any(p in texto_limpio for p in positivas):
        return "Positiva"
    elif any(n in texto_limpio for n in negativas):
        return "Negativa"
    return "Neutral"

# Pruebas Unitarias (HU04)
class TestClasificador(unittest.TestCase):
    def test_clasificacion_positiva(self):
        texto_limpio = limpiar_texto("¡El hotel es MARAVILLOSO y excelente!")
        resultado = clasificar_sentimiento(texto_limpio)
        self.assertEqual(resultado, "Positiva")

    def test_clasificacion_negativa(self):
        texto_limpio = limpiar_texto("La habitación estaba muy sucia y el servicio fue malo.")
        resultado = clasificar_sentimiento(texto_limpio)
        self.assertEqual(resultado, "Negativa")

if __name__ == '__main__':
    unittest.main()
