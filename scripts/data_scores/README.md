# Scripts for Data Scores

Scripts for calculating sample scores based on dataset features.

## Usage
``calculate_sentence_length.py``: 
```bash
python calculate_sentence_length.py --src BPE file --trg output file
```
Calculate the length of each sentence in the dataset.

``calculate_word_frequency.py``:
```bash
python calculate_word_frequency.py --src BPE file --trg output file 
```
Calculate the frequency for each word type and rank them. Word with rank 0 is the most frequent word.

``calculate_sentence_rank.py``:
```bash
python calculate_sentence_rank.py --src BPE file --wf word frequency file --trg output file --rank rank type(max/average)
```
Calculate the sentence rank by the ranks of words in the sentence. 
Max is to rank a sentence by the least frequent word in the sentence. Higher rank(more frequent) of the least frequent word gives the sentence higher rank.
Average is to rank a sentence by the average ranks of words in the sentence. 
