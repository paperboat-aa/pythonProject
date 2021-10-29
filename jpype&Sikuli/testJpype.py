# *encoding=utf-8
import jpype
from jpype import JClass
from jpype._core import isJVMStarted, startJVM
from jpype._jvmfinder import getDefaultJVMPath


def pjava():
    print(getDefaultJVMPath())  # 这个是java的默认路径
    # 启动虚拟机
    if not isJVMStarted():  # 判断java虚拟机是否启动
        startJVM(getDefaultJVMPath())  # 启动java
    pp = 'hello world'
    # 调用java的类代码
    keystore = JClass('java.lang.System')  # 调用java.System这个类
    keystore.out.println(pp)  # 执行输出
    jpype.ShutdownJVM()  # 关闭虚拟机


if __name__ == "__main__":
    pjava()
