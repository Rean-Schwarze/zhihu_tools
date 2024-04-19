# 此文件用来获取命令行参数的信息或者菜单选项的信息
import sys

class option:
    def __init__(self):
        self.type = ""

    def menu(self) -> None:
        print("1. Question 链接")
        print("2. Market   链接")
        print("3.          退出")
    # 获取命令行参数
    def getCommand(self) -> str:
        if len(sys.argv) == 2:
            return sys.argv[1]
        if (len(sys.argv) > 2):
            print("正确的命令行参数为: python3 main.py [链接]")
            return "None"
    # 获取选项
    def getOption(self) -> None:
        while(1):
            self.type = input("请输入选项: ")
            if(self.type == "1" or self.type == "2" or self.type == "3"):
                break
            else:
                print("输入错误, 请重新输入")

    def main(self) -> str:

        if self.getCommand() == "None":
            return None

        if(self.getCommand() == None):
            self.menu()
            self.getOption()
        return self.type
