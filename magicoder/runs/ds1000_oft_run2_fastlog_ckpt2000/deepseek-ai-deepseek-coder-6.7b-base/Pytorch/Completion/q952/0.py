mask = torch.zeros(len(lens), max(lens))
for i, l in enumerate(lens):
    mask[i, :l] = 1
