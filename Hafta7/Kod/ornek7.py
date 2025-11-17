from threading import Condition, Thread
from flask import Flask, jsonify
import numpy as np
from keras.models import Sequential
from keras.layers import Dense

cv = Condition()
model_egitildimi = False
keras_model = None

def train_model():
    global model_egitildimi, keras_model
    model = Sequential([Dense(1, input_shape=(1, ))])
    model.compile(optimizer = "sgd", loss="mse")
    # Stochastic gradient descent - stokastik gradyan azalması

    X = np.array([1.0, -1.0, 2.0, 3.0, 4.0, 5.0]) # 2x-1
    y = np.array([1.0, -3.0, 3.0, 5.0, 7.0, 9.0])

    model.fit(X, y, epochs=100, verbose=False)
    with cv:
        model_egitildimi = True
        keras_model = model
        cv.notify()

app = Flask(__name__)
@app.route("/")
def index():
    return "Henüz model eğitiliyor... /predict endpointine istek atiniz..."

@app.route("/predict")
def predict():
    with cv:
        while not model_egitildimi:
            cv.wait()
        predict = float(keras_model.predict(np.array([7.0])))
        return jsonify({"deger": 7.0, "tahmin": predict})

if __name__ == "__main__":
    t = Thread(target=train_model, args=())
    t.start()

    app.run(debug=True, threaded=True)



