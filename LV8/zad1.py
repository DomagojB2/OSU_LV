import numpy as np
import keras
from keras import layers
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# parametri
num_classes = 10
input_shape = (28, 28, 1)

# ucitaj podatke
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

print('Train: X=%s, y=%s' % (x_train.shape, y_train.shape))
print('Test: X=%s, y=%s' % (x_test.shape, y_test.shape))

# prikaz nekoliko slika
for i in range(5):
    plt.imshow(x_train[i], cmap='gray')
    plt.title(f'Oznaka: {y_train[i]}')
    plt.show()

# skaliranje
x_train_s = x_train.astype("float32") / 255
x_test_s = x_test.astype("float32") / 255

# dodaj kanal
x_train_s = np.expand_dims(x_train_s, -1)
x_test_s = np.expand_dims(x_test_s, -1)

print("x_train shape:", x_train_s.shape)

# one-hot encoding
y_train_s = keras.utils.to_categorical(y_train, num_classes)
y_test_s = keras.utils.to_categorical(y_test, num_classes)

# MODEL (ispravno definiran)
model = keras.Sequential([
    layers.Input(shape=input_shape),
    layers.Flatten(),
    layers.Dense(100, activation='relu'),
    layers.Dense(50, activation='relu'),
    layers.Dense(num_classes, activation='softmax')
])

model.summary()

# compile
model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

# treniranje (KORISTI SKALIRANE PODATKE!)
batch_size = 32
epochs = 20

history = model.fit(
    x_train_s, y_train_s,
    batch_size=batch_size,
    epochs=epochs,
    validation_split=0.1
)

# predikcije
predictions = model.predict(x_test_s)
y_test_p = np.argmax(predictions, axis=1)

# evaluacija (također skalirani + one-hot)
score = model.evaluate(x_test_s, y_test_s, verbose=0)
print('Accuracy:', score[1])

# matrica zabune
cm = confusion_matrix(y_test, y_test_p)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.show()

# spremanje modela
model.save('model.keras')