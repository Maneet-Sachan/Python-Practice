def tablegenerate(n):
    table="" 
    for i in range (1,11):
        table += f" {n} x {i} = {n*i} \n"
        with open(f"o/table_{n}.txt", "w") as f:
            f.write(table)


for i in range(1,100):

    tablegenerate(i)