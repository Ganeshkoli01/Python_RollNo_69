import array


arr_i = array.array('i', [10, -20, 30])
print("Signed int (i):", arr_i)


arr_I = array.array('I', [10, 20, 30])
print("Unsigned int (I):", arr_I)


arr_b = array.array('b', [1, -2, 100])
print("Signed char (b):", arr_b)


arr_B = array.array('B', [10, 200, 255])
print("Unsigned char (B):", arr_B)


arr_d = array.array('d', [1.1, 2.2, 3.3])
print("Double (d):", arr_d)




arr_u = array.array('u', ['A', 'B', 'C', 'g', 'h'])
print("Unicode char (u):", arr_u)


print("First element:", arr_u[0])   
print("Last element:", arr_u[-1])  


arr_u.append('Z')
print("After append:", arr_u)

