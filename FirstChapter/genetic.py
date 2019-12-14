# Reusable engine
import random
import datetime

class Chormosome:
    def __init__(self, genes, fitness):
        self.Genes = genes
        self.Fitness = fitness


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
        genes_str = ''.join(genes)
        # Se obtiene el fitness
        fitness =  self.get_fitness(genes_str)
        parent = Chormosome(genes_str, fitness)
        return(parent)

    def _mutate(self, parent):
        index = random.randrange(0, len(parent.Genes))
        childGenes = list(parent.Genes)
        newGene, alternate = random.sample(self.geneSet, 2)
        childGenes[index] = alternate \
            if newGene == childGenes[index] \
            else newGene
        childGenes_str = ''.join(childGenes)
        child_fitness = self.get_fitness(childGenes_str)
        child = Chormosome(childGenes_str, child_fitness)
        return(child)

    def get_fitness(self, genes):
        n_matches = sum(1 for expected_i, actual_guess_i in zip(self.target, genes)\
                        if expected_i == actual_guess_i)
        fitness = n_matches / self.length_target
        return(fitness)

    def display(self, parent):
        fitness = parent.Fitness
        timeDiff = datetime.datetime.now() - self.startTime
        print(F'{parent.Genes}\t{round(fitness, 3)}\t{str(timeDiff.total_seconds())} segundos')

    def get_best(self, verbose = True):
        self.startTime = datetime.datetime.now()
        bestParent = self._generate_parent()
        # bestFitness = self.get_fitness(bestParent)
        if verbose:
            print('Guess\t\tFitness\t\tTime')
            self.startTime = datetime.datetime.now()
            self.display(bestParent)
        # Optimizamos
        while bestParent.Fitness < self.optimalFitness:
            child = self._mutate(bestParent)
            # Si el fitness del padre es mayor, no actualizar
            if bestParent.Fitness >= child.Fitness:
                continue
            if verbose:
                self.display(child)
            if child.Fitness >= self.optimalFitness:
                return(child)
            # Si child tiene un fitness mayor al padre, pero menor al óptimo
            # actualiza
            bestParent = child

