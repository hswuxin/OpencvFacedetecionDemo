OpenCV haar级联分类器使用
===
环境配置
---
* Python 3.7.7
* opencv-python 3.4.3.18

文件介绍
---
`haarcascade_frontalface_alt2`：检测人脸快速LBP<br><br>
`haarcascade_eye_tree_eyeglasses.xml` ：检测是否戴眼镜<br><br>
`haarcascade_eye.xml`：检测眼睛<br><br>
`haarcascade_profileface`：检测是否斜视<br><br>

参数介绍
---
`detectMultiScale`<br>
* image–待检测图片，一般为灰度图像加快检测速度
* objects–被检测物体的矩形框向量组
* scaleFactor–表示在前后两次相继的扫描中，搜索窗口的比例系数,默认为1.1即每次搜索窗口依次扩大10%
* minNeighbors–表示构成检测目标的相邻矩形的最小个数(默认为3个)
* _minSize为目标的最小尺寸_
* _maxSize为目标的最大尺寸_
