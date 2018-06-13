# Data Scores

Sample scores calculated by dataset features.

## Scores

``bk``: Bucketed scores.

``sentence_length``: The length of sentences.

``sentence_length.deen``: The sum of the lengths of English and German pair sentences.

``sentence_max_rank``: Rank a sentence by the least frequent word in the sentence. Higher rank (more frequent) of the least frequent word in the sentence will give the sentence higher rank.

``sentence_max_rank.deen``: The rank of a sample will be determined by both the rank of the German version and the rank its English counterpart, and use the larger of the two values.

``sentence_average_rank``: Rank a sentence by the average ranks of words in the sentence.

``sentence_average_rank.deen``: For a sentence pair (x_de, y_en), if the length of x_de is l_de, the length of y_en is l_en, and the average rank of x_de is ar_de, the average rank of y_en is ar_en, then average rank of the combination is (l_de * ar_de + l_en * ar_en) / (l_de + l_en).
