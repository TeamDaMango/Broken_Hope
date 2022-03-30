# 游戏的脚本可置于此文件中。


# 游戏在此开始。

label start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为“bg room.png”或“bg room.jpg”）来显示。

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