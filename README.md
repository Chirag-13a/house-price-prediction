# 🏠 House Price Prediction – Beginner AI Project

## 📌 Project Overview

This is a **simple AI / Machine Learning project** created to understand the **basic concept of how an AI model is built and trained**.
The goal of this project is to predict the **price of a house** based on two inputs:

* **Area of the house (in square feet)**
* **Number of bedrooms**

The program takes these inputs from the user and predicts the **estimated house price** using a trained machine learning model.

This project was built as a **learning exercise to understand the initial stages of AI development**, including dataset usage, model training, and prediction.

---

## 🎯 Objective

The main objective of this project is to learn:

* How AI/ML models are created
* How training data is used to teach a model
* How a model learns patterns from data
* How predictions are made based on user input

---

## ⚙️ How the Project Works

1. A small dataset containing **house area, number of bedrooms, and price** is used.
2. The model is trained using **Linear Regression**.
3. During training, the algorithm learns the relationship between:

   * Area
   * Number of bedrooms
   * House price
4. After training, the model can **predict the price of a new house**.

---

## 🧠 AI Model Used

The project uses a **Linear Regression Model**, which is one of the simplest machine learning algorithms used for **prediction problems**.

The model learns a mathematical relationship between inputs and output:

```
Price = m1 × Area + m2 × Bedrooms + b
```

Where:

* **Area** → Size of the house (sq ft)
* **Bedrooms** → Number of bedrooms
* **Price** → Predicted house price
* **m1, m2, b** → Values learned during training

---

## 📥 User Input

When the program runs, it asks the user for:

1. **Area of the house (in square feet)**
2. **Number of bedrooms**

Example:

```
Enter area of the house (sq ft): 2000
Enter number of bedrooms: 3
```

---

## 📤 Output

The trained AI model predicts the price of the house.

Example output:

```
Estimated House Price: $320000
```

---

## 🛠️ Technologies Used

* **Python**
* **Scikit-learn**
* **NumPy**
* **Pandas**

---

## 📂 Project Structure

```
house-price-prediction
│
├── model.py
└── README.md
```

---

## 🚀 What I Learned

While building this project, I learned:

* Basics of **Machine Learning**
* How **Linear Regression works**
* How to **train a model using model.fit()**
* How to **make predictions using model.predict()**
* How AI models learn from data

This project helped me understand the **fundamental workflow of AI development**.

---

## 📈 Future Improvements

Possible improvements for this project:

* Add more features (location, bathrooms, floors)
* Use a **larger dataset**
* Build a **web interface**
* Add **data visualization**
* Use advanced ML algorithms

---

## 👨‍💻 Author

**Chirag Agarwal**

This project was created as a **beginner AI learning project** to understand how machine learning models are built and trained.
