import itchat
import time 
"""
    发送新年祝福
    @章仕烜
"""



"""
    注意第一个人是自己，别把发给女票的发给老妈
    自己的消息没法发给自己
    @param friend对象
"""
def get_friends():
    return itchat.get_friends()

"""
    搜索好友
"""
def search_friends(keyword):
    return itchat.search_friends(keyword)



