import pandas as pd
import matplotlib.pyplot as plt

# 1. Load CSV into DataFrame
df = pd.read_csv("weather.csv")
print(df)

# 2. Average, maximum, minimum temperature
print("Average Temperature:", round(df["Temperature"].mean(), 2))
print("Maximum Temperature:", df["Temperature"].max())
print("Minimum Temperature:", df["Temperature"].min())

# 3. Day with highest temperature
hottest = df.loc[df["Temperature"].idxmax()]
print("Hottest Day:", hottest["Date"])

# 4. Line chart
plt.plot(df["Date"], df["Temperature"], marker="o")
plt.title("Daily Temperature Changes")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 5. Histogram
plt.hist(df["Temperature"], bins=5, edgecolor="black")
plt.title("Temperature Distribution")
plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.show()

# 6. Scatter plot
plt.scatter(df["Humidity"], df["Temperature"])
plt.title("Humidity vs Temperature")
plt.xlabel("Humidity")
plt.ylabel("Temperature")
plt.show()