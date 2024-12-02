result = 0
with open("day2_input.txt", 'r') as file:
    for line in file:
        line_list = line.split()
        prev = int(line_list[0])
        safe = True
        increasing = False
        if int(line_list[1]) > int(line_list[0]):
            increasing = True
        for index in range(1, len(line_list)):
            diff = None
            if increasing:
                diff = int(line_list[index]) - prev
            else:
                diff = prev - int(line_list[index])
            if 1 > diff or diff > 3:
                print(f"{line_list} is invalid")
                safe = False
                prev = int(line_list[index])
                break
            prev = int(line_list[index])
        if safe:
            print(f"{line_list} is valid")
            result += 1

print(result)

# 383

