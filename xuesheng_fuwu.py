"""
udp 服务端流程 循环接收学生信息
使用udp 和 struct模块
      1. 从客户端循环录入学生信息，包含

         id   姓名  年龄   分数

      2. 将信息打包发送给服务端

      3. 在服务端判断如果学生的分数大于90分则将该学生
      信息写入到 student.txt文件中
      每位学生信息占一行
"""

from socket import *
import struct

st = struct.Struct("i60sif")  # 定义与客户端的打包解包格式
# socket
t = socket(AF_INET, SOCK_DGRAM, 0)
# bind
kk = ("0.0.0.0", 8848)
t.bind(kk)
# recvfrom

# 解包 新建文件  读  写到新文件
n = 0
while True:
    n += 1
    xinxi, addr = t.recvfrom(1024)
    print("接收到包")
    student_xinxi = st.unpack(xinxi)
    print("解包完毕")
    if student_xinxi[3] >= 90:
        avbc = open("student.txt", 'a+')
                                        #移除字符串头尾指定的字符
        name = student_xinxi[1].decode().strip('\x00')
                          #%.1f 浮点型保留小数点后一位
        info = "%d %s %d %.1f \n" % (student_xinxi[0], name, student_xinxi[2], student_xinxi[3])
        print("打开文件完毕")
        avbc.write(info)  # 解包后的数据为一个元组
        print("写入完毕")
        avbc.flush()
        t.sendto("满足90分,已录入".encode(), addr)
        print(n, "次接受完毕")
    else:
        print("成绩<90")
        t.sendto("不满足90分,不能录入".encode(), addr)
        print(n, "次接受完毕")
    # sendto
    # close
