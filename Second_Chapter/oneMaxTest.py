import datetime
import unittest
import genetic 

class OneMaxTest(unittest.TestCase):
    def test(self, length = 100):
        geneset = (0, 1)

    # Cuenta el número de 1s en el arreglo
    def get_fitness(genes):
        return(genes.count(1))

    def display(candidate, startTime):
        timeDiff = datetime.datetime.now() - startTime