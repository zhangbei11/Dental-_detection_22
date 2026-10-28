import warnings
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '3'
import tqdm

warnings.filterwarnings('ignore')
from ultralytics import RTDETR
if __name__ == '__main__':
    model = RTDETR('/data/zhangb/code/ultralytics-8.4.190/ultralytics/cfg/models/rt-detr/rtdetr-resnet50.yaml')
    model.train(data="/data/zhangb/code/ultralytics-8.4.190/ultralytics/cfg/datasets/tooth_oral22.yaml",
                cache=False,
                imgsz=640,
                epochs=100,
                batch=8,
                workers=4,
                # device='0,1',
                # resume='',  # last.pt path
                project='/data/zhangb/code/ultralytics-8.4.190/runs/train-22',
                name='1027-baseline'
                )