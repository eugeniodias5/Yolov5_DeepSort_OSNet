import os, shutil, random
from re import search

from requests import options

VIDEOS_PATH = os.path.join('..', '..', '..', '..', 'NoFilterSelection', 'Videos_renamed')
DATABASE_PATH = os.path.join('..', '..', '..', 'metadata', 'database')
YOLO_MODEL = "yolov5s.pt"
IMG_SIZE = "1280"
# Detect only dogs
CLASSES = "16"
OPTIONS = "--save-vid --save-crop"

# Check if folder 'Database' exists
if not os.path.exists(DATABASE_PATH):
    os.makedirs(DATABASE_PATH)

# Running each video in the Videos_Path
for video in os.listdir(VIDEOS_PATH):
    # Getting the number of the camera
    num_cam = "Camera_" + video.split("Indonesia_C")[1][:2]

    db_folder = os.path.join(DATABASE_PATH, num_cam, video.split('.')[0])
    video_folder = os.path.join(VIDEOS_PATH, video)
    # Running command on terminal
    os.system(f"python track.py --source {video_folder} --project {db_folder} --yolo_model {YOLO_MODEL} --img {IMG_SIZE} --classes {CLASSES} {OPTIONS}")

    # If there are no folders inside db_folder, delete it
    num_folders = len([folder for folder in os.listdir(db_folder) if os.path.isdir(os.path.join(db_folder, folder))])
    if num_folders == 0:
        shutil.rmtree(db_folder, ignore_errors=True)
