import os
import torch
import numpy as np
import json


def set_deterministic(seed):
    os.environ["CUBLAS_WORKSPACE_CONFIG"]=":4096:8"
    torch.use_deterministic_algorithms(True)
    torch.manual_seed(seed)
    np.random.seed(seed)

def print_config_description(conf_path):
    with open(conf_path, 'r') as f:
        config_dict = json.load(f)
    description = config_dict.get("description", None)
    if description is not None:
        print(description)
    else:
        print("Configuration file does not contain a description")
        print("We highly recommend you to add a description to the configuration file for the debugging")
        

def load_audio_and_label_file_paths(args):
    audio_path = '/media/lucas/08AE364B3D909CD8/ICMI_2023/data/' + args.corpus + '/Audios'
    video_path = '/media/lucas/08AE364B3D909CD8/ICMI_2023/data/' + args.corpus + '/Face_features'
    if args.corpus == 'MSP-IMPROV':
        if args.data_mode == 'primary':
            if args.num_classes == 'att':
                label_path = '/media/lucas/08AE364B3D909CD8/ICMI_2023/data/' + args.corpus + '/Partitioned_data_Primary_Emotion/labels_consensus_EmoP_4class_' + args.label_rule + '/labels_consensus_' + args.partition_number + '.csv'
        
    elif args.corpus == 'CREMA-D':
        label_path = '/media/lucas/08AE364B3D909CD8/ICMI_2023/data/' + args.corpus + '/labels_consensus_6class_' + args.label_rule + '/label_consensus_' + args.partition_number + '.csv'

    return audio_path, video_path, label_path
