import numpy as np
from tensorflow import keras
from matplotlib import pyplot as plt
from tensorflow.keras.models import load_model

model = load_model('model.keras')

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# skaliranje
x_test_s = x_test.astype("float32") / 255
x_test_s = np.expand_dims(x_test_s, -1)

# predikcije (ISPRAVNO)
predictions = model.predict(x_test_s)
y_test_p = np.argmax(predictions, axis=1)

# prikaz pogrešnih klasifikacija
count = 0
for i in range(len(x_test)):
    if y_test[i] != y_test_p[i]:
        plt.imshow(x_test[i], cmap='gray')
        plt.title(f'Stvarna: {y_test[i]}, Predviđena: {y_test_p[i]}')
        plt.show()
        count += 1
        if count == 5:   # prikaži samo 5
            break