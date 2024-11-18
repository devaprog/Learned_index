import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Load data
data = pd.read_csv("order_items.csv")
X = data["Unit_Price"].values.reshape(-1, 1)
y = data["OID"].values

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build the model
model = Sequential([
	Dense(64, activation="relu", input_shape=(1,)),
	Dense(32, activation="relu"),
	Dense(1)  # Output layer
])

model.compile(optimizer="adam", loss="mean_squared_error")
model.fit(X_train, y_train, epochs=50, batch_size=16, validation_split=0.2)

# Save the model
model.save("learned_index_model.h5")
