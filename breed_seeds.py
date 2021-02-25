import argparse
import numpy as np

parser = argparse.ArgumentParser(description='When two seeds love each other very much...')
parser.add_argument('seed1', type=int,
                    help='First seed')
parser.add_argument('seed2', type=int,
                    help='Second seed', nargs='?', default=None)
parser.add_argument('--num_children', type=int, default=10,
                    help='Number of child seeds to generate')
parser.add_argument('--mutation_strength', type=float, default=1,
                    help='how much randomness to add')

args = parser.parse_args()


def seed_to_array(seed, latent_size=512):
	formatter = "{:0" + str(latent_size) + "b}"
	return np.array([(1 if x == '1' else -1) for x in formatter.format(seed)])

def random_child(array1, array2, mutation_strength=1):
	average = array1 + array2
	noise = np.random.randn(len(average))*mutation_strength
	child = average + noise
	child[child > 0] = 1
	child[child <= 0] = -1
	return child

def array_to_seed(array):
	return int("".join(str(int(x > 0)) for x in array), 2)

array1 = seed_to_array(args.seed1)
array2 = array1
if args.seed2 is not None:
	array2 = seed_to_array(args.seed2)

print(",".join([str(array_to_seed(random_child(array1, array2, args.mutation_strength))) for _ in range(args.num_children)]))

