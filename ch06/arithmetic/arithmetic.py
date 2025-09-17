import cv2

def main():
    src1 = cv2.imread("lenna256.bmp", cv2.IMREAD_GRAYSCALE)
    src2 = cv2.imread("square.bmp", cv2.IMREAD_GRAYSCALE)

    if src1 is None or src2 is None:
        print("Image load failed!")
        return

    cv2.imshow("src1", src1)
    cv2.imshow("src2", src2)

    # 산술 연산
    dst1 = cv2.add(src1, src2)                        # 단순 덧셈 (포화연산)
    dst2 = cv2.addWeighted(src1, 0.5, src2, 0.5, 0)   # 가중치 합 (평균)
    dst3 = cv2.subtract(src1, src2)                   # 뺄셈 (음수는 0으로 클램핑)
    dst4 = cv2.absdiff(src1, src2)                    # 절댓값 차이

    # 결과 출력
    cv2.imshow("dst1", dst1)
    cv2.imshow("dst2", dst2)
    cv2.imshow("dst3", dst3)
    cv2.imshow("dst4", dst4)

    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
