import unittest
from algorithms.loop.breadth_first_search import search

class TestBreadthFirstSearch(unittest.TestCase):
    def create_names_graph(self):
        grafo = {}
        grafo['voce'] = ['alice', 'bob', 'claire']
        grafo['alice'] = ['peggy']
        grafo['bob'] = ['anuj', 'peggy']
        grafo['claire'] = ['jonny', 'thom']
        grafo['peggy'] = []
        grafo['anuj'] = []
        grafo['jonny'] = []
        grafo['thom'] = []

        return grafo

    def name_ends_with_b(self, name):
        return name[-1] == 'b'

    def name_ends_with_m(self, name):
        return name[-1] == 'm'

    def name_ends_with_z(self, name):
        return name[-1] == 'z'

    def name_is_length_six(self, name):
        return len(name) == 6

    def test_search(self):
        grafo = self.create_names_graph()
        self.assertEqual(search(grafo, 'voce', self.name_ends_with_m), 'thom')
        self.assertEqual(search(grafo, 'voce', self.name_ends_with_b), 'bob')
        self.assertEqual(search(grafo, 'voce', self.name_ends_with_z), None)
        self.assertEqual(search(grafo, 'voce', self.name_is_length_six), 'claire')
