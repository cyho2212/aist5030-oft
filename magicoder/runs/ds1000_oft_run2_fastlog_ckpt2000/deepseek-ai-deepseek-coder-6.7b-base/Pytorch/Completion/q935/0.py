# 1.
# If you want to change the learning rate after any epoch, you can do it by creating a new optimizer with the new learning rate.
# For example:
optim = torch.optim.SGD(..., lr=0.005)
# 2.
# If you want to change the learning rate after a certain number of epochs, you can use a scheduler.
# For example:
scheduler = torch.optim.lr_scheduler.StepLR(optim, step_size=10, gamma=0.1)
# Here, the learning rate will be multiplied by 0.1 after every 10 epochs.

# Now, you can use the scheduler to update the learning rate after each epoch.
# For example:
for epoch in range(num_epochs):
    # train the model
    # ...
    # update the learning rate
    scheduler.step()

# 3.
# If you want to change the learning rate based on the loss, you can use a callback function.
# For example:
def change_lr(optimizer, loss):
    if loss > 0.5:
        for param_group in optimizer.param_groups:
            param_group['lr'] = 0.0005
    else:
        for param_group in optimizer.param_groups:
            param_group['lr'] = 0.05

# Now, you can use this function to change the learning rate after each epoch.
# For example:
for epoch in range(num_epochs):
    # train the model
    # ...
    # get the loss
    loss = get_loss()
    # change the learning rate
    change_lr(optimizer, loss)
