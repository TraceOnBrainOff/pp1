done = False #crazy
i = 0
while not done:
    if i%7==0:
        if i%2==1 and i%3==1 and i%4==1 and i%5==1 and i%6==1:
            print(i)
            done = True
    i +=1