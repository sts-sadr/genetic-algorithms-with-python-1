# Reusable engine
import random
import datetime

class GA1:
    def __init__(self, target, geneSet):
        self.target = target
        self.geneSet = geneSet
        self.length_target = len(target)
        self.startTime = 0
        self.optimalFitness = 1

    def _generate_parent(self):
        genes = []
        while len(genes) < self.length_target:
            sampleSize = min(self.length_target - len(genes), len(self.geneSet))
            genes.extend(random.sample(self.geneSet, sampleSize))
        return(''.join(genes))

    def _mutate(self, parent):
        index = random.randrange(0, len(parent))
        childGenes = list(parent)
        newGene, alternate = random.sample(self.geneSet, 2)
        childGenes[index] = alternate \
            if newGene == childGenes[index] \
            else newGene
        childGenes_str = ''.join(childGenes)
        return(childGenes_str)

    def get_fitness(self, genes):
        n_matches = sum(1 for expected_i, actual_guess_i in zip(self.target, genes)\
                        if expected_i == actual_guess_i)
        fitness = n_matches / self.length_target
        return(fitness)

    def display(self, genes):
        fitness = self.get_fitness(genes)
        timeDiff = datetime.datetime.now() - self.startTime
        print(F'{genes}\t{round(fitness, 3)}\t{str(timeDiff.total_seconds())} segundos')

    def get_best(self, verbose = False):
        # random.seed()
        bestParent = self._generate_parent()
        bestFitness = self.get_fitness(bestParent)
        self.display(bestParent)
        if verbose:
            print('Guess\t\tFitness\t\tTime')
            self.startTime = datetime.datetime.now()
        # Optimizamos
        while bestFitness < self.optimalFitness:
            child = self._mutate(bestParent)
            childFitness = self.get_fitness(child)
            # Si el fitness del padre es mayor, no actualizar
            if bestFitness >= childFitness:
                continue
            if verbose:
                self.display(child)
            if childFitness >= self.optimalFitness:
                return(child)
            # Si child tiene un fitness mayor al padre, pero menor al óptimo
            # actualiza
            bestFitness = childFitness
            bestParent = child

