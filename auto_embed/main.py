import os
from collections import namedtuple
import cv2

from auto_embed import imgproc
from auto_embed import config

DEBUG = True


def main():

    # Capture Image
    # img = img_capture.capture()

    # Data cleaning process
    data_dir = config.file_paths['data_root_path']
    img_dir = os.path.join(data_dir, 'batch_3')
    crop_rec = namedtuple('crop_rec', 'start, end')

    for img_name in os.listdir(img_dir):
        img = cv2.imread(os.path.join(img_dir, img_name))
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        start_col, start_row, width, height, rect = imgproc.bounding_box(hsv_img)

        # To keep the cropped image square
        side_len = min(width, height)
        crop_rec.start = (start_row, start_col)
        crop_rec.end = (start_row + side_len, start_col + side_len)
        crop_img = imgproc.crop(img, crop_rec)
        out_path = data_dir + '//cleaned//clean_' + img_name
        cv2.imwrite(out_path, crop_img)

        if DEBUG:
            imgproc.view_img(img)
            imgproc.view_img(crop_img)
            imgproc.view_img(rect)


if __name__ == '__main__':
    main()
