# Groundwater Detection using Machine Learning

This repository contains code for a machine learning model that detects groundwater presence based on resistivity values from geophysical surveys.

## Table of Contents

- 1. Create Anaconda Environment
- 2. Conda Environment Setup
- 3. Training the Model
- 4. Dataset Format
- 5. Implementing the Model
- 6. Using the Trained Model
- 7. Future Improvements

## 1. Create Anaconda Environment

**To create a new Anaconda environment for this project, use the following command:**

conda create --name groundwater-env python=3.8

**Activate the environment:**

conda activate groundwater-env

## 2. Conda Environment Setup

**Install required packages using conda from the provided environment.yml file:**

conda env update -f environment.yml

## 3. Training the Model

1. Prepare your training data by following the dataset format guidelines.
2. Open the Jupyter Notebook or Python script for the model provided in this repository.
3. Execute the code step by step, following the comments for each section.
4. The model will be trained and evaluated, and feature importances will be displayed.

## 4. Dataset Format

The dataset for training the model should be in CSV format, containing the following columns:

- `elec_pos`: Electrode position
- `depth`: Depth value
- `rho`: Resistivity value
- `cond`: Conductivity value
- `groundwater_presence`: Binary indicator of groundwater presence (0 or 1)

Refer to the provided sample data for an example. Groundwater values can vary depending on your needs; the code already includes some lines to add the `groundwater_presence` column based on a defined rho threshold, see step 2.

## 5. Implementing the Model

To implement the trained model on new survey data:

1. Load your new survey data into a DataFrame with columns (`elec_pos`, `depth`, `rho`, `cond`).
2. Create a meshgrid for electrode positions and depth.
3. Predict groundwater presence using the trained model.
4. Visualize the results using contour plots.
5. Save the trained model as a *.pkl file

## 6. Using the Trained Model

To use the trained model for prediction on new data:

1. Load the trained model using joblib.
2. Load and preprocess the new, untrained data.
3. Preprocess the new data (same preprocessing as training data).
4. Predict using the loaded model.
5. Display predictions.

## 7. Future Improvements
**Feel free to do pull requests or for this repository to make improvements**

- Incorporate multiple surveys for more diverse training and improve model prediction accuracy.
- If we use 80/20 for training/test, we miss important information so it needs to be improved adding more surveys.
- Model is not working as expected at the center and at the bottom boundary.
- Groundwater precision and visualization of the data need to be improved as well.
- Explore other machine learning algorithms for comparison.
- Enhance the model's accuracy through hyperparameter tuning.
- Develop a user-friendly interface for input and visualization.
- Implement additional features like uncertainty estimation.

---

**Author:** Camilo Mejía

**License:** This project is licensed under the GNU GENERAL PUBLIC LICENSE.
