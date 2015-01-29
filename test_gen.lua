state_test =  {hardness=target_hardness,
               len=501,
               seed=1,
               kind=2,
               batch_size=params.batch_size,
               name="Test"}

load_data(state_test)
x_tst = state_test.data.x
y_tst = state_test.data.y
tst_file = torch.DiskFile("tst_file.txt_x", "w")

