output = MyNet(input)
conf, classes = torch.max(output.reshape(1, 3), 1)
class_names = '012'
confidence_score = conf.item()
print(confidence_score)
