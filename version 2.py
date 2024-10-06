import os
import keyboard  # 用于监测键盘事件
import time
import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
from xarm import XArmAPI
from xarm.wrapper import XArmAPI
import subprocess
import sys
import threading
import importlib.util
import multiprocessing
from tkinter import messagebox
from tkinter import ttk

class RobotMain(object):
    def __init__(self, robot):
        self.alive = True
        self._arm = robot
        self._tcp_speed = 100
        self._tcp_acc = 2000
        self._angle_speed = 20
        self._angle_acc = 500
        self._variables = {}

        # 添加初始化代码
        self._arm.clean_warn()
        self._arm.clean_error()
        self._arm.motion_enable(True)
        self._arm.set_mode(0)
        self._arm.set_state(0)

        self._init_collision_detection()

    def _init_collision_detection(self):
        # 注册反馈数据回调函数
        self._arm.register_report_callback(self._report_callback)

    def _report_callback(self, report_data):
        # 在这里检查反馈数据,判断是否发生碰撞
        # 例如,检查电流是否超过一定阈值
        print(f"Received report: {report_data}")
        if max(report_data['motor_curr']) > 3:  # 根据实际情况调整这个阈值
            print('Collision detected!')
            self._arm.emergency_stop()

    def run_omelette_with_ingredients(self, ingredients):
        # 首先添加所有选中的配料
        for ingredient in ingredients:
            if ingredient == 'green capsicum':
                self.green_capsicum_path()
            elif ingredient == 'yellow capsicum':
                self.yellow_capsicum_path()
            elif ingredient == 'onion':
                self.onion_path()

        # 然后执行煎蛋卷操作
        self.run('omelette')

        # 最后执行机器视觉检测
        self.launch_machine_vision()

    def green_capsicum_path(self):
        print("Adding green capsicum")
        self._angle_speed = 40
        self._angle_acc = 800
        for i in range(int(1)):
            if not self.is_alive:
                break
            code = self._arm.set_servo_angle(angle=[0.0, -30.0, -30.0, 0.0, 60.0, 2.0], speed=self._angle_speed,
                                             mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_gripper_position(800, wait=True, speed=5000, auto_enable=True)
            if not self._check_code(code, 'set_gripper_position'):
                return
            code = self._arm.set_servo_angle(angle=[-45.9, -29.6, -21.5, -177.1, 42.2, 2.0],
                                             speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_servo_angle(angle=[-88.1, -23.4, -17.9, -180.2, 45.7, -1.1],
                                             speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_servo_angle(angle=[-80.6, 17.3, -17.0, -166.4, 87.2, -1.1],
                                             speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_gripper_position(650, wait=True, speed=5000, auto_enable=True)
            if not self._check_code(code, 'set_gripper_position'):
                return
            code = self._arm.set_servo_angle(angle=[-82.6, 22.3, -25.8, -168.4, 87.4, -1.6],
                                             speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_gripper_position(520, wait=True, speed=5000, auto_enable=True)
            if not self._check_code(code, 'set_gripper_position'):
                return
            code = self._arm.set_servo_angle(angle=[-85.2, -20.9, -26.8, -167.0, 44.0, -10.5],
                                             speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_servo_angle(angle=[61.2, 11.7, -66.1, -38.4, 134.1, -31.6],
                                             speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_servo_angle(angle=[95.9, 32.0, -77.4, 10.9, 131.8, 6.5], speed=self._angle_speed,
                                             mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_servo_angle(angle=[86.8, 33.4, -77.5, -1.5, 138.1, -180.7],
                                             speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_servo_angle(angle=[95.9, 32.0, -77.4, 10.9, 131.8, 6.5], speed=self._angle_speed,
                                             mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_servo_angle(angle=[61.2, 11.7, -66.1, -38.4, 134.1, -31.6],
                                             speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_servo_angle(angle=[-85.2, -20.9, -26.8, -167.0, 44.0, -10.5],
                                             speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_servo_angle(angle=[-82.6, 22.3, -25.8, -168.4, 87.4, -1.6],
                                             speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_gripper_position(650, wait=True, speed=5000, auto_enable=True)
            if not self._check_code(code, 'set_gripper_position'):
                return
            code = self._arm.set_servo_angle(angle=[-80.6, 17.3, -17.0, -166.4, 87.2, -1.1],
                                             speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_servo_angle(angle=[-88.1, -23.4, -17.9, -180.2, 45.7, -1.1],
                                             speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_servo_angle(angle=[-45.9, -29.6, -21.5, -177.1, 42.2, 2.0],
                                             speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_gripper_position(800, wait=True, speed=5000, auto_enable=True)
            if not self._check_code(code, 'set_gripper_position'):
                return
            code = self._arm.set_servo_angle(angle=[0.0, -30.0, -30.0, 0.0, 60.0, 2.0], speed=self._angle_speed,
                                             mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
        pass

    def yellow_capsicum_path(self):
        print("Adding yellow capsicum")
        self._angle_speed = 40
        self._angle_acc = 800
        for i in range(int(1)):
            if not self.is_alive:
                break
            code = self._arm.set_servo_angle(angle=[0.0, -30.0, -30.0, 0.0, 60.0, 2.0], speed=self._angle_speed,
                                             mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_gripper_position(800, wait=True, speed=5000, auto_enable=True)
            if not self._check_code(code, 'set_gripper_position'):
                return
            code = self._arm.set_servo_angle(angle=[-45.9, -29.6, -21.5, -177.1, 42.2, 2.0],
                                             speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_servo_angle(angle=[-51.0, -8.4, -29.8, -134.8, 57.6, -27.3],
                                             speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_servo_angle(angle=[-43.9, 24.4, -34.0, -130.9, 80.6, -8.4],
                                             speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_gripper_position(650, wait=True, speed=5000, auto_enable=True)
            if not self._check_code(code, 'set_gripper_position'):
                return
            code = self._arm.set_servo_angle(angle=[-52.0, 28.7, -43.2, -138.4, 76.0, -10.8],
                                             speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_gripper_position(520, wait=True, speed=5000, auto_enable=True)
            if not self._check_code(code, 'set_gripper_position'):
                return
            code = self._arm.set_servo_angle(angle=[-56.3, -8.2, -41.6, -129.4, 49.3, -37.4],
                                             speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_servo_angle(angle=[61.2, 11.7, -66.1, -38.4, 134.1, -31.6],
                                             speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_servo_angle(angle=[95.9, 32.0, -77.4, 10.9, 131.8, 6.5], speed=self._angle_speed,
                                             mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_servo_angle(angle=[86.8, 33.4, -77.5, -1.5, 138.1, -180.7],
                                             speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_servo_angle(angle=[95.9, 32.0, -77.4, 10.9, 131.8, 6.5], speed=self._angle_speed,
                                             mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_servo_angle(angle=[61.2, 11.7, -66.1, -38.4, 134.1, -31.6],
                                             speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_servo_angle(angle=[-56.3, -8.2, -41.6, -129.4, 49.3, -37.4],
                                             speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_servo_angle(angle=[-52.0, 28.7, -43.2, -138.4, 76.0, -10.8],
                                             speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_gripper_position(650, wait=True, speed=5000, auto_enable=True)
            if not self._check_code(code, 'set_gripper_position'):
                return
            code = self._arm.set_servo_angle(angle=[-43.9, 24.4, -34.0, -130.9, 80.6, -8.4],
                                             speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_servo_angle(angle=[-51.0, -8.4, -29.8, -134.8, 57.6, -27.3],
                                             speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_servo_angle(angle=[-45.9, -29.6, -21.5, -177.1, 42.2, 2.0],
                                             speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_gripper_position(800, wait=True, speed=5000, auto_enable=True)
            if not self._check_code(code, 'set_gripper_position'):
                return
            code = self._arm.set_servo_angle(angle=[0.0, -30.0, -30.0, 0.0, 60.0, 2.0], speed=self._angle_speed,
                                             mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
        pass

    def onion_path(self):
        print("Adding onion")
        # 这里添加切碎并加入洋葱的具体机械臂动作代码
        self._angle_speed = 40
        self._angle_acc = 800
        for i in range(int(1)):
            if not self.is_alive:
                break
            code = self._arm.set_servo_angle(angle=[0.0, -30.0, -30.0, 0.0, 60.0, 2.0], speed=self._angle_speed,
                                             mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_gripper_position(800, wait=True, speed=5000, auto_enable=True)
            if not self._check_code(code, 'set_gripper_position'):
                return
            code = self._arm.set_servo_angle(angle=[-45.9, -29.6, -21.5, -177.1, 42.2, 2.0],
                                             speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_servo_angle(angle=[-69.2, -19.2, -20.7, -155.2, 49.7, -16.9],
                                             speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_servo_angle(angle=[-57.5, 19.9, -23.6, -143.1, 83.9, -3.4],
                                             speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_gripper_position(650, wait=True, speed=5000, auto_enable=True)
            if not self._check_code(code, 'set_gripper_position'):
                return
            code = self._arm.set_servo_angle(angle=[-64.6, 24.7, -33.4, -150.0, 81.3, -5.4],
                                             speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_gripper_position(520, wait=True, speed=5000, auto_enable=True)
            if not self._check_code(code, 'set_gripper_position'):
                return
            code = self._arm.set_servo_angle(angle=[-69.4, -15.3, -32.9, -144.5, 46.4, -26.7],
                                             speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_servo_angle(angle=[61.2, 11.7, -66.1, -38.4, 134.1, -31.6],
                                             speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_servo_angle(angle=[95.9, 32.0, -77.4, 10.9, 131.8, 6.5], speed=self._angle_speed,
                                             mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_servo_angle(angle=[86.8, 33.4, -77.5, -1.5, 138.1, -180.7],
                                             speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_servo_angle(angle=[95.9, 32.0, -77.4, 10.9, 131.8, 6.5], speed=self._angle_speed,
                                             mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_servo_angle(angle=[61.2, 11.7, -66.1, -38.4, 134.1, -31.6],
                                             speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_servo_angle(angle=[-69.4, -15.3, -32.9, -144.5, 46.4, -26.7],
                                             speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_servo_angle(angle=[-64.6, 24.7, -33.4, -150.0, 81.3, -5.4],
                                             speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_gripper_position(650, wait=True, speed=5000, auto_enable=True)
            if not self._check_code(code, 'set_gripper_position'):
                return
            code = self._arm.set_servo_angle(angle=[-57.5, 19.9, -23.6, -143.1, 83.9, -3.4],
                                             speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_servo_angle(angle=[-69.2, -19.2, -20.7, -155.2, 49.7, -16.9],
                                             speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_servo_angle(angle=[-45.9, -29.6, -21.5, -177.1, 42.2, 2.0],
                                             speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
            code = self._arm.set_gripper_position(800, wait=True, speed=5000, auto_enable=True)
            if not self._check_code(code, 'set_gripper_position'):
                return
            code = self._arm.set_servo_angle(angle=[0.0, -30.0, -30.0, 0.0, 60.0, 2.0], speed=self._angle_speed,
                                             mvacc=self._angle_acc, wait=True, radius=60.0)
            if not self._check_code(code, 'set_servo_angle'):
                return
        pass

    def run(self, egg_type):
        try:
            if egg_type == 'sunny_side':
                # Insert the code from sunny_side_path.script here
                # sunny side egg
                self._angle_speed = 40
                self._angle_acc = 800
                for i in range(int(1)):
                    if not self.is_alive:
                        break
                    code = self._arm.set_servo_angle(angle=[0.0, -30.0, -30.0, 0.0, 60.0, 2.0], speed=self._angle_speed,
                                                     mvacc=self._angle_acc, wait=True, radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(800, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[48.3, -7.8, -42.1, -120.8, 60.1, 141.1],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[52.6, 38.6, -48.8, -127.3, 84.8, 174.1],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(550, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[49.5, 0.6, -40.0, -124.2, 66.4, 150.5],speed=self._angle_speed, mvacc=self._angle_acc, wait=True,radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[49.5, 0.6, -40.0, -124.2, 66.4, 150.5],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[-32.5, -12.3, -28.2, -186.1, 50.6, 186.1],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[-29.6, 18.9, -33.8, -181.8, 76.0, 182.6],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[-32.1, 20.8, -37.3, -174.0, 74.4, 209.6],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[-32.1, 20.8, -37.3, -174.0, 74.4, 319.5],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(400, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_gripper_position(500, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[-32.1, 20.8, -37.3, -174.0, 74.4, 209.6],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[-29.6, 18.9, -33.8, -181.8, 76.0, 182.6],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[-32.5, -12.3, -28.2, -186.1, 50.6, 186.1],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[49.5, 0.6, -40.0, -124.2, 66.4, 150.5],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[52.6, 38.6, -48.8, -127.3, 84.8, 174.1],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(800, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[48.3, -7.8, -42.1, -120.8, 60.1, 141.1],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return

                    code = self._arm.set_servo_angle(angle=[0.0, -30.0, -30.0, 0.0, 60.0, 2.0], speed=self._angle_speed,
                                                     mvacc=self._angle_acc, wait=True, radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(800, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[3.2, -42.3, -6.2, 194.9, 23.6, -186.9],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(350, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[23.1, -7.0, -4.1, 207.6, 59.5, -185.0],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(131, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[21.8, -2.5, -3.2, 203.9, 67.3, -95.0],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(350, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[23.0, -22.4, 1.0, 215.8, 44.6, -109.6],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[0.0, -30.0, -30.0, 0.0, 60.0, 2.0], speed=self._angle_speed,
                                                     mvacc=self._angle_acc, wait=True, radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[-53.0, -9.0, -18.5, -235.0, 69.0, 297.0],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(250, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[-57.8, 22.8, -22.5, -233.6, 82.9, 277.7],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[-50.4, 25.1, -26.7, -226.3, 81.6, 279.1],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(150, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[-52.4, 32.0, -28.8, -228.1, 91.6, 276.9],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(100, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[-49.4, 2.8, -19.6, -226.4, 77.7, 291.4],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[-49.4, 2.8, -19.6, -226.4, 77.7, 305.0],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[-49.3, -1.3, -19.2, -232.9, 59.6, 296.5],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[-49.6, 15.8, -19.2, -221.0, 102.5, 283.6],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[-49.4, 2.8, -19.6, -226.4, 77.7, 277.3],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[-49.4, 2.8, -19.6, -226.4, 77.7, 291.4],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[-34.7, 8.7, -41.0, -295.1, 104.3, 308.2],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[-32.0, 21.3, -47.3, -294.9, 100.9, 304.6],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[-31.8, 24.4, -48.1, -295.1, 99.9, 302.6],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    time.sleep(1)
                    code = self._arm.set_gripper_position(250, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[-40.7, 15.3, -32.9, -304.6, 99.6, 295.7],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[-43.9, -13.0, -31.3, -300.4, 115.6, 318.3],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[0.0, -30.0, -30.0, 0.0, 60.0, 2.0], speed=self._angle_speed,
                                                     mvacc=self._angle_acc, wait=True, radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[60.9, -33.3, -10.8, 11.6, 49.6, -31.2],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(124, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[63.0, -27.1, -8.3, 13.8, 40.9, -36.0],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(49, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[60.6, -46.4, -23.0, 9.1, 74.6, -30.3],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[0.7, 21.6, -97.0, 9.1, 74.5, -92.9],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[6.1, -3.4, -44.5, 16.7, -0.9, -105.5],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[13.2, 15.1, -29.1, 16.7, -72.6, -105.5],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[6.1, -3.4, -44.5, 16.7, -0.9, -105.5],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[0.7, 21.6, -97.0, 9.1, 74.5, -92.9],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[60.6, -46.4, -23.0, 9.1, 74.6, -30.3],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[63.0, -27.1, -8.3, 13.8, 40.9, -36.0],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(124, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[60.9, -33.3, -10.8, 11.6, 49.6, -31.2],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[0.0, -30.0, -30.0, 0.0, 60.0, 2.0], speed=self._angle_speed,
                                                     mvacc=self._angle_acc, wait=True, radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[-43.9, -13.0, -31.3, -300.4, 115.6, 318.3],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[-40.7, 15.3, -32.9, -304.6, 99.6, 295.7],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(250, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[-31.8, 24.4, -48.1, -295.1, 99.9, 302.6],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(100, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    time.sleep(1)
                    code = self._arm.set_servo_angle(angle=[-33.0, 6.3, -45.3, -292.9, 106.7, 316.7],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[84.5, -39.5, -9.2, -163.0, 43.1, 266.8],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[141.6, -7.7, -23.9, -108.7, 79.5, 249.8],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[111.9, -31.4, -15.1, -102.2, 72.1, 339.6],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[110.6, -44.7, -22.6, -95.4, 67.8, 318.0],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[110.6, -44.7, -22.6, -95.4, 67.8, 213.8],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[1.9, -34.0, -22.7, -180.8, 32.0, 267.3],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[-53.0, -9.0, -18.5, -235.0, 69.0, 297.0],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[-51.5, 22.2, -25.7, -228.8, 83.6, 277.3],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[-52.0, 29.0, -26.6, -227.0, 92.2, 277.6],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(150, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[-53.9, 31.0, -29.6, -232.1, 89.2, 277.1],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[-72.2, 29.8, -23.6, -250.3, 90.4, 272.5],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[0.0, -30.0, -30.0, 0.0, 60.0, 2.0], speed=self._angle_speed,
                                                     mvacc=self._angle_acc, wait=True, radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[3.2, -42.7, -6.1, 195.0, 23.4, -186.9],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(350, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[24.4, -4.1, -3.8, 208.8, 64.2, -185.2],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(131, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[23.2, -5.1, -4.5, 208.2, 60.7, -273.4],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(350, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[23.0, -22.4, 1.0, 215.8, 44.6, -185.5],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[0.0, -30.0, -30.0, 0.0, 60.0, 2.0], speed=self._angle_speed,
                                                     mvacc=self._angle_acc, wait=True, radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                pass
            elif egg_type == 'omelette':
                # omelette
                self._angle_speed = 30
                self._angle_acc = 800
                for i in range(int(1)):
                    if not self.is_alive:
                        break
                    code = self._arm.set_servo_angle(angle=[0.0, -30.0, -30.0, 0.0, 60.0, 2.0], speed=self._angle_speed,
                                                     mvacc=self._angle_acc, wait=True, radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(800, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[48.3, -7.8, -42.1, -120.8, 60.1, 141.1],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[52.6, 38.6, -48.8, -127.3, 84.8, 174.1],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(530, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[49.5, 0.6, -40.0, -124.2, 66.4, 150.5],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[70.1, 24.1, -57.1, -107.6, 80.1, 150.9],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[47.7, 14.2, -63.1, -35.7, 35.2, 77.0],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[38.3, 55.2, -136.2, 20.7, 105.2, 41.6],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(450, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_gripper_position(500, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[38.3, 55.2, -136.2, 20.7, 105.2, 34.0],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(450, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_gripper_position(500, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[49.4, 12.7, -57.4, -39.8, 32.5, 83.4],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[69.7, 15.6, -44.0, -108.7, 81.3, 155.4],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[49.5, 0.6, -40.0, -124.2, 66.4, 150.5],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[52.6, 38.6, -48.8, -127.3, 84.8, 174.1],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(800, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[48.3, -7.8, -42.1, -120.8, 60.1, 141.1],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return

                    code = self._arm.set_servo_angle(angle=[0.0, -30.0, -30.0, 0.0, 60.0, 2.0], speed=self._angle_speed,
                                                     mvacc=self._angle_acc, wait=True, radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(800, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[2.9, -48.2, -3.3, 195.9, 20.5, -188.3],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(350, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[24.4, -4.1, -3.8, 208.8, 64.2, -185.2],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(131, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[22.2, -2.4, -2.9, 204.2, 67.7, -92.8],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(320, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[23.0, -22.4, 1.0, 215.8, 44.6, -109.6],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[0.0, -30.0, -30.0, 0.0, 60.0, 2.0], speed=self._angle_speed,
                                                     mvacc=self._angle_acc, wait=True, radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(250, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[17.3, -19.2, -30.0, 104.6, 75.8, -41.9],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[28.3, 34.0, -46.5, 120.8, 85.0, -78.3],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(350, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[33.2, 35.3, -51.1, 125.3, 82.2, -76.2],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(198, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[36.1, -0.4, -45.6, 120.3, 64.2, -50.6],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[-41.0, -13.1, -33.2, 63.5, 118.7, -48.7],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[-41.0, -13.1, -33.2, 63.5, 118.7, -37.3],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[-41.0, -13.1, -33.2, 63.5, 118.7, -67.7],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[-41.0, -13.1, -33.2, 63.5, 118.7, -48.7],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[-37.4, 15.5, -35.6, 58.3, 101.9, -72.4],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[-37.5, 17.6, -35.7, 57.8, 100.9, -72.3],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[-37.5, 17.6, -35.7, 57.8, 100.9, -59.7],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(250, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[-37.5, 17.3, -35.6, 57.8, 101.0, -65.4],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[-52.2, 5.6, -18.4, 41.2, 99.7, -84.2],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[0.0, -32.9, -37.9, 0.0, 70.8, 2.0], speed=self._angle_speed,
                                                     mvacc=self._angle_acc, wait=True, radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_pause_time(30)
                    if not self._check_code(code, 'set_pause_time'):
                        return
                    code = self._arm.set_servo_angle(angle=[60.9, -33.3, -10.8, 11.6, 49.6, -31.2],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(124, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[63.0, -27.1, -8.3, 13.8, 40.9, -36.0],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(49, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[60.6, -46.4, -23.0, 9.1, 74.6, -30.3],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[0.7, 21.6, -97.0, 9.1, 74.5, -92.9],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[6.1, -3.4, -44.5, 16.7, -0.9, -105.5],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[13.2, 15.1, -29.1, 16.7, -72.6, -105.5],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[6.1, -3.4, -44.5, 16.7, -0.9, -105.5],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[0.7, 21.6, -97.0, 9.1, 74.5, -92.9],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[60.6, -46.4, -23.0, 9.1, 74.6, -30.3],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[63.0, -27.1, -8.3, 13.8, 40.9, -36.0],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(124, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[58.9, -46.4, -33.0, 8.7, 84.7, -26.4],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[0.0, -30.0, -30.0, 0.0, 60.0, 2.0], speed=self._angle_speed,
                                                     mvacc=self._angle_acc, wait=True, radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_pause_time(270)
                    if not self._check_code(code, 'set_pause_time'):
                        return
                    code = self._arm.set_servo_angle(angle=[68.0, 10.8, -77.3, 0.0, 66.5, 70.0],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(225, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[76.4, 30.4, -75.0, 0.0, 44.6, 81.4],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(100, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[76.4, 20.3, -80.1, 0.0, 59.8, 81.4],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[-29.2, -30.8, -43.4, 80.9, 113.2, -16.2],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[30.2, 42.6, -131.0, -86.1, 121.2, -75.2],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[30.2, 61.8, -129.4, -78.6, 119.6, -64.9],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[30.2, 63.3, -129.6, -77.8, 119.3, -88.0],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[29.5, 73.4, -142.5, -79.7, 119.2, -109.9],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[29.4, 70.4, -137.9, -79.8, 117.0, -117.5],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[30.5, 61.1, -122.3, -76.1, 116.7, -110.4],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[30.5, 61.5, -122.4, -76.0, 116.6, -110.1],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[30.0, 60.8, -135.1, -82.5, 120.5, -80.5],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[29.6, 65.1, -142.9, -84.7, 120.6, -81.7],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[29.6, 64.8, -150.2, -89.3, 120.0, -90.5],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[68.0, 10.8, -77.3, 0.0, 66.5, 70.0],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[76.6, 21.4, -74.8, 6.0, 52.9, 76.7],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[76.8, 26.2, -72.5, 6.6, 45.9, 75.8],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(250, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[73.9, 28.5, -76.3, 6.5, 47.5, 73.2],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(500, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[87.6, 27.8, -81.7, 6.2, 72.6, 89.5],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[87.7, 36.9, -92.2, 6.2, 73.9, 89.7],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[83.3, 37.7, -93.6, 4.7, 75.0, 86.1],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[87.7, 36.9, -92.2, 6.2, 73.9, 89.7],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[68.0, 10.8, -77.3, 0.0, 66.5, 70.0],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[0.0, -30.0, -30.0, 0.0, 60.0, 2.0], speed=self._angle_speed,
                                                     mvacc=self._angle_acc, wait=True, radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(300, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[-52.2, 5.6, -18.4, 41.2, 99.7, -84.2],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[-37.3, 17.8, -36.0, 58.0, 100.9, -72.2],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(198, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[-40.7, -10.2, -33.2, 60.4, 114.9, -52.0],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[-41.7, -16.4, -35.3, 63.3, 119.4, -19.4],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[-40.7, -10.2, -33.2, 60.4, 114.9, -52.0],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[39.0, -44.8, -9.7, 119.7, 59.0, -43.9],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[86.8, -27.0, -24.6, 179.4, 41.0, -88.5],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[117.2, -65.7, -1.1, 232.5, 39.1, -135.9],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[145.1, -9.6, -36.6, 244.5, 69.5, -129.8],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[131.0, -36.1, -21.6, 238.3, 54.3, -81.7],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[109.1, -50.1, -20.7, 226.8, 30.8, -61.5],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[121.8, -46.0, -29.7, 246.2, 38.3, -80.5],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[145.1, -9.6, -36.6, 244.5, 69.5, -129.8],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[112.1, -38.1, -15.8, 216.1, 45.3, -117.5],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[79.3, -41.4, -15.2, 166.6, 36.9, -77.9],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[50.3, -26.1, -23.1, 132.9, 55.1, -55.4],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[33.0, -11.0, -38.3, 116.3, 64.6, -46.2],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[36.1, -0.4, -45.6, 120.3, 64.2, -50.6],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[33.2, 35.3, -51.1, 125.3, 82.2, -76.2],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(250, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[45.3, 29.3, -26.3, 138.1, 95.0, -91.2],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[0.0, -30.0, -30.0, 0.0, 60.0, 2.0], speed=self._angle_speed,
                                                     mvacc=self._angle_acc, wait=True, radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[2.9, -48.2, -3.3, 195.9, 20.5, -188.3],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(350, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[24.4, -4.1, -3.8, 208.8, 64.2, -185.2],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(131, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[24.8, -3.4, -3.8, 209.1, 64.9, -272.3],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_gripper_position(350, wait=True, speed=5000, auto_enable=True)
                    if not self._check_code(code, 'set_gripper_position'):
                        return
                    code = self._arm.set_servo_angle(angle=[23.0, -22.4, 1.0, 215.8, 44.6, -185.5],
                                                     speed=self._angle_speed, mvacc=self._angle_acc, wait=True,
                                                     radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                    code = self._arm.set_servo_angle(angle=[0.0, -30.0, -30.0, 0.0, 60.0, 2.0], speed=self._angle_speed,
                                                     mvacc=self._angle_acc, wait=True, radius=60.0)
                    if not self._check_code(code, 'set_servo_angle'):
                        return
                pass

        except Exception as e:
            print('MainException: {}'.format(e))
        self.alive = False

    @property
    def is_alive(self):
        return self.alive

    def quit(self):
        self.alive = False

    def _check_code(self, code, label):
        if not self.is_alive or code != 0:
            self.alive = False
        return self.is_alive

    def select_ingredients(self):
        ingredient_window = tk.Toplevel(root)
        ingredient_window.title("Select Ingredients for Omelette")
        ingredient_window.geometry("300x200")
        ingredient_window.resizable(False,False)

        ingredients = ['Green Capsicum', 'Yellow Capsicum', 'Onion']
        vars = []
        for i, ingredient in enumerate(ingredients):
            var = tk.BooleanVar()
            ttk.Checkbutton(ingredient_window, text=ingredient, variable=var).pack(pady=5)
            vars.append(var)

        selected_ingredients = []

        def confirm_selection():
            nonlocal selected_ingredients
            selected_ingredients = [ingredients[i].lower() for i, var in enumerate(vars) if var.get()]
            ingredient_window.quit()
            ingredient_window.destroy()

        ttk.Button(ingredient_window, text="Confirm", command=confirm_selection).pack(pady=10)

        ingredient_window.mainloop()
        return selected_ingredients
    def start_omelette_with_ingredients(ingredients):
        try:
            robot_main = RobotMain(arm)
            robot_main.run_omelette_with_ingredients(ingredients)
            robot_main.quit()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def launch_machine_vision(self):
        print("Launching Machine Vision AI...")

        yolo_script_path = r"D:\STEAM游戏软件路径\pythonProject\Test yolo.py"

        try:
            # 启动 YOLO 检测脚本作为一个子进程
            process = subprocess.Popen([sys.executable, yolo_script_path],
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       universal_newlines=True)

            start_time = time.time()
            result = "unknown"

            # 等待 10 秒或直到进程结束
            while time.time() - start_time < 20 and process.poll() is None:
                output = process.stdout.readline()
                if output:
                    print(output.strip())
                    if "normal" in output.lower():
                        result = "normal"
                    elif "burnt" in output.lower():
                        result = "burnt"

            print(f"YOLO detection finished. Result: {result}")

            # 直接执行相应的机械臂动作
            self.execute_arm_movement(result)

        except subprocess.TimeoutExpired:
            print("YOLO detection timed out")
            self.execute_arm_movement("unknown")
        except Exception as e:
            print(f"Error running YOLO detection: {e}")
            self.execute_arm_movement("unknown")

    def execute_arm_movement(self, detection_result):
        if detection_result == "normal":
            print("Executing normal egg movement")
            # 正常煎蛋的运动路径
            self._angle_speed = 20
            self._angle_acc = 500
            for i in range(int(1)):
                if not self.is_alive:
                    break
                code = self._arm.set_servo_angle(angle=[0.0, -30.0, -30.0, 0.0, 60.0, 2.0], speed=self._angle_speed,
                                                 mvacc=self._angle_acc, wait=True, radius=60.0)
                if not self._check_code(code, 'set_servo_angle'):
                    return
                code = self._arm.set_gripper_position(100, wait=True, speed=5000, auto_enable=True)
                if not self._check_code(code, 'set_gripper_position'):
                    return
                code = self._arm.set_servo_angle(angle=[4.1, -30.0, -28.0, 95.6, 84.5, -26.5], speed=self._angle_speed,
                                                 mvacc=self._angle_acc, wait=True, radius=60.0)
                if not self._check_code(code, 'set_servo_angle'):
                    return
                code = self._arm.set_servo_angle(angle=[19.8, 34.3, -38.3, 70.0, 88.5, -90.1], speed=self._angle_speed,
                                                 mvacc=self._angle_acc, wait=True, radius=60.0)
                if not self._check_code(code, 'set_servo_angle'):
                    return
                code = self._arm.set_servo_angle(angle=[24.7, 25.7, -26.3, 82.0, 81.0, -87.6], speed=self._angle_speed,
                                                 mvacc=self._angle_acc, wait=True, radius=60.0)
                if not self._check_code(code, 'set_servo_angle'):
                    return
                code = self._arm.set_servo_angle(angle=[26.9, 26.3, -25.2, 87.1, 81.3, -88.9], speed=self._angle_speed,
                                                 mvacc=self._angle_acc, wait=True, radius=60.0)
                if not self._check_code(code, 'set_servo_angle'):
                    return
                code = self._arm.set_gripper_position(12, wait=True, speed=5000, auto_enable=True)
                if not self._check_code(code, 'set_gripper_position'):
                    return
                code = self._arm.set_servo_angle(angle=[23.1, 17.7, -21.7, 83.7, 92.7, -83.8], speed=self._angle_speed,
                                                 mvacc=self._angle_acc, wait=True, radius=60.0)
                if not self._check_code(code, 'set_servo_angle'):
                    return
                code = self._arm.set_servo_angle(angle=[24.6, -22.2, -13.1, 87.8, 95.4, -52.5], speed=self._angle_speed,
                                                 mvacc=self._angle_acc, wait=True, radius=60.0)
                if not self._check_code(code, 'set_servo_angle'):
                    return
                code = self._arm.set_servo_angle(angle=[33.7, -33.4, -5.6, 116.3, 73.9, -55.4], speed=self._angle_speed,
                                                 mvacc=self._angle_acc, wait=True, radius=60.0)
                if not self._check_code(code, 'set_servo_angle'):
                    return
                code = self._arm.set_servo_angle(angle=[43.9, -37.8, -4.8, 148.0, 55.3, -68.8], speed=self._angle_speed,
                                                 mvacc=self._angle_acc, wait=True, radius=60.0)
                if not self._check_code(code, 'set_servo_angle'):
                    return
                code = self._arm.set_servo_angle(angle=[48.2, -38.1, -5.4, 181.8, 50.0, -89.0], speed=self._angle_speed,
                                                 mvacc=self._angle_acc, wait=True, radius=60.0)
                if not self._check_code(code, 'set_servo_angle'):
                    return
                code = self._arm.set_servo_angle(angle=[18.7, 18.3, -67.0, 142.7, 51.1, -60.7], speed=self._angle_speed,
                                                 mvacc=self._angle_acc, wait=True, radius=60.0)
                if not self._check_code(code, 'set_servo_angle'):
                    return
                code = self._arm.set_servo_angle(angle=[-4.6, 13.8, -59.0, 121.8, 66.6, -50.6], speed=self._angle_speed,
                                                 mvacc=self._angle_acc, wait=True, radius=60.0)
                if not self._check_code(code, 'set_servo_angle'):
                    return
                code = self._arm.set_servo_angle(angle=[-40.6, 63.5, -130.1, 95.3, 89.5, -21.2],
                                                 speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
                if not self._check_code(code, 'set_servo_angle'):
                    return
                code = self._arm.set_servo_angle(angle=[-38.5, 56.0, -118.5, 101.8, 74.0, -27.4],
                                                 speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
                if not self._check_code(code, 'set_servo_angle'):
                    return
                code = self._arm.set_servo_angle(angle=[-37.6, 71.0, -130.3, 103.1, 73.9, -30.8],
                                                 speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
                if not self._check_code(code, 'set_servo_angle'):
                    return
                code = self._arm.set_gripper_position(100, wait=True, speed=5000, auto_enable=True)
                if not self._check_code(code, 'set_gripper_position'):
                    return
                code = self._arm.set_servo_angle(angle=[-45.9, 49.4, -92.8, 100.7, 83.7, -45.3],
                                                 speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
                if not self._check_code(code, 'set_servo_angle'):
                    return
                code = self._arm.set_servo_angle(angle=[-45.5, 31.7, -91.2, 98.8, 80.7, -29.3], speed=self._angle_speed,
                                                 mvacc=self._angle_acc, wait=True, radius=60.0)
                if not self._check_code(code, 'set_servo_angle'):
                    return
                code = self._arm.set_servo_angle(angle=[0.0, -30.0, -30.0, 0.0, 60.0, 2.0], speed=self._angle_speed,
                                                 mvacc=self._angle_acc, wait=True, radius=60.0)
                if not self._check_code(code, 'set_servo_angle'):
                    return
            pass
        elif detection_result == "burnt":
            print("Executing burnt egg movement")
            # 焦煎蛋的运动路径
            self._angle_speed = 20
            self._angle_acc = 500
            for i in range(int(1)):
                if not self.is_alive:
                    break
                code = self._arm.set_servo_angle(angle=[0.0, -30.0, -30.0, 0.0, 60.0, 2.0], speed=self._angle_speed,
                                                 mvacc=self._angle_acc, wait=True, radius=60.0)
                if not self._check_code(code, 'set_servo_angle'):
                    return
                code = self._arm.set_gripper_position(100, wait=True, speed=5000, auto_enable=True)
                if not self._check_code(code, 'set_gripper_position'):
                    return
                code = self._arm.set_servo_angle(angle=[4.1, -30.0, -28.0, 95.6, 84.5, -26.5], speed=self._angle_speed,
                                                 mvacc=self._angle_acc, wait=True, radius=60.0)
                if not self._check_code(code, 'set_servo_angle'):
                    return
                code = self._arm.set_servo_angle(angle=[19.8, 34.3, -38.3, 70.0, 88.5, -90.1], speed=self._angle_speed,
                                                 mvacc=self._angle_acc, wait=True, radius=60.0)
                if not self._check_code(code, 'set_servo_angle'):
                    return
                code = self._arm.set_servo_angle(angle=[24.7, 25.7, -26.3, 82.0, 81.0, -87.6], speed=self._angle_speed,
                                                 mvacc=self._angle_acc, wait=True, radius=60.0)
                if not self._check_code(code, 'set_servo_angle'):
                    return
                code = self._arm.set_servo_angle(angle=[26.9, 26.3, -25.2, 87.1, 81.3, -88.9], speed=self._angle_speed,
                                                 mvacc=self._angle_acc, wait=True, radius=60.0)
                if not self._check_code(code, 'set_servo_angle'):
                    return
                code = self._arm.set_gripper_position(12, wait=True, speed=5000, auto_enable=True)
                if not self._check_code(code, 'set_gripper_position'):
                    return
                code = self._arm.set_servo_angle(angle=[24.6, -22.2, -13.1, 87.8, 95.4, -52.5], speed=self._angle_speed,
                                                 mvacc=self._angle_acc, wait=True, radius=60.0)
                if not self._check_code(code, 'set_servo_angle'):
                    return
                code = self._arm.set_servo_angle(angle=[54.6, -6.0, -28.9, 112.6, 78.3, -56.0], speed=self._angle_speed,
                                                 mvacc=self._angle_acc, wait=True, radius=60.0)
                if not self._check_code(code, 'set_servo_angle'):
                    return
                code = self._arm.set_servo_angle(angle=[107.7, -13.0, -24.5, 165.5, 54.8, -79.1],
                                                 speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
                if not self._check_code(code, 'set_servo_angle'):
                    return
                code = self._arm.set_servo_angle(angle=[110.2, 31.8, -59.0, 217.8, 35.1, -187.3],
                                                 speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
                if not self._check_code(code, 'set_servo_angle'):
                    return
                code = self._arm.set_servo_angle(angle=[107.7, -13.0, -24.5, 165.5, 54.8, -79.1],
                                                 speed=self._angle_speed, mvacc=self._angle_acc, wait=True, radius=60.0)
                if not self._check_code(code, 'set_servo_angle'):
                    return
                code = self._arm.set_servo_angle(angle=[54.6, -6.0, -28.9, 112.6, 78.3, -56.0], speed=self._angle_speed,
                                                 mvacc=self._angle_acc, wait=True, radius=60.0)
                if not self._check_code(code, 'set_servo_angle'):
                    return
                code = self._arm.set_servo_angle(angle=[24.6, -22.2, -13.1, 87.8, 95.4, -52.5], speed=self._angle_speed,
                                                 mvacc=self._angle_acc, wait=True, radius=60.0)
                if not self._check_code(code, 'set_servo_angle'):
                    return
                code = self._arm.set_servo_angle(angle=[26.9, 26.3, -25.2, 87.1, 81.3, -88.9], speed=self._angle_speed,
                                                 mvacc=self._angle_acc, wait=True, radius=60.0)
                if not self._check_code(code, 'set_servo_angle'):
                    return
                code = self._arm.set_gripper_position(100, wait=True, speed=5000, auto_enable=True)
                if not self._check_code(code, 'set_gripper_position'):
                    return
                code = self._arm.set_servo_angle(angle=[24.7, 25.2, -26.1, 81.9, 81.0, -87.3], speed=self._angle_speed,
                                                 mvacc=self._angle_acc, wait=True, radius=60.0)
                if not self._check_code(code, 'set_servo_angle'):
                    return
                code = self._arm.set_servo_angle(angle=[19.8, 34.3, -38.3, 70.0, 88.5, -90.1], speed=self._angle_speed,
                                                 mvacc=self._angle_acc, wait=True, radius=60.0)
                if not self._check_code(code, 'set_servo_angle'):
                    return
                code = self._arm.set_servo_angle(angle=[4.1, -30.0, -28.0, 95.6, 84.5, -26.5], speed=self._angle_speed,
                                                 mvacc=self._angle_acc, wait=True, radius=60.0)
                if not self._check_code(code, 'set_servo_angle'):
                    return
                code = self._arm.set_servo_angle(angle=[0.0, -30.0, -30.0, 0.0, 60.0, 2.0], speed=self._angle_speed,
                                                 mvacc=self._angle_acc, wait=True, radius=60.0)
                if not self._check_code(code, 'set_servo_angle'):
                    return
                # TODO: 在这里添加焦煎蛋的具体运动代码
            pass
        else:
            print("No valid result, not moving the arm")
            # 焦煎蛋的运动路径
            self._angle_speed = 40
            self._angle_acc = 800
            for i in range(int(1)):
                if not self.is_alive:
                    break
                code = self._arm.set_servo_angle(angle=[0.0, -30.0, -30.0, 0.0, 60.0, 2.0],
                                                 speed=self._angle_speed,
                                                 mvacc=self._angle_acc, wait=True, radius=60.0)
                if not self._check_code(code, 'set_servo_angle'):
                    return

    def quit(self):
        self.alive = False
        # 其他清理代码

def sunny_side():
    try:
        robot_main = RobotMain(arm)
        robot_main.run('sunny_side')
        robot_main.launch_machine_vision()
        robot_main.quit()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def omelette():
    try:
        robot_main = RobotMain(arm)
        selected_ingredients = robot_main.select_ingredients()
        robot_main.run_omelette_with_ingredients(selected_ingredients)
        robot_main.launch_machine_vision()
        robot_main.quit()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
# Create UArm instance
try:
    arm = XArmAPI('192.168.1.201', baud_checkset=False)
except Exception as e:
    messagebox.showerror("Error", f"Failed to connect to the arm: {str(e)}")
    sys.exit(1)

def start_machine_vision():
    robot_main = RobotMain(arm)
    robot_main.launch_machine_vision()

# Create main window
root = tk.Tk()
root.title("Egg Preparation")
root.geometry("400x300")
root.configure(bg="#F0F0F0")

# Create title label
title_font = font.Font(family="Helvetica", size=24, weight="bold")
title_label = tk.Label(root, text="Select Egg Style", font=title_font, bg="#F0F0F0")
title_label.pack(pady=20)

# Load and display images
image_size = (150, 150)
padding = 10

try:
    sunny_side_image = Image.open("E:\\Year4sem2\\FYP\\egg picture\\sunny side egg.png")
    sunny_side_image = sunny_side_image.resize(image_size, Image.LANCZOS)
    sunny_side_photo = ImageTk.PhotoImage(sunny_side_image)

    omelette_image = Image.open("E:\\Year4sem2\\FYP\\egg picture\\omelette.png")
    omelette_image = omelette_image.resize(image_size, Image.LANCZOS)
    omelette_photo = ImageTk.PhotoImage(omelette_image)
except Exception as e:
    messagebox.showerror("Error", f"Failed to load images: {str(e)}")
    sys.exit(1)

# Create buttons and bind click events
button_font = font.Font(family="Helvetica", size=14)

button_frame = tk.Frame(root, bg="#F0F0F0")
button_frame.pack(expand=True, fill='both')

button1 = tk.Button(button_frame, image=sunny_side_photo, compound=tk.TOP, text="Sunny Side", command=sunny_side,
                    font=button_font, bg="#FFD166", fg="#000000", padx=padding, pady=padding)
button1.pack(side=tk.LEFT, expand=True, fill='both')

button2 = tk.Button(button_frame, image=omelette_photo, compound=tk.TOP, text="Omelette", command=omelette,
                    font=button_font, bg="#EF476F", fg="#FFFFFF", padx=padding, pady=padding)
button2.pack(side=tk.RIGHT, expand=True, fill='both')

# Run main loop
root.mainloop()