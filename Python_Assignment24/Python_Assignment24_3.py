import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create data dictionary
data = {
        'Name':['Amit','pooja','sagar'],
        'Math':[85,90,78],
        'Science':[92,88,80],
        'English':[75,85,82],

    } 

# Create DataFrame
df = pd.DataFrame(data)

# Print original DataFrame
print(df)

# Min-Max scaling for 'Math' column
math_min = df['Math'].min()
math_max = df['Math'].max()

df['Math_Normalized'] = (df['Math'] - math_min) / (math_max - math_min)

print(df)

df['Gender'] = ['Male', 'Male', 'Female']

# Perform one-hot encoding
df_encoded = pd.get_dummies(df, columns=['Gender'], prefix='Gender')

print(df_encoded)

# Group by gender and calculate average marks
gender_avg = df.groupby('Gender')[['Math', 'Science','English']].mean()

print(gender_avg)