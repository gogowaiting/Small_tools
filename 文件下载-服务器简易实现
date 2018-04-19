import socket
import os

# 创建tcp 套接字
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 指定本地ip和端口,绑定
server_address = ("", 4433)
tcp_server_socket.bind(server_address)

# 设置监听
tcp_server_socket.listen(128)

while True:
    # 设置等待客户端链接
    client_socket, client_address = tcp_server_socket.accept()

    # 接收数据并设置接收最大字节
    file_name_data = client_socket.recv(1024)
    # 对接收的数据进行解码
    file_name = file_name_data.decode("utf-8")
    # 判断文件是否存在
    if os.path.exists(file_name):
        with open(file_name, "rb") as tmp:
            # 循环读取数据
            while True:
                tmp_data = tmp.read(1024)
                # 判断数据是否传输完成
                if tmp_data:
                    client_socket.send(tmp_data)
                else:
                    break
    else:
        print("文件不存在.")
    # 关闭客户端socket
    client_socket.close()
# 关闭监听socket
tcp_server_socket.close()
