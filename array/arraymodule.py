import array

# 1. 'i' → signed int (can be negative)
arr_i = array.array('i', [10, -20, 30])
print("Signed int (i):", arr_i)

# 2. 'I' → unsigned int (only positive numbers)
arr_I = array.array('I', [10, 20, 30])
print("Unsigned int (I):", arr_I)

# 3. 'b' → signed char (-128 to 127)
arr_b = array.array('b', [1, -2, 100])
print("Signed char (b):", arr_b)

# 4. 'B' → unsigned char (0 to 255)
arr_B = array.array('B', [10, 200, 255])
print("Unsigned char (B):", arr_B)

# 5. 'd' → double (floating numbers)
arr_d = array.array('d', [1.1, 2.2, 3.3])
print("Double (d):", arr_d)



# 'u' → Unicode characters
arr_u = array.array('u', ['A', 'B', 'C', 'g', 'h'])
print("Unicode char (u):", arr_u)

# Accessing elements
print("First element:", arr_u[0])   
print("Last element:", arr_u[-1])  

# Appending a new character
arr_u.append('Z')
print("After append:", arr_u)

