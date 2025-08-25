total = 0
for i in range(1000): 
    if i % 3 == 0 or i % 5 == 0: # 3 veya 5'in katıysa
        total += i 

print(total)
