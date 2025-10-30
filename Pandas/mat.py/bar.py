import matplotlib.pyplot as plt


students = ['Rahul', 'Priya', 'Amit', 'Sneha']
marks = [85, 90, 78, 92]


plt.bar(students, marks, color='skyblue')


plt.title("Students Marks Comparison")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()
