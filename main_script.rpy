
label start_mod:
    scene black
    with dissolve_scene_half
    stop music fadeout 10
    python:
        try: renpy.file(config.basedir + "/credits.txt")
        except: open(config.basedir + "/credits.txt", "wb").write(renpy.file("advanced_scripts/credits.txt").read())
    $ style.say_dialogue = style.default_monika
    $ config.allow_skipping = config.developer
    pause 2

    python:
        process_list = []
        currentuser = ""
        if renpy.windows:
            try:
                process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
            except:
                pass
            try:
                for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                    user = os.environ.get(name)
                    if user:
                        currentuser = user
                        persistent.user_found = True
                        player = currentuser
                        persistent.playername = player
            except:
                pass

    $ renpy.save_persistent()

    if persistent.playgame == 0:

        menu:
            "Чій рут ти вибрав в оригінальній грі?"
            "Сайорі":
                $ persistent.gameroute = "sayori"
                if renpy.random.randint(0,9) == 0:
                    "Молодець."
            "Нацукі":
                $ persistent.gameroute = "natsuki"
            "Юрі":
                $ persistent.gameroute = "yuri"
            "Всіх (хороша кінцівка)":
                "Значить, ти отримав так звану «хорошу» кінцівку, так?"
                "Цікаво."
                $ persistent.gameroute = "multiple"

    $ persistent.playgame = 1

    $ autosave()
    pause 5
    "Ем... ти мене чуєш?"
    pause 5
    "Ти чуєш мене?"
    pause 5
    show screen yes_no(message="Ти мене чуєш?", yes_action=Jump("confirm_yes"), no_action=Jump("confirm_no"))
    "{cps=5}Ти мене чуєш?{/cps}"
    return


label confirm_no:
    hide screen yes_no
    "Тоді як ти зміг відповісти?"
    $ renpy.quit()

label confirm_yes:
    hide screen yes_no
    "Цей мод може стати джерелом моральних страждань."
    menu:
        "Ти хочеш потратити декілька годин свого часу заради того, щоб пройти через цей кошмар?"
        "Так":
            show screen yes_no(message="Ти впевнений?", yes_action=Jump("confirm_yes2"), no_action=Jump("confirm_no"))
            ""
        "Ні":
            call confirm_no2 from _call_confirm_no2
    return

label confirm_no2:
    hide screen yes_no
    "Прекрасно."
    "Так буде краще для тебе."
    $ renpy.quit()

label confirm_yes2:
    hide screen yes_no
    "Ну добре."
    "Не говори потім, що тебе не попереджали, малий."
    jump day1_act1

label end_label:
    $ s_safe = False
    $ n_safe = False
    $ y_safe = False
    $ m_safe = False

    python:
        if persistent.gameend == True:
            try: open(config.basedir + "/characters/monika.chr", "r")
            except: m_safe = False
            else: m_safe = True
            try: open(config.basedir + "/characters/natsuki.chr", "r")
            except: n_safe = False
            else: n_safe = True
            try: open(config.basedir + "/characters/yuri.chr", "r")
            except: y_safe = False
            else: y_safe = True
            try: open(config.basedir + "/characters/sayori.chr", "r")
            except: s_safe = False
            else: s_safe = True
            pass
    if s_safe == True and n_safe == True and y_safe == True and m_safe == True:
        call true_end_mod from _call_true_end_mod
    else:
        scene final_image with dissolve_slow
        $ pause()
    $ renpy.quit()

label true_end_mod:

    $ s_name = "Сайорі"
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full

    play music t2
    "Звичайний будній день, схожий на любий інший."
    "Як зазвичай, мене оточували парочки і компанії друзів, що йдуть до школи."
    "Я постійно твердив собі, що одного разу познайомлюся з дівчатами чи щось у тому ж дусі..."
    show sayori 1a at t11
    s "Ей, [player]..."
    "...Що ж, одна дівчина вже є."
    "Її звуть Сайорі, вона моя подруга дитинства, і ми живемо по сусідству."
    "Ми завжди ходили до школи разом..."
    "...і останнім часом ми відродили цю традицію."
    s "[player], ти мною пишаєшся?"
    mc "Е? Чого б це?"
    s 1c "Ти що, не замітив?"
    s "Я стала прокидатись вчасно!"
    mc "Помітив, ти вже давно це робиш..."
    s 1l "Е-хе-хе!"
    s 4h "Але ти ніколи так про це нічого і не сказав!"
    show sayori at s11
    s "Хоча ми щодня разом ходимо до школи..."
    mc "Ну, так..."
    mc "Я завжди вважав, що це щось зрозуміле."
    mc "Мені ніяково говорити про це вголос."
    s 1d "Ну, будь ласка."
    s "Це чудово мотивує~"
    mc "добре, добре..."
    mc "Я пишаюсь тобою, Сайорі."
    show sayori at t11
    s 1q "Е-хе-хе~"
    show sayori zorder 1 at thide
    hide sayori
    "Ми перейшли вулицю і попрямували до школи."
    "У міру нашого наближення до школи вулиці все більше заповнювалися іншими учнями, які здійснюють свою щоденну прощу.."
    show sayori 3a zorder 2 at t11
    s "Доречі, [player]..."
    s "Ти вже вирішив, до якого клубу вступиш?"
    mc "Клуб?"
    mc "Я ж уже казав, мене клуби—"
    "Я вже хотів сказати свою улюблену фарзу, що клуби мене не цікавлять..."
    "Но щось мені підказало, що зараз Сайорі може на це дуже сильно образитись."
    "В кінці кінців, як я можу сказати їй, що клуби - це марна трата часу..."
    "...коли вона вирішила створити свій власний?"
    mc "...Взагалі-то, так."
    mc "Думаю, я прийняв рішення."
    show sayori at h11
    s 1m "Серйозно?!"
    s 1r "І яке ж? Скажи-скажи!"
    mc "Хм-м..."
    mc "Хай це буде сюрпризом."
    s 5d "Бу-у..."
    s "Злюка."
    mc "Прояви терпіння, скоро ти дізнаєшся."
    "Я задався питанням, чому я дозволяю звітувати себе настільки безтурботній дівчинці."
    "Але я почав розуміти, що в певної міри їй заздрю."
    "Коли Сайорі ставить собі ціль, вна здатна на великі справи."
    "Тому я відчуваю, що повинен зробити для неї що-небуть особливе."

    scene bg class_day
    with wipeleft_scene

    "Цілком звичайний день у школі непомітно добіг кінця."
    "Склавши речі в портфель, я зібрав всю мотивацію і встав."
    mc "Що ж, подивимось..."
    stop music fadeout 2.0

    scene bg corridor
    with wipeleft_scene
    "Я згадав номер кімнати, який бачив на листівці."
    "І пішов по шкільним коридорам і драбинам. У цьому крилі, відданому під навчальні класи третьорічок та клуби, я бував нечасто."
    "Не встиг я зрозуміти, як уже стояв перед потрібною кімнатою."
    "Я боязко відкрив двері."
    scene bg club_day
    with wipeleft
    play music t3
    mc "Здраствуйте?.."
    show sayori 1m at t32
    s "Ах!"
    s "[player]?!"
    s 1c "Щ-що ти тут робиш?"
    mc "Ну... Я просто..."
    "Е? Я обвів кімнату поглядом."
    show natsuki 3a at f31
    n "А-а."
    n "Так ти і є той самий [player], про якого Сайорі говорить без зупину?"
    show natsuki at t31
    show yuri 2t at f33
    y "Д-дякую, що глянув!"
    y 2m "Рада знайомству, [player]."
    y "Ми всі перебуваємо у літературному клубі."
    y 3v "Н-надіюсь, тобі тут сподобається!"
    show yuri at t33
    show natsuki at f31
    n 3g "Та гаразд тобі, Юрі..."
    n "Навіщо такий офіціоз?"
    n "Раптом він подумає, що ми і справді такі суворі чи типу того?.."
    show natsuki at t31
    $ y_name = "Юрі"
    $ n_name = "Нацукі"
    show yuri at f33
    y 3q "Ах..."
    y "Пробач, Нацукі..."
    show yuri at t33
    "Сама висока дівчина, котру звати, мабуть, Юрі, виглядає досить сором'язливою."
    "По зрівняннб з нею, дівчина по імені Нацукі, попри свій ріст, здається більш впевненою в собі."
    mc "Ем, приємно познайомитись."
    mc "Буду радий вашому суспільству."
    show sayori at f32
    s 1n "Н-нашому суспільству?.."
    s 1b "[player], невже..."
    s "Ти..."
    show sayori at t32
    mc "Вірно."
    mc "Клуб, до якого я вирішив вступити, – твій клуб, Сайорі."
    mc "Літературний клуб."
    "Очі Сайорі спалахнули."
    show sayori at f32
    s 1n "...Не може бути."
    s 1s "Не може бути!"
    show sayori at hf32
    s 4s "А-а-ах-ха-ха!"
    "Вона обхопила мене руками та застрибала від щастя."
    show sayori at t32
    mc "Е-ей!"
    show natsuki at f31
    n 3y "Е-хе-хе."
    n "Ну, коли Сайорі так радіє, я впевнена, що буде непогано, якщо ти до нас приєднаєшся."
    show natsuki 3a at t31
    show yuri at f33
    y 1s "Не кажучи вже про те, що нас тепер четверо."
    y "Це означає, що ми можемо стати офіційно зареєстрованим клубом."
    show yuri at t33
    show sayori at f32
    s 1x "У мене нема слів!"
    s "Це треба відзначити!"
    show sayori at t32
    show yuri at f33
    y 1m "Хе-хе."
    y "Який придатний для цього день, чи не так?"
    show yuri 1a at t33
    show sayori at f32
    s 1r "Ага!"
    s 1x "В кінці кінців, Нацукі вирішила—"
    show sayori at t32
    show natsuki at f31
    n 1w "Ей, не псуй сюрприз!"
    show natsuki at t31
    show sayori at f32
    s 5a "Е-хе-хе, пробач..."
    show sayori at t32
    show natsuki at f31
    n 1k "Сідайте, будь ласка, за стіл."
    show natsuki at t31
    show yuri at f33
    y 1a "Тоді, може, я заварю більше чаю?"
    hide sayori
    hide natsuki
    hide yuri
    with wipeleft
    "Дівчата зрушили кілька парт, щоби зробити великий стіл."
    "Нацукі з Юрі попрямували в куток кімнати, там Нацукі взяла накритий скатертиною підніс, а Юрі відчинила комору."
    "Все ще відчуваючи себе ніяково, я присів поряд з Сайорі."
    "Нацукі гордовито пройшла до столу з підносом у руці."
    show natsuki 2z zorder 2 at t22
    n "Та-а-ак, ви готові?"
    n "...Та-да-а-а!"
    show sayori 4m zorder 2 at t21
    s "Ого!"
    "Нацукі відкинула скатертину, під нею опинилося багато білих пишних кексів у формі кошенят."
    "Вусики були намальовані глазур'ю, а шматочки шоколаду утворювали вушка."
    show sayori at f21
    s 4r "Яка краса~!"
    show sayori at t21
    mc "Ух ти, виглядає приголомшливо."
    show natsuki at f22
    n 2d "Е-хе-хе. Ну, знаєшь..."
    n "Коротше, поспішіть і їжте вже!"
    show natsuki at t22
    "Першою кекс взяла Сайорі, я наслідував її приклад."
    show sayori at f21
    s 4q "Як фмафно!"
    show sayori at t21
    "Промимрила Сайорі з набитим ротом, вона вже встигла вимазати обличчя в глазурі."
    "Я покрутив кекс у руці, придивляючись, з якого боку його відкусити."
    show sayori zorder 1 at thide
    hide sayori
    show natsuki 1c zorder 2 at t32
    "Нацукі затихла."
    "Я не міг не помітити, як вона крадькома кидає погляди в мій бік."
    "Вона чекає, коли спробую?"
    "Нарешті я трохи відкусив."
    "Глазур солодка, з багатим насиченим смаком. Цікаво, чи вона сама її приготувала?"
    mc "Дуже смачно."
    mc "Дякую, Нацукі."
    n 42c "Кхем... Звісно смачно!"
    n "Як не як, я профі!"
    n 42a "Зовсім не треба мені дякувати..."
    show natsuki zorder 1 at thide
    hide natsuki
    "Поки Нацукі приймала компліменти, Юрі повернулася до столу, несучи в руках чайний сервіз."
    "Вона акуратно розставила перед нами чашки, чайник розмістився поруч із підносом."
    show yuri 1a zorder 2 at t11
    mc "Ти зберігаєш у класі цілий чайний сервіз?"
    y "Не хвилюйся, ми отримали дозвіл від учителів."
    y "І потім, гаряча чашка чаю допомагає насолодитися гарною книгою, згоден?"
    mc "А-а... м-мабуть..."
    show natsuki 2y at f31
    n "Е-хе-хе. Ти вже намагаєшся справити враження на нашого нового члена, Юрі?"
    show natsuki at t31
    show yuri at f11
    y 3n "Е-е?! Я зовсім не..."
    show yuri at t11
    show natsuki at thide
    hide natsuki
    "Юрі ображено відвернулася."
    y 4b "Я просто хотіла сказати, тобто..."
    mc "Я згоден з тобою."
    mc "Хоч я не книголюб і чай п'ю нечасто, я ніколи не проти їм пригоститися."
    y 2u "Я рада..."
    "Юрі ледь помітно посміхнулася, явно відчувши полегшення."
    y 1a "Слухай, [player], а що ти зазвичай читаєш?"
    mc "Ну... Е-е-е..."
    "Враховуючи те, як мало я читав останніми роками, мене таке питання поставило в глухий кут."
    mc "...Мангу..."
    "Промимрив я про себе ніби жартома."
    show natsuki 1c zorder 2 at t41
    "Нацукі раптом різко смикнула головою."
    "Схоже, вона хотіла щось сказати, але так і не наважилася."
    show natsuki zorder 1 at thide
    hide natsuki
    y 3u "В-видимо, ти не з книголюбів..."
    mc "...Ну, я можу змінитись..."
    "Що я несу?"
    "Я випалив це не подумавши, як побачив сумну посмішку Юрі."
    mc "А що нарахунок тебе, Юрі?"
    y 1l "Хм-м, треба подумати..."
    "Юрі провела пальцем по краєчку чашки."
    y 1a "Найбільше я люблю романи, в яких описуються глибокі та складні фентезійні світи."
    y "Мистецтво описів та творчий розмах у них просто неймовірні."
    y 1f "А історії, що відбуваються в паралельних всесвітах, затягують тебе з головою і дарують безліч вражень."
    "Було видно, з якою пристрастю Юрі розповідала про свої улюблені книги."
    "Перше моє враження про неї склалося як про сором'язливу і скромну дівчину, але, бачачи, як горять її очі, я розумію, що їй набагато комфортніше серед книг, ніж серед людей."
    y 2m "Але, взагалі-то, мені багато що подобається."
    y 2a "Не хвилюйся, якщо ти не так багато читаєш, гаразд?"
    y "Впевнена, що ми зможемо знайти те, що нас об'єднує."
    show yuri at t22
    show natsuki 2c at f21
    n "Ей, Юрі..."
    show natsuki at t21
    show yuri at f22
    y 2f "А?"
    show yuri at t22
    show natsuki at f21
    n 2h "Ну, про це... знаєш, перше, що він сказав..."
    show natsuki at t21
    mc "Манга?"
    show yuri at f22
    y 2i "Так, вірно..."
    y "Нацукі, як правило, читає у клубі мангу—"
    show yuri at t22
    show natsuki at f21
    n 1r "Ей, не розмовляй, коли не просять!!!"
    "Нацукі чомусь виглядає збентеженою."
    n 1q "Крім того..."
    n "Манга... це теж література, як не крути."
    n 1w "Тому... якщо [player] захоче взяти щось почитати з моєї манги, не надумайте йому заважати!"
    show natsuki 1i at t21
    show yuri at f22
    y 1l "Нацукі..."
    y "Я би цього не зробила."
    y 1i "Проте було б непогано розвиватися дещо різнобічно."
    y "Він може скористатися цією можливістю, щоб спробувати щось нове."
    y 1s "Ти не проти, [player]?"
    show yuri at t33
    show natsuki at t32
    show sayori 1l at f31
    s "М-може..."
    "Відчувши наростаючу напругу, Сайорі приєдналася до розмови."
    s 1x "Може, нам усім спробувати щось нове?!"
    s 1l "Думаю, це буде цікаво..."
    s 1c "І всі ми трохи краще впізнаємо один одного!"
    s 1l "Я хочу сказати..."
    s "...для цього літературні клуби і потрібні... вірно?"
    show sayori at t31
    show yuri at f33
    y 1v "..."
    y "Я... я не проти..."
    show yuri at t33
    show natsuki at f32
    n 2j "Ага..."
    n "Ти, як завжди, маєш рацію, президент."
    show natsuki at t32
    show sayori at f31
    s 1q "Е-хе-хе~"
    show sayori at t31
    show natsuki at f32
    n 2c "Значить, я маю прочитати роман чи щось на кшталт того, так?.."
    show natsuki at t32
    mc "Що ж, нас уже двоє..."
    mc "Я не проти зайнятися цим, якщо це робитиму не один."
    show sayori at thide
    hide sayori
    show natsuki at f21
    show yuri at t22
    n 2y "Що ж до Юрі..."
    show natsuki at t21
    show yuri at f22
    y 2n "А?.."
    y "Я... Я повинна читати мангу?.."
    show yuri at t22
    show natsuki at f21
    n 4i "Боже..."
    n 4h "Адже це ти запропонувала нам всебічно розвиватися!"
    n "Тобі варто бути менш консервативною..."
    n 4u "Це навіть трохи образливо..."
    show natsuki at t21
    show yuri at f22
    y 2t "Образливо?.."
    y 2v "Я... не розумію..."
    y "..."
    "Юрі задумалася, її обличчя набуло винного виразу."
    y 2w "Вибач за неповагу до твого хобі, Нацукі."
    y "Якщо... якщо це так тебе захоплює, я впевнена, що це вартий уваги літературний жанр."
    show yuri at t22
    show natsuki at f21
    n 5q "...Ти це просто так кажеш, з ввічливості?"
    show natsuki at t21
    show yuri at f22
    y "Ні..."
    y "Я зрозуміла свою помилку."
    y 2t "Тому, якщо ти готова спробувати почитати роман..."
    y 2u "...Я буду вдячна, якщо ти підбереш мені якусь мангу."
    show yuri at t22
    show natsuki at f21
    n 1l "Правда?!"
    n 12c "Т-тобто..."
    n "Я... дуже рада, що ти мене про це просиш, Юрі."
    n 2c "Довірся мені, і я підберу те, що справді тобі сподобається."
    show natsuki at t21
    show yuri at f22
    y 1m "Взаємно..."
    y 1h "Я, можливо, після клубу піду до книжкового."
    show yuri at t22
    show natsuki at f21
    n 1q "Ти підеш... одна?"
    show natsuki at t21
    show yuri at f22
    y 3q "А-ах..."
    y 4a "Ти хотіла б... скласти мені компанію?"
    show yuri at t22
    show natsuki at f21
    n 5s "Ну..."
    n "Якщо ти не проти..."
    show natsuki at t21
    show yuri at f22
    y 3t "Ні, звісно ні!"
    y "Просто я завжди ходила туди одна, тож..."
    show yuri at t22
    show natsuki at f21
    n "Так, я теж..."
    show natsuki at t21
    show sayori 4s at l41
    s "Як це мило~!"
    mc "Сайорі, заткнись..."
    show sayori at lhide
    hide sayori
    show natsuki at f21
    n 2j "Там я теж покажу тобі деяку мангу, добре?"
    show natsuki at t21
    show yuri at f22
    y 1a "Так."
    y "Чекаю з нетерпінням."
    show natsuki at thide
    show yuri at thide
    hide natsuki
    hide yuri
    "Нацукі та Юрі почали прибирати зі столу."

    show sayori 1q at t11
    s "Е-хе-хе~"
    s 1x "Що ж, сьогодні наша зустріч закінчена, так?"
    mc "Ага, сходе на це..."
    mc "Приємно бачити, як усі ладнають."
    s 1q "Правда ж, так?"
    s 1d "Мені здається, ти їм сподобався, [player]."
    mc "Думаєш?.."
    mc "Поряд з тобою, Сайорі, всі виглядають трохи щасливішими."
    s 1y "О-ой, [player]~"
    s "Не заставляй мене червоніти!"
    mc "І тим не менш..."
    mc "Я був надзвичайно здивований, коли ти сказала, що вирішила відкрити свій клуб..."
    mc "Но, думаю, ти чудово справляєшся."
    s 1r "Ми збираємося зробити наш клуб найкращим!"
    s 1x "А коли вже ти до нас приєднався, у нас буде ще веселіше."
    stop music fadeout 2.0
    s 1a "Слухай, [player]..."
    s "Я правда хочу тобі подякувати."
    s "Я хочу сказати, це дійсно чудово, що ти приєднався до нас, і таке інше..."
    s "Но... насправі я знала, що ти так поступиш."
    s 1q "Е-хе-хе~"
    s 1a "І ще дещо."
    if persistent.gameroute != "multiple":
        jump mediocre_end
    s 1y "Я...."
    s 1k "Я повинна вибачитись..."
    s 1g "За все, що зробила."
    s 2g "Це було так безглуздо з мого боку."
    s 2u "Я думала, ми тобі взагалі не потрібні, але як я помилилася!"
    show sayori 4w at h11
    s "Я ніколи у своєму житті не робила такої великої помилки!!!"
    s "Навіть після того, що я зробила, ти подарував нам шанс!"
    s "Ти повернув усіх нас назад!"
    s "Я така винна!!!!"
    show sayori 3v at t11
    $ answer = None
    show screen yes_no(message="Пробачиш її?", yes_action=Function(renpy.call, label="yes_answer"), no_action=Function(renpy.call,label= "no_answer"))
    ""
    hide screen yes_no

    if answer == "yes":
        mc "Нічого, Сайорі, я пробачаю тебе."
        s 3t "Дякую!"
        show sayori 4s at h11
        s "Дякую, дякую, дякую тобі!!!~"
        s "Велике-велике спасибі!"
    elif answer == "no":
        mc "Мені шкода, Сайорі, але ти трохи перетнула кордон."
        show sayori 1v at s11
        s "О-ох..."
        s 2k "Напевно, я на це заслуговую, так?"
        s 2i "Но не переживай, [player]!"
        s 2h "Я зможу знову завоювати твою довіру!"
        show sayori 4r at h11
        s "Клянусь!!!"

    s 1x "До речі, я зараз згадала дещо."
    s "Є дехто, кого тобі було б приємно побачити."
    show sayori 1a at t22
    play music tmonika fadein 2
    pause 2
    play sound closet_open
    show monika 1a at l21
    pause 1
    show monika 1b at f21
    m "Ага, ти таки зробив це?"
    m "Ти зміг повернути нас усіх назад."
    m 1n "Щоправда, маю таку підозру, що в тебе все одно не буде способу по-справжньому поговорити з нами."
    show monika 1a at t21

    show sayori 1o at f22
    s "Ну так, творець цього мода не такий талановитий."
    show sayori 1a at t22
    m 3b "До речі, я прочитала твої вірші."
    if poem1like == True:
        m 1b "Мені дуже сподобалося перше."
        m "Воно виявилося досить цікавим."
        if poem2like == True:
            m "І від другого вірша я теж була у захваті!"
        else:
            m 1n "Хоча другий вірш, мені здається, міг вийти і краще."
            m 1k "Втім, ти все одно дуже добре постарався!"
    else:
        if poem2like == True:
            m 1n "Мене трохи розчарувало перше."
            m 1k "Але друге мені дуже сподобалося."
        else:
            m 1n "Мені здається, тобі варто ще трохи попрактикуватись."
            m 1k "Але ти все одно дуже добре постарався!"
    s 2l "Знаєте... я маю пропозицію."
    s 1x "Давайте почнемо все спочатку."
    s "Створимо новий, повний життя світ!"
    show sayori 1a at t22
    show monika 1b at f21
    m "Нову реальність."
    m "І цього разу справжню!"
    m "Що скажете?"
    show monika 1a at t21
    mc "..."
    mc "..."
    mc "..."
    mc "Звучить непогано."

    $ persistent.playgame = 3
    call thanks_for_playing from _call_thanks_for_playing
    $ MainMenu(confirm=False)()
    return

label yes_answer:
    hide screen yes_no
    $ answer = "yes"
    return
label no_answer:
    hide screen yes_no
    $ answer = "no"
    return

label mediocre_end:
    show sayori 1k at t11
    pause 1
    show sayori 1j at t11
    s "Навіщо ти повернув нас назад?"
    s "Тільки не починай нести всю цю марення про те, що ми тобі {i}«потрібні»{/i}."
    s 1i "Ти брешеш, і ти чудово знаєш про це."
    s 1_d "У-у-у-у...."
    s 1_a "У будь-якому разі."
    s 1_b "Нехай навіть я проти такої кінцівки є ще одна людина, яка зі мною не погодиться."
    s 1z "Удачі вам обом."
    show sayori 1_b at lhide
    hide sayori
    play sound closet_open
    pause 0.7
    show monika 3g at l11
    m "Привіт, [player]."
    m 3g "Що сталося? Я тільки-но бачила, як Сайорі вибігла з класу. І по-моєму вона була розлюченою."
    m 1g "Невже ви говорили про...?"
    mc "..."
    m 1o "Ах..."
    m "Я думаю, що такого поняття, як «ідеальна кінцівка», взагалі не існує."
    play music tmonika fadein 2
    m 1n "Але ж ти постарався зробити все, що в твоїх силах."
    m 1k "Ти навіть повернув усіх нас назад."
    m 1l "Ну... майже всіх."
    m "Ми справді небайдужі тобі!"
    m 1e "І за це я дякую тобі."

    m 3b "До речі, я прочитала твої вірші."
    if poem1like == True:
        m 1b "Мені дуже сподобалося перше."
        m "Воно виявилося досить цікавим."
        if poem2like == True:
            m "І від другого вірша я теж була у захваті!"
        else:
            m 1n "Хоча другий вірш, мені здається, міг вийти і краще."
            m 1k "Втім, ти все одно дуже добре постарався!"
    else:
        if poem2like == True:
            m 1n "Мене трохи розчарувало перше."
            m 1k "Але друге мені дуже сподобалося."
        else:
            m 1n "Мені здається, тобі варто ще трохи попрактикуватись."
            m 1k "Але ти все одно дуже добре постарався!"
    m 1k "Но дсить про це."
    m 1e "Ще раз дякую тобі за те, що повернув нас назад."
    m "[player]."
    $ persistent.playgame = 4

    call thanks_for_playing from _call_thanks_for_playing_1
    $ MainMenu(confirm=False)()

label thanks_for_playing:
    $ persistent.autoload = "thanks_for_playing"
    scene tfp with dissolve_white

    $ renpy.pause()
    $ MainMenu(confirm=False)()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
