import numpy as np
import cPickle as pkl

data = pkl.load(open("data_400k_mix_cur_set.pkl"))
sdict = pkl.load(open("data_400k_mix_cur_dict.pkl"))

idict = {v:k for k, v in sdict.items()}
s1 = data['X'][10000]
a = ""
for c in list(s1):
    a += idict[c]
print a
