import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = {
    "area": [1000, 1500, 2000, 2500, 3000],
    "bedrooms": [2, 3, 4, 4, 5],
    "price":[200000, 300000, 400000, 500000, 600000]
}
df = pd.DataFrame(data)
 #print(df)
X = df[["area","bedrooms"]]
y = df["price"]

model = LinearRegression()
model.fit(X, y)
area = float(input("Enter the area in sq ft: "))
bedrooms = int(input("Enter the number of bedrooms: "))
predicted_price = model.predict([[area, bedrooms]])

print(f"Predicted  house price: ${predicted_price[0]:,.2f}")


