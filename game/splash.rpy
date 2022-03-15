

init python:

    splashMessage = "\'我\'不会成为过去的\'我\'"
    splashVersion = "Engine: Ren'py"
    splashMessageList = [
        "别忘了备份你的存档",
        "不要再靠近我了!!!\n你这个恶魔",
        "那些选择是正确的吗?",
        "不只是自己的命运哦",
        "作者是黑夜下的糖果酱!",
        "不要相信一些选项",
        "我的梦想是要成为一名游戏制作者!",
        "\'我\'的旅途才刚刚开始",
        "不要忘记你的使命",
        "\'我\'不是过去的\'我\'了\n我已经成长了"
    ]
    
image splashWarning = ParameterizedText(style="splashText", xalign=0.5, yalign=0.5)    


style splashText:
    color "#000"
    properties gui.text_properties()
    language gui.language

image mtos = "#000000"
image mtos2 = "#FFFFFF"

define gameDemo = True




label splashscreen:
    show white
    $ check()
    $ splashMessages = splashMessage

    if persistent.chapter >= 2 and renpy.random.randint(0,10):
        $ splashMessages = renpy.random.choice(splashMessageList)
    show white
    show splashWarning "[splashMessages]" with Dissolve(2.5)
    pause 2.5
    hide splashWarning with Dissolve(2.5)   


label before_main_menu:

    $ config.window_title = config.name + config.version

