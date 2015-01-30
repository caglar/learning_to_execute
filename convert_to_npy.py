import numpy as np
import cPickle as pkl

src_sym_dict = {"nil": 0}
tgt_sym_dict = {"eos": 0}
X = []
y = []

def add_to_dict(c, sym_dict):
    values = sym_dict.values()
    max_val = np.max(values)
    new_idx = max_val + 1
    sym_dict[c] = new_idx


def add_to_target(target, new_tar=None):
    char_tars = list(target)
    if new_tar is None:
        new_tar = []
    for ct in char_tars:
        if ct not in tgt_sym_dict:
            add_to_dict(ct, tgt_sym_dict)
        new_tar.append(tgt_sym_dict[ct])
    y.append(new_tar)
    return new_tar

def add_to_input(inp, new_inp=None):
    char_inps = list(inp)
    if new_inp is None:
        new_inp = []
    for ci in char_inps:
        if ci not in src_sym_dict:
            add_to_dict(ci, src_sym_dict)
        new_inp.append(src_sym_dict[ci])
    return new_inp

def create_file(filen):
    with open(filen, "r") as fileh:
        whole_data = fileh.readlines()

    print "Started processing the files."
    stack = []
    #1 for target, 0 for input
    mode = 1
    start_new = 0
    old_inp = None
    i = 0
    for line in whole_data:
        if line.strip() == "<q>":
            stack = []
            mode = 1
        elif line.strip() == "Target:":
            i+=1
            mode = 0
            X.append(old_inp)
            old_inp = None
            start_new = 1
        elif line.strip() == "Input:":
            mode = 1
            start_new=1
        else:
            if mode == 0:
                add_to_target(line)
            elif mode == 1:
                if start_new:
                    old_inp = add_to_input(line)
                    start_new = 0
                else:
                    old_inp = add_to_input(line, old_inp)

    print "There were %d targets." % i
    print "Saving files."
    data = {"X": X, "y": y}

    pkl_data_name = "%s_set.pkl" % filen[:-4]
    pkl.dump(data, open(pkl_data_name, "w"))
    print "Saved to %s, successfully." % pkl_data_name

    pkl_src_dict_name = "%s_src_dict.pkl" % filen[:-4]
    pkl.dump(src_sym_dict, open(pkl_dict_name, "w"))
    print "Saved to %s, successfully." % pkl_dict_name

    pkl_tgt_dict_name = "%s_tgt_dict.pkl" % filen[:-4]
    pkl.dump(tgt_sym_dict, open(pkl_dict_name, "w"))
    print "Saved to %s, successfully." % pkl_dict_name

create_file("data_400k_mix_cur.txt")
