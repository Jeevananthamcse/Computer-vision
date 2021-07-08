from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dropout, Dense
cnn = Sequential([Conv2D(filters=100, kernel_size=(3,3),
                         activation='relu'),
                  MaxPooling2D(pool_size=(2,2)),
                  Conv2D(filters=100, kernel_size=(3,3),
                         activation='relu'),
                  MaxPooling2D(pool_size=(2,2)),
                  Flatten(),
                  Dropout(0.5),
                  Dense(50),
                  Dense(35),
                  Dense(2)])
cnn.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])