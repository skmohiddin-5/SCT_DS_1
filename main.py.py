import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_127039.csv", skiprows=4)

countries = ["India", "United States", "China", "Japan", "Brazil"]

latest_year = "2022"


filtered_df = df[df["Country Name"].isin(countries)]


populations = filtered_df[latest_year]

plt.figure(figsize=(10,6))

plt.bar(filtered_df["Country Name"], populations)

plt.xlabel("Countries")
plt.ylabel("Population")
plt.title("Population Distribution (2022)")


plt.show()