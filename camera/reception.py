import socket
import cv2
import numpy
import subprocess


PORT = 50008

def run_another_program():
    # ここに実行したい別のプログラムを指定
    subprocess.run(["python3", "client.py"])

def main():
    # ソケットの作成
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # ソケットの設定
        s.bind(('', PORT))
        s.listen(1)
        print('Waiting for connection...')
        # クライアントからの接続を待つ
        # クライアントからの接続を待つ
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                # 違うプログラムを実行
                run_another_program()
                break
        

if __name__ == '__main__':
    while True:
        main()
