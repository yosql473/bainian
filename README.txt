拜年 bainian - 作者:章仕烜  

首先需要保证你的环境是python 3+
1.安装itchart
pip3 install itchat
2.在happyNewYear.py所在目录下使用python命令(Py3同版本)

2.1 导入
C:\Users\yosql473\Documents\Wechart-Emit>python
Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import happyNewYear

2.2 万事先登录
happyNewYear.login_wechat()
使用案例:
    >>> happyNewYear.login_wechat()
    Getting uuid of QR code.
    Downloading QR code.
    Please scan the QR code to log in.
    # 手机扫码登录
    Login successfully as 大不自多

2.3 把好友对象拎出来
方式1: 搜索单个好友
    friend = happyNewYear.search_a_friend("于红霞")
    使用案例:
        >>> friend = happyNewYear.search_a_friend("于红霞")
        恭喜幸运观众:[<User: {'MemberList': <ContactList: []>, 'Uin': 0, 'UserName': '@6b47315a398b5e93ac6068b6f85cc9c88a14bb338a104ad7e34b0f0976c03f9f', 'NickName': '鱼 、Fish。', 'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgeticon?seq=684945596&username=@6b47315a398b5e93ac6068b6f85cc9c88a14bb338a104ad7e34b0f0976c03f9f&skey=@crypt_1fa26c9_d8790635974e47bbc1939e0f2ccf55da', 'ContactFlag': 3, 'MemberCount': 0, 'RemarkName': '于红霞', 'HideInputBarFlag': 0, 'Sex': 2, 'Signature': '
        我们都在用我们自己的方式生活', 'VerifyFlag': 0, 'OwnerUin': 0, 'PYInitial': 'YFISH', 'PYQuanPin': 'yuFish', 'RemarkPYInitial': 'YHX', 'RemarkPYQuanPin': 'yuhongxia', 'StarFriend': 0, 'AppAccountFlag': 0, 'Statues': 0, 'AttrStatus': 135717, 'Province': '山东', 'City': '青岛', 'Alias': '', 'SnsFlag': 16, 'UniFriend': 0, 'DisplayName': '', 'ChatRoomId': 0, 'KeyWord': '', 'EncryChatRoomId': '', 'IsOwner': 0}>]
        请说出发给几号小婊子(你懂的，江湖规矩，从0开始):0
        幸运观众是:{'MemberList': <ContactList: []>, 'Uin': 0, 'UserName': '@6b47315a398b5e93ac6068b6f85cc9c88a14bb338a104ad7e34b0f0976c03f9f', 'NickName': '鱼 、Fish。', 'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgeticon?seq=684945596&username=@6b47315a398b5e93ac6068b6f85cc9c88a14bb338a104ad7e34b0f0976c03f9f&skey=@crypt_1fa26c9_d8790635974e47bbc1939e0f2ccf55da', 'ContactFlag': 3, 'MemberCount': 0, 'RemarkName': '于红霞', 'HideInputBarFlag': 0, 'Sex': 2, 'Signature': '我们都在用
        我们自己的方式生活', 'VerifyFlag': 0, 'OwnerUin': 0, 'PYInitial': 'YFISH', 'PYQuanPin': 'yuFish', 'RemarkPYInitial': 'YHX', 'RemarkPYQuanPin': 'yuhongxia', 'StarFriend': 0, 'AppAccountFlag': 0, 'Statues': 0, 'AttrStatus': 135717, 'Province': '山东', 'City': '青岛', 'Alias': '', 'SnsFlag': 16, 'UniFriend': 0, 'DisplayName': '', 'ChatRoomId': 0, 'KeyWord': '', 'EncryChatRoomId': '', 'IsOwner': 0}
        <User: {'MemberList': <ContactList: []>, 'Uin': 0, 'UserName': '@6b47315a398b5e93ac6068b6f85cc9c88a14bb338a104ad7e34b0f0976c03f9f', 'NickName': '鱼 、Fish。', 'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgeticon?seq=684945596&username=@6b47315a398b5e93ac6068b6f85cc9c88a14bb338a104ad7e34b0f0976c03f9f&skey=@crypt_1fa26c9_d8790635974e47bbc1939e0f2ccf55da', 'ContactFlag': 3, 'MemberCount': 0, 'RemarkName': '于红霞', 'HideInputBarFlag': 0, 'Sex': 2, 'Signature': '我们都在用我们
        自己的方式生活', 'VerifyFlag': 0, 'OwnerUin': 0, 'PYInitial': 'YFISH', 'PYQuanPin': 'yuFish', 'RemarkPYInitial': 'YHX', 'RemarkPYQuanPin': 'yuhongxia', 'StarFriend': 0, 'AppAccountFlag': 0, 'Statues': 0, 'AttrStatus': 135717, 'Province': '山东', 'City': '青岛', 'Alias': '', 'SnsFlag': 16, 'UniFriend': 0, 'DisplayName': '', 'ChatRoomId': 0, 'KeyWord': '', 'EncryChatRoomId': '', 'IsOwner': 0}>
方式2:获得全部好友对象列表
    friends = happyNewYear.get_all_friends()


2.4 发送祝福
    >>> happyNewYear.send_to_one(friend,"happy new year")

2.5 群发
    >>> happyNewYear.send_all_friends("happy new year")

2.5 微信轰炸机
    # 1s发一次 ，共发送10次
    >>> happyNewYear.boooooooooooooo(friend,"新的一年里你会天天快乐",10,1)



