import argparse

parser = argparse.ArgumentParser(description='Calculate sentence lengths')

parser.add_argument('--src', dest='src', type=str, required=True,
                    help='BPE data')
parser.add_argument('--trg', dest='trg', type=str, required=True,
                    help='Target file recording the lengths of sentences')

args = parser.parse_args()

# Read sentences
with open(args.src, 'r') as f:
    lines = f.readlines()

# Calculate sentence length
sen_lengths = []
for l in lines:
    sen_lengths.append(str(len(l.strip().split())))

# Write sentence lengths into target file
with open(args.trg, 'w') as f:
    f.write('\n'.join(sen_lengths))


