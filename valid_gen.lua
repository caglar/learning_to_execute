state_val = {hardness=current_hardness,
             len=501,
             seed=1,
             kind=1,
             batch_size=params.batch_size,
             name="Validation"}

load_data(state_val)
x_val = state_val.data.x
y_val = state_val.data.y
val_file = torch.DiskFile("val_file.txt_x", "w")

