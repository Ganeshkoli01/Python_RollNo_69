import numpy as np

# 1️ Create an array
arr1 = np.array([1, 2, 3, 4])
print("1️ np.array() ->", arr1)

# 2️ Array of zeros
arr2 = np.zeros((2, 3))
print("\n2️ np.zeros():\n", arr2)

# 3️ Array of ones
arr3 = np.ones((3, 2))
print("\n3️ np.ones():\n", arr3)

# 4️ Create a range of numbers
arr4 = np.arange(0, 10, 2)
print("\n4️ np.arange() ->", arr4)

# 5️ Evenly spaced numbers
arr5 = np.linspace(0, 1, 5)
print("\n5️ np.linspace() ->", arr5)

# 6️ Reshape an array
arr6 = np.arange(6)
reshaped = arr6.reshape(2, 3)
print("\n6️ np.reshape():\n", reshaped)

# 7️ Sum of elements
arr7 = np.array([1, 2, 3, 4])
print("\n7️ np.sum() ->", np.sum(arr7))

# 8️ Mean (average)
arr8 = np.array([10, 20, 30])
print("\n8 np.mean() ->", np.mean(arr8))

# 9️ Max and Min values
arr9 = np.array([5, 8, 2, 9])
print("\n9️ np.max() ->", np.max(arr9))
print("   np.min() ->", np.min(arr9))

#  Random numbers
arr10 = np.random.rand(2, 3)
print("\ np.random.rand():\n", arr10)
