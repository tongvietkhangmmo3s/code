from copy import copy
import random
from random import randint
from shutil import copy2
from time import sleep
import os, sys
import threading
import numpy as np
import sys
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
import json
from tkinter import *
from tkinter import  messagebox
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton
import sys
import re
import concurrent.futures
sys.stdout.reconfigure(encoding='utf-8')


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(814, 367)
                MainWindow.setEnabled(True)
                MainWindow.setFixedSize(814, 367)
                MainWindow.resize(814, 367)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("C:/Users/Admin/Pictures/ảnh làm qt/logontp.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                MainWindow.setWindowIcon(icon)
                MainWindow.setStyleSheet("background-color:rgb(238, 254, 255);")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
                self.groupBox.setGeometry(QtCore.QRect(20, 15, 321, 241))
                self.groupBox.setStyleSheet("QGroupBox {\n""                                border-radius: 10px;\n""                                border: 2px solid rgb(41, 128, 185);\n""                                font-weight: bold;\n""background-color:rgb(239, 249, 255);\n""                            }\n""                            QGroupBox::title {\n""                                subcontrol-origin: margin;\n""                                position: relative;\n""                               \n""                                color: rgb(41, 128, 185);\n""                                font-size: 20px;\n""                            }\n""                            QGroupBox::indicator {\n""                                width: 10px;\n""                                height: 10px;\n""                            }\n""                            QGroupBox::indicator:checked {\n""                                background-color: rgb(41, 128, 185);\n""                                border: 2px solid white;\n""                            }\n""                            QGroupBox::indicator:unchecked {\n""                                background-color: white;\n""                                border: 2px solid rgb(41, 128, 185);\n""                            }")
                self.groupBox.setObjectName("groupBox")
                self.listWidget = QtWidgets.QListWidget(self.groupBox)
                self.listWidget.setGeometry(QtCore.QRect(10, 21, 301, 211))
                self.listWidget.setStyleSheet("background-color:rgb(0, 0, 0) ;\n""border-radius: 10px;\n""border: 2px solid rgb(41, 128, 185);\n""color:rgb(0, 230, 0)")
                self.listWidget.setObjectName("listWidget")
                self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
                self.groupBox_2.setGeometry(QtCore.QRect(351, 14, 441, 241))
                self.groupBox_2.setStyleSheet("QGroupBox {\n""                                border-radius: 10px;\n""                                border: 2px solid rgb(41, 128, 185);\n""                                font-weight: bold;\n""background-color:rgb(239, 249, 255);\n""                            }\n""                            QGroupBox::title {\n""                                subcontrol-origin: margin;\n""                                position: relative;\n""                               \n""                                color: rgb(41, 128, 185);\n""                                font-size: 20px;\n""                            }\n""                            QGroupBox::indicator {\n""                                width: 10px;\n""                                height: 10px;\n""                            }\n""                            QGroupBox::indicator:checked {\n""                                background-color: rgb(41, 128, 185);\n""                                border: 2px solid white;\n""                            }\n""                            QGroupBox::indicator:unchecked {\n""                                background-color: white;\n""                                border: 2px solid rgb(41, 128, 185);\n""                            }")
                self.groupBox_2.setObjectName("groupBox_2")
                self.plainTextEdit_mail = QtWidgets.QPlainTextEdit(self.groupBox_2)
                self.plainTextEdit_mail.setGeometry(QtCore.QRect(230, 50, 193, 86))
                self.plainTextEdit_mail.setStyleSheet("QPlainTextEdit {\n""                background-color: rgb(239, 249, 255);\n""                color: black;\n""                font-size: 12pt;\n""                font-family: \'Arial\';\n""                border: 2px solid rgb(131, 131, 131);\n""                border-radius: 10px;\n""                padding: 5px;\n""            }\n""            QPlainTextEdit:hover {\n""                border: 2px solid rgb(131, 131, 131);\n""            }\n""            QPlainTextEdit:focus {\n""                border: 2px solid rgb(131, 131, 131);\n""                outline: none;\n""            }")
                self.plainTextEdit_mail.setObjectName("plainTextEdit_mail")
                self.label = QtWidgets.QLabel(self.groupBox_2)
                self.label.setGeometry(QtCore.QRect(288, 36, 61, 16))
                self.label.setStyleSheet("border-left: 2px solid rgb(131, 131, 131);\n""border-right: 2px solid  rgb(131, 131, 131);\n""border-top: 2px solid  rgb(131, 131, 131);\n""border-radius: 5px;")
                self.label.setObjectName("label")
                self.plainTextEdit_proxy = QtWidgets.QPlainTextEdit(self.groupBox_2)
                self.plainTextEdit_proxy.setGeometry(QtCore.QRect(24, 50, 193, 86))
                self.plainTextEdit_proxy.setStyleSheet("QPlainTextEdit {\n""                background-color: rgb(239, 249, 255);\n""                color: black;\n""                font-size: 12pt;\n""                font-family: \'Arial\';\n""                border: 2px solid rgb(131, 131, 131);\n""                border-radius: 10px;\n""                padding: 5px;\n""            }\n""            QPlainTextEdit:hover {\n""                border: 2px solid rgb(131, 131, 131);\n""            }\n""            QPlainTextEdit:focus {\n""                border: 2px solid rgb(131, 131, 131);\n""                outline: none;\n""            }")
                self.plainTextEdit_proxy.setObjectName("plainTextEdit_proxy")
                self.label_2 = QtWidgets.QLabel(self.groupBox_2)
                self.label_2.setGeometry(QtCore.QRect(79, 36, 71, 16))
                self.label_2.setStyleSheet("border-left: 2px solid rgb(131, 131, 131);\n""border-right: 2px solid  rgb(131, 131, 131);\n""border-top: 2px solid  rgb(131, 131, 131);\n""border-radius: 5px;")
                self.label_2.setObjectName("label_2")
                self.line = QtWidgets.QFrame(self.groupBox_2)
                self.line.setGeometry(QtCore.QRect(74, 140, 300, 3))
                self.line.setFrameShape(QtWidgets.QFrame.HLine)
                self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.line.setObjectName("line")
                self.label_3 = QtWidgets.QLabel(self.groupBox_2)
                self.label_3.setGeometry(QtCore.QRect(30, 180, 61, 16))
                self.label_3.setObjectName("label_3")
                self.soluong = QtWidgets.QSpinBox(self.groupBox_2)
                self.soluong.setGeometry(QtCore.QRect(88, 177, 42, 22))
                self.soluong.setStyleSheet(" QSpinBox{\n""        background-color: #e5f7e5; \n""        border: 1px solid #3c7e44; \n""        border-radius: 3px;\n""    }\n""    QSpinBox::up-button{\n""        background-color: #3c7e44;\n""        width: 20px;\n""    }\n""    QSpinBox::up-arrow{\n""        image: url(icons/up_arrow_light.png);\n""        width: 13px;\n""    }")
                self.soluong.setMinimum(2)
                self.soluong.setMaximum(20)
                self.soluong.setObjectName("soluong")
                self.line_2 = QtWidgets.QFrame(self.groupBox_2)
                self.line_2.setGeometry(QtCore.QRect(224, 141, 3, 68))
                self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
                self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.line_2.setObjectName("line_2")
                self.bat_dau_chay = QtWidgets.QPushButton(self.groupBox_2)
                self.bat_dau_chay.setGeometry(QtCore.QRect(264, 162, 91, 41))
                self.bat_dau_chay.setStyleSheet("QPushButton { color: #fff;\n""background-color: rgb(75, 223, 21);\n""border: none; \n""font-size:14px;\n""border-radius: 10px;\n""padding: 5px;\n""font-style:bold;\n""}\n""\n""QPushButton:hover {\n""color: #fff;\n""background-color: rgb(66, 125, 2);\n""}\n""QPushButton:pressed {background-color: #266c6e; }")
                self.bat_dau_chay.setObjectName("bat_dau_chay")
                self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
                self.groupBox_3.setGeometry(QtCore.QRect(20, 268, 771, 61))
                self.groupBox_3.setStyleSheet("QGroupBox {\n""                                border-radius: 10px;\n""                                border: 2px solid rgb(41, 128, 185);\n""                                font-weight: bold;\n""                                background-color:rgb(239, 249, 255);\n""                            }\n""                            QGroupBox::title {\n""                                subcontrol-origin: margin;\n""                                position: relative;\n""                               \n""                                color: rgb(41, 128, 185);\n""                                font-size: 20px;\n""                            }\n""                            QGroupBox::indicator {\n""                                width: 10px;\n""                                height: 10px;\n""                            }\n""                            QGroupBox::indicator:checked {\n""                                background-color: rgb(41, 128, 185);\n""                                border: 2px solid white;\n""                            }\n""                            QGroupBox::indicator:unchecked {\n""                                background-color: white;\n""                                border: 2px solid rgb(41, 128, 185);\n""                            }\n""")
                self.groupBox_3.setObjectName("groupBox_3")
                self.gridLayout = QtWidgets.QGridLayout(self.groupBox_3)
                self.gridLayout.setObjectName("gridLayout")
                self.sl_mail_da_check = QtWidgets.QLabel(self.groupBox_3)
                self.sl_mail_da_check.setObjectName("sl_mail_da_check")
                self.gridLayout.addWidget(self.sl_mail_da_check, 0, 0, 1, 1)
                self.mail_code_8 = QtWidgets.QLabel(self.groupBox_3)
                self.mail_code_8.setObjectName("mail_code_8")
                self.gridLayout.addWidget(self.mail_code_8, 1, 2, 1, 1)
                self.sl_mail_da_check_loi = QtWidgets.QLabel(self.groupBox_3)
                self.sl_mail_da_check_loi.setObjectName("sl_mail_da_check_loi")
                self.gridLayout.addWidget(self.sl_mail_da_check_loi, 1, 0, 1, 1)
                self.mail_lien_ket = QtWidgets.QLabel(self.groupBox_3)
                self.mail_lien_ket.setObjectName("mail_lien_ket")
                self.gridLayout.addWidget(self.mail_lien_ket, 0, 1, 1, 1)
                self.mail_code_6 = QtWidgets.QLabel(self.groupBox_3)
                self.mail_code_6.setObjectName("mail_code_6")
                self.gridLayout.addWidget(self.mail_code_6, 0, 2, 1, 1)
                self.mail_khong_lien_ket = QtWidgets.QLabel(self.groupBox_3)
                self.mail_khong_lien_ket.setObjectName("mail_khong_lien_ket")
                self.gridLayout.addWidget(self.mail_khong_lien_ket, 1, 1, 1, 1)
                self.label_6 = QtWidgets.QLabel(self.centralwidget)
                self.label_6.setGeometry(QtCore.QRect(700, 329, 90, 20))
                self.label_6.setObjectName("label_6")
                self.label_7 = QtWidgets.QLabel(self.centralwidget)
                self.label_7.setGeometry(QtCore.QRect(30, 330, 231, 20))
                self.label_7.setObjectName("label_7")
                MainWindow.setCentralWidget(self.centralwidget)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)
                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "Facebook link checker and code 6 8 | Tiến Phước"))
                self.groupBox.setTitle(_translate("MainWindow", "Result View"))
                self.groupBox_2.setTitle(_translate("MainWindow", "Settings"))
                self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Add Mail</span></p></body></html>"))
                self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Add Proxy</span></p></body></html>"))
                self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Số Luồng</span></p></body></html>"))
                self.bat_dau_chay.setText(_translate("MainWindow", "Bắt Đầu"))
                self.groupBox_3.setTitle(_translate("MainWindow", "View Data"))
                self.sl_mail_da_check.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Số Lượng Đã Mail Đã Check:____</span></p></body></html>"))
                self.mail_code_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Code 8:____</span></p></body></html>"))
                self.sl_mail_da_check_loi.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Số Lượng Đã Mail Đã Check Lỗi:____</span></p></body></html>"))
                self.mail_lien_ket.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Mail Liên Kết:____</span></p></body></html>"))
                self.mail_code_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Code 6:____</span></p></body></html>"))
                self.mail_khong_lien_ket.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Mail Không Liên Kết:____</span></p></body></html>"))
                self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; font-style:italic; text-decoration: underline;\">version 1.0.2</span></p></body></html>"))
                self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; font-style:italic; text-decoration: underline;\">Telegram: https://t.me/regslldomain</span></p></body></html>"))
                # self.plainTextEdit_proxy.setPlainText('dcm')
                # print(self.plainTextEdit_proxy.toPlainText())
                self.bat_dau_chay.clicked.connect(self.check)
        def check(self):
                self.oo =Check(self)
                self.oo.start()

class Check(QtCore.QThread):
        ee = QtCore.pyqtSignal(bool)
        def __init__(self,all):
                super().__init__()
                self.all  = all
                self.count = 0
                self.count_lienket = 0
                self.count_nolienket = 0
                self.count_loi = 0
                self.count_6 = 0
                self.count_8 = 0
                self.session = requests.Session()
                self.session.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"})
                # self.list_proxy = self.all.plainTextEdit_proxy.toPlainText().split("\n")
                self.proxy = {
                        'http': f'http://hndc9.proxyxoay.net:33106',
                        'https': f'http://hndc9.proxyxoay.net:33106'
                }
                # print(self.list_proxy)
        def run(self): # bố cục truyền dữ liệu vào check mail
                self.list_mail = self.all.plainTextEdit_mail.toPlainText().split("\n")
                with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
                        futures = []
                        for stt_mail, mail  in enumerate(self.list_mail):
                                futures.append(executor.submit(self.check_mail, stt_mail, mail))
                        concurrent.futures.wait(futures)
        def  check_mail(self,stt_mail, mail ): #bố cục xử lý code tool
                self.count += 1
                try:
                        if self.count % 10 == 0:
                                self.all.listWidget.clear()
                        if self.count % 100 == 0:
                                a = requests.get('https://proxyxoay.net/api/rotating-proxy/change-key-ip/25f9c8ca-37c8-46f9-a96c-4fd5adda047a',timeout=30).text
                                b = json.loads(a)
                                self.all.listWidget.addItem(f"=> Đang Đổi IP {b['message']} ")
                                
                                # print(a.text)
                                sleep(20)
                        # self.list_proxy = self.all.plainTextEdit_proxy.toPlainText().split("\n")
                        self.all.sl_mail_da_check.setText(f"<html><head/><body><p><span style=\" font-weight:600;\">Số Lượng Đã Mail Đã Check: {self.count}</span></p></body></html>")
                        headers = {
                                'authority': 'm.facebook.com',
                                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                                'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                                'cache-control': 'no-cache',
                                # 'cookie': 'datr=sDAdZOjFrj58kCZJJg2CkZIP; m_pixel_ratio=1; wd=457x969; fr=0XdKexMeN6BbjgiGE..BkHTDV.gl.AAA.0.0.BkHTDc.AWUf8o2Rm7w',
                                'pragma': 'no-cache',
                                'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
                                'sec-ch-ua-mobile': '?0',
                                'sec-ch-ua-platform': '"Windows"',
                                'sec-fetch-dest': 'document',
                                'sec-fetch-mode': 'navigate',
                                'sec-fetch-site': 'none',
                                'sec-fetch-user': '?1',
                                'upgrade-insecure-requests': '1',
                                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                        }

                        params = {
                                'ctx': 'recover',
                                'ars': 'facebook_login',
                                'from_login_screen': '0',
                        }
                        response = requests.get('https://m.facebook.com/login/identify/',timeout=60, proxies=self.proxy,params=params, headers=headers)
                        ketqua =response.text
                        cookie_index = response.headers['Set-Cookie']
                        jazoest = ketqua.split('name="jazoest" value="')[1].split('"')[0]
                        lsd = ketqua.split('name="lsd" value="')[1].split('"')[0]
                        hsi = ketqua.split('hsi":"')[1].split('"')[0]
                        __spin_r = ketqua.split('__spin_r":')[1].split(',')[0]
                        __spin_t = ketqua.split('__spin_t":')[1].split(',')[0]
                        # print(ketqua)
                        

                        
                        # check liên kết
                        headers1 = {
                        'authority': 'en-gb.facebook.com',
                        'accept': '*/*',
                        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                        'cache-control': 'no-cache',
                        'content-type': 'application/x-www-form-urlencoded',
                        'cookie': cookie_index,
                        'origin': 'https://en-gb.facebook.com',
                        'pragma': 'no-cache',
                        'referer': 'https://en-gb.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0',
                        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                        'x-asbd-id': '198387',
                        'x-fb-lsd': 'AVrNqfhQnfo',
                        }

                        params1 = {
                        'ctx': 'recover',
                        }

                        data1 = {
                                'jazoest': jazoest,
                                'lsd': lsd,
                                'email': mail,
                                'did_submit': '1',
                                '__user': '0',
                                '__a': '1',
                                '__dyn': '7xe6E5aQ1PyUbFuC1swgE98nwgU29zEdEc8uwdK0lW4o3Bw5VCwjE3awbG782Cw8G0umUS1vw5zwwwi81nE1u83mwaS0zE1bE1AE17U2ZwrU19E',
                                '__csr': '',
                                '__req': '4',
                                '__hs': '19440.BP:DEFAULT.2.0..0.0',
                                'dpr': '1',
                                '__ccg': 'UNKNOWN',
                                '__rev': '1007174414',
                                '__s': '776h1s:x0mh4m:3kv5tv',
                                '__hsi': hsi,
                                '__comet_req': '0',
                                '__spin_r': __spin_r,
                                '__spin_b': 'trunk',
                                '__spin_t': __spin_t,
                        }

                        response1 = requests.post(
                        'https://en-gb.facebook.com/ajax/login/help/identify.php',
                        params=params1,
                        headers=headers1,
                        data=data1,
                        proxies=self.proxy,
                        timeout=60
                        ).text
                        # print(response1)
                        
                        check_lienket = re.search('"#account_search",false,',response1)
                        if check_lienket == None:
                                self.count_lienket += 1
                                print(f'Mail Liên Kết: {self.count_lienket}')
                                self.all.mail_lien_ket.setText(f"<html><head/><body><p><span style=\" font-weight:600;\">Mail Liên Kết: {self.count_lienket}</span></p></body></html>")
                                self.all.listWidget.addItem(f"[Thread {stt_mail}] => {mail} >>> Có Liên Kết")
                                with open('FILE_MAIL_LIÊN_KẾT.txt','a', encoding= "utf-8") as mail_lien_ket:
                                                mail_lien_ket.write('\n'+mail)

                        else:
                                self.count_nolienket += 1
                                print(f'Mail Không Liên Kết: {self.count_nolienket}')
                                
                                self.all.listWidget.addItem(f"[Thread {stt_mail}] => {mail} >>> No Linked")
                                self.all.mail_khong_lien_ket.setText(f"<html><head/><body><p><span style=\" font-weight:600;\">Mail Không Liên Kết: {self.count_nolienket}</span></p></body></html>")
                                with open('FILE_MAIL_KHÔNG_LIÊN_KẾT.txt','a', encoding= "utf-8") as mail_khong_lien_ket:
                                                mail_khong_lien_ket.write('\n'+mail)
                except:
                        self.count += 1
                        try:
                                if self.count % 20 == 0:
                                        self.all.listWidget.clear()
                                if self.count % 100 == 0:
                                        a = requests.get('https://proxyxoay.net/api/rotating-proxy/change-key-ip/25f9c8ca-37c8-46f9-a96c-4fd5adda047a',timeout=60).text
                                        b = json.loads(a)
                                        self.all.listWidget.addItem(f"=> Đang Đổi IP {b['message']} ")
                                        
                                        print(a.text)
                                        sleep(20)
                                # self.list_proxy = self.all.plainTextEdit_proxy.toPlainText().split("\n")
                                self.all.sl_mail_da_check.setText(f"<html><head/><body><p><span style=\" font-weight:600;\">Số Lượng Đã Mail Đã Check: {self.count}</span></p></body></html>")
                                headers = {
                                        'authority': 'm.facebook.com',
                                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                                        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                                        'cache-control': 'no-cache',
                                        # 'cookie': 'datr=sDAdZOjFrj58kCZJJg2CkZIP; m_pixel_ratio=1; wd=457x969; fr=0XdKexMeN6BbjgiGE..BkHTDV.gl.AAA.0.0.BkHTDc.AWUf8o2Rm7w',
                                        'pragma': 'no-cache',
                                        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
                                        'sec-ch-ua-mobile': '?0',
                                        'sec-ch-ua-platform': '"Windows"',
                                        'sec-fetch-dest': 'document',
                                        'sec-fetch-mode': 'navigate',
                                        'sec-fetch-site': 'none',
                                        'sec-fetch-user': '?1',
                                        'upgrade-insecure-requests': '1',
                                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                                }

                                params = {
                                        'ctx': 'recover',
                                        'ars': 'facebook_login',
                                        'from_login_screen': '0',
                                }
                                response = requests.get('https://m.facebook.com/login/identify/',timeout=60, proxies=self.proxy,params=params, headers=headers)
                                ketqua =response.text
                                cookie_index = response.headers['Set-Cookie']
                                jazoest = ketqua.split('name="jazoest" value="')[1].split('"')[0]
                                lsd = ketqua.split('name="lsd" value="')[1].split('"')[0]
                                hsi = ketqua.split('hsi":"')[1].split('"')[0]
                                __spin_r = ketqua.split('__spin_r":')[1].split(',')[0]
                                __spin_t = ketqua.split('__spin_t":')[1].split(',')[0]
                                # print(ketqua)
                                

                                
                                # check liên kết
                                headers1 = {
                                'authority': 'en-gb.facebook.com',
                                'accept': '*/*',
                                'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                                'cache-control': 'no-cache',
                                'content-type': 'application/x-www-form-urlencoded',
                                'cookie': cookie_index,
                                'origin': 'https://en-gb.facebook.com',
                                'pragma': 'no-cache',
                                'referer': 'https://en-gb.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0',
                                'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
                                'sec-ch-ua-mobile': '?0',
                                'sec-ch-ua-platform': '"Windows"',
                                'sec-fetch-dest': 'empty',
                                'sec-fetch-mode': 'cors',
                                'sec-fetch-site': 'same-origin',
                                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                                'x-asbd-id': '198387',
                                'x-fb-lsd': 'AVrNqfhQnfo',
                                }

                                params1 = {
                                'ctx': 'recover',
                                }

                                data1 = {
                                        'jazoest': jazoest,
                                        'lsd': lsd,
                                        'email': mail,
                                        'did_submit': '1',
                                        '__user': '0',
                                        '__a': '1',
                                        '__dyn': '7xe6E5aQ1PyUbFuC1swgE98nwgU29zEdEc8uwdK0lW4o3Bw5VCwjE3awbG782Cw8G0umUS1vw5zwwwi81nE1u83mwaS0zE1bE1AE17U2ZwrU19E',
                                        '__csr': '',
                                        '__req': '4',
                                        '__hs': '19440.BP:DEFAULT.2.0..0.0',
                                        'dpr': '1',
                                        '__ccg': 'UNKNOWN',
                                        '__rev': '1007174414',
                                        '__s': '776h1s:x0mh4m:3kv5tv',
                                        '__hsi': hsi,
                                        '__comet_req': '0',
                                        '__spin_r': __spin_r,
                                        '__spin_b': 'trunk',
                                        '__spin_t': __spin_t,
                                }

                                response1 = requests.post(
                                'https://en-gb.facebook.com/ajax/login/help/identify.php',
                                params=params1,
                                headers=headers1,
                                data=data1,
                                proxies=self.proxy,
                                timeout=60
                                ).text
                                # print(response1)
                                
                                check_lienket = re.search('"#account_search",false,',response1)
                                if check_lienket == None:
                                        self.count_lienket += 1
                                        print(f'Mail Liên Kết: {self.count_lienket}')
                                        self.all.mail_lien_ket.setText(f"<html><head/><body><p><span style=\" font-weight:600;\">Mail Liên Kết: {self.count_lienket}</span></p></body></html>")
                                        self.all.listWidget.addItem(f"[Thread {stt_mail}] => {mail} >>> Có Liên Kết")
                                        with open('FILE_MAIL_LIÊN_KẾT.txt','a', encoding= "utf-8") as mail_lien_ket:
                                                        mail_lien_ket.write('\n'+mail)

                                else:
                                        self.count_nolienket += 1
                                        print(f'Mail Không Liên Kết: {self.count_nolienket}')
                                        
                                        self.all.listWidget.addItem(f"[Thread {stt_mail}] => {mail} >>> No Linked")
                                        self.all.mail_khong_lien_ket.setText(f"<html><head/><body><p><span style=\" font-weight:600;\">Mail Không Liên Kết: {self.count_nolienket}</span></p></body></html>")
                                        with open('FILE_MAIL_KHÔNG_LIÊN_KẾT.txt','a', encoding= "utf-8") as mail_khong_lien_ket:
                                                        mail_khong_lien_ket.write('\n'+mail)
                        except:
                                self.count_loi += 1
                                print(f'Số Lượng Đã Mail Đã Check Lỗi: {self.count_loi}')
                                
                                self.all.listWidget.addItem(f"[Thread {stt_mail}] => {mail} >>> Cần Check Lại")
                                self.all.sl_mail_da_check_loi.setText(f"<html><head/><body><p><span style=\" font-weight:600;\">Số Lượng Đã Mail Đã Check Lỗi: {self.count_loi}</span></p></body></html>")
                                with open('FILE_MAIL_LỖI_CẦN CHECK_LẠI.txt','a', encoding= "utf-8") as mail_error:
                                                mail_error.write('\n'+mail)

                        

                
                

if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
