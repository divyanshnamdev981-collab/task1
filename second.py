# Set seaborn style
sns.set(style='whitegrid')

# Plot temperature trend
plt.figure(figsize=(12, 6))
sns.lineplot(x='datetime', y='temperature', data=df, marker='o', color='tomato')
plt.title(f"Temperature Forecast for {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot humidity trend
plt.figure(figsize=(12, 6))
sns.lineplot(x='datetime', y='humidity', data=df, marker='o', color='royalblue')
plt.title(f"Humidity Forecast for {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
