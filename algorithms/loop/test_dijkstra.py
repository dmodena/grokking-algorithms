import unittest
from algorithms.loop.dijkstra import search

class TestDijkstra(unittest.TestCase):
    def create_graph(self):
        grafo = {}
        grafo['livro'] = {}
        grafo['livro']['lp'] = 5
        grafo['livro']['poster'] = 0
        grafo['lp'] = {}
        grafo['lp']['baixo'] = 15
        grafo['lp']['bateria'] = 20
        grafo['poster'] = {}
        grafo['poster']['baixo'] = 30
        grafo['poster']['bateria'] = 35
        grafo['baixo'] = {}
        grafo['baixo']['piano'] = 20
        grafo['bateria'] = {}
        grafo['bateria']['piano'] = 10
        grafo['piano'] = {}

        return grafo

    def test_search(self):
        grafo = self.create_graph()
        self.assertEqual(search(grafo, 'livro', 'piano'), ['livro', 'lp', 'bateria', 'piano'])
