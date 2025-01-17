# Copyright 2022 Dakewe Biotech Corporation. All Rights Reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
import random

import numpy as np
import torch
from torch.backends import cudnn

# Random seed to maintain reproducible results
random.seed(0)
torch.manual_seed(0)
np.random.seed(0)
# Use GPU for training by default
device = torch.device("cuda", 0)
# Turning on when the image size does not change during training can speed up training
cudnn.benchmark = True
# Image magnification factor
upscale_factor = 50
# Current configuration parameter method
mode = "test"
# Experiment name, easy to save weights and log files
exp_name = "srcnn_jpeg_baseline_x{}".format(upscale_factor)

if mode == "train":
    # Dataset
    train_image_dir = "./data/T91/SRCNN/train"
    valid_image_dir = "./data/T91/SRCNN/valid"
    test_image_dir = "./data/Set5/GTmod12"

    image_size = 32
    batch_size = 16
    num_workers = 4

    # Incremental training and migration training
    resume = ""

    # Total number of epochs
    epochs = 10000

    # SGD optimizer parameter
    model_lr = 1e-4
    model_momentum = 0.9
    model_weight_decay = 1e-4
    model_nesterov = False

    # How many iterations to print the training result
    print_frequency = 200

if mode == "test":
    dataset_list = ["Set5", "Set14", "BSDS100", "BSDS200", "General100", "SunHays80", "Urban100", "Historical"]
    dataset = dataset_list[5]
    print("{0} dataset is processing...".format(dataset))
    # Test data address
    lr_dir = f"./results/test/{exp_name}/{dataset}/lr"
    sr_dir = f"./results/test/{exp_name}/{dataset}/sr"
    hr_dir = f"./data/{dataset}/original"

    model_path = f"results/{exp_name}/best.pth.tar"
