import turtle as t

t.shape('turtle')
t.penup()
size = 20
for i in range(30):
    t.stamp()
    size = size + 3
    t.forward(size)
    t.right(24)
t.done()