import os
from glob import glob
abs_dir = r"C:/aivill_sey_ryeong/labeling/라벨링툴\srs클립/주행환경/"
CLIP = "Clip_00053"
camera_blur = glob(f"{abs_dir}/{CLIP}/Camera/FrontCenter/blur/*")
camera_meta = glob(f"{abs_dir}/{CLIP}/Camera/FrontCenter/meta/*")
radar = glob(f"{abs_dir}/{CLIP}/Radar/Radar_Center/*")
lidar = glob(f"{abs_dir}/{CLIP}/Lidar/*")
for i in camera_blur:
    os.rename(i, f"{os.path.dirname(i)}/481_ND_{CLIP[-5:]}_CF_{os.path.basename(i)}")
for i in camera_meta:
    os.rename(i, f"{os.path.dirname(i)}/481_ND_{CLIP[-5:]}_CF_{os.path.basename(i)}")
os.rename(f"{abs_dir}/{CLIP}/Camera/FrontCenter/", f"{abs_dir}/{CLIP}/Camera/CameraFront/")
os.rename(f"{abs_dir}/{CLIP}/GNSS_INS/event1.txt", f"{abs_dir}/{CLIP}/GNSS_INS/481_ND_{CLIP[-5:]}_GI_001.txt")
for i in lidar:
    os.rename(i, f"{os.path.dirname(i)}/481_ND_{CLIP[-5:]}_LR_{os.path.basename(i)}")
for i in radar:
    os.rename(i, f"{os.path.dirname(i)}/481_ND_{CLIP[-5:]}_RF_{os.path.basename(i)}")
os.rename(f"{abs_dir}/{CLIP}/Radar/Radar_Center/", f"{abs_dir}/{CLIP}/Radar/RadarFront/")
os.rename(f"{abs_dir}/{CLIP}/Calib/Lidar_camera_calib/cam0.txt", f"{abs_dir}/{CLIP}/Calib/Lidar_camera_calib/481_ND_{CLIP[-5:]}_LCC_CF.txt")
os.rename(f"{abs_dir}/{CLIP}/Calib/Lidar_radar_calib/srs_front_center.txt", f"{abs_dir}/{CLIP}/Calib/Lidar_radar_calib/481_ND_{CLIP[-5:]}_LRC_RF.txt")
os.rename(f"{abs_dir}/{CLIP}/Calib/Lidar_radar_calib/srs_front_left.txt", f"{abs_dir}/{CLIP}/Calib/Lidar_radar_calib/481_ND_{CLIP[-5:]}_LRC_RFL.txt")
os.rename(f"{abs_dir}/{CLIP}/Calib/Lidar_radar_calib/srs_front_right.txt", f"{abs_dir}/{CLIP}/Calib/Lidar_radar_calib/481_ND_{CLIP[-5:]}_LRC_RFR.txt")
os.rename(f"{abs_dir}/{CLIP}/Calib/Lidar_radar_calib/srs_rear_left.txt", f"{abs_dir}/{CLIP}/Calib/Lidar_radar_calib/481_ND_{CLIP[-5:]}_LRC_RBL.txt")
os.rename(f"{abs_dir}/{CLIP}/Calib/Lidar_radar_calib/srs_rear_right.txt", f"{abs_dir}/{CLIP}/Calib/Lidar_radar_calib/481_ND_{CLIP[-5:]}_LRC_RBR.txt")
os.rename(f"{abs_dir}/{CLIP}/Calib/", f"{abs_dir}/{CLIP}/calib/")