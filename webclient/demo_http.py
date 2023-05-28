##
# 尊重原项目puppet,向原项目作者致以诚挚感谢。
# 尊重技术改变生活，尊重知识产权，
# 现有项目在其基础上进行了大量修改工作。
# 交流学习：554712718 ,VX:shushuolaoa
##

import requests
import json
import  pandas as pd

# host_site 为 安装飞鸟巡仓服务的 主机地址端口，  IP 替换为对应地址即可
host_site="http://127.0.0.1:8080"
HTTP_header={"Content-type":"application/json", "charset":"utf-8"}
key='woshifeiniao'

def get_token(keys=key):
    token_key =keys
    dic={'key':token_key}
    json_strin=json.dumps(dic)
    url=host_site+'/get_token'
    r = requests.post(url, data=json_strin, headers=HTTP_header)
    print("token",r.text)
    return r.text



## 市价委托，买入量

def buy_market(symbol,vol=100):
    token=get_token(keys=key)
    dic = {'vol':vol,
           'symbol': symbol,
           'token':token,
           'key':key
           }
    json_strin = json.dumps(dic)
    url=host_site+"/buy_market"
    r = requests.post(url, data=json_strin,headers=HTTP_header)
    rsult=json.loads(r.text)
    print(r)
    return rsult

# 原始上面制定了数量
def buy_market_static(symbol):
    token=get_token(keys=key)
    dic = {'symbol': symbol,'token':token,"key":key}
    # dic = { 'symbol': symbol}
    json_strin = json.dumps(dic)
    url=host_site+"/buy_market_static"
    r = requests.post(url, data=json_strin,headers=HTTP_header)
    rsult=json.loads(r.text)
    print(rsult)
    return rsult



#市价委托卖出
def sell_market(symbol,vol=100):
    token=get_token(keys=key)
    dic = {'vol': vol, 'symbol': symbol,'token':token,"key":key}
    json_strin = json.dumps(dic)
    url=host_site+"/sell_market"
    r = requests.post(url, data=json_strin,headers=HTTP_header)
    rsult=json.loads(r.text)
    print(rsult)

## 在交易界面已经自己写死了，每次交易的手数，就直接跳过了
def sell_market_static(symbol):
    token=get_token(keys=key)
    dic = {'symbol': symbol,'token':token,"key":key}
    # dic = { 'symbol': symbol}
    json_strin = json.dumps(dic)
    url=host_site+"/sell_market_static"
    r = requests.post(url, data=json_strin,headers=HTTP_header)
    rsult=json.loads(r.text)
    print(rsult)
    return rsult
#查询总仓和可用额度
def query_summary():
    url=host_site+"/query_summry"

    r=requests.get(url,headers=HTTP_header)
    if r.status_code==200:
        rsult=json.loads(r.text)
        rt_pd = pd.DataFrame(rsult,index=[0])
        print(rsult)
        return rt_pd

#查询持仓
def query_pos():
    url=host_site+"/query_pos"
    print("请求web地址：",url)
    r=requests.get(url,headers=HTTP_header)
    rsult=json.loads(r.text)

    rt_pd=pd.DataFrame(rsult)
    # print("返回持仓，结果如下：")
    print(rt_pd)
    return rt_pd

##查询 当日的成交单
def query_deal():
    url = host_site + "/query_deal"
    print("请求web地址：", url)
    r = requests.get(url, headers=HTTP_header)
    rsult = json.loads(r.text)
    rt_pd = pd.DataFrame(rsult)
    # print("返回持仓，结果如下：")
    print(rt_pd)
    return rt_pd

#查询历史的成交单
def query_his_deal():
    url = host_site + "/query_his_deal"
    print("请求web地址：", url)
    r = requests.get(url, headers=HTTP_header)
    rsult = json.loads(r.text)
    rt_pd = pd.DataFrame(rsult)
    # print("返回持仓，结果如下：")
    print(rt_pd)
    return rt_pd


#查询 当日的委托单
def query_order():
    url = host_site + "/query_order"
    print("请求web地址：", url)
    r = requests.get(url, headers=HTTP_header)
    rsult = json.loads(r.text)
    rt_pd = pd.DataFrame(rsult)
    # print("返回持仓，结果如下：")
    print(rt_pd)
    return rt_pd

#取消所有买委托
def cancel_buy_all():
    url=host_site+"/cancel_buy_all"
    r=requests.get(url,headers=HTTP_header)
    rsult=json.loads(r.text)
    return rsult
#取消所有卖委托
def cancel_sell_all():
    url=host_site+"/cancel_sell_all"
    r=requests.get(url,headers=HTTP_header)
    rsult=json.loads(r.text)
    return rsult

def test():
    url=host_site+"/test"
    r=requests.get(url,headers=HTTP_header)
    rsult=json.loads(r.text)
    print(rsult)
    return rsult

if __name__ == '__main__':
    # sell_market(symbol="002158",vol=100)
    query_summary()  # 英文没事

    # query_his_deal()
    # query_pos()
    # test()
    # buy_market('510050',100)