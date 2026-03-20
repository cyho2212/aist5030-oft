embedding_weights = torch.FloatTensor(word2vec.wv.vectors)
embedding_layer = torch.nn.Embedding.from_pretrained(embedding_weights)
embedded_input = embedding_layer(input_Tensor)
