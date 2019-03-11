import os
import numpy as np


def loader(path="./dvector.npz"):
    return np.load(path)['vector'], np.load(path)['label']


if __name__ == "__main__":
    # print("Run Y = tsne.tsne(X, no_dims, perplexity) to perform t-SNE on your dataset.")
    # print("Running example on 2,500 MNIST digits...")
    print('hi')
    utt2spk = np.loadtxt("utt2spk", dtype=bytes).astype(str)

    vector, _ = loader()
    all_labels = []

    for i in utt2spk:
        all_labels.append(i[1])

    spk = {}
    # 6333
    for i in all_labels:
        # if len(spk) == 10:
        #    break
        if i not in spk:
            dic = {i: 0}
            spk.update(dic)

    for i in all_labels:
        spk[i] += 1

    check = []

    for i in range(10):
        key = max(spk, key=spk.get)
        check.append(key)
        spk.pop(key)

    print(check)

    labels = []
    x = []
    for i in range(len(all_labels)):
        if all_labels[i] in check:
            labels.append(all_labels[i].strip('id'))
            x.append(vector[i])

    if not os.path.exists("data"):
        os.makedirs("data")

    with open('data/data.dat', 'w') as f:
        for i in x:
            for j in i:
                f.write(str(j))
                f.write(" ")
            f.write('\n')

    with open("data/data.lab", 'w') as f:
        for i in labels:
            f.write(str(i))
            print(str(i))
            f.write('\n')
