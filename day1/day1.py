
result0th = []
result1st = []
with open("day1/input.txt", 'r') as file:
    for line in file:
        number1, number2 = line.split()
        result0th.append(int(number1))
        result1st.append(int(number2))

sorted_result0th = sorted(result0th)
sorted_result1st = sorted(result1st)

result = 0
for i in range(len(sorted_result1st)):
    result += abs(sorted_result0th[i] - sorted_result1st[i])

print(result)



