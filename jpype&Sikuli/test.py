# _*_ coding:utf-8  _*_
import jpype
jvmPath = jpype.getDefaultJVMPath()  # 默认的JVM路径
print(jvmPath)
jpype.startJVM(jvmPath)
jpype.java.lang.System.out.println("hello jpype!")
jpype.shutdownJVM()