# The script of the game goes in this file.

# Characters
define narration = Character(what_color="#cce")
define kuma = Character("Kuma", color="#cce")
define katia_unnamed = Character("???", color="#e4a8be")
define katia = Character("Katia", color="#e4a8be")

# The game starts here.
label start:
    play music "audio/music/exploring.wav"
    show screen chapter_display
    scene bg street 1 at center:
        zoom 1.5
    show bear cute at center
    with fade
    narration "I am Kuma. I am cute bear."
    narration "One day, someone bumped into me."

    voice "audio/voice/katia_some_assistance.wav"
    katia_unnamed "Pardon me, I need some assistance."


    show bear cute at left
    with move

    show katia normal:
        xalign 2.0
        yalign 1.0
    with dissolve
    katia_unnamed "Could you provide directions to the plaza? I'm entirely lost."

    # A decision choice!
    menu:
        "I would love to help!":
            jump help_katia
        "I don't meddle with demons.":
            jump leave_katia

# Kuma helps Katia find the plaza
label help_katia:
    kuma "Sure! I would love to help you =D"

    show katia normal at center
    with move
    voice "audio/voice/katia_my_friends_call_me.wav"
    katia "My friends call me Katia Yurievna by the way. I'm glad to meet you."

    narration "And so, Katia and the cute bear go to the plaza."
    narration "They have a wonderful time there, and they become the best of
    friends."

    scene bg black with dissolve
    "{b}Good end.{/b}"
    return

label leave_katia:
    kuma "I don't meddle with the affairs of demons =("

    show katia at right:
        xalign 2.0
        yalign 1.0
    with move
    voice "audio/voice/katia_i_am_not_a_demon.wav"
    katia_unnamed "I beg your pardon...! I am not a demon. I am a kindly devil! There is a
    great difference."

    hide katia with dissolve
    "And so, Katia storms off angrily, having apparently forgotten
    what she was here for in the first place."

    scene bg black with dissolve
    "{b}Bad end.{/b}"
    return
