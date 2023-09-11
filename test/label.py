from tensorflow import keras
import numpy as np
import tensorflow_hub as hub
import tensorflow_text as text


def predict_label(question):

    question = [question]

    # 모델 로드
    model = keras.models.load_model("C:\GP\BackEnd\models\IntentModel.h5", custom_objects={'KerasLayer': hub.KerasLayer})


    return [np.argmax(pred) for pred in model.predict(question)][0]

question = '해시계가 뭐야?'
print(predict_label(question))