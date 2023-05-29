import os
import glob
import json
import os
from sklearn import model_selection
import random
import random

def get_all(path):
    with open("all.txt", "w") as f:
        f.close()

    # 遍历每个文件夹，代表一个视频
    folders=os.listdir(path)
    print(folders)
    random.shuffle(folders)
    for folder in folders:
        # 创建一个空的数据集列表
        dataset = []
        # 获取视频的标注文件路径
        label_file = os.path.join(path, folder, "IR_label.json")
        # 打开标注文件并读取内容
        with open(label_file, "r") as f:
            label_data = json.load(f)
        # 遍历每一帧图像和对应的标注
        for i in range(len(label_data["exist"])):
            # 获取图像文件路径
            name=i+1
            image_file = os.path.join(path, folder, f"{name:06d}.jpg")

            # 获取该帧是否存在无人机的标志
            exist = label_data["exist"][i]
            # 获取该帧无人机的坐标，如果不存在则为空列表
            if exist ==1 :
                gt_rect = label_data["gt_rect"][i]
                gt_rect[2]=gt_rect[2]+ gt_rect[0]
                gt_rect[3]= gt_rect[3]+ gt_rect[1]

            # 将图像和标注组成一个元组并添加到数据集列表中
            dataset.append((image_file, exist, gt_rect))
        with open("all.txt", "a+") as f:    #打开文件
        
            # 返回数据集列表
            for i in range(len(dataset)):
                f.write(dataset[i][0])  #这句话自带文件关闭功能，不需要再写f.close()
                if dataset[i][1]==1:
                    str = ','.join('%s' %id for id in dataset[i][2])
                    f.write(" "+str+",0")  #这句话自带文件关闭功能，不需要再写f.close()


                f.write("\n")  #这句话自带文件关闭功能，不需要再写f.close()

def get_train(path="all.txt"):
    # 使用random.random()方法
    with open(path, "r") as f:
        n = sum(1 for line in f) # 获取总行数
        m = int(n * 0.8) # 计算80%的行数
        f.seek(0) # 重置文件指针到开头
        with open("train.txt", "w") as f1, open("test.txt", "w") as f2:
            for line in f:
                r = random.random() # 生成一个0到1之间的随机数
                if r < 0.2: # 以20%的概率写入到test.txt
                    f2.write(line)

                f1.write(line)# 以100%的概率写入到train.txt
    
def append_test():
   
    folders=os.listdir(test_path)

    for folder in folders:
        # 创建一个空的数据集列表
        dataset = []
        # 获取视频的标注文件路径
        label_file = os.path.join(test_path, folder, "IR_label.json")
        # 打开标注文件并读取内容
        with open(label_file, "r") as f:
            label_data = json.load(f)
        # 遍历每一帧图像和对应的标注
        for i in range(1):
            # 获取图像文件路径
            name=i+1
            image_file = os.path.join(test_path, folder, f"{name:06d}.jpg")

            # 获取该帧是否存在无人机的标志
            gt_rect = label_data["res"][i]
            print(len(gt_rect))
            print(gt_rect)
            # 获取该帧无人机的坐标，如果不存在则为空列表
            if len(gt_rect) ==4 :

                gt_rect[2]=gt_rect[2]+ gt_rect[0]
                gt_rect[3]= gt_rect[3]+ gt_rect[1]

            # 将图像和标注组成一个元组并添加到数据集列表中
            dataset.append((image_file, 1, gt_rect))

        with open("test.txt", "a+") as f:    #打开文件
        
            # 返回数据集列表
            for i in range(len(dataset)):
                f.write(dataset[i][0])  #这句话自带文件关闭功能，不需要再写f.close()
                if dataset[i][1]==1:

                    str = ','.join('%s' %id for id in dataset[i][2])
                    f.write(" "+str+",0")  #这句话自带文件关闭功能，不需要再写f.close()


                f.write("\n")  #这句话自带文件关闭功能，不需要再写f.close()







# 获取当前文件路径
current_path = os.path.abspath(__file__)
# 获取当前文件的父目录
father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
# 获取当前文件的父目录的父目录
father_father_path = os.path.abspath(os.path.dirname(father_path) + os.path.sep + ".")
# 获取train文件夹目录
train_path = os.path.abspath(father_father_path+ os.path.sep+"train")

test_path = os.path.abspath(father_father_path+ os.path.sep+"test")

get_all(train_path)
get_train()
append_test()


            
