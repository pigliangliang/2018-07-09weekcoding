#author_by zhuxiaoliang
#2018-07-18 上午9:57

from multiprocessing import Pool
import requests
import json
import os


def get_page(url):
    print('进程%s get %s' %(os.getpid(),url))
    response = requests.get(url)
    if response.status_code ==200:
        return {'url':url,"text":response.text}

if __name__=='__main__':
    urls = [
        'https://www.baidu.com',
        'https://www.python.org',
        'https://www.openstack.org',
        'https://help.github.com/',
        'http://www.sina.com.cn/'
    ]

    p = Pool(5)
    res_l = []
    for url in urls:
        res = p.apply_async(get_page,args=(url,))
        res_l.append(res)
    p.close()
    p.join()
    print(res_l)