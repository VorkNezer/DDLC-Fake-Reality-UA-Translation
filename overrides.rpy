






init 10 python:
    pass




init 501 python:
    pass






init python:
    if persistent.playgame == 1 or persistent.playgame == 2:
        config.main_menu_music = audio.ghostmenu
    elif persistent.playgame == 3:
        config.main_menu_music = audio.tmonika
    else:
        config.main_menu_music = audio.t1
    pass






python early:
    pass
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
