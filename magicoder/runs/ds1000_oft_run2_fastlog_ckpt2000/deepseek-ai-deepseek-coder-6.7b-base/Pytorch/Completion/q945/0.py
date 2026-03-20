    A_log = A_log.numpy()
    B = B.numpy()
    C = B[:, A_log]
    return torch.from_numpy(C)
