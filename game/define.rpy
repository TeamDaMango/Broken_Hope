
define persistent.steam = False
define config.developer = False
#define config.console = False


image black = "#000000"
image white = "#FFFFFF"
image red = "#FF0000"
image green = "#00FF00"
image blue = "#0000FF"
image orange = "#FF3000"

image weChatQrCode = ("qrcode/MyWechatQrCode.png")

#image sWarning = "bg/splashWarning.png"
#image sWarning2 = "bg/splashWarning2.png"

define cAlt = Character("作者")
define cAltN = Character("作者",kind=nvl)

define mcN = DynamicCharacter("player",kind=nvl)
define mc = DynamicCharacter("player")


define mcAltN = DynamicCharacter("mangoAlt",kind=nvl)
define mcAlt = DynamicCharacter("mangoAlt")

define mcdadN = Character("Mango父亲",kind=nvl)
define mcdad = Character("Mango父亲")
define mcmomN = Character("Mango母亲",kind=nvl)
define mcmom = Character("Mango母亲")
define mcbroN = Character("Mango哥哥",kind=nvl)
define mcbro = Character("Mango哥哥")
define mcsis = Character("???",kind=nvl)

define n1 = Character("学生A")
define n2 = Character("学生B")
define n3 = Character("学生C")
define n4 = Character("学生D")
define n5 = Character("学生E")
define n6 = Character("学生F")
define n7 = Character("学生G")
define n8 = Character("学生H")
define n1N = Character("学生A",kind=nvl)
define n2N = Character("学生B",kind=nvl)
define n3N = Character("学生C",kind=nvl)
define n4N = Character("学生D",kind=nvl)
define n5N = Character("学生E",kind=nvl)
define n6N = Character("学生F",kind=nvl)
define n7N = Character("学生G",kind=nvl)
define n8N = Character("学生H",kind=nvl)

define nall = Character("恶霸同学")
define nallN = Character("恶霸同学",kind=nvl)

define n11 = Character("老师")
define n12 = Character("班主任")
define n13 = Character("校长")
define n11N = Character("老师",kind=nvl)
define n12N = Character("班主任",kind=nvl)
define n13N = Character("校长",kind=nvl)

define n21 = Character("群主")
define n22 = Character("群管理")
define n23 = Character("群成员A")
define n24 = Character("群成员B")
define n25 = Character("群成员C")
define n26 = Character("群成员D")
define n27 = Character("群成员E")
define n28 = Character("群成员F")
define n29 = Character("群成员G")
define n211 = Character("群成员H")
define n212 = Character("不理智的群成员")
define n21N = Character("群主",kind=nvl)
define n22N = Character("群管理",kind=nvl)
define n23N = Character("群成员A",kind=nvl)
define n24N = Character("群成员B",kind=nvl)
define n25N = Character("群成员C",kind=nvl)
define n26N = Character("群成员D",kind=nvl)
define n27N = Character("群成员E",kind=nvl)
define n28N = Character("群成员F",kind=nvl)
define n29N = Character("群成员G",kind=nvl)
define n211N = Character("群成员H",kind=nvl)
define n212N = Character("不理智的群成员",kind=nvl)

define n31 = Character("粉丝")
define n32 = Character("不理智的粉丝")
define n33 = Character("黑粉")
define n34 = Character("吃瓜群众")
define n35 = Character("键盘侠")
define n36 = Character("喷子")
define n31N = Character("粉丝",kind=nvl)
define n32N = Character("不理智的粉丝",kind=nvl)
define n33N = Character("黑粉",kind=nvl)
define n34N = Character("吃瓜群众",kind=nvl)
define n35N = Character("键盘侠",kind=nvl)
define n36N = Character("喷子",kind=nvl)

define a1 = Character("微博话题",kind=nvl)
define a2 = Character("B站话题",kind=nvl)
define a3 = Character("???",kind=nvl)
define a1N = Character("微博话题",kind=nvl)
define a2N = Character("B站话题",kind=nvl)
define a3N = Character("???",kind=nvl)

default persistent.player = ""
default player = persistent.player

default mcName = player
default mcNameAlt = "Mango"
default mangoAlt = "Mango旁白"

#记录第几章节
default persistent.chapter = 0
default chapter = persistent.chapter

#记录第几部分
default persistent.chpart = 0
default chpart = persistent.chpart

# 记录正确的选择
default persistent.correctChoice = 0
# 记录错误的选择
default persistent.wrongChoice = 0
# 记录因为错误的选择或hp为0触发的游戏结束
# default persistent.gameover = 0
# 记录获得结局数
default persistent.endingCount = 0