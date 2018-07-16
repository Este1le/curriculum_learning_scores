import random
import argparse

parser = argparse.ArgumentParser(description="Generate random scores for samples.")

parser.add_argument('--num-samples', dest='num_samples', type=int, required=True,
                    help="Number of samples in the dataset.")

parser.add_argument('--trg', dest='trg', required=True, help="Target file to store scores.")

args = parser.parse_args()

random.seed(13)

with open(args.trg, 'w') as f:
    f.write("\n".join([str(random.randint(0,4)) for i in range(args.num_samples)]))
    f.write("\n")
