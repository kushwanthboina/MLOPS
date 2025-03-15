# MLOPS Project: Banking Term Deposit Prediction

This project implements an end-to-end MLOps pipeline for predicting whether a client will subscribe to a term deposit. It covers data ingestion, validation, model training and experiment tracking, deployment, user interface development, and model monitoring.

---

## Project Overview

- **Data Preparation & Validation:**  
  The dataset is ingested, validated using Pandera, profiled with ydata-profiling, and split into training, test, and production sets.

- **Experiment Tracking & Model Training:**  
  An ML pipeline is built with scikit-learn and multiple experiments are tracked with MLflow. The best model (RandomForest) was selected based on cross-validation and test accuracies.

- **Model Deployment:**  
  The chosen model is deployed using FastAPI, and the deployment is integrated with a Streamlit UI for user interaction.

- **Model Monitoring:**  
  Data drift (both numeric and categorical) is monitored using alibi-detect and chi-square tests to ensure that the production data remains consistent with the training data.

---

## Setup Instructions

**Clone the Repository:**

   ```bash
   cd MLOPS_Project
   git clone https://github.com/<username>/MLOPS_Project.git
   ```
## Running the Notebooks and Components

### Notebook 1: Data Preparation, Validation, and Experiment Tracking
- **Content:**  
  Contains code for data ingestion, validation with Pandera, data profiling, train-test-production split, building the ML pipeline, and MLflow experiment tracking.
- **Usage:**  
  Open and run `Notebook1.ipynb` in your Jupyter environment to reproduce the experiments.

### Notebook 2: Model Deployment using FastAPI
- **Content:**  
  Contains FastAPI code to deploy the best model.
- **Converted to Python File:**  
  The code has been converted to `Notebook2.py` for command-line execution.
- **Run the FastAPI App:**
  ```bash
  cd MLOPS Project
  uvicorn Notebook2:app --host 127.0.0.1 --port 8000 --reload
  ```
### Notebook 3: User Interface with Streamlit
- **Content:**  
  Contains the Streamlit UI code for collecting user inputs and displaying predictions.
- **Converted to Python File:**  
  The code has been converted to `Notebook3.py`.
- **Run the Streamlit UI:**
  ```bash
  cd MLOPS Project
  streamlit run Notebook3.py
  ```
### Notebook 4: Model Monitoring (Data Drift Detection)
- **Content:**  
  Uses alibi-detect and chi-square tests to monitor numeric and categorical drift.
- **Usage:**  
  Run `Notebook4.ipynb` in your Jupyter environment to view drift detection results in tabular format.

