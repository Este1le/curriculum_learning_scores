import argparse
import jenkspy

parser = argparse.ArgumentParser(description='Split scores of sentences into buckets based on Jenks natural breaks classification method')

parser.add_argument('--scr', dest='scr', type=str, required=True, 
                    help='Sentence score file')
parser.add_argument('--num-buckets', dest='num_buckets', type=int, required=True, 
                    help='Number of buckets to be generated')
parser.add_argument('--trg', dest='trg', type=str, required=True,
                    help='Target file for recording the bucket for each sentence')

args = parser.parse_args()

# Read sentence scores
with open(args.scr, 'r') as f:
    lines = f.readlines() 
scores = [float(score.strip()) for score in lines]

# Get the breaks to arrange scores to different classes
breaks = jenkspy.jenks_breaks(scores, nb_class=args.num_buckets)

# Assign sentences to correponding score buckets
sen_buckets = []
for s in range(len(scores)):
    for i in range(len(breaks)-1):
        s_score = scores[s]
        if breaks[i] <= s_score and breaks[i+1] >= s_score:
            sen_buckets.append(str(i))
            break

# Print number of sentences in each bucket
counts = [0] * args.num_buckets
for sb in sen_buckets:
    counts[int(sb)] += 1
print("There are {} buckets of scores.".format(args.num_buckets))
print("Sentence counts in buckets are: " + ','.join([str(c) for c in counts]) + '.')

# Write bucket assignment into target file
with open(args.trg, 'w') as f:
    f.write('\n'.join(sen_buckets))


