import numpy as np
from tensorflow import keras
from tensorflow.keras import models, layers

# A good resource is here: https://www.tensorflow.org/tutorials/images/cnn

EPOCHS = 10
BATCH_SIZE = 128

def mlp(input_shape, num_classes):
    """5-layer MLP with BatchNorm and Dropout."""
    model = models.Sequential([
        layers.Input(shape=input_shape),
        layers.Flatten(),
        layers.Dense(units=512, activation='relu', kernel_initializer='he_normal'),
        layers.BatchNormalization(),
        layers.Dropout(0.5),

        layers.Dense(units=256, activation='relu', kernel_initializer='he_normal'),
        layers.BatchNormalization(),
        layers.Dropout(0.5),

        layers.Dense(units=144, activation='relu', kernel_initializer='he_normal'),
        layers.BatchNormalization(),
        layers.Dropout(0.5),

        layers.Dense(units=96, activation='relu', kernel_initializer='he_normal'),
        layers.BatchNormalization(),
        layers.Dropout(0.5),

        layers.Dense(units=36, activation='relu', kernel_initializer='he_normal'),
        layers.BatchNormalization(),
        layers.Dropout(0.5),

        layers.Dense(num_classes, activation='softmax')
    ])
    model.compile(
        optimizer=keras.optimizers.Adam(),
        loss=keras.losses.CategoricalCrossentropy(),
        metrics=[keras.metrics.CategoricalAccuracy()]
    )
    return model

def cnn(input_shape, num_classes):
    """Standard CNN based off the VGG-16 architecture."""
    model = models.Sequential([
        layers.Input(shape=input_shape),
        layers.Conv2D(filters=64, kernel_size=(3, 3), padding='same', kernel_initializer='he_normal'),
        layers.BatchNormalization(),
        layers.Activation('relu'),
        layers.Conv2D(filters=64, kernel_size=(3, 3), padding='same', kernel_initializer='he_normal'),
        layers.BatchNormalization(),
        layers.Activation('relu'),
        layers.MaxPool2D(pool_size=(2, 2), padding='same'),
        
        layers.Conv2D(filters=128, kernel_size=(3, 3), padding='same', kernel_initializer='he_normal'),
        layers.BatchNormalization(),
        layers.Activation('relu'),
        layers.Conv2D(filters=128, kernel_size=(3, 3), padding='same', kernel_initializer='he_normal'),
        layers.BatchNormalization(),
        layers.Activation('relu'),
        layers.MaxPool2D(pool_size=(2, 2), padding='same'),
        
        layers.Conv2D(filters=192, kernel_size=(3, 3), padding='same', kernel_initializer='he_normal'),
        layers.BatchNormalization(),
        layers.Activation('relu'),
        layers.Conv2D(filters=192, kernel_size=(3, 3), padding='same', kernel_initializer='he_normal'),
        layers.BatchNormalization(),
        layers.Activation('relu'),
        layers.MaxPool2D(pool_size=(2, 2), padding='same'),
        
        layers.Conv2D(filters=256, kernel_size=(3, 3), padding='same', kernel_initializer='he_normal'),
        layers.BatchNormalization(),
        layers.Activation('relu'),
        layers.Conv2D(filters=256, kernel_size=(3, 3), padding='same', kernel_initializer='he_normal'),
        layers.BatchNormalization(),
        layers.Activation('relu'),
        layers.MaxPool2D(pool_size=(2, 2), padding='same'),
        
        layers.Flatten(),
        layers.Dense(units=512, activation='relu'),
        layers.Dropout(0.2),
        layers.Dense(units=256, activation='relu'),
        layers.Dropout(0.2),
        layers.Dense(units=num_classes, activation='softmax')
    ])
    model.compile(
        optimizer=keras.optimizers.Adam(),
        loss=keras.losses.CategoricalCrossentropy(),
        metrics=[keras.metrics.CategoricalAccuracy()]
    )
    return model

def train(model, data, load_from_weights=False, ):
    if load_from_weights:
        model.load_weights('cnn.h5')
    else:
        (X_train, y_train), (X_test, y_test) = data
        history = model.fit(x=X_train, y=y_train, 
                            validation_data=(X_test, y_test), 
                            batch_size=BATCH_SIZE, epochs=EPOCHS, verbose=2)
    model.save_weights('cnn.h5')
    return model, history

def get_data(dataset):
    if dataset == 'cifar10':
        (X_train, y_train), (X_test, y_test) = keras.datasets.cifar10.load_data()

    elif dataset == 'mnist':
        (X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()

    input_shape = X_train[0].shape
    num_classes = max(y_train) + 1
    # Add channel dimension if images don't have one already (e.g. grayscale)
    if len(input_shape) < 4:
        X_train = np.expand_dims(X_train, axis=-1)
        X_test = np.expand_dims(X_test, axis=-1)
        input_shape = X_train[0].shape
    # convert uint8 RGB images to float RGB images in range [0,1]
    X_train = X_train.astype(np.float32) / 255.0
    X_test = X_test.astype(np.float32) / 255.0
    # convert class labels to one-hot encoding
    y_train = keras.utils.to_categorical(y_train, num_classes=num_classes)
    y_test = keras.utils.to_categorical(y_test, num_classes=num_classes)
    data = (X_train, y_train), (X_test, y_test)
    return data, input_shape, num_classes

if __name__ == '__main__':

    data, input_shape, num_classes = get_data('mnist')
    models = mlp(input_shape, num_classes), cnn(input_shape, num_classes)
    for model in models:
        model, history = train(model, data)
        single_example = data[1][0][0:1]
        print(model.predict(single_example))
        if history:
            print(max(history.history['val_categorical_accuracy']))
    