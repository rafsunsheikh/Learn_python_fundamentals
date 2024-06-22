list1 = ["I am", "YOu are"]
list2 = ["healthy", "fine", "good"]

list2_size = len(list2)

for item in list1:
    print("This is the first outer loop")

    i = 0

    while i < list2_size:
        print(item, list2[i])

        i = i + 1
    print("End for loop")