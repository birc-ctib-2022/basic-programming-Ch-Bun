
# Print the numbers described in the exercise

case_numbers = []
for i in range(10):
    case_numbers.append(int(i+1))
    print(*case_numbers ,sep=" ", end="\n")