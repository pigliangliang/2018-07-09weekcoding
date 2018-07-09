#author_by zhuxiaoliang
#2018-07-09 下午3:32

with open('readme','r') as f :
    for line in f.read():
        print(line)
        print(type(line))
    #for line in f.read():
    #    print(line)
    #for line in f.readlines():
     #   print(line)
#

'''
总结f.read():整个文件读取，包括空格和标点，类型为str，循环输出的话是一个一个字符串形式
    f.readline():只读取首行，类型为str
    f.readlines():读取整个文件，类型为列表。循环输出每一行。
'''