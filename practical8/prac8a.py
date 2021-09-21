'''Open a new file in IDLE (“New Window” in the “File” menu) and save it as
geometry.py in the directory where you keep the files you create for this course.
Then copy the functions you wrote for calculating volumes and areas in the
“Control Flow and Functions” exercise into this file and save it. Try and add print dir(geometry) to the file and run it.
'''

import geometry

def pointyShapeVolume(x, h, squareBase):
    if squareBase:
        base = geometry.squareArea(x)
        return ((1/3) * base * h)
    else:
        base = geometry.circleArea(x)
        return (h * (base / 3.0))
print (dir(geometry))
print (pointyShapeVolume(4, 2.6, True))
print (pointyShapeVolume(4, 2.6, False))
