import random as a
num = a.randint(1,10)

ans = input('數字: ')
if ans == '1' or ans == '2':
    ans = int(ans)
    if num == ans:
        print('恭喜答對')
    else:
        
        if ans == '3' or ans == '4':
            ans = int(ans)
            if num == ans:
                print('恭喜答對')
        else:
            if ans == '5' or ans == '6':
                ans = int(ans)
                if num == ans:
                    print('恭喜答對')
            else:
                if ans == '7' or ans == '8':
                    ans = int(ans)
                if num == ans:
                    print('恭喜答對')
                else:
                    if ans == '9' or ans == '10':
                        ans = int(ans)
                    if num == ans:
                        print('恭喜答對')
                    else:
                        print('答錯')
else:
    print('輸入錯誤')