print("hello word！！！")
print("你好，樊强强欢迎您！")
print("12345")
print(12345)
print(type("12345"))
print(123+123)
print("123"+"123")
print("12345",123456789)
print(type(2.3333))
print(type(False))
print((1+4)*(4-1))
# print(233333)
'''
多行注释
print(999999999)
变量
赋值
'''
a=str(True)
print(type(a))
b="哈哈哈哈"
c=float("1")
print(c+789456123)
print("c的类型:",type(c))
print("哈"*100)
a=None  #空
print(type(a))
'''
True  真
False 假
'''

xxx=[1,2,3,4,"哈哈","嘻嘻",True,88]
yyy="哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈"
print(len(xxx))
print(len(yyy))
print(xxx[4])
print(xxx)
del xxx[4]    #删除
print(xxx)
xxx.append("小樊")    #新增
print(xxx)
xxx.insert(0,"樊强强")    #指定位置插入
print(xxx)
xxx.reverse()  #按下标倒序
print(xxx)
for i in range(1,10):
    for j in range(1,i+1):
        print(i,"X",j,"=",i*j,"\t",end="")
    print("")



hlist = [34,44,24,89,99,78,57,89,54,78,46,87,97,100,7,56]
lowlist = []
highlist = []
for i in hlist:
    if i >60:
     highlist.append(i)
print(hlist)
print(lowlist)
print(highlist)
{'code': 200, 'msg': 'success', 'result': {'app_id': 2300102, 'datas': [{'data_type': 'text', 'time_interval': 0, 'value': '蛤？~~'}, {'data_type': 'text', 'time_interval': 400, 'value': '你好呀～'}, {'data_type': 'text', 'time_interval': 400, 'value': '找我干嘛？'}], 'intent': 'chat', 'parse_type': 21}}









while True:
    url = "http://open.turingapi.com/v1/openapi"  # 接口地址
    headers = {   # 请求头
        "Content-Type": "application/json;charset=UTF-8"
    }
    input_text = input("请输入：")  # 获取聊天的内容
    if input_text == "退出":
        break
    data = {   # 接口的数据
        "input_text":input_text,
        "user_info":{"open_id":"b19b81b2-0ab9-42eb-86f6-8deb464d7d63"},
        "robot_id":"205436"
        }
    res = requests.request("POST",url,headers=headers,json=data)  # 调用接口，获取接口返回值
    result = res.json().get("result")  
    datas = result.get("datas")
    for i in datas:
        print("机器人说：",i["value"])
