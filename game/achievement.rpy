init python:

    if not persistent.steam:
        achievement.register("第一次游玩")
        achievement.register("第一次失败")
        achievement.register("完成第一章第一幕")
        achievement.register("完成第一章第二幕")
        achievement.register("完成第一章第三幕")
        achievement.register("完成第一章第四幕")
        achievement.Sync()
    else:
        achievement.register("第一次游玩",steam)
        achievement.register("第一次失败",steam)
        achievement.register("完成第一章第一幕",steam)
        achievement.register("完成第一章第二幕",steam)
        achievement.register("完成第一章第三幕",steam)
        achievement.register("完成第一章第四幕",steam)
        achievement.Sync()

    def check():
        if renpy.has_label("splashscreen"):
            achievement.grant("第一次游玩")
        if renpy.has_label("story1_1") or renpy.has_label("story1_1Alt"):
            achievement.grant("完成第一章第一幕")