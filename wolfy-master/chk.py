from maps import translate

for j in range(31):
    if j in range(11):
        k = translate(j, 0, 10, 0, 180)
        print(k)
        print("loop1")
    elif j in range(11,21):
        k = translate(j, 11, 21, 0, 180)
        print(k)
        print("loop2")

    elif j in range(21,31):
        k = translate(j, 21, 31, 0, 180)
        print(k)
        print("loop3")