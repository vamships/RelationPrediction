import logging
import numpy as np
import pandas as pd

logging.basicConfig(
    format="%(asctime)s| %(message)s", datefmt="%d-%m-%y %H:%M:%S", level=logging.INFO
)

logger = logging.getLogger("conver_openke_to_rgcn")

def read_openke_edges(filename):
    idx = 0
    header = ['head', 'relation', 'tail']
    num_samples = None
    df_edges = None
    for line in open(filename, 'r+'):
        line = line.strip().split('\t')
        if idx == 0:
            num_samples = int(line[0])
            df_edges = pd.DataFrame(np.zeros((num_samples, 3)), columns=header)
        else:
            # logger.info(idx)
            # logger.info(line)
            df_edges.iloc[idx-1, :] = [int(line[0]), int(line[2]), int(line[1])]
        idx += 1

    return df_edges


def write_openke_entities(filename, output_file):
    idx = 0
    with open(output_file, mode="w") as file_handle:
        for line in open(filename, 'r+'):
            line = line.strip().split('\t')
            if idx > 0:
                file_handle.write("{}\t{}\n".format(line[1],line[0]))
            idx += 1


def main():
    path_to_data = "/Users/vamship/Downloads/to_openke_700/"
    train_data = read_openke_edges(path_to_data+"train2id.txt")
    train_data.to_csv("train_triplets.csv", index=False, float_format='%d')
    valid_data = read_openke_edges(path_to_data + "valid2id.txt")
    valid_data.to_csv("valid_triplets.csv", index=False, float_format='%d')
    test_data = read_openke_edges(path_to_data + "test2id.txt")
    test_data.to_csv("test_triplets.csv", index=False, float_format='%d')
    write_openke_entities(path_to_data+"entity2id.txt", "entities.dict")
    write_openke_entities(path_to_data + "relation2id.txt", "relations.dict")

if __name__ == "__main__":
    main()
