import pandas as pd
import shutil

def is_float_convertible(s: str):
    try:
        r = float(s)
        return True, r
    except ValueError:
        return False, s


df = pd.read_csv("BUSBRA/10-fold-cv.csv")
filenames = list(df["ID"])
classifications = list(df["Pathology"])

df.fillna(-1, inplace=True)

# Selecting only the columns you want to sum
cols_to_sum = ['valid_1', 'valid_2', 'valid_3', 'valid_4', 'valid_5', 'valid_6', 'valid_7', 'valid_8', 'valid_9', 'valid_10']

# Calculate the sum of specified columns for each row
df['sum_valid'] = df[cols_to_sum].sum(axis=1)

# Append the sum of each row to a final list
final_sum_list = df['sum_valid'].tolist()

ls = list(set([filename.split("-")[0] for filename in filenames]))
final_ls_dict = {l: {"r": final_sum_list[filenames.index("-".join([l, "r"]))] if "-".join([l, "r"]) in filenames else -10, "l": final_sum_list[filenames.index("-".join([l, "l"]))] if "-".join([l, "l"]) in filenames else -10, "s": final_sum_list[filenames.index("-".join([l, "s"]))] if "-".join([l, "s"]) in filenames else -10} for l in ls}

viewtoindex = {0: "r", 1: "l", 2: "s"}

filepaths = []
classes = []
for l in ls:
    namesums = [final_ls_dict[l]["r"], final_ls_dict[l]["l"], final_ls_dict[l]["s"]]
    maxindex = namesums.index(max(namesums))
    filepath = f'BUSBRA/Images/{"-".join([l, viewtoindex[maxindex]])}.png'
    classification = classifications[filenames.index("-".join([l, viewtoindex[maxindex]]))]
    if classification == "benign":
        shutil.copy(src=filepath, dst="training3/benign")
    elif classification == "malignant":
        shutil.copy(src=filepath, dst="training3/malignant")
    else:
        continue
