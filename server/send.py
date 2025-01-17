import socket
import cv2
import numpy

# サーバーのIPアドレスとポート
HOST = 'localhost'
PORT = 50008

def main():
    # ソケットの作成
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # サーバーに接続
        s.connect((HOST, PORT))

if __name__ == '__main__':
    main()
