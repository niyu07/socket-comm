# tcpで画像を受信するサーバー
# 画像を受信するとファイル名に基づいて保存する
import socket
import cv2
import numpy
import os

# 待ち受けtcpポート
PORT = 50007

def main():
    # ソケットの作成
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # ソケットの設定
        s.bind(('', PORT))
        s.listen(1)
        print('Waiting for connection...')
        # クライアントからの接続を待つ
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            
            # ファイル名を受信（最初の1024バイトでファイル名を受信）
            file_name = conn.recv(1024).decode().strip()  # バイトを文字列に変換
            if not file_name:
                print("Received an empty file name. Exiting.")
                return

            # データ本体を受信
            data = b""  # バイナリデータを保持する変数
            while True:
                packet = conn.recv(4096)  # データを分割して受信
                if not packet:
                    break
                data += packet

            # 受信したデータを画像に変換
            img = cv2.imdecode(numpy.frombuffer(data, dtype='uint8'), cv2.IMREAD_COLOR)
            if img is None:
                print("Failed to decode image. Data might be corrupted.")
                return

            # 受信したファイル名で画像を保存
            # 保存先ディレクトリを指定
            save_dir = "./images"
            os.makedirs(save_dir, exist_ok=True)  # 画像保存用のディレクトリがない場合は作成
            file_path = os.path.join(save_dir, file_name)
            cv2.imwrite(file_path, img)
            print(f"Image saved to {file_path}")
            

if __name__ == '__main__':
    while True:
        main()
