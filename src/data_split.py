import os
import shutil
import random

SOURCE_DIR = "data/PlantVillage"
TARGET_DIR = "data"

train_path = os.path.join(TARGET_DIR, "train")
val_path   = os.path.join(TARGET_DIR, "val")
test_path  = os.path.join(TARGET_DIR, "test")

for p in [train_path, val_path, test_path]:
    os.makedirs(p, exist_ok=True)

for cls in os.listdir(SOURCE_DIR):
    cls_path = os.path.join(SOURCE_DIR, cls)
    if not os.path.isdir(cls_path):
        continue

    images = os.listdir(cls_path)
    random.shuffle(images)

    n = len(images)
    train_split = int(0.8 * n)
    val_split   = int(0.9 * n)

    train_imgs = images[:train_split]
    val_imgs   = images[train_split:val_split]
    test_imgs  = images[val_split:]

    os.makedirs(os.path.join(train_path, cls), exist_ok=True)
    os.makedirs(os.path.join(val_path, cls), exist_ok=True)
    os.makedirs(os.path.join(test_path, cls), exist_ok=True)

    for img in train_imgs:
        shutil.copy(os.path.join(cls_path, img), os.path.join(train_path, cls))

    for img in val_imgs:
        shutil.copy(os.path.join(cls_path, img), os.path.join(val_path, cls))

    for img in test_imgs:
        shutil.copy(os.path.join(cls_path, img), os.path.join(test_path, cls))

print("Dataset split into train/val/test.")
