import os
from collections import namedtuple
import cv2

from auto_embed import imgproc
from auto_embed import config


def main():

    # Data cleaning process
    data_dir = config.file_paths['data_root_path']
    img_dir = os.path.join(data_dir, "batch_2//pigskin")
    crop_rec = namedtuple("crop_rec", "start, end")

    for img_name in os.listdir(img_dir):
        img = cv2.imread(os.path.join(img_dir, img_name))
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        x, y, w, h, _ = imgproc.bounding_box(hsv_img)
        crop_rec.start = (y, x)
        crop_rec.end = (y + h, x + w)
        crop_img = imgproc.crop(img, crop_rec)
        imgproc.view_img(crop_img)

        out_path = data_dir + "//cleaned//clean_" + img_name
        cv2.imwrite(out_path, crop_img)

    # Data augmentation process

    # Save data with pickle


if __name__ == '__main__':
    main()
