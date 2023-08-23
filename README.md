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

# Important note:

**If you don't have a Nvidia GPU you may get this error when installing environment.yml:**

Could not solve for environment specs
The following packages are incompatible
├─ libxgboost ==1.7.6 cuda120h75debf4_0 is uninstallable because it requires
│  └─ __cuda  , which is missing on the system;
├─ py-xgboost ==1.7.6 cuda120py310h379b205_0 is uninstallable because it requires
│  └─ __cuda  , which is missing on the system;
└─ xgboost ==1.7.6 cuda120py310h379b205_0 is uninstallable because it requires
   └─ __cuda  , which is missing on the system.

**In this case you should install the package manually using:**

conda install -c conda-forge py-xgboost

## 3. Training the Model

1. Prepare your training data by following the dataset format guidelines.
2. Open the Jupyter Notebook or Python script for the model provided in this repository (groundwater.ipynb)
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
**Feel free to do pull requests to this repository to make improvements**

- Incorporate multiple surveys for more diverse training and improve model prediction accuracy.
- Instead of using a fixed 80/20 split, techniques like cross-validation can be used to improve the model's ability to generalize.
- Adding more variables to the dataframe (i.e. rock type, porosity) to improve the criteria for groundwater prediction.
- Improve Model Performance at Boundaries.
- Enhance Groundwater Visualization by using dedicated libraries like GeoPandas.
- Explore other machine learning algorithms for comparison.
- Enhance the model's accuracy through hyperparameter tuning.
- Develop a user-friendly interface for input and visualization.
- Implement additional features like uncertainty estimation (boostrapping or Monte Carlo).

---

**Author:** Camilo Mejía

**License:** This project is licensed under the GNU GENERAL PUBLIC LICENSE.
