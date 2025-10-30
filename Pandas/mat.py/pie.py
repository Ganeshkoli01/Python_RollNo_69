import matplotlib.pyplot as plt


activities = ['Study', 'Sleep', 'Exercise', 'Leisure']
hours = [6, 8, 2, 8]
explode=(0,0,0,0.1)

plt.pie(hours,explode=explode ,labels=activities, autopct='%1.1f%%',shadow=True, startangle=90)


plt.title("Daily Time Distribution")


plt.show()
