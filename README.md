# Simple-Python-OCR
translate simple image verification code to string by Python

###安装
```
#1 pytesseract 在线安装
#2 Pillow （64位python2.7的非官方版PIL封装库 主要包含Image等图像处理模块 
视本地python版本而定 32位python可以直接安装官方PIL库 则无需再安装Pillow) 和
#3 tesseract-ocr位于./src目录
```
- 1.[pytesseract](https://github.com/madmaze/pytesseract)
    - pip install pytesseract
        
- 2.[Pillow](http://www.lfd.uci.edu/~gohlke/pythonlibs/)
    - cd ./src
    - pip install ./Pillow-3.0.0-cp27-none-win_amd64.whl
        
- 3.[tesseract-ocr](https://code.google.com/p/tesseract-ocr/)
    - cd ./src && 双击*.exe文件
    - 安装时点选额外安装English语言包
    - 安装完成后 用本项目中src/eng.traineddata文件覆盖原*:\Program Files (x86)\Tesseract-OCR\tessdata\eng.traineddata
         

###运行
- 将ocr.py与调用脚本置于同一目录

```   
>>>import ocr
>>>text = ocr.image_to_string("test.jpg")
>>>print text
ackgza
```



  <br>
   <br>
   <br>
   <br>
   <br>
   <br>
   <br>
   <br>
   <br>
   <br>
   <br>
   <br>
   <br>
   <br>
   <br>
   <br>
   <br>
   <br>
   <br>
   <br>
   <br>
   <br>
   <br>
   <br>
   <br>

 

 
 

 
 

 

 

 
 

 
 
 

 
- 其他
    - [Pillow 其他架构的非官方PIL封装](http://www.itnose.net/detail/6190636.html)
    - [tesseract-ocr 字符识别的样本训练](http://blog.csdn.net/yasi_xi/article/details/8763385)
    - [训练集编辑器jTessBoxEditor主页](http://vietocr.sourceforge.net/training.html)
    - [jTessBoxEditor下载](http://sourceforge.net/projects/vietocr/files/jTessBoxEditor/)
    - [GUIs and Other Projects using Tesseract OCR](https://github.com/tesseract-ocr/tesseract/wiki/3rdParty#gui)
