import numpy as np
import matplotlib.pyplot as plt

plt.rc("font", size=18)  # 그림의 폰트 크기를 18로 고정
gray = {"facecolor": "gray"}
black = {"facecolor": "black"}
red = {"facecolor": "red"}
green = {"facecolor": "green"}
blue = {"facecolor": "blue"}

a = np.array([1, 2])
b = np.array([2, 1])
c = a + b
plt.annotate('', xy=a, xytext=(0, 0), arrowprops=gray)
plt.annotate('', xy=b, xytext=(0, 0), arrowprops=gray)
plt.annotate('', xy=c, xytext=(0, 0), arrowprops=black)
plt.plot(0, 0, 'kP', ms=10)
plt.plot(a[0], a[1], 'ro', ms=10)
plt.plot(b[0], b[1], 'ro', ms=10)
plt.plot(c[0], c[1], 'ro', ms=10)
plt.plot([a[0], c[0]], [a[1], c[1]], 'k--')
plt.plot([b[0], c[0]], [b[1], c[1]], 'k--')
plt.text(0.35, 1.15, "$a$")
plt.text(1.15, 0.25, "$b$")
plt.text(1.25, 1.45, "$c$")
plt.xticks(np.arange(-2, 5))
plt.yticks(np.arange(-1, 4))
plt.xlim(-1.4, 4.4)
plt.ylim(-0.6, 3.8)
plt.title(" sum of vectors")
plt.show()


''' 벡터의 합 - 두번째 벡터를 첫번째 벡터의 끝점으로 평행이동 한 후 
원점에서 부터 평행 이동한 벡터의 끝점 까지의 벡터와 동일 '''


a = np.array([1, 2])
b = np.array([2, 1])
c = a + b
plt.annotate('', xy=a, xytext=(0, 0), arrowprops=gray)
plt.annotate('', xy=c, xytext=a, arrowprops=gray)
plt.annotate('', xy=c, xytext=(0, 0), arrowprops=black)
plt.plot(0, 0, 'kP', ms=10)
plt.plot(a[0], a[1], 'ro', ms=10)
plt.plot(c[0], c[1], 'ro', ms=10)
plt.text(0.35, 1.15, "$a$")
plt.text(1.45, 2.45, "$b$")
plt.text(1.25, 1.45, "$c$")
plt.xticks(np.arange(-2, 5))
plt.yticks(np.arange(-1, 4))
plt.xlim(-1.4, 4.4)
plt.ylim(-0.6, 3.8)
plt.title(" sum of vectors 2 ")
plt.show()

