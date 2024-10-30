import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 日本語フォントの設定
font_path = '/usr/share/fonts/opentype/ipafont-gothic/ipagp.ttf'  # システム内のIPAフォントパスを指定
font_prop = fm.FontProperties(fname=font_path)  # フォントプロパティとして指定

# --- 問題1のグラフ ---
X = np.array([-3, -1, 1, 3])
Y = np.array([0, 1, 2, 4])

A = np.vstack([X, np.ones(len(X))]).T
a, b = np.linalg.lstsq(A, Y, rcond=None)[0]

plt.figure(figsize=(8, 6))
plt.scatter(X, Y, color='blue', label='データ点')
plt.plot(X, a * X + b, color='red', label=f'回帰直線: y = {a:.2f}x + {b:.2f}')
plt.xlabel('X', fontproperties=font_prop)
plt.ylabel('Y', fontproperties=font_prop)
plt.title('最小二乗法による直線フィッティング', fontproperties=font_prop)
plt.legend(prop=font_prop)
plt.grid(True)
plt.savefig("linear_fit.png")
plt.show()

# --- 問題Ex1のグラフ ---
A_ex1 = np.vstack([X**2, X, np.ones(len(X))]).T
a_ex1, b_ex1, c_ex1 = np.linalg.lstsq(A_ex1, Y, rcond=None)[0]

x_plot = np.linspace(-4, 4, 100)
y_plot = a_ex1 * x_plot**2 + b_ex1 * x_plot + c_ex1

plt.figure(figsize=(8, 6))
plt.scatter(X, Y, color='blue', label='データ点')
plt.plot(x_plot, y_plot, color='red', label=f'回帰曲線: y = {a_ex1:.2f}x^2 + {b_ex1:.2f}x + {c_ex1:.2f}')
plt.xlabel('X', fontproperties=font_prop)
plt.ylabel('Y', fontproperties=font_prop)
plt.title('最小二乗法による二次関数フィッティング', fontproperties=font_prop)
plt.legend(prop=font_prop)
plt.grid(True)
plt.savefig("quadratic_fit.png")
plt.show()
