mask = torch.tensor([[1 if i < j else 0 for i in range(lens[j])] for j in range(len(lens))])
print(mask)
