import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Step 1: Load your data
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Step 2: Preprocess the data
def preprocess_data(data):
    X = data.drop('label', axis=1)  # Assuming the label column is named 'label'
    y = data['label']
    
    # Normalize features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    return train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Step 3: Define the model
def create_model(input_shape):
    model = keras.Sequential([
        layers.Dense(64, activation='relu', input_shape=input_shape),
        layers.Dense(32, activation='relu'),
        layers.Dense(1, activation='sigmoid')  # Use softmax for multi-class
    ])
    
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',  # Use 'categorical_crossentropy' for multi-class
                  metrics=['accuracy'])
    
    return model

# Step 4: Train the model
def train_model(X_train, y_train, model):
    model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

# Step 5: Evaluate the model
def evaluate_model(X_test, y_test, model):
    loss, accuracy = model.evaluate(X_test, y_test)
    print(f'Test Accuracy: {accuracy:.2f}')

# Main function to run the process
def main(file_path):
    data = load_data(file_path)
    X_train, X_test, y_train, y_test = preprocess_data(data)
    
    model = create_model((X_train.shape[1],))
    train_model(X_train, y_train, model)
    evaluate_model(X_test, y_test, model)

# Example usage
if __name__ == '__main__':
    main('path_to_your_data.csv')
