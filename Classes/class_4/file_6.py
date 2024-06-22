for i in range(2,6):
    for j in range(1,11):
        if i == j:
            break
        print(f'{i} * {j} = {i*j}')