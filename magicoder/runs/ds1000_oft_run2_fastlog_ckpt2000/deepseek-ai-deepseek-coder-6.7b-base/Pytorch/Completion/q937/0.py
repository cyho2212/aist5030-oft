    # Get the word2vec model's vocabulary
    vocab = word2vec.wv.vocab
    # Get the embedding weights from the word2vec model
    embedding_weights = word2vec.wv.vectors
    # Create a PyTorch embedding layer with the same vocabulary and embedding weights
    embedding_layer = torch.nn.Embedding.from_pretrained(torch.from_numpy(embedding_weights), freeze=False)
    # Use the embedding layer to embed the input data
    embedded_input = embedding_layer(input_Tensor)
    return embedded_input
