import os
from collections import namedtuple
import cv2

from auto_embed import imgproc
from auto_embed import config
from auto_embed import img_capture

DEBUG = True


def on_edge(input_img):

    orientation = [0, 0, 0]

    # Capture Image
    # img = img_capture.capture()

    # Data cleaning process
    data_dir = config.file_paths['data_root_path']
    img_dir = os.path.join(data_dir, 'batch_4')
    crop_rec = namedtuple('crop_rec', 'start, end')

    if DEBUG:
        count = 0

    for img_name in os.listdir(img_dir):
        img = cv2.imread(os.path.join(img_dir, img_name))
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        start_col, start_row, width, height, rect = imgproc.bounding_box(hsv_img)

        # To keep the cropped image square
        side_len = min(width, height)
        crop_rec.start = (start_row, start_col)
        crop_rec.end = (start_row + side_len, start_col + side_len)
        crop_img = imgproc.crop(img, crop_rec)


        bgr = cv2.cvtColor(crop_img, cv2.COLOR_HSV2BGR)
        eq_img = imgproc.hisEqulColor(bgr)
        # lab = cv2.cvtColor(rgb, cv2.COLOR_RGB2LAB)
        # CLAHE = cv2.createCLAHE()
        # contrast_img = CLAHE.apply(lab)


        out_path = data_dir + '//cleaned//clean_' + img_name
        cv2.imwrite(out_path, img)

        if DEBUG:
            imgproc.view_img(img)
            imgproc.view_img(eq_img)
            imgproc.view_img(rect)
            count += 1
            if count > 5:
                break

    return orientation


if __name__ == '__main__':

    if not DEBUG:
        # Initialise cameras
        video_capture = cv2.VideoCapture(0)

    while True:
        # 1. Integration with Automation System
        # TODO:
        #   - code to communicate with PLC and asks for clamp status
        #   - receive bool isClamp flag from PLC when new G120C FSAA is in place and clamped
        # e.g. isClamped = plc.request_status()

        # Placeholder code for assuming product is clamped
        isClamped = True

        if not isClamped:
            continue

        isClamped = False

        # 2. Image capture
        if not DEBUG:
            input_img = img_capture.img_capture(video_capture)

        # PLACEHOLDER CODE FOR READING TEMPORARY IMAGES FOR DEMO PURPOSE
        else:
            filepath = 'sample_files//TUBULAR.JPG'
            input_img = cv2.imread(filepath)

        orientation = end_orientation(input_img)
        # orientation = edge_orientation(input_img)

    # # 7. Robot control
    # # todo
    #   - potential to use a Siemens IOT2020/2040 to run this code/communicate with the PLC
    #     robot.send(x_offset, z_offset, rotation)
    #
        # If the entire testing process is complete, exit the while loop
        isComplete = True
        if isComplete:
            break

    if not DEBUG:
        # Close connection to camera device
        video_capture.release()
