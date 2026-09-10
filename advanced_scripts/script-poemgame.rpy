






init python:
    import random


    class PoemWord:
        def __init__(self, word, sPoint, nPoint, yPoint, glitch=False):
            self.word = word
            self.sPoint = sPoint
            self.nPoint = nPoint
            self.yPoint = yPoint
            self.glitch = glitch


    POEM_DISLIKE_THRESHOLD = 29
    POEM_LIKE_THRESHOLD = 45


    full_wordlist = []
    wordfile = """#File format: word,sPoint,nPoint,yPoint

#Sayori's winning words
щастя,0,0,0
печаль,5,2,1
смерть,5,1,2
трагедія,5,1,2
самотній,5,1,2
кохання,5,2,1
пригода,0,2,1
солодкий,0,2,1
ажіотаж,0,2,1
феєрверк,0,2,1
романтика,5,2,1
сльози,5,1,2
депресія,5,1,2
серце,5,2,1
весілля,0,2,1
пристрасть,5,2,1
дитинство,0,2,1
радість,0,2,1
колір,0,2,1
надія,0,1,2
друзі,0,2,1
сім'я,5,2,1
вечірка,0,2,1
канікули,0,2,1
лінь,0,2,1
мріњ,0,1,2
біль,5,1,2
свято,0,2,1
ліжко,0,2,1
перо,0,2,1
сором,5,1,2
страх,5,1,2
теплота,0,2,1
квітка,0,2,1
затишок,0,2,1
танець,0,2,1
спів,0,2,1
плач,5,1,2
сміх,0,2,1
похмурий,5,1,2
сонячний,0,2,1
хмара,5,2,1
спокій,0,1,2
дурний,0,2,1
літаючий,0,2,1
чудовий,0,2,1
нерозділений,0,1,2
троянда,0,1,2
разом,5,2,1
обіцянка,0,2,1
обійми,0,2,1
краса,0,2,1
веселощі,0,2,1
посмішка,0,2,1
зламаний,5,1,2
дорогоцінний,5,2,1
благання,5,1,2
незграбний,0,2,1
прощення,5,1,2
природа,0,2,1
океан,0,2,1
блиск,0,2,1
особливий,5,2,1
музика,5,2,1
щасливий,0,2,1
неудача,5,1,2
гучний,0,2,1
мирний,0,1,2
захоплення,0,1,2
захід сонця,0,2,1
світлячки,0,2,1
райдуга,0,2,1
образа,5,1,2
іскритися,0,2,1
шрами,5,1,2
пустий,5,1,2
дивовижний,0,2,1
горе,0,1,2
обійми,0,1,2
надзвичайний,3,2,1
приголомшливий,0,2,1
поразка,5,1,2
безнадійний,5,1,2
страждання,5,1,2
скарб,0,2,1
блаженство,0,2,1
спогади,3,2,1

#Natsuki's words
милий,2,5,1
пухнастий,2,5,1
чистий,1,5,2
цукерка,2,5,1
покупки,2,5,1
цуцення,2,5,1
кошення,2,5,1
хмари,2,5,1
помада,1,5,2
парфе,2,5,1
полуниця,2,5,1
розовий,2,5,1
шоколад,2,5,1
мить,3,5,2
поцілунок,1,5,2
мелодія,3,5,1
білий бант,3,5,1
жвавий,2,5,1
докі-докі,5,5,1
кавайний,2,5,1
спідниця,2,5,1
щоки,2,5,1
е-мейл,2,5,1
липкий,2,5,1
енергічний,2,5,1
блискучий,2,5,1
гризти,2,5,1
фантазія,1,5,2
цукор,2,5,1
хіхікати,3,5,1
зефір,2,5,1
скакати,2,5,1
класики,3,5,1
тиша,2,5,1
обертання,2,5,1
крутити,2,5,1
льодяник,2,5,1
пуф,2,5,1
бульбашки,2,5,1
шепіт,2,5,1
літо,2,5,1
водоспад,1,5,2
купальник,2,5,1
ваніль,2,5,1
наушники,3,5,1
ігри,5,5,1
шкарпетки,2,5,1
волосся,2,5,1
пісочниця,2,5,1
піжама,1,5,2
ковдра,1,5,2
молоко,2,5,1
губки,2,5,1
злість,5,5,1
тато,2,5,1
валентинка,2,5,1
миша,1,5,2
свист,2,5,1
жмяк,2,5,1
кролик,2,5,1
аніме,2,5,1
стрибати,2,5,1

#Yuri's words
рішучість,5,1,5
суіцид,5,1,5
уява,2,1,5
потайний,2,1,5
життєвість,1,1,5
існування,5,1,5
блискучий,1,1,5
багровий,1,1,5
вихор,1,1,5
післяобраз,0,1,5
запаморочення,1,1,5
дезорієнтація,5,1,5
сутність,2,1,5
обтічний,2,1,5
хмарочос,2,1,5
сум'яття,1,1,5
забруднення,1,1,5
інтелектуальний,1,1,5
аналіз,1,1,5
ентропія,1,1,5
жвавий,1,1,5
нез'ясовний,2,1,5
несумісний,1,1,5
гнів,2,1,5
посланий,2,1,5
бійня,2,1,5
філософія,3,1,5
непостійний,1,1,5
наполегливий,1,1,5
аура,2,1,5
нестійкий,1,1,5
інферно,2,1,5
нездатний,5,1,5
доля,5,1,5
непогрішний,1,1,5
болісний,2,1,5
розбіжність,5,1,5
неконтрольований,5,1,5
екстремальний,2,1,5
тікати,5,1,5
мрія,2,2,5
катастрофа,5,1,5
мальовничий,2,1,5
пишучий,1,2,5
питання,0,2,5
нарив,2,1,5
застереження,2,1,5
клітина,5,2,5
вибухати,1,2,5
насолода,0,2,5
хіть,1,2,5
відчуття,1,2,5
кульмінація,1,2,5
електрика,1,2,5
зрікатися,1,1,5
зневажати,5,1,5
нескінченний,5,1,5
вічність,5,1,5
час,2,1,5
всесвіт,3,1,5
нескінченний,2,1,5
краплі,0,1,5
жадати,1,1,5
нестримний,1,1,5
пейзаж,2,1,5
портрет,2,1,5
подорож,2,1,5
убогий,1,1,5
занепокоєння,5,1,5
лякаючий,5,1,5
жах,0,1,5
меланхолія,5,1,5
проникливість,2,1,5
викуплення,2,1,5
дихати,1,2,5
бранець,2,1,5
бажання,5,2,5
цвинтар,0,1,5

#Monika words!
допомога,5,1,1
реальність,5,1,1
помилка,5,1,1
жаль,5,1,1
файли,5,1,1
код,5,1,1
стіна,5,1,1
застряглий,5,1,1
смарагдовий,5,1,1
вибач,5,1,1
втрачений,5,1,1
безмежний,5,1,1
нестача,5,1,1
"""
    for line in wordfile.split("\n"):
        
        line = line.strip()
        
        if line == '' or line[0] == '#': continue
        
        
        x = line.split(',')
        full_wordlist.append(PoemWord(x[0], float(x[1]), float(x[2]), float(x[3])))

    seen_eyes_this_chapter = False
    sayoriTime = renpy.random.random() * 4 + 4
    natsukiTime = renpy.random.random() * 4 + 4
    yuriTime = renpy.random.random() * 4 + 4
    monikaTime = renpy.random.random() * 4 + 4
    sayoriPos = 0
    natsukiPos = 0
    yuriPos = 0
    monikaPos = 0
    sayoriOffset = 0
    natsukiOffset = 0
    yuriOffset = 0
    monikaOffset = 0
    sayoriZoom = 1
    natsukiZoom = 1
    yuriZoom = 1
    monikaZoom = 1



    def randomPauseSayori(trans, st, at):
        if st > sayoriTime:
            global sayoriTime
            sayoriTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomPauseNatsuki(trans, st, at):
        if st > natsukiTime:
            global natsukiTime
            natsukiTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomPauseYuri(trans, st, at):
        if st > yuriTime:
            global yuriTime
            yuriTime = renpy.random.random() * 4 + 4
            return None
        return 0


    def randomPauseMonika(trans, st, at):
        if st > monikaTime:
            global monikaTime
            monikaTime = renpy.random.random() * 4 + 4
            return None
        return 0


    def randomMoveSayori(trans, st, at):
        global sayoriPos
        global sayoriOffset
        global sayoriZoom
        if st > .16:
            if sayoriPos > 0:
                sayoriPos = renpy.random.randint(-1,0)
            elif sayoriPos < 0:
                sayoriPos = renpy.random.randint(0,1)
            else:
                sayoriPos = renpy.random.randint(-1,1)
            if trans.xoffset * sayoriPos > 5: sayoriPos *= -1
            return None
        if sayoriPos > 0:
            trans.xzoom = -1
        elif sayoriPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * sayoriPos
        sayoriOffset = trans.xoffset
        sayoriZoom = trans.xzoom
        return 0

    def randomMoveNatsuki(trans, st, at):
        global natsukiPos
        global natsukiOffset
        global natsukiZoom
        if st > .16:
            if natsukiPos > 0:
                natsukiPos = renpy.random.randint(-1,0)
            elif natsukiPos < 0:
                natsukiPos = renpy.random.randint(0,1)
            else:
                natsukiPos = renpy.random.randint(-1,1)
            if trans.xoffset * natsukiPos > 5: natsukiPos *= -1
            return None
        if natsukiPos > 0:
            trans.xzoom = -1
        elif natsukiPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * natsukiPos
        natsukiOffset = trans.xoffset
        natsukiZoom = trans.xzoom
        return 0

    def randomMoveYuri(trans, st, at):
        global yuriPos
        global yuriOffset
        global yuriZoom
        if st > .16:
            if yuriPos > 0:
                yuriPos = renpy.random.randint(-1,0)
            elif yuriPos < 0:
                yuriPos = renpy.random.randint(0,1)
            else:
                yuriPos = renpy.random.randint(-1,1)
            if trans.xoffset * yuriPos > 5: yuriPos *= -1
            return None
        if yuriPos > 0:
            trans.xzoom = -1
        elif yuriPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * yuriPos
        yuriOffset = trans.xoffset
        yuriZoom = trans.xzoom
        return 0

    def randomMoveMonika(trans, st, at):
        global monikaPos
        global monikaOffset
        global monikaZoom
        if st > .16:
            if monikaPos > 0:
                monikaPos = renpy.random.randint(-1,0)
            elif monikaPos < 0:
                monikaPos = renpy.random.randint(0,1)
            else:
                monikaPos = renpy.random.randint(-1,1)
            if trans.xoffset * monikaPos > 5: monikaPos *= -1
            return None
        if monikaPos > 0:
            trans.xzoom = -1
        elif monikaPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * monikaPos
        monikaOffset = trans.xoffset
        monikaZoom = trans.xzoom
        return 0



label poem(transition=True, music_swap=True):
    if music_swap:
        stop music fadeout 2.0 



    scene bg notebook
    show screen quick_menu

    show m_sticker at sticker_mid

    if transition:
        with dissolve_scene_full

    if music_swap:
        play music t4 

    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False

    python:
        poemgame_glitch = False
        played_baa = False
        progress = 1
        numWords = 20
        sPointTotal = 0
        nPointTotal = 0
        yPointTotal = 0
        wordlist = list(full_wordlist)

        sayoriTime = renpy.random.random() * 4 + 4
        natsukiTime = renpy.random.random() * 4 + 4
        yuriTime = renpy.random.random() * 4 + 4
        sayoriPos = renpy.random.randint(-1,1)
        natsukiPos = renpy.random.randint(-1,1)
        yuriPos = renpy.random.randint(-1,1)
        sayoriOffset = 0
        natsukiOffset = 0
        yuriOffset = 0
        sayoriZoom = 1
        natsukiZoom = 1
        yuriZoom = 1





        while True:
            ystart = 160
            
            pstring = str(progress)
            ui.text(pstring + "/" + str(numWords), style="poemgame_text", xpos=810, ypos=80, color='#000')
            for j in range(2):
                if j == 0: x = 440
                else: x = 680
                ui.vbox()
                for i in range(5):
                    
                    
                    word = random.choice(wordlist)
                    wordlist.remove(word)
                    ui.textbutton(word.word, clicked=ui.returns(word), text_style="poemgame_text", xpos=x, ypos=i * 56 + ystart)
                ui.close()
            
            t = ui.interact()
            
            renpy.play(gui.activate_sound)
            
            if t.sPoint >= 3:
                renpy.show("m_sticker hop")
                sPointTotal += t.sPoint
            
            
            
            
            progress += 1
            if progress > numWords:
                break 
    $ poem += 1
    if sPointTotal >= 65:
        if poem == 1:
            $ poem1like = True
        if poem == 2:
            $ poem2like = True


    $ config.allow_skipping = config.developer
    $ allow_skipping = config.developer
    if music_swap:
        stop music fadeout 2.0
    hide screen quick_menu
    show black as fadeout:
        alpha 0
        linear 1.0 alpha 1.0
    pause 1.0
    return



image bg eyes_move:
    "images/bg/eyes.png"
    parallel:
        yoffset 720 ytile 2
        linear 0.5 yoffset 0
        repeat
    parallel:
        0.1
        choice:
            xoffset 20
            0.05
            xoffset 0
        choice:
            xoffset 0
        repeat
image bg eyes:
    "images/bg/eyes.png"


image s_sticker:
    "gui/poemgame/s_sticker_1.png"
    xoffset sayoriOffset xzoom sayoriZoom
    block:
        function randomPauseSayori
        parallel:
            sticker_move_n
        parallel:
            function randomMoveSayori
        repeat

image n_sticker:
    "gui/poemgame/n_sticker_1.png"
    xoffset natsukiOffset xzoom natsukiZoom
    block:
        function randomPauseNatsuki
        parallel:
            sticker_move_n
        parallel:
            function randomMoveNatsuki
        repeat

image y_sticker:
    "gui/poemgame/y_sticker_1.png"
    xoffset yuriOffset xzoom yuriZoom
    block:
        function randomPauseYuri
        parallel:
            sticker_move_n
        parallel:
            function randomMoveYuri
        repeat

image y_sticker_cut:
    "gui/poemgame/y_sticker_cut_1.png"
    xoffset yuriOffset xzoom yuriZoom
    block:
        function randomPauseYuri
        parallel:
            sticker_move_n
        parallel:
            function randomMoveYuri
        repeat

image m_sticker:
    "gui/poemgame/m_sticker_1.png"
    xoffset monikaOffset xzoom monikaZoom
    block:
        function randomPauseMonika
        parallel:
            sticker_move_n
        parallel:
            function randomMoveMonika
        repeat


image s_sticker hop:
    "gui/poemgame/s_sticker_2.png"
    xoffset sayoriOffset xzoom sayoriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "s_sticker"

image n_sticker hop:
    "gui/poemgame/n_sticker_2.png"
    xoffset natsukiOffset xzoom natsukiZoom
    sticker_hop
    xoffset 0 xzoom 1
    "n_sticker"

image y_sticker hop:
    "gui/poemgame/y_sticker_2.png"
    xoffset yuriOffset xzoom yuriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker"

image y_sticker_cut hop:
    "gui/poemgame/y_sticker_cut_2.png"
    xoffset yuriOffset xzoom yuriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker_cut"


image y_sticker hopg:
    "gui/poemgame/y_sticker_2g.png"
    xoffset yuriOffset xzoom yuriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker"

image m_sticker hop:
    choice:
        "gui/poemgame/m_sticker_2.png"
    choice:
        "m_sticker_hop_horror"
    xoffset monikaOffset xzoom monikaZoom
    sticker_hop
    xoffset 0 xzoom 1
    "m_sticker"

image m_sticker_hop_horror:
    choice:
        "m_sticker_glitch1"
    choice:
        "m_sticker_glitch2"

image m_sticker_glitch1:
    choice:
        "gui/poemgame/m_sticker_2.png"
    choice:
        "gui/poemgame/m_sticker_2.png"
    choice:
        "gui/poemgame/m_sticker_2.png"
    choice:
        "gui/poemgame/m_sticker_2.png"
    choice:
        "gui/poemgame/m_sticker_2.png"
    choice:
        "gui/poemgame/m_sticker_2.png"
    choice:
        "gui/poemgame/m_sticker_2.png"
    choice:
        "gui/poemgame/m_sticker_2.png"
    choice:
        "gui/poemgame/m_sticker_2.png"
    choice:
        "mod_assets/m_sticker_glitch1.png"

image m_sticker_glitch2:
    choice:
        "gui/poemgame/m_sticker_2.png"
    choice:
        "gui/poemgame/m_sticker_2.png"
    choice:
        "gui/poemgame/m_sticker_2.png"
    choice:
        "gui/poemgame/m_sticker_2.png"
    choice:
        "gui/poemgame/m_sticker_2.png"
    choice:
        "gui/poemgame/m_sticker_2.png"
    choice:
        "gui/poemgame/m_sticker_2.png"
    choice:
        "gui/poemgame/m_sticker_2.png"
    choice:
        "gui/poemgame/m_sticker_2.png"
    choice:
        "mod_assets/m_sticker_glitch2.png"


image y_sticker glitch:
    "gui/poemgame/y_sticker_1_broken.png"
    xoffset yuriOffset xzoom yuriZoom zoom 3.0
    block:
        function randomPauseYuri
        parallel:
            sticker_move_n
        parallel:
            function randomMoveYuri
        repeat


transform sticker_left:
    xcenter 100 yalign 0.9 subpixel True

transform sticker_mid:
    xcenter 220 yalign 0.9 subpixel True

transform sticker_right:
    xcenter 340 yalign 0.9 subpixel True

transform sticker_glitch:
    xcenter 50 yalign 1.8 subpixel True

transform sticker_m_glitch:
    xcenter 100 yalign 1.35 subpixel True

transform sticker_move_n:
    easein_quad .08 yoffset -15
    easeout_quad .08 yoffset 0

transform sticker_hop:
    easein_quad .18 yoffset -80
    easeout_quad .18 yoffset 0
    easein_quad .18 yoffset -80
    easeout_quad .18 yoffset 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
