screen custom_navigation():
    key "mousedown_4" action ShowMenu("history")
    key "mousedown_5" action Return()

# 开始
label start:
    show screen custom_navigation
    scene black with fade
    "——隆隆——隆隆"

    # 火车上
    scene BgTrain1 with dissolve
    "睁开眼，窗外是蓝色的天空，万里无云，澄澈无边。\n"
    extend "仿佛深吸一口气就能清空胸中所有的郁结与迷茫。"
    "然而我现在尝试不了，不知道实际会是怎样的感觉。"

    scene BgTrain2 with dissolve
    show CgChenYan
    with dissolve
    "这是去澄沫市的火车，我的新学校所在的地方。"
    "据说是个能看到海的地方，还真是令人期待啊。我以前只在手机和书上见过对于海的各种描述和图像，但是从来没有自己亲眼见过。"
    "海……会比这片天空更蓝吗？更摄人心魄吗？那宛如圣地一般的种种描述，好想真的亲自见识。"
    "“尊敬的女士们先生们，火车即将停靠——请要在澄沫站下车的旅客做好准备，火车即将停靠。”"
    "到站了。"
    jump TrainStation

# 下车后（火车站）
label TrainStation:
    scene BgTrainStation with fade
    show CgChenYan
    with dissolve
    "车门打开，热浪扑面而来。"
    "只能说不愧是南方吗，即使是在夏季末也完全没有想象中海边应有的清爽。"
    "哎，还是先把行李拿到学校里去吧，等放完就去看看现实中的海到底长什么样。"
    jump Dormitory

# 宿舍
label Dormitory:
    scene BgDormitory with blinds
    show CgChenYan
    with dissolve
    "做完各种繁琐的工作后，终于是到了宿舍门前，一打开门就看到一个人正站在房间中央。"
    show CgGuZhou at guzhouleft
    show CgChenYan at right
    with dissolve
    SpeakerUnknown "啊，你好。"
    SpeakerChenYan "你好。（点头）以后我们就是室友了？"
    SpeakerGuZhou "嗯。我叫顾洲，你呢？"
    SpeakerChenYan "陈言。希望相处愉快！"
    hide CgGuZhou with dissolve
    show CgChenYan at center
    with dissolve
    "看样子应该是个话不怎么多的人。"
    "打完招呼放完东西，终于可以出去走走看看了。"
    jump RoadToSea

# 前往海边的路
label RoadToSea:
    scene BgRoadToSea with fade
    show CgChenYan
    with dissolve
    "走在去往海边的路上，天色也开始渐渐暗了下来，温度也渐渐降低，带来一丝凉意。"
    "看来今天也不能怎么欣赏大海的真实容貌啊，不过倒也可以看看夜晚会是什么样子。"
    jump NightSea

# 夜晚的海边
label NightSea:
    scene BgNightSea with fade
    show CgChenYan
    with dissolve
    "我继续向前走着，走着。"
    "前方好像有一个人影。也许也是和我一样来逛逛看的外地新生吧。"

    hide CgChenYan with dissolve
    show CgChenYan at right:
        yanchor -0.1
    show CgYouLin at left:
        yanchor -0.24
    with dissolve
    "我边走近边借着身后路灯的光，看见那人是个短发女生。"
    "她蹲了下来，伸出手触摸了海水。"
    "应该是很舒服的感觉吧，我也想试试。这么想着我也向那边走近了些。"
    hide CgYouLin with moveoutleft
    "......"
    "她似乎被我吓了一跳，回头看了我一眼然后迅速往旁边逃一样地走了。"
    "应该是没想到会有别人来再加上可能社恐吧。"
    "不管了，先试试被海浪拍到手上的感觉。凉凉的，还有泡沫破开残留水渍在手背上，被风一吹更加感觉凉爽。"
    "海，虽然现在给我的体验似乎和普通水槽的效果差不了太多，但是身临其境的感觉果然还是不太一样。"
    """\
    风吹，潮汐，令人有点晕眩的低气压以及似有似无的咸腥气味\n
    这就是海吗。这就是海啊。
    """
    "不过似乎该回去了，一个人大晚上在外面待太久也不太好。之后有空再看吧。"
    jump SecondDayDormitory

label SecondDayDormitory:
    scene BgDormitory with fade
    "翌日中午，宿舍。"
    show CgChenYan at right:
        yanchor -0.1
    show CgGuZhou at left
    with dissolve
    SpeakerGuZhou "等会儿要开会，群里说的。"
    SpeakerChenYan "不是才开学吗有什么会？"
    SpeakerGuZhou "估计就是新生见面会之类的吧。"
    SpeakerChenYan "哦，还有这回事。等会儿吃完饭一起去吧。"
    SpeakerGuZhou "行。"
    jump Classroom

label Classroom:
    scene BgClassroom with fade
    "教室开会。"
    "老师" "好的，那么有人想当班委吗，临时的。后面再根据大家的了解来再次进行选举。"
    "一片骚动后，有几个人被选上了。"

    show CgChenYan at right:
        yanchor -0.1
    show CgGuZhou at left
    with dissolve
    SpeakerChenYan "你没兴趣当吗？"
    SpeakerGuZhou "不想管这些事，感觉还是多做点自己的事更好。"
    SpeakerChenYan "也对，我也不是什么很多精力的人，管好自己就行。"
    "老师" """\
    那么现在我们的班长就是何沐阳，大家有事都可以找他\n
    而你也要尽好管理的责任，相信你一定能够做好的！
    """

    hide CgChenYan
    hide CgGuZhou
    show CgHeMuYang
    with dissolve
    SpeakerHeMuYang """\
    谢谢老师给我的机会！我会认真工作的。\n
    也希望同学们可以信任我并配合我的工作，也希望我的工作能让大家在正式\n
    评选时继续支持我。
    """

    hide CgHeMuYang
    show CgChenYan at right:
        yanchor -0.1
    show CgGuZhou at left
    with dissolve
    "顾洲抬头看了一眼，皱眉轻声嗯了一下然后又低头继续玩手机。"
    SpeakerChenYan "你认识他？"
    SpeakerGuZhou "不认识。"
    SpeakerChenYan "啊，那你刚刚是。"
    SpeakerGuZhou "感觉有点太活力了不太想和他接触的感觉。"
    SpeakerChenYan "哦这样。（那我是不是应该少说点话）"
    SpeakerGuZhou "还好。不是一种感觉。"
    SpeakerChenYan "哦。（居然听见了。）"
    "会议结束了，顾洲和我站起身准备回宿舍。"
    "我一回头，看到身后坐的人是昨天晚上看到那个女生。"

    hide CgChenYan
    hide CgGuZhou
    show CgChenYan:
        xpos 0.7
        yanchor -0.1
    show CgYouLin
    show CgGuZhou:
        xpos 0.05
    with dissolve
    "不过，与其说“坐”，她其实是趴在桌子上正在睡觉。"
    "她这才睁开眼睛，和我对视上了一眼，随即又眯起眼睛笑着说。"
    menu:
        SpeakerUnknown "抱歉抱歉，我听树叶讲故事听睡着了。"
        "……？":
            jump Choice
        "啊，这样啊，很有意思的样子":
            jump Choice

label Choice:
    SpeakerGuZhou "（ 这人，有点怪吧。）"
    SpeakerChenYan "（哈哈……）"
    SpeakerGuZhou "（反正你都叫醒她了，快走吧）"
    SpeakerChenYan "（别急你等会儿，急的话可以先走。）同学你叫什么名字呀，是哪个宿舍的？"
    SpeakerYouLin "我的名字是游鳞……宿舍号是……A203？应该没记错，嗯。"
    SpeakerChenYan "啊！那不就是和我们寝室在对门吗？我们一起回去吧，怎么样？"
    "我看向顾洲，她缓缓闭了下眼睛，应该是同意了。不同意应该会摇头吧。"
    SpeakerYouLin "好啊，我对这里也不熟，你们带着我就不怕走错路了。"
    "随后她就站起来跟着我们走了。"

    hide CgGuZhou with moveoutleft
    hide CgYouLin with moveoutleft
    "嗯该怎么说呢，"
    extend "这么容易就相信别人还跟着走了，这就是清澈愚蠢的大学生吗。"
    jump DiningHall

label DiningHall:
    scene BgDiningHall with fade
    show CgChenYan:
        xpos 0.7
        yanchor -0.1
    show CgYouLin
    show CgGuZhou:
        xpos 0.05
    with dissolve
    "几日后，食堂"
    SpeakerGuZhou "你要真心抽时间出来肯定还是能去看的。"
    SpeakerChenYan "哎可是我感觉要时间够多再去才比较好，我说的看又不是真的只是看一眼。"
    SpeakerChenYan "哎！不要夹我的菜！游鳞你又这样……我的和你的明明就是一样的。"
    menu:
        SpeakerYouLin "不在我的盘子里，不一样。"
        "那我也要吃你的（夹走）":
            jump C1
        "那这也是我的，不是你的。":
            jump C1

label C1:
    "感觉到被游鳞一直盯着"
    "人多嘈杂，眼睛都感觉会看花，耳朵边也一直充斥着一定音量的听不清的交谈声。"
    "然而就是在这个情况下有人看到了我们"
    hide CgGuZhou
    hide CgYouLin
    hide CgChenYan
    with dissolve

    show CgGuZhou:
        xpos 0.025
    show CgYouLin:
        xpos 0.35
        yanchor -0.24
    show CgChenYan:
        xpos 0.55
        yanchor -0.1
    show CgHeMuYang:
        xpos 0.75
        yanchor -0.1
    with dissolve
    SpeakerHeMuYang "下午好，熟悉学校了吗？"
    SpeakerGuZhou "难道你很熟？"
    SpeakerHeMuYang "啊，这不是正在熟悉吗，和班上的同学。如果说的是环境的话，那确实也算是挺熟的了。"
    SpeakerYouLin "你是不是……叫什么洋来着？……海洋？……"
    SpeakerChenYan "何沐阳……"
    SpeakerHeMuYang "哈……我就说我名字应该也不难记吧。"
    SpeakerHeMuYang "下次会记得住吗，游鳞同学？"
    "（顾洲闭上了她的眼睛并向后靠在了椅背上）"
    SpeakerChenYan "（怎么。）"
    SpeakerGuZhou "（感觉好装。）"
    """\
    何沐阳应该是没听到，但是看得到顾洲的闭眼后仰。\n
    总之尬笑了两下然后低头看了一眼自己手里捏的东西，随后马上又抬起头
    """
    SpeakerHeMuYang "每个同学个性不一样，不想和我说话也很正常。还是祝你们校园生活愉快！"

    hide CgHeMuYang with moveoutright
    "然后他就这么走了，留下一个感觉有点落寞的背影。"
    "老实说，他能在这么大一堆人里面一下找到没见过几次面的我们也挺厉害的。好吧，也许不是挺厉害，是很厉害，而且看样子似乎也记住了我们的名字。是真的厉害吧。"
    jump GoOut

label GoOut:
    scene BgDormitory with pixellate
    show CgChenYan with dissolve
    "暑气已经渐渐消去，太阳已经一周没有毒打过我了。"

    hide CgChenYan
    show CgYouLin
    with dissolve
    "可能也正是因为太阳不会把人晒得蔫蔫的了，游鳞也比前一个月看起来更有活力。"

    hide CgYouLin
    show CgGuZhou at center
    with dissolve
    "至于顾洲，还是一样不怎么喜欢说话，只是做着自己的事，我不提议就也不来找我。但是一旦我叫上她，她十有八九都会来，不来的情况也是有ddl在手。"

    hide CgGuZhou with dissolve
    "而这周她也是一样在忙着做自己的事情，我就决定约游鳞一起出去。"
    jump Classroom2

label Classroom2:
    scene BgClassroom with fade
    "于是等我们在同一个教室的课下课后我一下就找到她。"
    
    show CgYouLin at left:
        yanchor -0.24
    show CgChenYan at right:
        yanchor -0.1
    with dissolve
    SpeakerChenYan "游鳞游鳞！你明天周六有没有空？有的话我们去看海吧，我还没有好好去看过。刚好最近天气也没那么热了，这时候去也很合适吧？"
    "游鳞听着我说话，眼睛慢慢睁大，使得她的眼睛反射的亮光更多，看起来更加有活力。"
    SpeakerYouLin """\
    好啊好啊！我也想去！\n
    明天什么时候？就我们吗？怎么去？走路吗？几点回来？要带东西吗？去了\n
    会下水吗？
    """
    SpeakerChenYan "等一下！好多问题！"
    SpeakerChenYan """\
    明天吃完午饭走路去，我记得你也不会骑车吧？\n
    六点左右回来差不多可以吃晚饭，然后下水的话就看你心情！\n
    反正我是有点想就在岸边踩一下浅水的地方。
    """
    SpeakerYouLin "好哦！"
    jump Sea

label Sea:
    scene BgSea with blinds
    "就这样，到了第二天"
    "海边，白天的海边啊。"
    """\
    原来也不是那样的湛蓝澄澈。它只是反射出天空的状态吧。\n
    它看起来没那么好是因为现在的天空也没那么晴朗无边了吧。
    """

    show CgChenYan at right:
        yanchor -0.1
    with dissolve
    "我站在岸边眺望着那水天相接的地方，两种颜色浑然一体。"
    "所以，其实海洋的颜色，就是天空的颜色吗。"
    "那我之前期盼的更为撼动心灵的蓝是根本就没有存在过的吗。"
    "是这样啊。"
    hide CgChenYan with dissolve
    "我视线下移，看到一抹纯粹的蓝在移动，那是游鳞在蹲着捡贝壳。"
    "那样专注，那样投入。"
    "算了，至少浪花不会辜负触碰它的人，它会给你真实的触感。"
    "如此，过了不知道到底多久，听到一声呼喊把我拉回了这个我感觉很真实的现实。"
    "“陈言！”"
    "是游鳞在喊我。"
    "我回过神来，坐起身抹了一把脸。刚刚我躺在潮汐处一直等着浪花的击打。"
    show CgYouLin with dissolve
    """\
    我望向她，她的笑颜是如此令人难以忘怀。\n
    她手里捧着一堆精挑细选过后的贝壳与海螺，再加上她身上那条蓝色的裙子\n
    仿佛此刻天地间唯有她才是最真实的存在。
    """

    """\
    她小跑过来蹲在我旁边\n
    挑出一个颜色最多，个头最大，又很干净的海螺递给我，\n
    又用那只手将鬓发抹到耳后。
    """

    SpeakerYouLin """\
    哼哼~躺在这里很舒服吧——这个送给你，我挑了这么久感觉最漂亮的\n
    它也觉得自己最适合送人。
    """

    "她依然笑着。"

    show CgYouLin at left
    show CgChenYan at right:
        yanchor -0.1
    with dissolve
    SpeakerChenYan "嗯，谢谢你……"
    SpeakerChenYan "……谢谢你，谢谢。"
    SpeakerYouLin "啊，看那边，是橙色的！"

    hide CgChenYan
    show CgYouLin at center
    with dissolve
    "我顺着她手指的方向看过去，是夕阳，和它所照射到的云还有那一片天空，都成了橙色的。"
    "也很好看啊。"
    SpeakerChenYan "走吧，是时候该回去了吧。（淡笑）"

    "未完待续……"
    return
