    x_sign = torch.sign(x)
    y_sign = torch.sign(y)
    x_abs = torch.abs(x)
    y_abs = torch.abs(y)
    min_abs = torch.min(x_abs, y_abs)
    min_sign = torch.where(x_abs < y_abs, x_sign, y_sign)
    return min_abs * min_sign
