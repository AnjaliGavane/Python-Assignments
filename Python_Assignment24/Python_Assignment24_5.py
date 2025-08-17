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

# Fill NaN values with mean of respective columns
df.fillna(df.mean(numeric_only=True), inplace=True)

# Print updated DataFrame
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

# Get Sagar's row
sagar_data = df[df['Name'].str.lower() == 'sagar'][['Math', 'Science', 'English']].iloc[0]


# Plot pie chart
plt.figure(figsize=(6, 6))
plt.pie(sagar_data, labels=sagar_data.index, autopct='%1.1f%%', startangle=90, colors=['#66b3ff','#99ff99','#ffcc99'])
plt.title("Sagar's Marks Distribution")
plt.axis('equal')  # Equal aspect ratio ensures the pie is circular.
plt.show()

# Calculate total marks across subjects
df['Total'] = df['Math'] + df['Science'] + df['English']

# Assign pass/fail based on total
df['Status'] = df['Total'].apply(lambda x: 'Pass' if x >= 250 else 'Fail')

print(df[['Name', 'Math', 'Science','English' ,'Total', 'Status']])