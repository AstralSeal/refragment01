label cutscene_1 :
    scene black with Dissolve(1.0)
    scene cutscene00 with Dissolve(1.0)
    play sound "audio/UIsound/sumahokessai.mp3" volume 1.0
    scene cutscene01 with Dissolve(1.0)
    $renpy.pause(1, hard=True)
    scene black with Dissolve(1.0)
    jump s2_1
