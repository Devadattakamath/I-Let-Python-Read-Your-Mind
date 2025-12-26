import turtle,random
t=turtle.Turtle();t.speed(0)
p=[random.random()*360 for _ in range(200)]
while 1:
    t.clear()
    [t.goto(200*__import__("math").cos(a),200*__import__("math").sin(a)) or t.dot(3) for a in p]
    p=[a+random.uniform(-0.05,0.05) for a in p]

