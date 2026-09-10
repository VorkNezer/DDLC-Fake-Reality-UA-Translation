


init python:


    def HKBHideButtons():
        
        
        
        if mas_HKBIsVisible():
            config.overlay_screens.remove("hkb_overlay")
            renpy.hide_screen("hkb_overlay")



    def HKBShowButtons():
        
        
        
        if not mas_HKBIsVisible():
            config.overlay_screens.append("hkb_overlay")


    def mas_HKBRaiseShield():
        """RUNTIME ONLY
        Disables the hotkey buttons
        """
        store.hkb_button.talk_enabled = False
        store.hkb_button.music_enabled = False
        store.hkb_button.play_enabled = False


    def mas_HKBDropShield():
        """RUNTIME ONLY
        Enables the hotkey buttons
        """
        store.hkb_button.talk_enabled = True
        store.hkb_button.music_enabled = True
        store.hkb_button.play_enabled = True


    def mas_HKBIsEnabled():
        """
        RETURNS: True if all the buttons are enabled, False otherwise
        """
        return (
            store.hkb_button.talk_enabled
            and store.hkb_button.music_enabled
            and store.hkb_button.play_enabled
        )


    def mas_HKBIsVisible():
        """
        RETURNS: True if teh Hotkey buttons are visible, False otherwise
        """
        return "hkb_overlay" in config.overlay_screens


init -1 python in hkb_button:


    talk_enabled = True


    music_enabled = True


    play_enabled = True


    movie_buttons_enabled = False







define gui.hkb_button_width = 120
define gui.hkb_button_height = None
define gui.hkb_button_tile = False

define gui.hkb_button_text_font = gui.default_font
define gui.hkb_button_text_size = gui.text_size
define gui.hkb_button_text_xalign = 0.5

define gui.hkb_button_text_idle_color = "#000"
define gui.hkb_button_text_hover_color = "#fa9"
define gui.hkb_button_text_kerning = 0.2



style hkb_vbox is vbox
style hkb_button is button
style hkb_button_text is button_text

style hkb_vbox:
    spacing 0

style hkb_button is default:
    properties gui.button_properties("hkb_button")
    idle_background "mod_assets/hkb_idle_background.png"
    hover_background "mod_assets/hkb_hover_background.png"
    ypadding 5

    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style hkb_button_text is default:
    properties gui.button_text_properties("hkb_button")
    outlines []


style hkbd_vbox is vbox
style hkbd_button is button
style hkbd_button_text is button_text

style hkbd_vbox:
    spacing 0

style hkbd_button is default:
    properties gui.button_properties("hkb_button")
    idle_background "mod_assets/hkb_disabled_background.png"
    hover_background "mod_assets/hkb_disabled_background.png"

style hkbd_button_text is default:

    font gui.default_font
    size gui.text_size
    idle_color "#000"
    hover_color "#000"
    kerning 0.2
    outlines []

style hkb_text is default:
    xalign 0.5
    size gui.text_size
    font gui.default_font
    color "#000"
    kerning 0.2
    outlines []

screen hkb_overlay():

    zorder 50

    style_prefix "hkb"

    vbox:
        xpos 0.05

        ypos 0.80








        if store.hkb_button.talk_enabled:
            textbutton _("Button 1") action Function(button_one)
        else:
            frame:
                ypadding 5
                xsize 120

                background Image("mod_assets/hkb_disabled_background.png")
                text "Button 1"


        if store.hkb_button.music_enabled:
            textbutton _("Button 2") action Function(button_two)
        else:
            frame:
                ypadding 5
                xsize 120

                background Image("mod_assets/hkb_disabled_background.png")
                text "Button 2"


        if store.hkb_button.play_enabled:
            textbutton _("Button 3") action Function(button_thr)
        else:
            frame:
                ypadding 5
                xsize 120

                background Image("mod_assets/hkb_disabled_background.png")
                text "Button 3"


init python:

    def button_one():
        """
        Handler for the first button 
        This one works as a python function callback
        """
        renpy.call_in_new_context("button_one_label")


    def button_two():
        """
        Handler for the second button 
        This one works as a python function callback
        """
        renpy.call_in_new_context("button_two_label")


    def button_thr():
        """
        Handler for the third button 
        This one works as a python function callback
        """
        renpy.call_in_new_context("button_thr_label")


label button_one_label:
    m "You clicked button 1!"
    return

label button_two_label:
    m "You clicked button 2!"
    return

label button_thr_label:
    m "You clicked button 3!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
