import argparse
import string 

parser = argparse.ArgumentParser(description='Calculate the word frequency')

parser.add_argument('--src', dest='src', type=str, required=True,
                    help='BPE file')
parser.add_argument('--trg', dest='trg', type=str, required=True,
                    help='Target file recording the word frequency')

args = parser.parse_args()

# Create a dictionary mapping word to frequency
vocab_dict = {}
with open(args.src, 'r') as f:
    lines = f.readlines()
for line in lines:
    for word in line.strip().split():
        # Remove punctuations and digits
        if (word not in string.punctuation) and (not word.isdigit()):
            if word in vocab_dict:
                vocab_dict[word] += 1
            else:
                vocab_dict[word] = 1

# Sort words by frequency and rank them
# Word with rank 0 is the most frequent word
freqs = []
rank = 0
for word, freq in sorted(vocab_dict.items(), key=lambda kv : (kv[1],kv[0]), reverse=True):
    freqs.append((rank, word, freq))
    rank += 1

# Write rank, word and frequency to target file
with open(args.trg, 'w') as f:
    f.write('\n'.join([' '.join([str(rank),word,str(freq)]) for (rank, word,freq) in freqs]))



