# Copyright (c) SenseTime. All Rights Reserved.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from yacs.config import CfgNode as CN

__C = CN()

cfg = __C

__C.META_ARC = "udatcar_r50_l234"

__C.CUDA = True

# ------------------------------------------------------------------------ #
# Training options
# ------------------------------------------------------------------------ #
__C.TRAIN = CN()

# Anchor Target
__C.TRAIN.EXEMPLAR_SIZE = 127

__C.TRAIN.SEARCH_SIZE = 255

__C.TRAIN.OUTPUT_SIZE = 25

__C.TRAIN.RESUME = ''

__C.TRAIN.RESUME_2 = ''

__C.TRAIN.RESUME_D = ''

__C.TRAIN.RESUME_D_2 = ''

__C.TRAIN.PRETRAINED = ''

__C.TRAIN.PRETRAINED_2 = ''

__C.TRAIN.LOG_DIR = '/home/user/V4R/LHY/MDAT/UDAT/CAR/log/logs-web'

__C.TRAIN.SNAPSHOT_DIR = '/home/user/V4R/LHY/MDAT/UDAT/CAR/snapshot-web'

__C.TRAIN.EPOCH = 20

__C.TRAIN.START_EPOCH = 0

__C.TRAIN.BATCH_SIZE = 32

__C.TRAIN.NUM_WORKERS = 8

__C.TRAIN.MOMENTUM = 0.9

__C.TRAIN.WEIGHT_DECAY = 0.0001

__C.TRAIN.CLS_WEIGHT = 1.0

__C.TRAIN.LOC_WEIGHT = 2.0

__C.TRAIN.CEN_WEIGHT = 1.0

__C.TRAIN.PRINT_FREQ = 20

__C.TRAIN.LOG_GRADS = False

__C.TRAIN.GRAD_CLIP = 10.0

__C.TRAIN.BASE_LR = 0.005

__C.TRAIN.BASE_LR_d = 0.005

__C.TRAIN.LR = CN()

__C.TRAIN.LR.TYPE = 'log'

__C.TRAIN.LR.KWARGS = CN(new_allowed=True)

__C.TRAIN.LR_WARMUP = CN()

__C.TRAIN.LR_WARMUP.WARMUP = True

__C.TRAIN.LR_WARMUP.TYPE = 'step'

__C.TRAIN.LR_WARMUP.EPOCH = 5

__C.TRAIN.LR_WARMUP.KWARGS = CN(new_allowed=True)

__C.TRAIN.NUM_CLASSES = 2

__C.TRAIN.NUM_CONVS = 4

__C.TRAIN.PRIOR_PROB = 0.01

__C.TRAIN.LOSS_ALPHA = 0.25

__C.TRAIN.LOSS_GAMMA = 2.0

# ------------------------------------------------------------------------ #
# Dataset options
# ------------------------------------------------------------------------ #
__C.DATASET = CN(new_allowed=True)

# Augmentation
# for template
__C.DATASET.TEMPLATE = CN()

# for detail discussion
__C.DATASET.TEMPLATE.SHIFT = 4

__C.DATASET.TEMPLATE.SCALE = 0.05

__C.DATASET.TEMPLATE.BLUR = 0.0

__C.DATASET.TEMPLATE.FLIP = 0.0

__C.DATASET.TEMPLATE.COLOR = 1.0

__C.DATASET.SEARCH = CN()

__C.DATASET.SEARCH.SHIFT = 64

__C.DATASET.SEARCH.SCALE = 0.18
# __C.DATASET.SEARCH.SCALE = 0

__C.DATASET.SEARCH.BLUR = 0.0

__C.DATASET.SEARCH.FLIP = 0.0

__C.DATASET.SEARCH.COLOR = 1.0

# for detail discussion
__C.DATASET.NEG = 0.0

__C.DATASET.GRAY = 0.0

# __C.DATASET.NAMES = ('VID', 'COCO', 'DET', 'YOUTUBEBB')

# change the multipul source dataset here
__C.DATASET.SOURCE = ['WEB_mid','WEB_ver'] # only train on COCO for test  'VID', , 'DET', 'YOUTUBEBB' , 'COCO', 'YOUTUBEBB'
# __C.DATASET.SOURCE2 = ['Track112','UAV123','UAVDT'] # train: low altitude source for daytime
__C.DATASET.TARGET = ['NAT']  # only train on COCO for test  'VID', , 'DET', 'YOUTUBEBB'

#VID
__C.DATASET.VID = CN()
__C.DATASET.VID.ROOT = '/data1/Train_dataset/vid/crop511'          # VID dataset path
__C.DATASET.VID.ANNO = '/data1/Train_dataset/vid/train.json'
__C.DATASET.VID.FRAME_RANGE = 100
__C.DATASET.VID.NUM_USE = -1 # 10000  # repeat until reach NUM_USE

#VID
__C.DATASET.WEB_mid = CN()
__C.DATASET.WEB_mid.ROOT = '/data2/Train_dataset/WEB3-UAV/train_middle_view/crop_511'          # VID dataset path
__C.DATASET.WEB_mid.ANNO = '/data2/Train_dataset/WEB3-UAV/train_middle_view/train.json'
__C.DATASET.WEB_mid.FRAME_RANGE = 100
__C.DATASET.WEB_mid.NUM_USE = -1 # 10000  # repeat until reach NUM_USE

#VID
__C.DATASET.WEB_ver = CN()
__C.DATASET.WEB_ver.ROOT = '/data2/Train_dataset/WEB3-UAV/train_verticle_view/crop_511'          # VID dataset path
__C.DATASET.WEB_ver.ANNO = '/data2/Train_dataset/WEB3-UAV/train_verticle_view/train.json'
__C.DATASET.WEB_ver.FRAME_RANGE = 100
__C.DATASET.WEB_ver.NUM_USE = -1 # 10000  # repeat until reach NUM_USE

#YOUTUBEEBB
__C.DATASET.YOUTUBEBB = CN()
__C.DATASET.YOUTUBEBB.ROOT = 'train_dataset/yt_bb/crop511'  # YOUTUBEBB dataset path
__C.DATASET.YOUTUBEBB.ANNO = 'train_dataset/yt_bb/train.json'
__C.DATASET.YOUTUBEBB.FRAME_RANGE = 3
__C.DATASET.YOUTUBEBB.NUM_USE = -1  # use all not repeat

#COCO
__C.DATASET.COCO = CN()
__C.DATASET.COCO.ROOT = 'train_dataset/coco/crop511'         # COCO dataset path
__C.DATASET.COCO.ANNO = 'train_dataset/coco/train2017.json'
__C.DATASET.COCO.FRAME_RANGE = 1
__C.DATASET.COCO.NUM_USE = -1

#DET
__C.DATASET.DET = CN()
__C.DATASET.DET.ROOT = 'train_dataset/det/crop511'           # DET dataset path
__C.DATASET.DET.ANNO = 'train_dataset/det/train.json'
__C.DATASET.DET.FRAME_RANGE = 1
__C.DATASET.DET.NUM_USE = -1

#GOT
__C.DATASET.GOT = CN()
__C.DATASET.GOT.ROOT = '/data1/Train_dataset/got10k/crop511'         # GOT dataset path
__C.DATASET.GOT.ANNO = '/data1/Train_dataset/got10k/train.json'
__C.DATASET.GOT.FRAME_RANGE = 50
__C.DATASET.GOT.NUM_USE = -1 # 100000

#LaSOT
__C.DATASET.LaSOT = CN()
__C.DATASET.LaSOT.ROOT = 'train_dataset/lasot/crop511'         # LaSOT dataset path
__C.DATASET.LaSOT.ANNO = 'train_dataset/lasot/train.json'
__C.DATASET.LaSOT.FRAME_RANGE = 100
__C.DATASET.LaSOT.NUM_USE = 100000

# UAV123
__C.DATASET.UAV123 = CN()
__C.DATASET.UAV123.ROOT = '/data1/Test_dataset/UAV123/crop_511'         # UAV123 dataset path
__C.DATASET.UAV123.ANNO = '/data1/Test_dataset/UAV123/train.json'
__C.DATASET.UAV123.FRAME_RANGE = 100
__C.DATASET.UAV123.NUM_USE = -1

# UAVDT
__C.DATASET.UAVDT = CN()
__C.DATASET.UAVDT.ROOT = '/data1/Train_dataset/UAVDT/crop_511'         # UAV123 dataset path
__C.DATASET.UAVDT.ANNO = '/data1/Train_dataset/UAVDT/train.json'
__C.DATASET.UAVDT.FRAME_RANGE = 100
__C.DATASET.UAVDT.NUM_USE = -1

# UAVTrack112
__C.DATASET.Track112 = CN()
__C.DATASET.Track112.ROOT = '/data1/Test_dataset/UAVTrack112/crop_511'         # UAV123 dataset path
__C.DATASET.Track112.ANNO = '/data1/Test_dataset/UAVTrack112/train.json'
__C.DATASET.Track112.FRAME_RANGE = 100
__C.DATASET.Track112.NUM_USE = -1

#DarkTrack
__C.DATASET.DarkTrack = CN()
__C.DATASET.DarkTrack.ROOT = '/home/mist/v4r/train_dataset/random_train/random_crop511' # '/home/mist/v4r/train_dataset/NAT2021-train/crop_511'         # GOT dataset path
__C.DATASET.DarkTrack.ANNO = '/home/mist/v4r/train_dataset/random_train/train_random.json' # '/home/mist/v4r/train_dataset/NAT2021-train/train.json'
__C.DATASET.DarkTrack.FRAME_RANGE = 50
__C.DATASET.DarkTrack.NUM_USE = 10000 # 100000

#NAT2021
__C.DATASET.NAT = CN()
__C.DATASET.NAT.ROOT = '/data1/Train_dataset/NAT2021-train/random_train/random_crop511' # '/home/mist/v4r/train_dataset/NAT2021-train/crop_511'         # GOT dataset path
__C.DATASET.NAT.ANNO = '/data1/Train_dataset/NAT2021-train/random_train/train_random.json' # '/home/mist/v4r/train_dataset/NAT2021-train/train.json'
__C.DATASET.NAT.FRAME_RANGE = 50
__C.DATASET.NAT.NUM_USE = 10000 # 100000

__C.DATASET.VIDEOS_PER_EPOCH = 20000 #600000
# ------------------------------------------------------------------------ #
# Backbone options
# ------------------------------------------------------------------------ #
__C.BACKBONE = CN()

# Backbone type, current only support resnet18,34,50;alexnet;mobilenet
__C.BACKBONE.TYPE = 'res50'

__C.BACKBONE.KWARGS = CN(new_allowed=True)

# Pretrained backbone weights
__C.BACKBONE.PRETRAINED = 'snapshot/general_model.pth'

# Train layers
__C.BACKBONE.TRAIN_LAYERS = ['layer2', 'layer3', 'layer4']

# Layer LR
__C.BACKBONE.LAYERS_LR = 0.1

# Switch to train layer
__C.BACKBONE.TRAIN_EPOCH = 10

# ------------------------------------------------------------------------ #
# Adjust layer options
# ------------------------------------------------------------------------ #
__C.ADJUST = CN()

# Adjust layer
__C.ADJUST.ADJUST = True

__C.ADJUST.KWARGS = CN(new_allowed=True)

# Adjust layer type
__C.ADJUST.TYPE = "AdjustAllLayer"

# ------------------------------------------------------------------------ #
# Align layer options
# ------------------------------------------------------------------------ #
__C.ALIGN = CN()

# Align layer
__C.ALIGN.ALIGN = True

__C.ALIGN.KWARGS = CN(new_allowed=True)

# ALIGN layer type
__C.ALIGN.TYPE = "Adjust_Transformer"

# ------------------------------------------------------------------------ #
# RPN options
# ------------------------------------------------------------------------ #
__C.CAR = CN()

# RPN type
__C.CAR.TYPE = 'MultiCAR'

__C.CAR.KWARGS = CN(new_allowed=True)

# ------------------------------------------------------------------------ #
# Tracker options
# ------------------------------------------------------------------------ #
__C.TRACK = CN()

__C.TRACK.TYPE = 'SiamCARTracker'

# Scale penalty
__C.TRACK.PENALTY_K = 0.04

# Window influence
__C.TRACK.WINDOW_INFLUENCE = 0.44

# Interpolation learning rate
__C.TRACK.LR = 0.4

# Exemplar size
__C.TRACK.EXEMPLAR_SIZE = 127

# Instance size
__C.TRACK.INSTANCE_SIZE = 255

# Context amount
__C.TRACK.CONTEXT_AMOUNT = 0.5

__C.TRACK.STRIDE = 8


__C.TRACK.SCORE_SIZE = 25

__C.TRACK.hanming = True

__C.TRACK.NUM_K = 2

__C.TRACK.NUM_N = 1

__C.TRACK.REGION_S = 0.1

__C.TRACK.REGION_L = 0.44


# ------------------------------------------------------------------------ #
# HP_SEARCH parameters [lr, pk, wi]
# ------------------------------------------------------------------------ #
__C.HP_SEARCH = CN()

__C.HP_SEARCH.UAV123 = [0.39, 0.04, 0.37] 

__C.HP_SEARCH.NAT = [0.39, 0.04, 0.37] 

__C.HP_SEARCH.NAT_L = [0.39, 0.04, 0.37] 

__C.HP_SEARCH.UAVDark70 = [0.32, 0.04, 0.36] 

__C.HP_SEARCH.UAVDark135 = [0.32, 0.04, 0.36] 