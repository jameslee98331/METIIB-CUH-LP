import numpy as np
from collections import namedtuple
from data_processing import imgproc


def test_crop():
    test_img = np.asarray([[(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6), (1, 2, 3)],
                           [(2, 3, 4), (5, 6, 7), (1, 2, 3), (1, 2, 3), (4, 5, 6)],
                           [(4, 5, 6), (7, 8, 9), (5, 6, 7), (7, 6, 5), (1, 2, 3)],
                           [(3, 4, 5), (7, 8, 5), (1, 2, 4), (4, 5, 6), (5, 6, 7)],
                           [(8, 6, 7), (9, 0, 0), (8, 6, 5), (1, 3, 4), (1, 2, 3)]])
    test_start = (2, 2)
    test_finish = (4, 4)
    test_rect = namedtuple('rect', 'start, finish')
    test_corner = test_rect(test_start, test_finish)

    assert np.array_equal(imgproc.crop(test_img, test_corner), np.asarray([[(5, 6, 7), (7, 6, 5)],
                                                                       [(1, 2, 4), (4, 5, 6)]]))
