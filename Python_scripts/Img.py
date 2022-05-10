import cv2
import numpy as np

image1 = cv2.imread('xxx.png')  #画像ファイル名
image2 = cv2.imread('yyy.png.png')  #比較する画像ファイル名

"""
比較する画像ファイルを複数用意する場合は
上記の様に
変数名 = cv2.imread('画像ファイル名')と指定してやれば良い
"""

img_size = (200 , 200)  ##画像サイズの設定

image1 = cv2.resize(image1 , img_size)  #画像ファイルのリサイズ
image2 = cv2.resize(image2 , img_size)  #画像ファイルのリサイズ

print(np.count_nonzero(image1 == image2) / image1.size) #画像の一致率を比較して出力