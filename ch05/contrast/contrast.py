import cv2
import numpy as np

def contrast1():
    src = cv2.imread(r"C:\tortoisegit_opencv\lenna.bmp", cv2.IMREAD_GRAYSCALE)
    if src is None:
        print("Image load failed!")
        return

    s = 2.0
    dst = cv2.multiply(src, s)

    cv2.imshow("src", src)
    cv2.imshow("dst", np.clip(dst, 0, 255).astype(np.uint8))
    cv2.waitKey()
    cv2.destroyAllWindows()

def contrast2():
    src = cv2.imread(r"C:\tortoisegit_opencv\lenna.bmp", cv2.IMREAD_GRAYSCALE)
    if src is None:
        print("Image load failed!")
        return

    alpha = 1.0
    dst = src + (src - 128) * alpha

    cv2.imshow("src", src)
    cv2.imshow("dst", np.clip(dst, 0, 255).astype(np.uint8))
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    contrast1()
    contrast2()
