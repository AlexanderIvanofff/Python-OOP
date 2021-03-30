from project.mammal import Mammal
import unittest


class MammalTest(unittest.TestCase):
    def setUp(self):
        self.mammal = Mammal('Pol', 'cat', 'mql')

    def test_name(self):
        self.assertEqual('Pol', self.mammal.name)

    def test_type(self):
        type_animal = self.mammal.type
        self.assertEqual('cat', type_animal)

    def test_sound(self):
        type_sound = self.mammal.sound
        self.assertEqual('mql', type_sound)

    def test_get_make_sound(self):
        sound = self.mammal.make_sound()
        self.assertEqual(sound, 'Pol makes mql')

    def test_kingdom_initial(self):
        result = self.mammal._Mammal__kingdom
        expected_result = "animals"
        self.assertEqual(result, expected_result)

    def test_get_kingdom(self):
        info = self.mammal.get_kingdom()
        self.assertEqual(info, 'animals')

    def test_info(self):
        info = self.mammal.info()
        self.assertEqual(info, 'Pol is of type cat')


if __name__ == '__main__':
    unittest.main()