import pandas as pd
from sklearn.linear_model import LinearRegression
import kagglehub
import os

# Download dataset
path = kagglehub.dataset_download("shree1992/housedata")

# Check files
print("Files:", os.listdir(path))

# Load dataset
df = pd.read_csv(os.path.join(path, "data.csv"))

# Check columns
print("Columns:", df.columns)

# Select correct features
X = df[["sqft_living", "bedrooms"]]
y = df["price"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Take user input
area = float(input("Enter the area in sq ft: "))
bedrooms = int(input("Enter the number of bedrooms: "))

# Predict
predicted_price = model.predict([[area, bedrooms]])

print(f"Predicted house price: ${predicted_price[0]:,.2f}")