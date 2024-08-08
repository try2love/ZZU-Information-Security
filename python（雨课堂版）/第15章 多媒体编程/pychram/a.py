import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


# 使用OpenGL创建窗口类，重写构造函数，初始化OpenGL环境，指定显示模式以及用于绘图的函数。
class MyPyOpenGLTest:
    def __init__(self, width=640, height=480, title=b'MyPyOpenGLTest'):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(width, height)
        self.window = glutCreateWindow(title)
        glutDisplayFunc(self.Draw)
        glutIdleFunc(self.Draw)
        self.InitGL(width, height)

    # 根据特定的需要，进一步完成OpenGL的初始化。
    def InitGL(self, width, height):
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        glShadeModel(GL_SMOOTH)
        glEnable(GL_POINT_SMOOTH)
        glEnable(GL_LINE_SMOOTH)
        glEnable(GL_POLYGON_SMOOTH)
        glMatrixMode(GL_PROJECTION)
        glHint(GL_POINT_SMOOTH_HINT, GL_NICEST)
        glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)
        glHint(GL_POLYGON_SMOOTH_HINT, GL_FASTEST)
        glLoadIdentity()
        gluPerspective(45.0, float(width) / float(height), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

    # 定义自己的绘图函数
    def Draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glutSwapBuffers()

    # 消息主循环
    def MainLoop(self):
        glutMainLoop()


# 实例化窗口类，运行程序
if __name__ == '__main__':
    w = MyPyOpenGLTest()
    w.MainLoop()
