import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create data dictionary
data = {
    'Name': ['Amit', 'pooja', 'sagar'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82],
}

# Create DataFrame
df = pd.DataFrame(data)

# Min-Max scaling for 'Math' column
math_min = df['Math'].min()
math_max = df['Math'].max()
df['Math_Normalized'] = (df['Math'] - math_min) / (math_max - math_min)

# Correct gender assignment
df['Gender'] = ['Male', 'Female', 'Male']

# One-hot encoding
df_encoded = pd.get_dummies(df, columns=['Gender'], prefix='Gender')
print(df_encoded)

# Group by gender and calculate average marks
gender_avg = df.groupby('Gender')[['Math', 'Science', 'English']].mean()
print("\nAverage Marks by Gender:\n", gender_avg)

# Compute total and status
df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)
df['Status'] = df['Total'].apply(lambda x: 'Pass' if x >= 250 else 'Fail')
print("\nStudent Status:\n", df[['Name', 'Total', 'Status']])

# Plot pie chart for Sagar
sagar_data = df[df['Name'].str.lower() == 'sagar'][['Math', 'Science', 'English']].iloc[0]
plt.figure(figsize=(6, 6))
colors = ['#66b3ff', '#99ff99', '#ffcc99']
plt.pie(sagar_data, labels=sagar_data.index, autopct='%1.1f%%', startangle=90, colors=colors)
plt.title("Sagar's Marks Distribution")
plt.axis('equal')
plt.show()