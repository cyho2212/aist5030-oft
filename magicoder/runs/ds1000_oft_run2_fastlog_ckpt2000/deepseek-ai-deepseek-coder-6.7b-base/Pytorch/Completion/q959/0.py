    if a.shape[0] == 1 and b.shape[0] == 1:
        return torch.stack((a, b), 0)
    elif a.shape[0] == 2 and b.shape[0] == 1:
        return torch.cat((a, b.expand(2, -1)), 0)
    elif a.shape[0] == 1 and b.shape[0] == 2:
        return torch.cat((a.expand(2, -1), b), 0)
    else:
        raise ValueError("Invalid input shapes")

ab = solve(a, b)
