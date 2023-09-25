import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
import numpy as np
import tensorflow_hub as hub

# 사용 예시
data_path = './sejong3000QA.csv'
save_path = './IntentModel.h5'


def prepare_data_and_train_model(data_path, save_path):
    # Read the CSV dataset
    df = pd.read_csv(data_path)

    num_classes = len(df["label"].value_counts())
    y = tf.keras.utils.to_categorical(df["label"].values, num_classes=num_classes)

    x_train, x_test, y_train, y_test = train_test_split(df['Q'], y, test_size=0.25)

    preprocessor = hub.KerasLayer("https://tfhub.dev/google/universal-sentence-encoder-cmlm/multilingual-preprocess/2")
    encoder = hub.KerasLayer("https://tfhub.dev/google/universal-sentence-encoder-cmlm/multilingual-base/1")

    i = tf.keras.layers.Input(shape=(), dtype=tf.string, name='text')
    x = preprocessor(i)
    x = encoder(x)
    x = tf.keras.layers.Dropout(0.2, name="dropout")(x['pooled_output'])
    x = tf.keras.layers.Dense(num_classes, activation='softmax', name="output")(x)

    model = tf.keras.Model(i, x)

    x_train = np.array([np.array(val) for val in x_train])  # reconstruct
    n_epochs = 20

    model.compile(optimizer="adam",
                  loss="categorical_crossentropy")

    model_fit = model.fit(x_train,
                          y_train,
                          epochs=n_epochs)

    # Save the trained model
    model.save(save_path)


prepare_data_and_train_model(data_path, save_path)
