import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("students.csv")

print("First 5 rows:")
print(df.head())

# Average marks
df['Average'] = (df['Math'] + df['Science'] + df['English']) / 3

print("\nAverage Marks:")
print(df[['Name', 'Average']])

# Top student
top_student = df.sort_values(by='Average', ascending=False).head(1)
print("\nTop Student:")
print(top_student[['Name', 'Average']])

# Plot average marks
sns.barplot(x='Name', y='Average', data=df)
plt.title("Student Performance")
plt.xticks(rotation=45)
plt.show()

# Study hours vs average
sns.scatterplot(x='StudyHours', y='Average', data=df)
plt.title("Study Hours vs Performance")
plt.show()

# Gender comparison
sns.boxplot(x='Gender', y='Average', data=df)
plt.title("Performance by Gender")
plt.show()