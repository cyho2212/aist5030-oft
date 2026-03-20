cnt_not_equal = torch.sum(A[:, -x:] != B[:, -x:]).item()
