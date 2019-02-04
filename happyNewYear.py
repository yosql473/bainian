import itchat
import time 
import itchat_utils

"""
    登录微信:扫二维码登录
"""
def login_wechat():
    itchat.login()

"""
    搜索并获得好友对象
"""
def search_a_friend(keyword):
    objective_friend = None
    friends_searched = itchat_utils.search_friends(keyword)
    print("恭喜幸运观众:"+str(friends_searched))
    length = len(friends_searched)
    num_str = input("请说出发给几号小婊子(你懂的，江湖规矩，从0开始):")
    try:
        num = int(num_str)
        if num >= 0 and num < length:
            print("幸运观众是:"+str(friends_searched[num]))
            objective_friend = friends_searched[num]
        else:
            print("过年了，这事不是开玩笑的!")
    except Exception as e:
        print(e)
        print("过年了，这事不是开玩笑的!")
    return objective_friend

"""
    获得所有好友
"""
def get_all_friends():
    return itchat_utils.get_friends()[0:]


"""
    发给一个人文本
"""
def send_to_one(user,content):
    itchat.send(content,toUserName=user.UserName)

"""
    搜索好友并发送
    @param keyword 关键字
"""
def search_and_send_to_one(keyword,content):
    friends_searched = itchat_utils.search_friends(keyword)
    print("恭喜幸运观众:"+str(friends_searched))
    length = len(friends_searched)
    num_str = input("请说出发给几号小婊子(你懂的，江湖规矩，从0开始):")
    try:
        num = int(num_str)
        if num >= 0 and num < length:
            print("幸运观众是:"+str(friends_searched[num]))
            send_to_one(friends_searched[num],content)
        else:
            print("过年了，这事不是开玩笑的!")
    except Exception as e:
        print(e)
        print("过年了，这事不是开玩笑的!")


"""
    微信轰炸机
    @param count 发送的次数
    @param inteval 时间间隔
"""
def boooooooooooooo(user,content,count,inteval):
    counter = 0
    while counter < count:
        send_to_one(user,content)
        time.sleep(inteval)
        counter += 1


"""
    祝福群发
    @param content
"""
def send_all_friends(content):
    friends = itchat_utils.get_friends()
    for friend in friends[0:]:
        try:
            send_to_one(friend,content)
        except Exception as e:
            print(e)



