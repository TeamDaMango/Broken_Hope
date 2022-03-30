default sMenu_xalign = 0.5
default sMenu_yalign = 0.85


screen story_menu():
    tag menu

    vbox:
        style_prefix "story_menu"
        xpos 0.02
        ypos 0.01

        if persistent.chapterName != "":
            text _("章节名: [persistent.chapterName]")
        else:
            text _("章节名: ")    

    vbox:
        style_prefix "story_menu"
        xpos 0.82
        ypos 0.01

        text _("暂未开放")



    vbox:
        style_prefix "story_menu"

        xalign sMenu_xalign
        yalign sMenu_yalign

        spacing 40

        textbutton _("Chapter 1") action Start("story1") hovered SetVariable("persistent.chapterName","开端")
        textbutton _("Chapter 2") action Start("story2") hovered SetVariable("persistent.chapterName","一场没有悬念的游戏") 
        textbutton _("Chapter 3") action Start("story3") hovered SetVariable("persistent.chapterName","在绝望之中的唱喊") 
        textbutton _("Chapter 4") action Start("story4") hovered SetVariable("persistent.chapterName","???") 
        textbutton _("Chapter 5") action Start("story5") hovered SetVariable("persistent.chapterName","???")
        textbutton _("Chapter 6") action Start("story6") hovered SetVariable("persistent.chapterName","???")


style story_menu_text is gui_text

style story_menu_button is gui_button
style story_menu_button_text is gui_button_text

style story_menu_text:
    properties gui.text_properties("story_menu",accent=True)

style story_menu_button:
    size_group "story_menu"
    properties gui.button_properties("story_menu_button")

style story_menu_button_text:
    properties gui.button_text_properties("story_menu_button")
    size 40
    color "#ff0000"
    outlines [(2, "#000000", 0, 0),(1, "#000000", 0, 0)]
    hover_outlines [(1, "#ff7474", 1,1)]
