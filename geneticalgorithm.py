import random
import argparse

DICT = {'0000' : 0,
'0001' : 1,
'0010' : 2,
'0011' : 3,
'0100' : 4,
'0101' : 5,
'0110' : 6,
'0111' : 7,
'1000' : 8,
'1001' : 9,
'1010' : '+',
'1011' : '-',
'1100' : '*',
'1101' : '/'}

parser = argparse.ArgumentParser(prog='geneticalgorithm')
parser.add_argument('-n', '--number', type=float, default=random.randint(0, 1000), help='Target number')
parser.add_argument('-l', '--length', type=int, default=300, help='Chromosome length')
parser.add_argument('-c', '--crossover', type=float, default=0.7, help='Crossover rate')
parser.add_argument('-m', '--mutation', type=float, default=0.01, help='Mutation rate')

args = parser.parse_args()

CHROMO_LENGTH = args.length
GENE_LENGTH = 4
POPULATION_SIZE = 100 # Must be even

CROSSOVER_RATE = args.crossover
MUTATION_RATE = args.mutation

def main():
    target_num = args.number

    population = []
    # Generate Initial Population
    for i in range(POPULATION_SIZE):
        population.append([get_random_chromosome(), 0])

    # Search For A Solution
    generation = 0
    solution_found = False
    while(not solution_found):
        # Test population
        for chromosome in population:
            result, formula = decode_chromosome(chromosome[0])
            chromosome[1] = calculate_fitness(target_num, result)

        # Find best chromosome, then print information
        best_chromosome = [0, -999]
        for i in population:
            if i[1] > best_chromosome[1]:
                best_chromosome = i

        result, formula = decode_chromosome(best_chromosome[0])
        print('Generation: ' + str(generation))
        print('Target Number: ' + str(target_num))
        print(str(best_chromosome[1]) + ': ' + formula + ' = ' + str(result))
        print()

        if result == target_num:
            solution_found = True

        # Breed new generation
        new_population = []
        for i in range(int(POPULATION_SIZE / 2)):
            offspring1, offspring2 = crossover(roulette(population), roulette(population))
            mutate(offspring1)
            mutate(offspring2)
            new_population.append([offspring1, 0])
            new_population.append([offspring2, 0])

        population = new_population
        generation += 1

def crossover(chrom1, chrom2):
    if random.uniform(0, 1) <= CROSSOVER_RATE:
        crossover = random.randrange(0, CHROMO_LENGTH)
        offspring1 = chrom1[0: crossover] + chrom2[crossover:]
        offspring2 = chrom2[0: crossover] + chrom1[crossover:]
        return offspring1, offspring2
    return chrom1, chrom2

def mutate(chromosome):
    for i in range(len(chromosome)):
        if random.uniform(0, 1) <= MUTATION_RATE:
            if chromosome[i] == '0':
                chromosome[i] = '1'
            elif chromosome[i] == '1':
                chromosome[i] = '0'

def roulette(population):
    total_fitness = 0
    for i in population:
        total_fitness += i[1]

    pie_slice = random.uniform(0, 1) * total_fitness
    fitness = 0
    for i in population:
        fitness += i[1]
        if(fitness >= pie_slice):
            return i[0]

def calculate_fitness(target, result):
    if target == result:
        return 9999
    else:
        return 1 / abs(target - result)


def decode_chromosome(chrom):
    c = "".join(chrom)
    chromosome = [c[i:i+GENE_LENGTH] for i in range(0, len(c), GENE_LENGTH)]

    characters = []
    for i in chromosome:
        try:
            characters.append(DICT[str(i)])
        except KeyError:
            continue

    last_valid_character = ''
    result = 0
    formula = ''
    for i in characters:
        if last_valid_character == '' and is_integer(i):
            last_valid_character = i
            formula = formula + str(i)
            result = i
        elif last_valid_character == '' and not is_integer(i):
            continue
        else:
            if not is_integer(last_valid_character) and is_integer(i):
                if last_valid_character == '+':
                    result += i
                elif last_valid_character == '-':
                    result -= i
                elif last_valid_character == '*':
                    result *= i
                elif last_valid_character == '/':
                    if i == 0:
                        continue
                    result /= i
                last_valid_character = i
                formula = formula + str(i)
            elif is_integer(last_valid_character) and not is_integer(i):
                last_valid_character = i
                formula = formula + str(i)
    if not is_integer(formula[-1]):
        formula = formula[:-1]
    return result, formula

def is_integer(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

def get_random_chromosome():
    chromosome = []
    for i in range(CHROMO_LENGTH):
        chromosome.append(random.choice(('0', '1')))
    return chromosome

if __name__ == '__main__':
    main()
