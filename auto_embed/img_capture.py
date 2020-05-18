import cv2


def img_capture(vid_cap):
    """
    Args:
        vid_cap: Connection to camera opened by cv.VideoCapture(camera)
    Returns:
        np.ndarray: captured image nd array
    """

    # Read picture. ret === True on success
    ret, frame = vid_cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Check success
    if not ret:
        raise Exception("Camera not connected")

    return frame
