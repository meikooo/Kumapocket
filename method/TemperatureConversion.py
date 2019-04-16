def c2f(cel):
    fah = cel*1.8 +32
    return fah
def f2f(fah):
    cel=(fah-32)/1.8
    return cel

def test():
    print('test,0摄氏度=%.2f华氏度'%c2f(0))
    print('test,0华氏度=%.2f摄氏度'%c2f(0))


#采用下面方法，其它模块引用该方法时calc.py ，会将测试内容也打印了出来
#是Python不知道该该模块是以程序运行还是导入到其它程序中运行导致的
#运行TemperatureConversion.py时，是作为主程序，所以会将测试代码打印出阿里
# test()

#采用下面方法，其它模块引用该方法时 ，不会将测试内容也打印了出来
if __name__=='__main__':
    test()