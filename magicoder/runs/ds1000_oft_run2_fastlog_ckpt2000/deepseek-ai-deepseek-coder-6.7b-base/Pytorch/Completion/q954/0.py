    mask = torch.zeros(len(lens), max(lens))
    for i, l in enumerate(lens):
        mask[i, :l] = 1
    return mask

# Test
lens = [3, 5, 4]
mask = get_mask(lens)
print(mask)
