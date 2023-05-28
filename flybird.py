from flybird_deault.client_ths import Account
from bottle import get,post, run, request, response,Bottle
from flybird_deault.token_key import generate_token,certify_token

def run_web(host='127.0.0.1', port=80):
    # response.add_header({'content-type': 'text/plain; charset=utf-8'})
    response.charset.encode('utf-8')
    print("飞鸟量化交易接口启动端口: ",port)
    print("可以用浏览器测试：http://127.0.0.1:"+str(port)+"/query_pos")
    print("更多接口请查看文档 or 联系作者")
    root = Bottle()

    # 解决跨域问题https://simpledao.win/2018/05/20/python-bottle%E8%A7%A3%E5%86%B3%E8%B7%A8%E5%9F%9F%E9%97%AE%E9%A2%98/
    @root.hook('after_request')
    def enable_cors():
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers[
            'Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

    @root.route("/buy_market",method='POST')
    def buy_market():
        data = request.json
        symbol=data["symbol"]
        vol=data["vol"]
        token=data['token']
        key=data['key']
        if certify_token(key=key,token=token):
            rsult=acc.buy_market(symbol=symbol,quantity=int(vol))
            print(rsult)
        else:
            rsult={"flybird":' your token is not right or  expired'}
        return rsult

    @root.route("/buy_market_static",method='POST')
    def buy_market_static():
        data = request.json
        symbol = data["symbol"]
        key=data['key']
        token = data['token']
        if certify_token(key,token):
            rsult = acc.buy_market_static(symbol=symbol)
            print(rsult)
        else:
            rsult = {"flybird": ' your token is not right or  expired'}
        return rsult


    @root.route('/query_summry')
    def query_summry():
            return acc.query_summary()

    @root.route('/query_pos')
    def query_pos():
        return acc.query_pos()

    @root.route("/query_order")
    def query_order():
            # acc=Account(title="网上股票交易系统5.0")
            r=acc.query_order()
            print(r)
            return r

    @root.route('/query_deal')
    def query_deal():
        r = acc.query_deal()
        print(r)
        return r

    @root.route('/query_his_deal')
    def query_his_deal():
        r = acc.query_his_deal()
        print(r)
        return r


    @root.route('/sell_market',method='POST')
    def sell_market():
        data = request.json
        symbol=data["symbol"]
        vol=data["vol"]
        token=data['token']
        key=data['key']
        if certify_token(key,token):
            rsult=acc.sell_market(symbol=symbol,quantity=int(vol))
            print(rsult)
        else:
            rsult={"flybird":' your token is not right or  expired'}
        return rsult

    @root.route('/sell_market_static',method='POST')
    def sell_market_static():
        data = request.json
        symbol = data["symbol"]
        key = data["key"]
        token = data['token']
        if certify_token(key, token):
            rsult = acc.sell_market(symbol=symbol)
            print(rsult)
        else:
            rsult = {"flybird": ' your token is not right or  expired'}
        return rsult

    @root.route("/get_token",method="POST")
    def get_token():
        #每次必须要获得token 带着时间戳呢
        data = request.json
        key = data["key"]
        token= generate_token(key,300) # 5分钟过期
        return token

    @root.route("/cancel_buy_all",method='POST')
    def cancel_buy_all():
        rsult=acc.cancel_buy_all()
        return rsult

    @root.route("/cancel_sell_all",method='POST')
    def cancel_sell_all():
        rsult = acc.cancel_sell_all()
        return rsult

########################
##以下基金和两融模型，在开发中，会放到收费版。或者有此资金量的时候，买券商的 量化交易接口
    # @post("/fund_purchase")
    # def fund_purchase():
    #     data = request.json
    #     symbol=data["symbol"]
    #     vol=data["vol"]
    #     token=data['token']
    #     key=data['key']
    #     if certify_token(key,token):
    #         rsult=acc.fund_purchase(symbol=symbol,amount=int(vol))
    #         print(rsult)
    #     else:
    #         rsult={"flybird":' your token is not right or  expired'}
    #     return rsult


    # @post('/fund_redeem')
    # def fund_redeem():   #基金赎回，还没做呢
    #     data = request.json
    #     symbol = data["symbol"]
    #     vol = data["vol"]
    #     token = data['token']
    #     key = data['key']
    #     if certify_token(key, token):
    #         rsult = acc.fund_redeem(symbol=symbol, share=int(vol))
    #         print(rsult)
    #     else:
    #         rsult = {"flybird": ' your token is not right or  expired'}
    #     return rsult

    # @post('/buy_on_rongzi')  #融资买入
    # def buy_on_rongzi():
    #     pass
    #
    # @post('/sell_for_repay')
    # def sell_for_repay():  # 融资还款
    #     pass


    # @post('/sell_on_rongquan')
    # def buy_for_repay(): #买券还款
    #     pass
    #
    # @get('rongquan_target')
    # def rongquan_target():  #获取融券的标的
    #     pass


    @root.route('/test')
    def test():
        reult={'flybird': "返回这条语句，代表http 端口通信是成功的"}
        return reult

    print(r"请确保已经自行启动，同花顺交易委托界面，再次启动本程序")
    # print(r"默认辅助打开目录：C:\同花顺软件\同花顺\xiadan.exe")
    accinfos = {
        'account_no': '234r134',
        'password': '123329329456',
        'comm_pwd': True,  # 模拟交易端必须为True
        'client_path': r'C:\同花顺软件\同花顺\xiadan.exe'
    }

    acc=Account(to_dict=True,title="网上股票交易系统5.0")
    root.run(host=host, port=port,quiet=True)


if __name__ == "__main__":
    run_web(host='0.0.0.0',port=8080)
