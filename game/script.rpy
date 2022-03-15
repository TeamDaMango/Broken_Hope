# 游戏的脚本可置于此文件中。

#注意:该功能如果关闭则游戏无法进行
default ifTestVer = True


# 游戏在此开始。

label start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为“bg room.png”或“bg room.jpg”）来显示。

    if ifTestVer == False:
        "警告,你并非测试游玩人员,无法游玩该作品"
        $ renpy.quit()
    else:
        pass

    python:
        if not persistent.player:
            name = renpy.input("请输入该主角的名字。(限制2~12个字符\n请不要用自己的名字代入进去)",length=12)
            name = name.strip()

            if not name:
                name = "Mango"
                player = name
                persistent.player = player
            elif name == "Mango":
                name = "Mango"
                player = name
                persistent.player = player
            else:
                player = name
                persistent.player = player  
        else:
            pass    

        

    menu (nvl=True):
        "选择剧情阅读方式"
        "NVL模式":
            mcAltN "..."
            call story1Alt

        "ADV模式":
            mcAlt "..."
            call story1

    return

label storyEnd:
    stop music
    show black with dissolve
    "End"

    return



label qrcode:

    show weChatQrCode at center with dissolve:
        xzoom 0.4 yzoom 0.4
    "目标-2元(优惠价1元):完成第一章,4元(优惠价2元):增加新功能,22元(优惠价11元):设计UI,8元(优惠价4元):增加背景,6元(优惠价2元)更新破灭的希望DLC"

    return    