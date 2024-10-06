import cv2
import numpy as np
from ultralytics import YOLO
import time


class Yolo_Detect:
    def __init__(self):
        # 指定您的权重文件路径
        weight_path = r"D:\STEAM游戏软件路径\pythonProject\YOLOv8\Yolov8_ros\yolov8_ros\weights\best.pt"  # 请替换为您的实际权重文件路径

        self.model = YOLO(weight_path)
        self.model.fuse()

        self.conf = 0.5  # 可以根据需要调整置信度阈值
        self.visualize = True

        # 初始化摄像头
        self.cap = cv2.VideoCapture(1)

        self.visualize = True

    def run(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            # 运行YOLOv8检测
            start_time = time.time()
            results = self.model(frame, show=False, conf=self.conf)
            end_time = time.time()

            # 计算FPS
            fps = 1 / (end_time - start_time)

            self.dectshow(results[0], frame.shape[0], frame.shape[1])

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

    def dectshow(self, result, height, width):
        self.frame = result.plot()
        print(f"Inference time: {result.speed['inference']:.2f} ms")
        fps = 1000.0 / result.speed['inference']
        cv2.putText(self.frame, f'FPS: {int(fps)}', (20,50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2, cv2.LINE_AA)

        if self.visualize:
            cv2.imshow('YOLOv8', self.frame)

def main():
    yolo_detect = Yolo_Detect()
    yolo_detect.run()

if __name__ == "__main__":
    main()