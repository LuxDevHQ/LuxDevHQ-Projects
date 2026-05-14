### **Developer Salary Prediction (Stack Overflow Dataset)**

In this project, you will build a machine learning model that predicts a software developer’s salary based on real-world survey data from Stack Overflow. 
You will learn how to clean messy data, build a scikit-learn pipeline, train an XGBoost model, and optionally deploy your solution as a web app.

### **Dataset.**

Use the Stack Overflow Annual Developer Survey dataset: https://survey.stackoverflow.co

The dataset is large, real-world, and messy—expect missing values and inconsistent responses.

### Project Requirements

You must complete the project in the following structured steps:

---

### STEP 1: Setup Project Structure

Create a clean project folder with the following structure:

- data/ (raw and processed data)  
- notebooks/ (EDA and experimentation)  
- src/ (all Python scripts)  
- models/ (saved trained model)  
- app/ (Streamlit app)  
- requirements.txt  
- README.md  

---

### STEP 2: Load and Understand the Data

- Load the dataset using pandas  
- Explore columns and identify the target variable  
- Understand missing values and data types  

---

### STEP 3: Define Target Variable

- Select `ConvertedCompYearly` as your target (salary)  
- Remove rows with missing salary values  

---

### STEP 4: Feature Selection

Select meaningful features such as:

- Country  
- Years of professional coding experience  
- Education level  
- Employment type  
- Programming languages used  

---

### STEP 5: Data Cleaning

- Handle missing values (numeric and categorical)  
- Standardize inconsistent responses where needed  

---

### STEP 6: Build a Preprocessing Pipeline

Use scikit-learn to:

- Impute missing values  
- Encode categorical variables (OneHotEncoding)  
- Prepare a reusable preprocessing pipeline  

---

### STEP 7: Train Machine Learning Model

- Split data into training and testing sets  
- Train an XGBoost regression model  
- Use a scikit-learn Pipeline to combine preprocessing + model  

---

### STEP 8: Model Evaluation

- Evaluate model using MAE (Mean Absolute Error)  
- Interpret performance and write observations  

---

### STEP 9: Save the Model

- Save your trained pipeline using `joblib` or `pickle`  
- Store it inside the `models/` folder  

---

### STEP 10 (Optional but Recommended): Build a Streamlit App

Create a simple web app where users can:
- Input their profile (country, experience, education, etc.)  
- Get predicted salary instantly  

---

### 📊 Deliverables

You must submit:

- Clean GitHub repository  
- Trained model file  
- Python scripts (not only notebooks)  
- README with explanation  
- (Bonus) Streamlit deployed app  

---

### ⭐ Evaluation Criteria

Your project will be graded based on:

- Code structure and organization  
- Data preprocessing quality  
- Model performance  
- Use of pipelines (very important)  
- Clarity of README  
- (Bonus) Deployment  

---

### 🚀 Goal of This Project

By the end, you should be able to:

- Handle real-world messy datasets  
- Build an end-to-end ML pipeline  
- Train and evaluate regression models  
- Deploy a working ML application  
