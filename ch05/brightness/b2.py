import cv2
import numpy as np

# 이미지 파일 경로
path = "lenna.bmp"

# 컬러로 읽기 (BGR)
img = cv2.imread(path, cv2.IMREAD_COLOR)
if img is None:
    raise FileNotFoundError(f"이미지를 찾을 수 없음: {path}")

# 또는 방법 B: OpenCV 함수 사용 (같은 결과, 조금 더 간편)
alpha = 1.0  # 대비(스케일)
beta = 50   # 밝기 추가량
bright = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

# 결과 저장 및 표시
cv2.imwrite("lena_2.png", bright)
# 화면에서 바로 보려면 (GUI 환경에서만 작동)
cv2.imshow("bright", bright)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("저장 완료: lena_2.png")
