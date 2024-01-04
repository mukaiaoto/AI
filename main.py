import time

# 別のファイルから関数をインポート
from camera import capture_and_save_photo
from ai import predict

# 実行間隔を5分に設定
interval = 5 * 60

# プログラムを実行する関数を作成
def capture_photo_and_predict():
  photo = capture_and_save_photo(file_path, camera_index)
  predict(picture)

while True:
  capture_photo_and_predict()
  time.sleep(interval)
