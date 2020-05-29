from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
# more info on callbakcs: https://keras.io/callbacks/ model saver is cool too.
from tensorflow.keras.callbacks import TensorBoard
# from keras.optimizers import RMSprop
import tensorflow as tf
import pickle
import time


# from tensorflow import keras
# from kerastuner import RandomSearch
# from kerastuner.engine.hyperparameters import HyperParameters

pickle_in = open("X.pickle", "rb")
X = pickle.load(pickle_in)

pickle_in = open("y.pickle", "rb")
y = pickle.load(pickle_in)

X = X/255.0

dense_layers = [0]
layer_sizes = [64]
conv_layers = [3]


# def build(hp):
#     model = keras.Sequential(
#         [keras.layers.Conv2D(filters=hp.Int('conv_1_filter', min_value=32, max_value=128, step=16),
#                              kernel_size=hp.Choice(
#                                  'conv_1_kernel', values=[3, 5]),
#                              activation='relu', input_shape=X.shape[1:]),
#          keras.layers.Conv2D(filters=hp.Int('conv_2_filter', min_value=32, max_value=64, step=16),
#                              kernel_size=hp.Choice(
#                                  'conv_2_kernel', values=[3, 5]),
#                              activation='relu'),
#          keras.layers.Flatten(),
#          keras.layers.Dense(units=hp.Int('dense_1_units', min_value=32, max_value=128, step=16),
#                             activation='relu'),
#          keras.layers.Dense(10, activation='softmax')])

#     model.compile(optimizer=keras.optimizers.Adam(hp.Choice('learning_rate', values=[1e-2, 1e-3])),
#                   loss='sparse_categorical_crossentropy',
#                   metrics=['accuracy'])

#     return model


# def train():
for dense_layer in dense_layers:
    for layer_size in layer_sizes:
        for conv_layer in conv_layers:
            NAME = "{}-conv-{}-nodes-{}-dense-{}".format(
                conv_layer, layer_size, dense_layer, int(time.time()))
            print(NAME)

            model = Sequential()

            model.add(Conv2D(layer_size, (3, 3), input_shape=X.shape[1:]))
            model.add(Activation('relu'))
            model.add(MaxPooling2D(pool_size=(2, 2)))

            for l in range(conv_layer-1):
                model.add(Conv2D(layer_size, (3, 3)))
                model.add(Activation('relu'))
                model.add(MaxPooling2D(pool_size=(2, 2)))

            model.add(Flatten())

            for _ in range(dense_layer):
                model.add(Dense(layer_size))
                model.add(Activation('relu'))
                model.add(Dropout(0.5))

            model.add(Dense(1))
            model.add(Activation('sigmoid'))

            tensorboard = TensorBoard(log_dir="logs/{}".format(NAME))

            # opt = RMSprop()
            opt = tf.keras.optimizers.Adam(learning_rate=0.001)

            model.compile(loss='binary_crossentropy',
                            optimizer=opt,
                            metrics=['accuracy'])

            model.fit(X, y,
                        batch_size=32,
                        epochs=10,
                        validation_split=0.2,
                        callbacks=[tensorboard])

model.save('64x3-CNN.model')


# tuner_search = RandomSearch(build,
#                             objective='val_acc',
#                             max_trials=5, directory='output', project_name="Waste Classifier")

# tuner_search.search(X, y, epochs=3, validation_split=0.1)
