import json
from collections import OrderedDict

import matplotlib
import matplotlib.pyplot as plt

from vis_tools.toos import _vis_semantic_map3d, CLASS_TO_COLOR_MAP


matplotlib.use('TkAgg')


if __name__ == '__main__':
    gt_miniroom_1_json_path = './data/miniroom_1.json'
    pr_miniroom_1_json_path = './data/my_semantic_slam_0.json'

    with open(gt_miniroom_1_json_path, 'r') as f:
        gt_miniroom_1_json = json.load(f)

    with open(pr_miniroom_1_json_path, 'r') as f:
        pr_miniroom_1_json = json.load(f)

    gt_miniroom_1_objects = gt_miniroom_1_json['ground_truth']['objects']
    pr_miniroom_1_objects = pr_miniroom_1_json['results']['objects']

    # Visualise ground-truth vs predicted semantic maps
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Visualise ground-truth map
    _vis_semantic_map3d(ax, gt_miniroom_1_objects, CLASS_TO_COLOR_MAP, 'r')

    # Display ground-truth objects labels
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = OrderedDict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys(), loc='upper right')

    # Visualise predicted map
    _vis_semantic_map3d(ax, pr_miniroom_1_objects, CLASS_TO_COLOR_MAP, 'k')

    plt.title(f"{gt_miniroom_1_json['environment']['name']}:{gt_miniroom_1_json['environment']['variant']}")
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()
