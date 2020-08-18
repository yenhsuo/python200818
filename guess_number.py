import random as a
num = a.randint(1,20)
i = 0
while i <= 5:
    i = i + 1
    ans = int(input('數字: '))
    if ans > num:
        print('太大')
    elif ans < num:
        print('太小')
    elif ans == num:
        print('答對了','總共猜了',i,'次')
        a = 0
        break
if i > 5:
    print('已結束')