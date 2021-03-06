#
# config.py: configuration for semantic segmentation
# (c) Neil Nie, 2017
# All Rights Reserved.
#

batch_size = 8
img_height = 512
img_width = 512
learning_rate = 1e-4

test_results = False
visualize_gen = False
epochs = 2

data_path = "/Volumes/Personal_Drive/Datasets/ULC/"
infer_model_path = './weights/enet-c-v1-3.h5'
test_dataset = "/Volumes/Personal_Drive/Datasets/CityScapes/"
