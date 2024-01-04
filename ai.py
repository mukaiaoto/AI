from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

# モデルを使って推論する処理を関数にまとめた
# 引数として画像のパスを受け取り、推論結果を返す
def predict(picture_path: str) -> str:
    np.set_printoptions(suppress=True)

    # ファイル名からモデルを読み込む
    model = load_model("keras_model.h5", compile=False)

    # ファイル名からクラス名を読み込む
    class_names = open("labels.txt", "r").readlines()

    # モデルに入力する画像データを格納する配列を作成(画像1枚、横224ピクセル、縦224ピクセル、RGBの3色)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # ファイル名から画像を読み込む、引数として入力された画像のパスを指定
    image = Image.open(picture_path).convert("RGB")

    # 画像のサイズを224x224ピクセルに変換
    size = (224, 224)
    image = image.resize((size),resample=Image.BICUBIC)

    # 画像をnumpy配列に変換
    image_array = np.asarray(image)

    # 画像を正規化
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # 画像をモデル入力用配列に格納
    data[0] = normalized_image_array

    # 推論を実行
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # 推論結果を表示
    print("Class:", class_name[2:], end="")
    print("Confidence Score:", confidence_score)

    # 分類結果(クラス名)を呼び出し元に返す
    return class_name[2:]
