import requests, json, matplotlib.pyplot as plt
from datetime import date, timedelta

priceList = []
days = []
response = requests.get("https://api.coindesk.com/v1/bpi/historical/close.json").json()

for i in range(1, len(response["bpi"])+1):
    dateInput = (date.today()-timedelta(days=i))
    data = response["bpi"][str(dateInput)]
    priceList.append(data)
    days.append(str(dateInput))

plt.plot(days, priceList)
plt.xticks([days[0], days[7], days[15], days[23], days[30]])
plt.xlabel("Days")
plt.ylabel("Price (USD)")
plt.title("The Price of Bitcoin the past month")
plt.grid(True)
plt.show()
