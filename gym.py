while True:
    craft = input().split()
    scor1 = input().split()
    scor2 = input().split()
    scor3 = input().split()
    s1 = [eval(f1) for f1 in scor1]
    s2 = [eval(f2) for f2 in scor2]
    s3 = [eval(f3) for f3 in scor3]
    total = (((s1[0]*2)+(s2[0]*3)+s3[0])-((s1[1]*2)+(s2[1]*3)+s3[1]))
    if total < 0:
        print(craft[1])
    elif total > 0:
        print(craft[0])
    else:
        print("Draw")
    break
        