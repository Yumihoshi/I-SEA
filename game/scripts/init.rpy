# 初始化
init python:
    # 定义左右位置的Transform
    left = Transform(xpos=0.175, xanchor=0.0)    # 左对齐（20%屏幕宽度）
    right = Transform(xpos=0.825, xanchor=1.0)  # 右对齐（80%屏幕宽度，锚点右对齐）

    guzhouleft = Transform(xpos=0.1, xanchor=0.0)

init:
    # 角色定义
    define SpeakerUnknown = Character("？？")
    define SpeakerChenYan = Character("陈言")
    define SpeakerGuZhou = Character("顾洲")
    define SpeakerHeMuYang = Character("何沐阳")
    define SpeakerYouLin = Character("游鳞")

    # 背景
    image BgTrain1:
        "images/Bg/train1.png"
        fit "cover"

    image BgTrain2:
        "images/Bg/train2.png"
        fit "cover"

    image BgTrainStation:
        "images/Bg/TrainStation.png"
        fit "cover"

    image BgDormitory:
        "images/Bg/Dormitory.png"
        fit "cover"

    image BgRoadToSea:
        "images/Bg/RoadToSea.png"
        fit "cover"

    image BgNightSea:
        "images/Bg/NightSea.png"
        fit "cover"

    image BgClassroom:
        "images/Bg/Classroom.png"
        fit "cover"

    image BgDiningHall:
        "images/Bg/DiningHall.png"
        fit "cover"

    # 角色立绘
    image CgChenYan:
        "images/Character/ChenYan.png"
        zoom 0.9

    image CgGuZhou:
        "images/Character/GuZhou.png"
        zoom 0.9
        yanchor -0.15

    image CgHeMuYang:
        "images/Character/HeMuYang.png"
        zoom 0.9

    image CgYouLin:
        "images/Character/YouLin.png"
        zoom 0.9
