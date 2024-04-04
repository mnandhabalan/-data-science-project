import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the hotel data from Excel file
hotel_data = pd.read_excel("hotel_bookings.xlsx")

# Data Cleaning and Preparation
# Convert arrival_date_month to string
hotel_data['arrival_date_month'] = hotel_data['arrival_date_month'].astype(str)

# Combine year and month for easier analysis
hotel_data['arrival_date'] = pd.to_datetime(hotel_data['arrival_date_year'].astype(str) + '-' + hotel_data['arrival_date_month'])

# Define function to visualize hotel occupancy across months
def plot_hotel_occupancy(data):
    plt.figure(figsize=(12, 6))
    sns.countplot(data=data, x='arrival_date_month', hue='hotel', palette='Set2')
    plt.title('Hotel Occupancy Across Months')
    plt.xlabel('Month')
    plt.ylabel('Number of Bookings')
    plt.xticks(rotation=45)
    plt.legend(title='Hotel')
    plt.tight_layout()
    plt.show()

# Visualize hotel occupancy across months
plot_hotel_occupancy(hotel_data)

# Define function to visualize average daily rate across months
def plot_avg_daily_rate(data):
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=data, x='arrival_date', y='adr', hue='hotel', palette='Set2')
    plt.title('Average Daily Rate Across Months')
    plt.xlabel('Month')
    plt.ylabel('Average Daily Rate')
    plt.xticks(rotation=45)
    plt.legend(title='Hotel')
    plt.tight_layout()
    plt.show()

# Visualize average daily rate across months
plot_avg_daily_rate(hotel_data)

# Define function to visualize hotel cancellations across months
def plot_cancellations(data):
    cancelled_bookings = data[data['is_canceled'] == 1]
    plt.figure(figsize=(12, 6))
    sns.countplot(data=cancelled_bookings, x='arrival_date_month', hue='hotel', palette='Set2')
    plt.title('Hotel Cancellations Across Months')
    plt.xlabel('Month')
    plt.ylabel('Number of Cancellations')
    plt.xticks(rotation=45)
    plt.legend(title='Hotel')
    plt.tight_layout()
    plt.show()

# Visualize hotel cancellations across months
plot_cancellations(hotel_data)
