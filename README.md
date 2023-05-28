# flybird_ths_trader

作者曾是一名程序员，后来又搞起了大数据，喜欢上了炒股。有一个梦想，让上班族包括自己无需盯盘，当股票买卖出现时，能够及时提示我。再根据自己认知，决定是否下单。
至于别人口头说他会涨会跌，没有数据证明，很难相信。
在经历三年的打磨过程中，找到了一些经验，也做了一些工具。其中 API 自动化交易就是本次分享给大家的一个小工具。请放心使用，无毒，无害，不套取个人信息。

<img width="524" alt="image" src="https://github.com/shushuolaoa/flybird_ths_trader/assets/134842596/44784392-e0ef-49f1-9dc6-3112d8369092">


## 以下为个人的交易认知：

#### 加入微信： shushuolaoa   or  qq: 554712718 一起交流学习

可提供量化咨询，框架本地化，教育教学辅导

<img width="523" alt="image" src="https://github.com/shushuolaoa/flybird_ths_trader/assets/134842596/fe5ab5f6-78bb-41da-a4ab-48bd13e4e0e2">


## flybird量化交易API原理

1.模拟人工操作过程， 比如点击》买入菜单》股票代码》数量》确定，整个流程，通过程序自动盯着屏幕的方式，代替你进行操作。

2.能够将程序提取到的同花顺界面信息，返回给调用者。


3.通信协议为 通用的HTTP协议

<img width="366" alt="image" src="https://github.com/shushuolaoa/flybird_ths_trader/assets/134842596/166cb9b8-c5f6-4c8f-87f8-5ddcda0b0394">


# 三. 服务端使用教程

## 3.1 操作系统要求

    A: 关闭防火墙（重点）
		   本程序启动windows的8080端口， 防火墙会默认阻止访问， 请自行关闭。	
		B：显示屏分辨率（重点）
			本程序测试通过的显示屏分辨率为 1920X1200   和 2500 X 1440    满足市面上大多数显示屏
      
## 3.2 将先启动并设置同花顺交易终端

	在同花顺官网下载，最新免费版，同花顺客户端。 最新版：V9.20
	自行登录交易终端。
	按照如下图进行交易设置。
  
	
  <img width="229" alt="image" src="https://github.com/shushuolaoa/flybird_ths_trader/assets/134842596/54dd866e-09a3-41e9-bad5-dba431282d55">



## 3.3 安装飞鸟巡仓程序	

源码安装：

  1. 安装 相关依赖
              pip install -r requirement.txt
  2. 测试本地接口
            python  -m test_localapi.py
  
  3. 启动web代理
          python -m flybird.py   
  
  
  4. 测试web 接口
          python -m  demo_http.py

当出现如下界面时就是代表跑起来了。
<img width="396" alt="image" src="https://github.com/shushuolaoa/flybird_ths_trader/assets/134842596/ef3b612e-a2c7-40ba-ba5d-11b6422bd60b">



3.3 验证是否成功

浏览器输入, 查询当前持仓的接口：  http://127.0.0.1:8080/query_pos

如果不能访问，请尝试
方法： 1.关闭重新打开， 2. 关闭windows防火墙等限制端口访问的安全设置。

<img width="324" alt="image" src="https://github.com/shushuolaoa/flybird_ths_trader/assets/134842596/4840f4fd-2cd9-4226-adf5-bd9ef2727d0b">



# 四．客户端使用（请看demo代码）

1.查询当前总资金情况

2.查询当前持仓情况

3.查询今日成交

4.查询历史成交—一周内的

5.查询今日委托

6.按照市价买入

7.按照市价卖出

8.取消所有买

9.取消所有卖



  
