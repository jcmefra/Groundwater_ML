# Groundwater Detection using Machine Learning

This repository contains code for a machine learning model that detects groundwater presence based on resistivity values from geophysical surveys.

## Table of Contents

- 1. Create Anaconda Environment
- 2. Conda Environment Setup
- 3. Training the Model
- 4. Dataset Format
- 5. Implementing the Model
- 6. Future Improvements

## 1. Create Anaconda Environment

**To create a new Anaconda environment for this project, use the following command:
**
conda create --name groundwater-env python=3.8

**Activate the environment:
**
conda activate groundwater-env


## Conda Environment Setup

**Install required packages using conda from the provided environment.yml file:
**
conda env update -f environment.yml


## Training the Model

1. Prepare your training data by following the dataset format guidelines.
2. Open the Jupyter Notebook or Python script for the model provided in this repository.
3. Execute the code step by step, following the comments for each section.
4. The model will be trained and evaluated, and feature importances will be displayed.

## Dataset Format

The dataset for training the model should be in CSV format, containing the following columns:

- `elec_pos`: Electrode position
- `depth`: Depth value
- `rho`: Resistivity value
- `cond`: Conductivity value
- `groundwater_presence`: Binary indicator of groundwater presence (0 or 1)

Refer to the provided sample data for an example.

## Implementing the Model

To implement the trained model on new survey data:

1. Load your new survey data in a DataFrame with columns (`elec_pos`, `depth`, `rho`, `cond`).
2. Create a meshgrid for electrode positions and depth.
3. Predict groundwater presence using the trained model.
4. Visualize the results using contour plots.

Refer to the provided code for prediction and visualization steps.

## Future Improvements

- Incorporate multiple surveys for more diverse training.
- Explore other machine learning algorithms for comparison.
- Enhance the model's accuracy through hyperparameter tuning.
- Develop a user-friendly interface for input and visualization.
- Implement additional features like uncertainty estimation.

Feel free to contribute to this repository by submitting pull requests or issues!

---

**Author:** Camilo Mejía

**License:** This project is licensed under the GNU GENERAL PUBLIC LICENSE.
