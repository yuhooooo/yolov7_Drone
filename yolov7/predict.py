#-----------------------------------------------------------------------#
#   predict.py进行目录遍历检测等功能
#   
#-----------------------------------------------------------------------#

from PIL import Image
from yolo import YOLO
import os
import json

result_path=""
def get_test(path):
    data={    "res":[]    }
   
    video=os.listdir(path)
    txt = os.path.basename(path)
    exist=os.listdir(result_path)
    file=txt+".txt"
    if (file in exist):
        return
    
    
   
    
        
    for img in video:
        img=os.path.join(path, img)          
        try:
            image = Image.open(img)
        except:
            print('Open Error! Try again!')
            continue
        else:
            is_exist,x,y,w,h = yolo.detect_image(image)
            if is_exist :                
                x=int(x)
                y=int(y)
                w=int(w)
                h=int(h)
                          
                data["res"].append([x,y,w,h])
            else :
                data["res"].append([])

    with open(result_path+"/"+file, "w") as f:                
        f.write(json.dumps(data))
   
   



if __name__ == "__main__":
   
    mode = "predict"
  
   
  
    yolo = YOLO()
    
    if mode == "predict":
        '''
        1、如果想要进行检测完的图片的保存，利用r_image.save("img.jpg")即可保存，直接在predict.py里进行修改即可。 
        2、如果想要获得预测框的坐标，可以进入yolo.detect_image函数，在绘图部分读取top，left，bottom，right这四个值。
        3、如果想要利用预测框截取下目标，可以进入yolo.detect_image函数，在绘图部分利用获取到的top，left，bottom，right这四个值
        在原图上利用矩阵的方式进行截取。
        4、如果想要在预测图上写额外的字，比如检测到的特定目标的数量，可以进入yolo.detect_image函数，在绘图部分对predicted_class进行判断，
        比如判断if predicted_class == 'car': 即可判断当前目标是否为车，然后记录数量即可。利用draw.text即可写字。
        '''       
       
        
        # 获取当前文件路径
        current_path = os.path.abspath(__file__)
        # 获取当前文件的父目录
        father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
        # 获取当前文件的父目录的父目录
        father_father_path = os.path.abspath(os.path.dirname(father_path) + os.path.sep + ".")
        result_path=os.path.abspath(father_father_path+ os.path.sep+"result")
        
        # 获取test文件夹目录
        test_path = os.path.abspath(father_father_path+ os.path.sep+"test")
        
        # 遍历每个文件夹，代表一个视频
     
         
        
        for folder in os.listdir(test_path):  
            get_test(os.path.join(test_path, folder))


        

