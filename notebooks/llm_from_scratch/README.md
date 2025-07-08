# Build an LLM From Scratch #
This is a fun side project in my deep learning journey, where I'm building a language model from scratch while following Sebastian Raschka’s book. I’ll use this as a daily journal to document my learnings and progress along the way. Once I finish the book, I hope to reflect on and summarize my biggest takeaways.

## Summary of Learnings ##

## Logs ##

### 05-Jul-2025 ###
- More cool stuff.
- The token embeddings only tell the model what the tokens are, not where they appear. This is crucial, especially in tasks like language translation, where the same word may need to be interpreted differently depending on its position in the sentence.
- To help the model understand token positions, token embeddings are combined with another set of weights called the positional embedding matrix. There are two types of positional embeddings: absolute and relative.
- I don’t fully understand the details yet, but based on the book’s example, the positional embedding matrix is similar to the token embedding matrix. It is essentially a lookup table that returns a positional embedding vector for a given position. It has the shape [no_of_positions, embedding_dim], and is added to the token embeddings to produce the final input embeddings for the model.
- This means the same token, when it appears in different positions, ends up with different final embeddings, allowing the model to distinguish its usage based on context.
- As a result, the model can learn not just which words co-occur, but also how their positions influence meaning, and whether certain substitutions preserve meaning or not. For example, "I have a pet (cat/dog)" makes sense, but "I cat food my own app" doesn't. Even if the words are from similar clusters.
- It’s probably obvious that our brains store relationships between concepts based on both meaning and context, even when those concepts are expressed differently across languages.
- We intuitively know when words or phrases can be swapped and when they can’t. And remarkably, we can often recognize these patterns across languages too. For example, when I first learned Hindi, I could immediately relate many idioms to their equivalents in my native language, even if they didn’t seem similar at first glance. Take “Bandar aur Adrak” in Hindi and “Kazhudhai and Karpoora Vasanai” in Tamil — different imagery, different animals, even different cultural contexts — yet the same underlying idea. It’s a kind of conceptual clustering that seems to happen naturally. 
- And sometimes, swapping these clustered words where they should not be creates humor or even new ideas. Isn’t that just super cool?

### 04-Jul-2025 ###
- Models require numeric inputs, but many real-world problems — like text — are inherently non-numeric. These inputs must be converted into a numerical form (e.g. token IDs, embeddings) before the model can process them. This final form of input to the model are called embeddings
- Implemented an embeddings lookup table to encode tokenized Asimov text. This table acts as a compressed alternative to one-hot encoding.
Instead of using a sparse one-hot vector with 50,000 dimensions (one for each vocabulary entry), we map each token ID directly to a weight (embedding) vector of a lower dimension, such as 128 or 256.
- Embeddings are final inputs that get passed to the model
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


