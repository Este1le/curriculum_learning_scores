import argparse
import string 

parser = argparse.ArgumentParser(description='Calculate sentence ranks by different metrics')

parser.add_argument('--src', dest='src', type=str, required=True,
                    help='BPE file')
parser.add_argument('--wf', dest='wf', type=str, required=True,
                    help='Word frequency file')
parser.add_argument('--trg', dest='trg', type=str, required=True,
                    help='Target file recording ranks of sentences')
parser.add_argument('--rank',dest='rank',type=str,choices=['max','average'],
                    help='Type of sentence rank')

args = parser.parse_args()

# Read BPE file
sens = []
with open(args.src, 'r') as f:
    lines = f.readlines()

sens = [[w for w in line.strip().split()
        if (w not in string.punctuation) and (not w.isdigit())] 
        for line in lines]

# Read word frequency file
word_rank_dict = {}
with open(args.wf, 'r') as f:
    lines = f.readlines()
for line in lines:
    rank, word, freq = line.strip().split()
    word_rank_dict[word] = int(rank)

# Map words in sentences to ranks
sen_word_ranks = [[word_rank_dict[w] for w in s] if s else [0] for s in sens]

# Calculate scores for sentences
sen_ranks = []
for wrs in sen_word_ranks:
    if args.rank == 'max':
        sen_ranks.append(max(wrs))
    elif args.rank == 'average':
        sen_ranks.append(round(sum(wrs)/float(len(wrs))))

# Write sentence scores into target file
with open(args.trg, 'w') as f:
    f.write('\n'.join([str(r) for r in sen_ranks]))

