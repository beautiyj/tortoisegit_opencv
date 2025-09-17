import cv2
import numpy as np
import matplotlib.pyplot as plt

def calcGrayHist(img):
    assert len(img.shape) == 2  # grayscale check
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    return hist

def getGrayHistImage(hist):
    hist = hist.flatten()
    hist_max = hist.max()

    imgHist = np.full((100, 256), 255, dtype=np.uint8)
    for x in range(256):
        cv2.line(imgHist, (x, 100),
                 (x, 100 - int(hist[x] * 100 / hist_max)),
                 color=0)
    return imgHist

def histogram_stretching():
    src = cv2.imread("hawkes.bmp", cv2.IMREAD_GRAYSCALE)
    if src is None:
        print("Image load failed!")
        return

    gmin, gmax, _, _ = cv2.minMaxLoc(src)
    dst = ((src - gmin) * 255.0 / (gmax - gmin)).astype(np.uint8)

    cv2.imshow("src", src)
    cv2.imshow("srcHist", getGrayHistImage(calcGrayHist(src)))
    cv2.imshow("dst", dst)
    cv2.imshow("dstHist", getGrayHistImage(calcGrayHist(dst)))

    cv2.waitKey()
    cv2.destroyAllWindows()

def histogram_equalization():
    src = cv2.imread("hawkes.bmp", cv2.IMREAD_GRAYSCALE)
    if src is None:
        print("Image load failed!")
        return

    dst = cv2.equalizeHist(src)

    cv2.imshow("src", src)
    cv2.imshow("srcHist", getGrayHistImage(calcGrayHist(src)))
    cv2.imshow("dst", dst)
    cv2.imshow("dstHist", getGrayHistImage(calcGrayHist(dst)))

    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    histogram_stretching()
    histogram_equalization()
