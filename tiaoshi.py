# import cv2
# import numpy as np
#
# img1 = cv2.imread("D:\\demo\\lesson\\wuziqi\\fiveChess-main\\fiveChess-main\\package\\PVE.png")
# img2 = cv2.resize(img1, (512, 512))
# cv2.imshow('start', img2)
# cv2.imwrite("D:\\demo\\lesson\\wuziqi\\fiveChess-main\\fiveChess-main\\package\\PVE02.png",img2)
# cv2.waitKey()
# cv2.destroyWindow('start')
import cv2
import numpy as np
#144621、142832、142836、142744、142739、142733、145448、

# 图片路径
img = cv2.imread("start02.png")
a = []
b = []


def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        a.append(x)
        b.append(y)
        cv2.circle(img, (x, y), 1, (0, 0, 255), thickness=-1)
        cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                    1.0, (0, 0, 0), thickness=1)
        cv2.imshow("image", img)


cv2.namedWindow("image")
cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
cv2.imshow("image", img)
cv2.waitKey(0)
print(a[0], b[0])

