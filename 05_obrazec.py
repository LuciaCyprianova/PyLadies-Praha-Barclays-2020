def obrazec():
    for i in range(6):
        if i == 0 or i ==5:
            for j in range(6):
                print("X", end=" ")
            print()
        else:
            for j in range(6):
                if j == 0 or j == 5:
                    print("X", end=" ")
                else:
                    print(" ", end=" ")
            print()  
obrazec()