import time
import cv2

def capture_and_save_photo(file_path, camera_index):
 # カメラをオープン
    cap = cv2.VideoCapture(camera_index)

    # カメラが正常にオープンされたか確認
    if not cap.isOpened():
        print("Error: カメラが正常にオープンされませんでした。")
        return

    # フレームをキャプチャ
    ret, frame = cap.read()

    # カメラを解放
    cap.release()

    # キャプチャが成功した場合、画像を保存
    if ret:
        cv2.imwrite(file_path, frame)
        print(f"写真を {file_path} に保存しました。")
    else:
        print("Error: 画像のキャプチャに失敗しました。")

if __name__ == "__main__":
    # キャプチャして保存するファイルのパスを指定
    file_path = 'captured_photo.jpg'

    # カメラのインデックスを指定 (通常は0から始まります)
    camera_index = 0

    # 写真を撮影して保存
    capture_and_save_photo(file_path, camera_index)
