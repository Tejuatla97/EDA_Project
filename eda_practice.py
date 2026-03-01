import pandas as pd
import numpy as np

# Create sample data
data = {
    "Name": ["Teju", "Rahul", "Anu", "Kiran"],
    "Age": [22, 25, 23, 24],
    "Salary": [30000, 40000, 35000, 45000]
}

df = pd.DataFrame(data)

print("Dataset:\n")
print(df)

print("\nAverage Salary:", df["Salary"].mean())