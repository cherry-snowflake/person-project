import requests
import re

# 1.起始目标
def get_data():
    url = 'https://book.douban.com/top250'
    # 构造身份信息（伪装）
    header = {
       'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
    }
    response = requests.get(url,headers=header)
    if response.status_code == 200:
        return response.text
    else:
        print('请求失败',response.status_code)  # 查看状态码

# 2.解析数据
def parse_data(data):
    z = '<tr\sclass="item">.*?<img\ssrc="(.*?)"\swidth=".*?">'
    # '.*?<a\shref="(.*?)"\sonclick=".*?"\stitle=".*?">(.*?)</a>.*?<p\sclass="pl">(.*?)</p>'
    result = re.findall(z,data,re.S)
    # print(result)
    for data in result:
        img_src = data
        print(img_src)




if __name__ == '__main__':
    html = get_data()
    parse_data(html)