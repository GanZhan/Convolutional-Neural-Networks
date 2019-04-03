import numpy as np
import math

img = np.array([[[1,1,1],
                 [2,2,2],
                 [3,3,3]],

                [[4,4,4],
                 [5,5,5],
                 [6,6,6]],

                [[7,7,7],
                 [8,8,8],
                 [9,9,9]]])

# img = np.array([[[1,2,3],
#                  [4,5,6],
#                  [7,8,9]]])
print(np.shape(img))

def im2col(img_matrix, window_height, window_width, stride=1):
    """
    padding is default as "valid", i suggest we do padding before im2col
    first calculate the number of anchors based on the given params: img_matrix, window_height, window_width, stride=1
    then in the loop for anchors: get the index of temp anchor, fill the rest part of window
    repeat it.
    :param img_matrix:
    :param window_height:
    :param window_width:
    :param stride:
    :return:
    """
    img_c, img_h, img_w = np.shape(img_matrix)
    if window_width>img_w or window_height>img_h:
        print("the conv window is too large for input image, check the window height or width.")
        return None
    else:
        # round down principle,calculate how many steps filter window should move in row direction and col direction
        row_steps = math.floor((img_w - window_width)/stride) + 1
        col_steps = math.floor((img_h - window_height)/stride) + 1
        filter_window = []

        for c in range(img_c):
            channel_window = []
            for i in range(col_steps):
                for j in range(row_steps):
                    window_temp = []
                    # find the anchor first, then get the elements of whole window
                    anchor = img_matrix[c, i*stride, j*stride]
                    for k in range(window_height):
                        for m in range(window_width):
                            window_temp.append(img_matrix[c, i*stride+k, j*stride+m])
                    channel_window.append(window_temp)
            filter_window.append(channel_window)
            # don't forget change the type of filter_window
            # list and numpy array are different data types.
        filter_window = np.array(filter_window)
        return filter_window

im2col_matrxi = im2col(img, 2, 2, stride=1)
im2col_shape = np.shape(im2col_matrxi)
print(im2col_matrxi)
print(im2col_shape)
