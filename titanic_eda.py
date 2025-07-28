import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Titanic dataset
df = sns.load_dataset('titanic')

# Set style
sns.set(style="whitegrid")

# 1. Bar Plot - Survival Count
plt.figure(figsize=(6, 4))
sns.countplot(x='survived', data=df, palette=['#FF6F61', '#6B5B95'])  # Coral & Indigo
plt.title('Survival Count (0 = No, 1 = Yes)')
plt.xlabel('Survived')
plt.ylabel('Number of Passengers')
plt.show()

# 2. Count Plot - Survival by Gender
plt.figure(figsize=(6, 4))
sns.countplot(x='sex', hue='survived', data=df, palette=['#F7CAC9', '#92A8D1'])  # Pink & Soft Blue
plt.title('Survival by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.legend(title='Survived', labels=['No', 'Yes'])
plt.show()

# 3. Bar Plot - Survival by Passenger Class
plt.figure(figsize=(6, 4))
sns.countplot(x='pclass', hue='survived', data=df, palette=['#88B04B', '#F28C28'])  # Green & Orange
plt.title('Survival by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Count')
plt.legend(title='Survived', labels=['No', 'Yes'])
plt.show()

# 4. Box Plot - Age Distribution by Survival
plt.figure(figsize=(6, 4))
sns.boxplot(x='survived', y='age', data=df, palette=['#00CED1', '#9370DB'])  # Turquoise & Purple
plt.title('Age Distribution by Survival')
plt.xlabel('Survived')
plt.ylabel('Age')
plt.show()

# 5. Violin Plot - Age vs. Class and Survival
plt.figure(figsize=(8, 5))
sns.violinplot(x='pclass', y='age', hue='survived', data=df, split=True, palette=['#FFB347', '#779ECB'])  # Orange & Blue
plt.title('Age vs Class by Survival')
plt.xlabel('Passenger Class')
plt.ylabel('Age')
plt.show()
