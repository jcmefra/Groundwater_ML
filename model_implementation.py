import pandas as pd
import joblib

import numpy as np
import matplotlib.pyplot as plt

# Load the trained model
model_file = 'Trained_model.pkl'  # Replace with your actual filename
loaded_model = joblib.load(model_file)

# Load and preprocess the new, untrained data
data_file = 'data_for_training/Guapota_Res.csv'  # Replace with the filename of your new data
data = pd.read_csv(data_file)
data_predict = data.drop(columns=['elec_pos'])

# Preprocess the new data (same preprocessing as training data)
# ...

# Predict using the loaded model
predicted_presence = loaded_model.predict(data_predict)

# Display predictions
for idx, prediction in enumerate(predicted_presence):
    if prediction == 1:
        print(f"Data point {idx+1}: Groundwater Presence: Yes")
    else:
        print(f"Data point {idx+1}: Groundwater Presence: No")

# Create a meshgrid for electrode position and depth
elec_pos_values = np.unique(data['elec_pos'])
depth_values = np.unique(data['depth'])
X, Y = np.meshgrid(elec_pos_values, depth_values)

# Reshape the data for visualization: create a new array to hold the predicted values.
Z = np.zeros(X.shape)
index = 0
for i, elec_pos in enumerate(elec_pos_values):
    for j, depth in enumerate(depth_values):
        if index < len(predicted_presence):
            Z[j, i] = predicted_presence[index]
        index += 1
        if index >= len(predicted_presence):
            break

# Create the contour plot
plt.figure(figsize=(10, 8))
contour = plt.contourf(X, Y, Z, levels=20, cmap='viridis')
plt.colorbar(contour, label='Groundwater Presence')
plt.ylabel('Depth')
plt.gca().invert_yaxis()

plt.title('2D Subsurface Profile - Predicted Groundwater Presence', pad=20)
plt.xlabel('Electrode Position')
plt.gca().xaxis.tick_top()
plt.gca().xaxis.set_label_position('top')
plt.yticks(fontsize=8)
plt.subplots_adjust(top=0.85)

plt.savefig('predicted_new_data.png')
plt.show()
