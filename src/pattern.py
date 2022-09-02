
# Print the pattern
stars_list = []
for i in range(5):
    stars_list.append("*")
    print(*stars_list ,sep=" ", end="\n")
for j in range(4):
    stars_list.pop(-1)
    print(*stars_list ,sep=" ", end="\n")