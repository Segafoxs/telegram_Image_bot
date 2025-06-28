import cv2

def downLoadsImage(file_ids):
    image = cv2.imread("downloads\\{}.jpg".format(file_ids[0]))
    return image

def resized_photo(image):
    final_wide = 800
    r = float(final_wide) / image.shape[1]
    d = (final_wide, int(image.shape[0] * r))
    return cv2.resize(image, d, interpolation=cv2.INTER_AREA)

