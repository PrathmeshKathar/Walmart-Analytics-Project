import joblib
import pandas as pd


model = joblib.load(r"C:\Users\Laptop\Desktop\walmart_data_anlytic project\scripts\scripts\xgb_sales_model.pkl")


sample_data = pd.DataFrame([{
    'Branch': 'WALM003',
    'City': 'San Antonio',
    'category': 'Health and beauty',
    'unit_price': 70.0,
    'quantity': 8,
    'rating': 9.0,
    'day': 5,
    'month': 1,
    'hour': 13
}])

prediction = model.predict(sample_data)
print(f" Predicted Total Sales: {prediction[0]:.2f}")
