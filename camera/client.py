# send.jpgをサーバーに送信するクライアント
import socket
import cv2
import numpy

# サーバーのIPアドレスとポート
HOST = 'localhost'
PORT = 50007

def main():
    try:
        # ソケットの作成
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # サーバーに接続
            s.connect((HOST, PORT))
            
            # 画像の読み込み
            file_name = 'kouyo.jpg'
            img = cv2.imread(file_name)
            if img is None:
                raise FileNotFoundError(f"File {file_name} not found or unable to read")
            
            # 画像をバイト列に変換
            data = cv2.imencode('.jpg', img)[1].tobytes()
            
            # ファイル名を送信（1024バイトに固定）
            s.sendall(file_name.encode().ljust(1024))
            
            # 画像データをチャンクに分けて送信
            chunk_size = 4096
            for i in range(0, len(data), chunk_size):
                s.sendall(data[i:i + chunk_size])
            
            print(f"{file_name} sent successfully")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
