# 🧠 Employee Salary Prediction

This project uses a **Linear Regression** model to predict an employee's salary based on features such as job type, education level, major, industry, years of experience, and distance from a metropolis. It includes a **Streamlit** web app for user interaction and real-time predictions.

---

## 📂 Project Structure

├── Employees.xlsx # Dataset

├── Salary Prediction.ipynb # Main Jupyter notebook

├── Linearmodel.pkl # Saved trained model

├── App.py / streamlit_app.py # Streamlit web app

├── App Demo.webm # App Demo 

├── PPT for Employees Salary Prediction.pptx # PPT

└── README.md # Project description


---

## 🧾 Problem Statement

Companies often want to estimate employee salaries based on various attributes. This project aims to build a machine learning model that accurately predicts salaries using structured employee data. The application provides predictions through a simple user interface.

---

## 📊 Dataset

- **Source:** [Kaggle – Company Employees Dataset](https://www.kaggle.com/datasets/abdallahwagih/company-employees)
- **Features:**
  - `jobType`
  - `degree`
  - `major`
  - `industry`
  - `yearsExperience`
  - `milesFromMetropolis`
  - `salary` (Target variable)

---

## 🧪 Tech Stack

- **Language:** Python
- **Libraries:** 
  - pandas, numpy
  - scikit-learn
  - joblib
  - Streamlit (for UI)
- **Model Used:** Linear Regression

---

## ⚙️ How It Works

1. Load and clean the dataset.
2. Encode categorical features using LabelEncoder.
3. Train a Linear Regression model.
4. Evaluate performance (visual inspection, regression line).
5. Save model using `joblib`.
6. Predict salary using Streamlit UI based on user input.

---

## 🚀 Run the Project Locally
streamlit run App.py

---

# Results
Basic linear model captures salary trends relative to experience.

Streamlit app provides instant predictions.

Ideal for quick demonstrations or baseline salary estimations.

---

# Future Enhancements

Use advanced regression techniques (Random Forest, XGBoost).

Improve model evaluation with R², MAE, RMSE.

Deploy on cloud platforms (Render, Heroku, AWS).

Add more interactive UI elements and input validations.

---

# References

Scikit-learn Documentation: 
https://scikit-learn.org/stable/documentation.html

Streamlit Documentation: 
https://docs.streamlit.io/

Kaggle Dataset: 
https://www.kaggle.com/datasets/abdallahwagih/company-employees/data

---

# Author
Dharma Devi K
