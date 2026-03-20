result = torch.cat((torch.tensor([[-1, -1, -1, -1]]), t), dim=0)
result = torch.cat((result, torch.tensor([[-1, -1, -1, -1]])), dim=0)
