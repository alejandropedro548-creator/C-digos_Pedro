
import unittest
from media import calcular_media, classificar_media

class TestMedia(unittest.TestCase):
    def test_calcular_media_basico(self):
        self.assertAlmostEqual(calcular_media([7, 8, 6, 9]), 7.5, places=2)

    def test_calcular_media_uma_nota(self):
        self.assertAlmostEqual(calcular_media([10]), 10.0, places=2)

    def test_calcular_media_erro_lista_vazia(self):
        with self.assertRaises(ValueError):
            calcular_media([])

    def test_classificar_media_aprovado(self):
        self.assertEqual(classificar_media(7.0), "Aprovado(a) ✅")
        self.assertEqual(classificar_media(9.5), "Aprovado(a) ✅")

    def test_classificar_media_recuperacao(self):
        self.assertEqual(classificar_media(5.0), "Recuperação ⚠️")
        self.assertEqual(classificar_media(6.9), "Recuperação ⚠️")

    def test_classificar_media_reprovado(self):
        self.assertEqual(classificar_media(4.99), "Reprovado(a) ❌")

if __name__ == '__main__':
    unittest.main()
