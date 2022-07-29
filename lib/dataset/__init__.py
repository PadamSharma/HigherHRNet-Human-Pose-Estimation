# ------------------------------------------------------------------------------
# Copyright (c) Microsoft
# Licensed under the MIT License.
# Written by Bin Xiao (leoxiaobin@gmail.com)
# ------------------------------------------------------------------------------

from .COCOKeypoints import CocoKeypoints as coco
from .CrowdPoseKeypoints import CrowdPoseKeypoints as crowd_pose
from .build import make_dataloader
from .build import make_test_dataloader

# dataset dependent configuration for visualization
coco_part_labels = [
    'Front Right Wheel',  # 1
    'Front Left Wheel',  # 2
    'Rear Right Wheel',  # 3
    'Rear Left Wheel',  # 4
    'Front Right Headlight',  # 5
    'Front Left Headlight',  # 6
    'Rear Right Taillight',  # 7
    'Rear Left Taillight',  # 8
    'Front Right Rooftop Corner',  # 9
    'Front Left Rooftop Corner',  # 10
    'Rear Right Rooftop Corner',  # 11
    'Rear Left Rooftop Corner'  # 12
]
coco_part_idx = {
    b: a for a, b in enumerate(coco_part_labels)
}

# skeleton = [[1, 2], [1, 3], [4, 3], [4, 2],
#             [5, 6], [5, 7], [8, 7], [8, 6],
#             [9, 10], [9, 11], [12, 11], [12, 10],
#             [1, 5], [2, 6], [3, 7], [4, 8],
#             [5, 9], [6, 10], [7, 11], [8, 12]
#             ]

coco_part_orders = [('Front Right Wheel', 'Front Left Wheel'), ('Front Right Wheel', 'Rear Right Wheel'), ('Rear Left '
                                                                                                           'Wheel',
                                                                                                           'Rear Right '
                                                                                                           'Wheel'),
                    ('Rear Left Wheel', 'Front Left Wheel'),
                    ('Front Right Headlight','Front Left Headlight'), ('Front Right Headlight','Rear Right Taillight'), ('Rear Left Taillight','Rear Right Taillight'), ('Rear Left Taillight','Front Left Headlight'),
                    ('Front Right Rooftop Corner','Front Left Rooftop Corner'), ('Front Right Rooftop Corner','Rear Right Rooftop Corner'), ('Rear Left Rooftop Corner','Rear Right Rooftop Corner'), ('Rear Left Rooftop Corner','Front Left Rooftop Corner'),
                    ('Front Right Wheel','Front Right Headlight'), ('Front Left Wheel','Front Left Headlight'), ('Rear Right Wheel','Rear Right Taillight'), ('Rear Left Wheel','Rear Left Taillight'),
                    ('Front Right Headlight','Front Right Rooftop Corner'),('Front Left Headlight','Front Left Rooftop Corner'),('Rear Right Taillight','Rear Right Rooftop Corner'),('Rear Left Taillight','Rear Left Rooftop Corner')
                    ]
# coco_part_orders = [
#     ('nose', 'eye_l'), ('eye_l', 'eye_r'), ('eye_r', 'nose'),
#     ('eye_l', 'ear_l'), ('eye_r', 'ear_r'), ('ear_l', 'sho_l'),
#     ('ear_r', 'sho_r'), ('sho_l', 'sho_r'), ('sho_l', 'hip_l'),
#     ('sho_r', 'hip_r'), ('hip_l', 'hip_r'), ('sho_l', 'elb_l'),
#     ('elb_l', 'wri_l'), ('sho_r', 'elb_r'), ('elb_r', 'wri_r'),
#     ('hip_l', 'kne_l'), ('kne_l', 'ank_l'), ('hip_r', 'kne_r'),
#     ('kne_r', 'ank_r')
# ]

crowd_pose_part_labels = [
    'left_shoulder', 'right_shoulder', 'left_elbow', 'right_elbow',
    'left_wrist', 'right_wrist', 'left_hip', 'right_hip',
    'left_knee', 'right_knee', 'left_ankle', 'right_ankle',
    'head', 'neck'
]
crowd_pose_part_idx = {
    b: a for a, b in enumerate(crowd_pose_part_labels)
}
crowd_pose_part_orders = [
    ('head', 'neck'), ('neck', 'left_shoulder'), ('neck', 'right_shoulder'),
    ('left_shoulder', 'right_shoulder'), ('left_shoulder', 'left_hip'),
    ('right_shoulder', 'right_hip'), ('left_hip', 'right_hip'), ('left_shoulder', 'left_elbow'),
    ('left_elbow', 'left_wrist'), ('right_shoulder', 'right_elbow'), ('right_elbow', 'right_wrist'),
    ('left_hip', 'left_knee'), ('left_knee', 'left_ankle'), ('right_hip', 'right_knee'),
    ('right_knee', 'right_ankle')
]

VIS_CONFIG = {
    'COCO': {
        'part_labels': coco_part_labels,
        'part_idx': coco_part_idx,
        'part_orders': coco_part_orders
    },
    'CROWDPOSE': {
        'part_labels': crowd_pose_part_labels,
        'part_idx': crowd_pose_part_idx,
        'part_orders': crowd_pose_part_orders
    }
}
