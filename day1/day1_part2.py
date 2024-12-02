from collections import defaultdict

result0th = []
result1st = []
with open("input.txt", 'r') as file:
    for line in file:
        number1, number2 = line.split()
        result0th.append(int(number1))
        result1st.append(int(number2))

right_number_count = defaultdict(int)
for num in result1st:
    right_number_count[num] += 1

result = 0
for num in result0th:
    result += num * right_number_count[num]

print(result)

# 18567089