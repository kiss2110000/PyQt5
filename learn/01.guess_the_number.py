import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from random import randint


# QWidget小部件是PyQt5中所有用户界面对象的基类。 我们提供了QWidget的默认构造函数。 默认构造函数没有父类。 没有父类口小部件称为窗口。
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.num = randint(1, 100)

    # GUI界面用initUI()函数创建。
    def initUI(self):
        # 设置窗口的大小和位置
        self.setGeometry(300, 300, 300, 200)
        # 设置窗口的标题
        self.setWindowTitle("猜数字")
        # 设置窗口的图标
        self.setWindowIcon(QIcon('icon.png'))

        # 在窗口上添加按钮,设置名称,并指定给了一个属性变量
        self.bt1 = QPushButton('我猜', self)
        # 设置按钮的大小和位置
        self.bt1.setGeometry(115, 150, 70, 30)
        # 设置按钮的提示信息
        self.bt1.setToolTip('<b>点击这里猜数字</b>')
        # 当按钮被单击时，调用showMessage())方法去响应执行
        self.bt1.clicked.connect(self.showMessage)

        # 在窗口上添加一个文本框,设置默认字符,并指定给了一个属性变量
        self.text = QLineEdit('在这里输入数字', self)
        # 设置文本框的大小和位置
        self.text.setGeometry(80, 50, 150, 30)
        # 理解为将“在这里输入数字”进行全选，方便输入数字，否则你还得手动全选删除默认字符
        self.text.selectAll()
        # 就是让光标焦点置于文本栏中，方便用户输入，不然还得手动在文本栏中单击一下，很是麻烦
        self.text.setFocus()

        # show（）方法在屏幕上显示窗口小部件。 一个小部件首先在内存中创建，然后在屏幕上显示。
        self.show()

    def showMessage(self):
        # 获取文本框的内容,并转为证书
        guessnumber = int(self.text.text())

        if guessnumber > self.num:
            QMessageBox.about(self, '看结果', '猜大了')
            self.text.setFocus()
            self.text.selectAll()
        elif guessnumber < self.num:
            QMessageBox.about(self, '看结果', '猜小了')
            self.text.setFocus()
            self.text.selectAll()
        else:
            QMessageBox.about(self, '看结果', '答对了！进入下一轮！')
            self.num = randint(1, 100)
            self.text.setText('在这里输入数字')
            self.text.selectAll()
            self.text.setFocus()


if __name__ == "__main__":
    # QApplication 创建一个应用程序对象。sys.argv从命令行获取的参数列表。
    app = QApplication(sys.argv)
    ex = Example()
    # 如果我们调用exit（）方法或者主窗口小部件被破坏，那么主循环(main loop)就会结束。sys.exit（）方法确保一个干净的退出。
    sys.exit(app.exec_())
