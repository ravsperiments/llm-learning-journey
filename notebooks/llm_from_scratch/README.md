# Build an LLM From Scratch #
This is a fun side project in my deep learning journey, where I'm building a language model from scratch while following Sebastian Raschka’s book. I’ll use this as a daily journal to document my learnings and progress along the way. Once I finish the book, I hope to reflect on and summarize my biggest takeaways.

## Summary of Learnings ##

## Logs ##


### 04-Jul-2025 ###
- Implemented an embeddings lookup table to encode tokenized Asimov text. This table acts as a compressed alternative to one-hot encoding.
Instead of using a sparse one-hot vector with 50,000 dimensions (one for each vocabulary entry), we map each token ID directly to a weight (embedding) vector of a lower dimension, such as 128 or 256.
- Mathematically, this works because multiplying a one-hot vector by a weight matrix of shape [vocab_size, embedding_dim] simply selects the row corresponding to the token ID. Since all entries in the one-hot vector are zero except at the token's index, the result of the matrix multiplication is just the relevant row of the embedding matrix.
- The embeddings matrix is thus a lookup table where each row is the embedding for a specific token.
- In a way, these embeddings can be imagined as a layer in the neural network with just weights and no biases. These weights are learned through gradient descent, just like any other model parameters.
- This is very powerful, as weights for related concepts — such as pet animals like dogs and cats — start to cluster together during the learning process organically, which is so cool.

### 02-Jul-2025 ###
- Implemented a simple tokenizer and used it to tokenize the text of Asimov's first book in the Foundation series
- It splits the text into words and special characters
- Surprised to see over 40K tokens — while this includes proper nouns and numbers, it still feels like a large vocabulary
- Even more surprised when I later used the GPT-2 tokenizer from tiktoken and saw that its vocabulary is only around 50K, not much larger than Asimov's
- Later, I learned that GPT-2’s tokenizer has a similar vocabulary size to my simple tokenizer on Asimov’s text because of how it works — it uses subwords and common word fragments to compress the vocabulary
- This made a lot of sense, since a smaller vocabulary leads to more efficient training and inference
- But it also made me doubly surprised that the ~600K word vocab of English can be encoded with just 1/12th of its vocab size


