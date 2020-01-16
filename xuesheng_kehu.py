"""
udp 客户端 发送学生打包信息

"""

from socket import *
import struct

st = struct.Struct("i60sif")
t = socket(AF_INET, SOCK_DGRAM, 0)
n = 0
while True:
    n += 1
    print(("第 %d 次打包发送") % (n))
    id = int(input("ID:"))
    name = input("name:").encode()
    age = int(input("age:"))
    score = float(input("score:"))
    data = st.pack(id, name, age, score)
    t.sendto(data, ("127.0.0.1", 8848))
    print("发送完毕")
    mes, addr = t.recvfrom(1024)
    print("收到新消息："+mes.decode())
