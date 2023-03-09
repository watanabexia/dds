"""
Using the result to calculate f1 score of a segment of the video.
"""

import sys

sys.path.append("/home/cc/dds")

from dds_utils import evaluate_partial, read_results_dict

class calculator:

    def __init__(self) -> None:
        self.profile_folder_path = "/home/cc/dds/workspace"
        self.real_video_name = "rene"
        self.low_resolution = 0.5
        self.high_resolution = 0.8
        self.low_qp = 40
        self.high_qp = 30
        self.rpn_enlarge_ratio = 0.0

        self.low_threshold = 0.3

        self.min_fid = 5
        self.max_fid = 9

    def get_f1_partial(self):
        results = read_results_dict(f"{self.profile_folder_path}/results/{self.real_video_name}_dds_{self.low_resolution}_{self.high_resolution}_{self.low_qp}_{self.high_qp}_{self.rpn_enlarge_ratio}_twosides_batch_5_0.5_0.8_0.4")
        gt = read_results_dict(f"{self.profile_folder_path}/results/{self.real_video_name}_gt")

        tp, fp, fn, _, _, _, f1 = evaluate_partial(
            min_fid = self.min_fid, 
            max_fid = self.max_fid, 
            map_dd = results,
            map_gt = gt,
            gt_confid_thresh = self.low_threshold, 
            mpeg_confid_thresh = 0.5, 
            max_area_thresh_gt = 0.4, 
            max_area_thresh_mpeg = 0.4)

        return f1

print(calculator().get_f1_partial())