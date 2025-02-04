import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

days_df = pd.read_csv('dataset/day.csv')
hours_df = pd.read_csv('dataset/hour.csv')

days_df.loc[:, 'season_group'] = days_df['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
days_df.loc[:, 'holiday_group'] = days_df['holiday'].map({0: 'Non-Holiday', 1: 'Holiday'})
days_df.loc[:, 'workingday_group'] = days_df['workingday'].map({0: 'Non-Working Day', 1: 'Working Day'})
days_df.loc[:, 'weathersit_group'] = days_df['weathersit'].map({
    1: 'Clear',
    2: 'Mist',
    3: 'Light Rain',
})

hours_df.loc[:, 'season_group'] = hours_df['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
hours_df.loc[:, 'holiday_group'] = hours_df['holiday'].map({0: 'Non-Holiday', 1: 'Holiday'})
hours_df.loc[:, 'workingday_group'] = hours_df['workingday'].map({0: 'Non-Working Day', 1: 'Working Day'})
hours_df.loc[:, 'weathersit_group'] = hours_df['weathersit'].map({
    1: 'Clear',
    2: 'Mist',
    3: 'Light Rain',
    4: 'Heavy Rain'
})

# Set page title and layout
st.set_page_config(page_title="Bike Rental Analysis Dashboard", layout="wide")

st.title("Bike Rental Analysis Dashboard")
st.markdown("Explore the impact of weather conditions on daily bike rentals.")

st.header("Impact of Weather Conditions on Daily Bike Rentals")

# Boxplot for distribution of rentals per weather condition
fig, ax = plt.subplots(figsize=(8, 6))
sns.boxplot(x='weathersit_group', y='cnt', data=days_df, ax=ax)
ax.set_title('Distribution of Bike Rentals per Weather Condition')
ax.set_xlabel('Weather Condition')
ax.set_ylabel('Number of Rentals')
st.pyplot(fig)

# Correlation heatmap
correlation_matrix = days_df[['temp', 'atemp', 'hum', 'windspeed', 'cnt']].corr()
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
ax.set_title('Correlation between Weather Variables and Number of Rentals')
st.pyplot(fig)

st.header("Characteristics of High-Rental Days")

# Define high rental threshold
high_rental_threshold = days_df['cnt'].quantile(0.9)
high_rental_days = days_df[days_df['cnt'] > high_rental_threshold]

# Boxplots for characteristics of high-rental days
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
sns.boxplot(x='season_group', y='cnt', data=high_rental_days, ax=axes[0, 0])
axes[0, 0].set_title('Distribution of Rentals per Season')
sns.boxplot(x='holiday_group', y='cnt', data=high_rental_days, ax=axes[0, 1])
axes[0, 1].set_title('Distribution of Rentals on Holidays vs Non-Holidays')
sns.boxplot(x='workingday_group', y='cnt', data=high_rental_days, ax=axes[1, 0])
axes[1, 0].set_title('Distribution of Rentals on Working Days vs Non-Working Days')
sns.boxplot(x='weathersit_group', y='cnt', data=high_rental_days, ax=axes[1, 1])
axes[1, 1].set_title('Distribution of Rentals per Weather Condition')
plt.tight_layout()
st.pyplot(fig)

st.header("Rental Patterns Within High-Rental Days")

# Filter hours_df for high-rental days
high_rental_dates = high_rental_days['dteday'].unique()
high_rental_hours = hours_df[hours_df['dteday'].isin(high_rental_dates)]

# Line plot for rental patterns within high-rental days
hourly_rental_avg = high_rental_hours.groupby('hr')['cnt'].mean()
fig, ax = plt.subplots(figsize=(10, 5))
hourly_rental_avg.plot(kind='line', marker='o', ax=ax)
ax.set_title('Rental Patterns Within High-Rental Days')
ax.set_xlabel('Hour')
ax.set_ylabel('Average Number of Rentals')
ax.set_xticks(range(24))
ax.grid(True)
st.pyplot(fig)

# Add interactive elements
weather_condition = st.selectbox("Select Weather Condition", days_df['weathersit_group'].unique())
filtered_days = days_df[days_df['weathersit_group'] == weather_condition]
fig, ax = plt.subplots(figsize=(8, 6))
sns.boxplot(x='weathersit_group', y='cnt', data=filtered_days, ax=ax)
ax.set_title(f'Distribution of Bike Rentals for Weather Condition {weather_condition}')
ax.set_xlabel('Weather Condition')
ax.set_ylabel('Number of Rentals')
st.pyplot(fig)