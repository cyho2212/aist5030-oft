result = torch.cat((a[:, :2], (a[:, 2:].mean(dim=1, keepdim=True) + b[:, :1]), b[:, 1:]), dim=1)
