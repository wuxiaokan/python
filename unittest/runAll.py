# coding=utf-8
from testcase import *
from unittest import TestSuite, makeSuite  # 到入unittest框架中的TestSuite, makeSuite
from HTMLTestRunner import *  # 需要将HTMLTestRunner文件放到C: Python27\Lib目录下

T = TestSuite()  # 将测试用例集TestSuite()赋给对象T
T.addTest(makeSuite(Login))  # Login是在case中封装的类名
# T.addTest(Login('test1'))
# T.addTest(Login('test2'))
# T.addTest(Login('test3'))
# T.addTest(Login('test4'))

# file()是生成文件函数，./代表生成文件存放到当前路径，w代表写的权限，b代表覆盖权限
fp = file('./result.html', 'wb')
fb = HTMLTestRunner(fp, title=u'自动化测试报告', description=u'测试用例结果')
fb.run(T)
fp.close()
