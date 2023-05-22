"""
Author: Lucas Goncalves
2023

Code adapted using pieces from code by Radek Danecek

"""

from hashlib import new
from utils.FaceVideoDataModule import TestFaceVideoDM
# import gdl
from pathlib import Path
import shutil
from tqdm import auto
import argparse
import os
import torch 
from torchvision import  transforms
import numpy as np
from PIL import Image
from tqdm import tqdm


def main():
    root = '/path_to_data_dir/data/Dataset_Name/'

    input_folder = root + 'Videos/' 
    output_folder = root + 'faces/'

    if not os.path.isdir(output_folder):
        os.mkdir(output_folder)

    save_to = root + 'Face_features'
    if not os.path.isdir(save_to):
        os.mkdir(save_to)

    #loading model
    model = torch.load('./model/enet_b2_8_best.pt')
    model.classifier = torch.nn.Identity()
    model.eval()

    IMG_SIZE = 224

    test_transforms = transforms.Compose(
        [
            transforms.Resize((IMG_SIZE,IMG_SIZE)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                        std=[0.229, 0.224, 0.225])
        ]
    )

    list_of_dirs = os.listdir(input_folder)
    list_of_dirs.sort()

    videos = os.listdir(output_folder)

    print(len(videos))

    for ldir in list_of_dirs:

        try:
            if ldir.replace('.mp4','') not in videos:

                input_video = input_folder + ldir
                processed_subfolder = None
                dm = TestFaceVideoDM(input_video, output_folder, processed_subfolder=processed_subfolder,face_detector_threshold=0.96, 
                    batch_size=20, num_workers=20)
                dm.prepare_data()
                dm.setup()
                processed_subfolder = Path(dm.output_dir).name
                filename = ldir.replace('.mp4','')
                folder = output_folder + processed_subfolder + '/' + filename + '/videos'
                shutil.rmtree(folder)
                shutil.move(output_folder + processed_subfolder + '/' + filename, output_folder)
                shutil.rmtree(output_folder + processed_subfolder)
                file_path = output_folder + filename
                feature_vector = []
                detections_folder = os.path.join(file_path, "detections")
                for image_name in sorted(os.listdir(detections_folder)):
                    if image_name[-3:] == 'png':
                        image_path = os.path.join(detections_folder, image_name)
                        image = Image.open(image_path)
                        image = test_transforms(image).unsqueeze(0).cuda()

                        with torch.no_grad():
                            features = model(image).cpu()
                            feature_vector.append(features)
                    
                feature_vector = np.concatenate(feature_vector, axis=0)
                feature_file = os.path.join(save_to, filename + ".npy")
                np.save(feature_file, feature_vector)


            else:
                print(ldir, 'ALREADY IN!')
            
        except:
            
            print('ERROR IN ', ldir)
            break
    print("Done")

if __name__ == '__main__':
    main()
 
