import turtle as t
a = int(input('邊數: '))
b = a - 2
b = b * 180
b = b / a
for i in range(a):
    t.forward(30)
    t.right(180 - b)