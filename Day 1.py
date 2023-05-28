import py5

x = 500
y = 500

def setup():
    py5.size(x,y)


def draw():
    #dark blue background
    py5.background('#004477')
    py5.no_stroke()
    py5.fill('#ff0000') # red 
    py5.arc(250, 250, 350, 350, py5.PI, py5.TWO_PI)

    py5.fill('#ff9900') # orange 
    py5.arc(250, 250, 300, 300, py5.PI, py5.TWO_PI)

    py5.fill('#ffff00') # yellow
    py5.arc(250, 250, 300-50, 300-50, py5.PI, py5.TWO_PI)

    py5.fill('#00ff00') # green
    py5.arc(250, 250, 300-100, 300-100, py5.PI, py5.TWO_PI)

    py5.fill('#0099ff') # blue
    py5.arc(250, 250, 300-150, 300-150, py5.PI, py5.TWO_PI)

    py5.fill('#6633ff') # purple
    py5.arc(250, 250, 300-200, 300-200, py5.PI, py5.TWO_PI)

    py5.fill('#004477')
    py5.arc(250, 250, 300-250, 300-250, py5.PI, py5.TWO_PI)

py5.run_sketch()


