import datetime
import unittest
from genetic_2 import GA2

class OneMaxTest(unittest.TestCase):
    def __init__(self, length = 100):
        self.length = length

    def test(self):
        geneset = [0, 1]
        startTime = datetime.datetime.now()

        def fnDisplay(candidate):
            display(candidate, startTime)

        def fnGetfitness(genes):
            return get_fitness(genes)

        # el fitness óptimo es el que equivale a la longitud del geneSet
        optimalFitness = self.length
        best = GA2.get_best(fnGetfitness, self.length, optimalFitness,
                                geneset, fnDisplay)
        self.assertEqual(best.Fitness, optimalFitness)

# Cuenta el número de 1s en el arreglo, el valor resultatnte corresponde al fitness del problema
def get_fitness(genes):
    return(genes.count(1))

def display(candidate, startTime, proportion_to_display = 0.2):
    timeDiff = datetime.datetime.now() - startTime
    # printing
    # Calculamos la proporción del gen que mostraremos en el display
    proportion_size = candidate.length * proportion_to_display / 2
    print('{0}...{1}\t{2:3.2f}\t{3}'.format(
        ''.join(map(str, candidate.Genes[: proportion_size])),
        ''.join(map(str, candidate.Genes[-proportion_size:])),
        candidate.Fitness,
        str(timeDiff)
    ))