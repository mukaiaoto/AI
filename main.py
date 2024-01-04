import time

# 別のファイルから関数をインポート
from camera import capture_and_save_photo
from ai import estimate

# 実行間隔を5分に設定
interval = 5 * 60

# プログラムを実行する関数を作成
def take_picture_and_estimate():
  capture_and_save_photo(file_path, camera_index)
  estimate()

while True:
  take_picture_and_estimate()
  time.sleep(interval)
