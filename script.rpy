
label start:


    $ anticheat = persistent.anticheat


    $ chapter = 0


    $ _dismiss_pause = config.developer

    $ nextscene = None

    $ s_name = "Сайорі"
    $ m_name = "Моніка"
    $ n_name = "Нацукі"
    $ y_name = "Юрі"

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ in_sayori_kill = None
    $ allow_skipping = True
    $ config.allow_skipping = True

    if persistent.playgame == 2:
        $ renpy.quit()

    if persistent.playgame != 0:
        if s_safe == True and m_safe == True and y_safe == True and n_safe == True:
            call end_label from _call_end_label
    call start_mod from _call_start_mod
    call please_work_for_the_love_of_god from _call_please_work_for_the_love_of_god
    call start_mod from _call_start_mod_1
    python:
        try: renpy.file(config.basedir + "/save_location.txt")
        except: open(config.basedir + "/save_location.txt", "wb").write(renpy.file("advanced_scripts/save_location.txt").read())
    "If you can see this, I am afraid you'll have to delete all your saves from the location written on the save_location.txt file you just got. Or you can start a new game from the autosave."
    return

label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return


label please_work_for_the_love_of_god:
    call start_mod from _call_start_mod_2
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
