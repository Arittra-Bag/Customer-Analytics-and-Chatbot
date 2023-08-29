import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

customer_data = pd.read_csv('/kaggle/input/customer-segmentation/Mall_Customers.csv')

# Calculate the top spenders
top_spenders = customer_data.nlargest(5, 'Spending Score (1-100)')

# Customer Statistics
# 1. Age vs Spending Score (1-100)
age_vs_spending = customer_data.groupby('Age')['Spending Score (1-100)'].mean().reset_index()

# 2. Gender vs Spending Score (1-100)
gender_vs_spending = customer_data.groupby('Gender')['Spending Score (1-100)'].mean().reset_index()

# 3. Age vs Gender
age_vs_gender = customer_data.groupby(['Age', 'Gender']).size().unstack(fill_value=0)

# Display the statistics
print("\nCustomer Statistics:")
print("\n1. Age vs Spending Score (1-100):")
print(age_vs_spending.to_string(index=False))

print("\n2. Gender vs Spending Score (1-100):")
print(gender_vs_spending.to_string(index=False))

print("\n3. Age vs Gender:")
print(age_vs_gender)

# Data Visualizations
# 1. Age vs Spending Score (1-100)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=customer_data, x='Age', y='Spending Score (1-100)', hue='Gender')
plt.title('Age vs Spending Score (1-100)')
plt.xlabel('Age')
plt.ylabel('Spending Score (1-100)')
plt.show()

# 2. Gender vs Spending Score (1-100)
plt.figure(figsize=(6, 4))
sns.barplot(data=gender_vs_spending, x='Gender', y='Spending Score (1-100)')
plt.title('Gender vs Spending Score (1-100)')
plt.xlabel('Gender')
plt.ylabel('Average Spending Score (1-100)')
plt.show()

# 3. Age vs Gender
age_vs_gender.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Age vs Gender')
plt.xlabel('Age')
plt.ylabel('Count')
plt.legend(title='Gender')
plt.show()

# Display Top Spenders
print("\nTop Spenders:")
print(top_spenders.to_string(index=False))