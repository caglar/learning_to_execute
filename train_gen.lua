state = {hardness=_G[opt.strategy],
        len=opt.nvals,
        seed=1,
        kind=0,
        nvals=opt.nvals,
        batch_size=params.batch_size,
        name="Training"}
load_data(state)

x_train = state.data.x
y_train = state.data.y
train_file = torch.DiskFile("train_file_x.txt", "w")
train_file:writeObject(x_train)
train_file:close()

