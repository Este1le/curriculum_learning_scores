import os 
import argparse

parser = argparse.ArgumentParser(description="Combine scores. " \
                                             " Usage example: python combine_score.py --scores ../scores/model_scores_ted/ted.1best_score.en.bk"\
                                             "../scores/data_scores_ted/ted.sentence_max_rank.en.bk"\
                                             "--weights 2 1 --dest ../scores/combine_scores_ted/ted.combine_1best_max.en.bk")

parser.add_argument('--scores', dest='scores', nargs='+', required=True, help="path for scores to combine")
parser.add_argument('--weights', dest='weights', nargs='+', type=int, required=True, 
                    choices=[1,2, 3], help="weights assigned to scores")
parser.add_argument('--dest', dest='dest', required=True,
                    help="path to write the new scores")

args = parser.parse_args()

if len(args.weights) != len(args.scores):
    print("Number of given weights is not equal to the number of scores.")
    exit(0)

bks = [None] *len(args.scores)

for i in range(len(args.scores)):
    score = args.scores[i]
    if not os.path.exists(score):
        print("Score file does not exist: " + score)
        exit(0)
    if not score.endswith("bk"):
        print("Scores are not bucketed: " + score)
        exit(0)
    else:
        with open(score) as f:
            bks[i] = f.readlines()
        bks[i] = [int(x.strip()) for x in bks[i] if x.strip()]

combine_scores = [0] * len(bks[0])
for j in range(len(combine_scores)):
    combine_scores[j] = int(round(float(sum([bks[i][j]*args.weights[i] for i in range(len(bks))])) / sum(args.weights)))

with open(args.dest, "w") as f:
    f.write("\n".join([str(x) for x in combine_scores]))

for i in range(len(bks)):
    score = args.scores[i]
    num_change = sum([combine_scores[j]!=bks[i][j] for j in range(len(combine_scores))])
    per_change = float(num_change)/len(combine_scores) * 100
    print("********************************************************************")
    print("Number and percentage of changed scores compared to {0}: {1}, {2:.2f}%".format(score, num_change, per_change))
    print("Distribution of scores in {0}:\n {1}".format(score, ",".join(["{0:2f}%".format(float(bks[i].count(b))/len(combine_scores)) for b in range(len(set(bks[i])))])))

print("#######################################################")
print("New distribution of scores is: " + ",".join(["{0:2f}%".format(float(combine_scores.count(b))/len(combine_scores)) for b in range(len(set(combine_scores)))]))

# ********************************************************************
# Number and percentage of changed scores compared to ../scores/model_scores_ted/ted.1best_score.en.bk: 51039, 33.66%
# Distribution of scores in ../scores/model_scores_ted/ted.1best_score.en.bk:
#  0.084457%,0.192057%,0.283782%,0.294011%,0.145693%
# ********************************************************************
# Number and percentage of changed scores compared to ../scores/data_scores_ted/ted.sentence_max_rank.en.bk: 112362, 74.10%
# Distribution of scores in ../scores/data_scores_ted/ted.sentence_max_rank.en.bk:
#  0.327079%,0.220996%,0.173716%,0.147982%,0.130227%
# #######################################################
# New distribution of scores is: 0.074518%,0.281348%,0.299201%,0.260653%,0.084279%

