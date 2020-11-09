import unittest
import gato

class testgato(unittest.TestCase):
    """docstring for testgato."""
    '''test for correct init of board'''
    def test_initboard(self):
        self.assertEqual(gato.initboard(),[['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']])
    '''test if player won, first tests rows, then diagonals then columns'''
    def test_win(self):
        self.assertEqual(gato.win([['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']],'x'),False)
        self.assertEqual(gato.win([['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']],'o'),False)
        self.assertEqual(gato.win([['x', 'x', 'x'], ['_', '_', '_'], ['_', '_', '_']],'x'),True)
        self.assertEqual(gato.win([['o', 'o', 'o'], ['_', '_', '_'], ['_', '_', '_']],'o'),True)
        self.assertEqual(gato.win([['o', 'o', 'o'], ['_', '_', '_'], ['_', '_', '_']],'x'),False)
        self.assertEqual(gato.win([['o', '_', '_'], ['_', 'o', '_'], ['_', '_', 'o']],'o'),True)
        self.assertEqual(gato.win([['_', '_', 'x'], ['_', 'x', '_'], ['x', '_', '_']],'x'),True)
        self.assertEqual(gato.win([['x', '_', '_'], ['x', '_', '_'], ['x', '_', '_']],'x'),True)

    def test_toggle(self):
        self.assertEqual(gato.toggleplayer(0),'x')
        self.assertEqual(gato.toggleplayer(1),'o')
if __name__=='__main__':
    unittest.main()
