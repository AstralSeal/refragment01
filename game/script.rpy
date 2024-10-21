# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define en = Character(None,color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "eng"')
define th = Character(None,color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "thai"')
init python:
    import os
    # Steam Achievements
    achievement.register("START_GAME")
    achievement.register("START_CH01")
    achievement.register("START_CH02")
    achievement.register("CHOICE_CH02_CORRECTANSWER")
    achievement.register("CHOICE_CH02_WRONGANSWER")
    achievement.register("END_DEMO")

    def get_agree_text():
        if persistent.language == "eng":
            return "Agree"
        elif persistent.language == "thai":
            return "เห็นด้วย"
        else:
            return "Agree/เห็นด้วย"

    def get_disagree_text():
        if persistent.language == "eng":
            return "Disagree"
        elif persistent.language == "thai":
            return "ไม่เห็นด้วย"
        else:
            return "Disagree/ไม่เห็นด้วย"
    
    def get_2_6_choice1():
        if persistent.language == "eng":
            return "Please let me touch your melons"
        elif persistent.language == "thai":
            return "ผมขอจับหน่มน๊มของรุ่นพี่มายะได้ไหมครับ"
        else:
            return ""

    def get_2_6_choice2():
        if persistent.language == "eng":
            return "Please wrap your legs around my neck"
        elif persistent.language == "thai":
            return "ช่วยเอาต้นขามารัดคอผมหน่อยได้ไหมครับ"
        else:
            return "Disagree/ไม่เห็นด้วย"

    def get_choice(s1,s2):
        if persistent.language == "thai":
            return s1
        elif persistent.language == "eng":
            return s2
        else:
            return ""
    
    def is_has_patch(directory):
        for file in os.listdir(directory):
            if file.endswith("patch_installed.txt"):
                persistent.patch_installed = True
                return
        persistent.patch_installed = False
    is_has_patch(renpy.config.gamedir)



# define yuma = Character("ยูมะ", color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])
# define yuno_0 = Character("???", color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])


# define maya_0 = Character("???",image ="maya", color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])
# define student_m_a = Character("นักเรียนชาย A", color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])
# define student_m_b = Character("นักเรียนชาย B", color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])
# define student_m_c = Character("นักเรียนชาย C", color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])

# define student_f_a = Character("นักเรียนหญิง A", color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])
# define student_f_b = Character("นักเรียนหญิง B", color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])
# define student_f_c = Character("นักเรียนหญิง C", color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])

# define everyone = Character("ทุกคน", color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])

# define reika = Character("เรย์กะ", image ="reika" , color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])
# define yuno = Character("ยูโนะ", image ="yuno" , color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])
# define maya = Character("มายะ", image ="maya" , color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])

# define akane = Character("อาคาเนะ", image ="akane" , color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])
# define kazuma = Character("คาซึมะ", image ="kazuma" , color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])
# define risa = Character("ริซะ", image ="risa" , color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])

##############THAI###############################
define yuma_th = Character("ยูมะ", color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "thai"')
define yuno_0_th = Character("???", color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "thai"')
define flying_seal_th = Character("ตู้แมวน้ำบิน", color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "thai"')

define maya_0_th = Character("???",image ="maya", color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "thai"')
define student_m_a_th = Character("นักเรียนชาย A", color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "thai"')
define student_m_b_th = Character("นักเรียนชาย B", color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "thai"')
define student_m_c_th = Character("นักเรียนชาย C", color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "thai"')

define student_f_a_th = Character("นักเรียนหญิง A", color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "thai"')
define student_f_b_th = Character("นักเรียนหญิง B", color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "thai"')
define student_f_c_th = Character("นักเรียนหญิง C", color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "thai"')

define everyone_th = Character("ทุกคน", color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "thai"')

define reika_th = Character("เรกะ", image ="reika" , color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "thai"')
define reika_p_th = Character("เรกะ", image ="reika_p" , color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "thai"')
define reika_c_th = Character("เรกะ", image ="reika_c" , color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "thai"')
define yuno_th = Character("ยูโนะ", image ="yuno" , color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "thai"')
define maya_th = Character("มายะ", image ="maya" , color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "thai"')
define maya_c2_th = Character("มายะ", image ="maya_c2" , color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "thai"')

define akane_th = Character("อากาเนะ", image ="akane" , color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "thai"')
define kazuma_th = Character("คาซึมะ", image ="kazuma" , color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "thai"')
define risa_th = Character("ริสะ", image ="risa" , color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "thai"')

define yuno_p_th = Character("ยูโนะ", image ="yuno_p" , color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "thai"')
define yuno_c_th = Character("ยูโนะ", image ="yuno_c" , color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "thai"')

define student_m_2_th = Character("นักเรียกชาย" , color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "thai"')
define staff_th = Character("พนักงาน" , color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "thai"')
define speaker_th = Character("พิธีกร" , color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "thai"')
################## ENg####################

define yuma_en = Character("Yuuma", color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "eng"')
define yuno_0_en = Character("???", color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "eng"')
define flying_seal_en = Character("Flying Seal Vending Machine ", color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "eng"')

define maya_0_en = Character("???",image ="maya", color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "eng"')
define student_m_a_en = Character("Male Student A", color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "eng"')
define student_m_b_en = Character("Male Student B", color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "eng"')
define student_m_c_en = Character("Male Student C", color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "eng"')

define student_f_a_en = Character("Female Student A", color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "eng"')
define student_f_b_en = Character("Female Student B", color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "eng"')
define student_f_c_en = Character("Female Student C", color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "eng"')

define everyone_en = Character("Everyone", color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "eng"')

define reika_en = Character("Reika", image ="reika" , color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "eng"')
define reika_p_en = Character("Reika", image ="reika_p" , color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "eng"')
define reika_c_en = Character("Reika", image ="reika_c" , color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "eng"')
define yuno_en = Character("Yuno", image ="yuno" , color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "eng"')
define maya_en = Character("Maya", image ="maya" , color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "eng"')
define maya_c2_en = Character("Maya", image ="maya_c2" , color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "eng"')

define akane_en = Character("Akane", image ="akane" , color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "eng"')
define kazuma_en = Character("Kazuma", image ="kazuma" , color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "eng"')
define risa_en = Character("Risa", image ="risa" , color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "eng"')

define yuno_p_en = Character("Yuno", image ="yuno_p" , color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "eng"')
define yuno_c_en = Character("Yuno", image ="yuno_c" , color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "eng"')

define student_m_2_en = Character("Male Student" , color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "eng"')
define staff_en = Character("Staff" , color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "eng"')
define speaker_en = Character("Speaker" , color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "eng"')
#########################################



image NightSky2 = im.Scale("bg/NightSky2.png",1920,1080)
image NightSky1 = im.Scale("bg/NightSky1.png",1920,1080)
image sunset1 = im.Scale("bg/sunset1.png",1920,1080)
image sunset2 = im.Scale("bg/sunset2.png",1920,1080)
image moonlight3 = im.Scale("bg/moonlight3.png",1920,1080)
image sky_cloudy = im.Scale("bg/sky_cloudy.png",1920,1080)
image sky_summer = im.Scale("bg/sky_summer.png",1920,1080)
image classroom_sunset = im.Scale("bg/classroom_sunset.png",1920,1080)
image classroom_morning = im.Scale("bg/classroom_morning.jpg",1920,1080)
image sky_morning = im.Scale("bg/sky_morning.png",1920,1080)
image nightsky = im.Scale("bg/nightsky.png",1920,1080)

image star3 = im.Scale("puzzle/star3.png",1920,1080)


image hospital =im.Scale("bg/hospital.png",1920,1080)
image road = im.Scale("bg/road.jpg",1920,1080)

image kitchen03 = im.Scale("bg/kitchen03.png",1920,1080)

image fb1 = im.Scale("cg/fb1.png",1920,1080)
image fb2_1 = im.Scale("cg/fb2_1.png",1920,1080)
image fb2_2 = im.Scale("cg/fb2_2.png",1920,1080)
image fb2_3 = im.Scale("cg/fb2_3.png",1920,1080)

image fb3_1 = im.Scale("cg/fb3_1.png",1920,1080)
image fb3_2 = im.Scale("cg/fb3_2.png",1920,1080)
image fb3_3 = im.Scale("cg/fb3_3.png",1920,1080)
image fb3_4 = im.Scale("cg/fb3_4.png",1920,1080)
image fb3_5 = im.Scale("cg/fb3_5.png",1920,1080)
image fb3_6 = im.Scale("cg/fb3_6.png",1920,1080)
image cg3 = im.Scale("cg/cg3.png",1920,1080)

label endding:
    $ achievement.grant("END_DEMO")
    $ achievement.sync()
    $ renpy.block_rollback()
    stop music
    $renpy.pause(1, hard=True)
    scene white with Dissolve(2.0)
    $ renpy.block_rollback()
    play movie "ending2.mp4"
    $renpy.pause(65, hard=True)
    $ renpy.end_replay()
    jump s2_11
    return

# image reika normal :
#     zoom 0.75
#     xoffset 25
#     im.Composite((1433,3100), (0,1700),"Sprite/reika01/reika01_body.png" , (0,1700),"Sprite/reika01/reika01_normal.png") 

# image reika angry1 :
#     zoom 0.75
#     xoffset 25
#     im.Composite((1433,3100), (0,1700),"Sprite/reika01/reika01_body.png" , (0,1700),"Sprite/reika01/reika01_angry1.png") 

# image reika p_normal :
#     zoom 0.75
#     xoffset 25
#     im.Composite((1433,3100), (0,1700),"Sprite/reika01/reika01_p_body.png" , (0,1700),"Sprite/reika01/reika01_normal.png") 

# image reika p_angry1 :
#     zoom 0.75
#     xoffset 25
#     im.Composite((1433,3100), (0,1700),"Sprite/reika01/reika01_p_body.png" , (0,1700),"Sprite/reika01/reika01_angry1.png") 


# image reika normal_2 :
#     zoom 0.75
#     xoffset 25
#     im.Composite((1433,3100), (0,1700),"Sprite/reika02/reika02_body.png" , (0,1700),"Sprite/reika02/reika02_normal.png") 

# image reika angry1_2 :
#     zoom 0.75
#     xoffset 25
#     im.Composite((1433,3100), (0,1700),"Sprite/reika02/reika02_body.png" , (0,1700),"Sprite/reika02/reika02_angry.png") 


label splashscreen:
    scene seal3 with Dissolve(1.0)
    pause 2
    scene warning with Dissolve(1.0)
    pause 2
    $ achievement.grant("START_GAME")
    $ achievement.sync()
    jump title1
    return

label title1:
    scene white with Dissolve(1.0)
    scene main01_01 with Dissolve(1)
    scene main01_02 with Dissolve(1)
    scene main01_03 with Dissolve(0.5)
    scene main01_04 with Dissolve(0.5)
    scene main01_05 with Dissolve(0.5)
    scene main01_05_trial with Dissolve(0.5)
    return


######## Custom #########
image reika angry:
    zoom 0.75
    xoffset 25
    im.Composite((1433,3100), (0,1700), "Sprite/reika01/reika01_body.png" ,(0,1700), "Sprite/reika01/reika01_angry1.png" )

image reika bored_2:
    zoom 0.75
    xoffset 25
    im.Composite((1433,3100), (0,1700), "Sprite/reika02/reika02_body.png" ,(0,1700), "Sprite/reika02/reika02_Bored.png" )

image reika shy_2_shy:
    zoom 0.75
    xoffset 25
    im.Composite((1433,3100), (0,1700), "Sprite/reika01/reika01_body_shy.png" ,(0,1700), "Sprite/reika01/reika01_shy2.png" )

image side reika shy_2_shy:
    zoom 0.55
    xoffset -200
    yoffset 370
    im.Composite((1433,3100), (0,1700), "Sprite/reika01/reika01_body_shy.png" ,(0,1700), "Sprite/reika01/reika01_shy2.png" )

image reika shy_2:
    zoom 0.75
    xoffset 25
    im.Composite((1433,3100), (0,1700), "Sprite/reika02/reika02_body_shy.png" ,(0,1700), "Sprite/reika02/reika02_shy.png" )

image side reika shy_2:
    zoom 0.55
    xoffset -200
    yoffset 370
    im.Composite((1433,3100), (0,1700), "Sprite/reika02/reika02_body_shy.png" ,(0,1700), "Sprite/reika02/reika02_shy.png" )

image reika sadistic_2_s:
    zoom 0.75
    xoffset 25
    im.Composite((1433,3100), (0,1700), "Sprite/reika01/reika01_body_s.png" ,(0,1700), "Sprite/reika01/reika01_sadistic.png" )

image side reika sadistic_2_s:
    zoom 0.55
    xoffset -200
    yoffset 370
    im.Composite((1433,3100), (0,1700), "Sprite/reika01/reika01_body_s.png" ,(0,1700), "Sprite/reika01/reika01_sadistic.png" )

image reika sadistic2_2_s:
    zoom 0.75
    xoffset 25
    im.Composite((1433,3100), (0,1700), "Sprite/reika02/reika02_body_sadistic.png" ,(0,1700), "Sprite/reika02/reika02_sadistic.png" )

image side reika sadistic2_2_s:
    zoom 0.55
    xoffset -200
    yoffset 370
    im.Composite((1433,3100), (0,1700), "Sprite/reika02/reika02_body_sadistic.png" ,(0,1700), "Sprite/reika02/reika02_sadistic.png" )

image reika shy_shy:
    zoom 0.75
    xoffset 25
    im.Composite((1433,3100), (0,1700), "Sprite/reika01/reika01_body_shy.png" ,(0,1700), "Sprite/reika01/reika01_shy1.png" )

image side reika shy_shy:
    zoom 0.55
    xoffset -200
    yoffset 370
    im.Composite((1433,3100), (0,1700), "Sprite/reika01/reika01_body_shy.png" ,(0,1700), "Sprite/reika01/reika01_shy1.png" )


image akane s2:
    zoom 0.75
    xoffset 25
    im.Composite((1433,3100), (0,1700), "Sprite/akane/akane_bodys.png" ,(0,1700), "Sprite/akane/akane_s2.png" )

image side akane s2:
    zoom 0.55
    xoffset -200
    yoffset 370
    im.Composite((1433,3100), (0,1700), "Sprite/akane/akane_bodys.png" ,(0,1700), "Sprite/akane/akane_s2.png" )

image akane s2_s:
    zoom 0.75
    xoffset 25
    im.Composite((1433,3100), (0,1700), "Sprite/akane/akane_bodys.png" ,(0,1700), "Sprite/akane/akane_s2.png" )

image side akane s2_s:
    zoom 0.55
    xoffset -200
    yoffset 370
    im.Composite((1433,3100), (0,1700), "Sprite/akane/akane_bodys.png" ,(0,1700), "Sprite/akane/akane_s2.png" )

image risa sadistic_s:
    zoom 0.75
    xoffset 25
    im.Composite((1433,3100), (0,1700), "Sprite/risa/risa_body_s.png" ,(0,1700), "Sprite/risa/risa_sadistic.png" )

image side risa sadistic_s:
    zoom 0.55
    xoffset -200
    yoffset 370
    im.Composite((1433,3100), (0,1700), "Sprite/risa/risa_body_s.png" ,(0,1700), "Sprite/risa/risa_sadistic.png" )
######## Custom ######### 
image flyingseal01:
    "SD/flyingseal/flyingseal01.png" with dissolve
    pause 0.5
    "SD/flyingseal/flyingseal01.png" with dissolve
    pause 0.5
    "SD/flyingseal/flyingseal02.png" with dissolve
    pause 0.5
    "SD/flyingseal/flyingseal02.png" with dissolve
    pause 0.5
    repeat

image excited:
    "emotion/excited2.png" with dissolve
    pause 0.5
    "emotion/excited1.png" with dissolve
    pause 0.5
    repeat


image kick01:
    "SD/kick/kick01.png" with dissolve
    pause 0.25
    "SD/kick/kick02.png" with dissolve
    pause 0.25
    repeat

image kick04:
    "SD/kick/kick04.png" with dissolve
    pause 0.5
    "SD/kick/kick05.png" with dissolve
    pause 0.5
    repeat
image imagine = im.Scale("imagine.png",1920,1080)
image sunset4 = im.Scale("bg/sunset4.png",1920,1080)
transform zoom_in:
    zoom 1.5
    yoffset 420
transform left_50:
    xoffset 50
transform emotion_zoom:
    yoffset -50
    xoffset 100


transform zoom_in_yuno:
    zoom 1.5
    yoffset 350
style default:
    line_spacing 10
init python:
    def prepare(s):
        return s.lower().replace(" ", "").replace("_","").replace("-","")
label start:
    $ reika_mall_pass = False
    $ akane_mall_pass = False
    $ kazuma_mall_pass = False
    $ risa_mall_pass = False
    jump s1_1
   
    # show reika normal with dissolve
    # reika normal "Word1" with dissolve
    # reika angry1 "Word2" with dissolve
    # reika normal "Word3" with dissolve

    # reika normal_2 "Word1" with dissolve
    # reika angry1_2 "Word2" with dissolve
    # reika normal_2 "Word3" with dissolve

    # reika normal "Word1" with dissolve
    # reika angry1_2 "Word2" with dissolve
    # reika normal "Word3" with dissolve

    # reika p_normal "Word1" with dissolve
    # reika p_angry1 "Word2" with dissolve
    # reika p_normal "Word3" with dissolve
    # reika normal "Word1" with dissolve
    # reika onegai_2 "Word1" with dissolve
    # reika smile "Word3" with dissolve
    # reika sad "Word4" with dissolve

    # hide reika with dissolve

    # show yuno normal with dissolve
    # yuno normal "Word1" with dissolve
    # yuno onegai "Word1" with dissolve
    # yuno smile "Word3" with dissolve
    # yuno sad "Word4" with dissolve

    # hide yuno with dissolve

    # show maya normal with dissolve
    # maya normal "Word1" with dissolve
    # maya onegai "Word1" with dissolve
    # maya smile "Word3" with dissolve
    # maya sad "Word4" with dissolve
    

 
    # This ends the game.

    return


image dot:
    "emotion/dot1.png"
    pause 0.5
    "emotion/dot2.png"
    pause 0.5
    "emotion/dot3.png"
    pause 0.5
    "emotion/dot1.png"
    repeat

image laught:
    "emotion/laught.png"
    pause 0.5
    "emotion/laught2.png"
    pause 0.5
    repeat
transform offset_laught:
    xoffset 30


image panic:
    "emotion/panic1.png"
    pause 0.5
    "emotion/panic2.png"
    pause 0.5
    repeat

image angry:
    "emotion/angry.png"

image aware:
    "emotion/aware.png"

image border:
    "emotion/border.png"

image dark:
    "emotion/dark.png"
image down:
    "emotion/down.png"

image happy:
    "emotion/happy.png"
image heart:
    "emotion/heart.png"
image huh:
    "emotion/huh.png"
image moyamoya:
    "emotion/moyamoya.png"
image pout:
    "emotion/pout.png"
image question:
    "emotion/question.png"
image shine:
    "emotion/shine.png"
    pause 0.5
    "emotion/shine02.png"
    pause 0.5
    repeat
image surprise:
    "emotion/surprise.png"
image sweat:
    "emotion/sweat.png"
image wakaru:
    "emotion/wakaru.png"

image spotlight:
    "emotion/spotlight.png"


screen map_screen:
    add "screen_new/choice_mall/choice_mall_bg.png"  

    if not akane_mall_pass:
        imagebutton auto "screen_new/choice_mall/akane_choice_%s.png":
            focus_mask True
            action [Hide("map_screen"),Jump("s2_4_akane")]
    else:
        imagebutton idle "akane_choice_disable"

    if not reika_mall_pass:
        imagebutton auto "screen_new/choice_mall/reika_choice_%s.png":
            focus_mask True
            action [Hide("map_screen"),Jump("s2_4_reika")]
    else:
        imagebutton idle "reika_choice_disable"

    if not kazuma_mall_pass:
        imagebutton auto "screen_new/choice_mall/kazuma_choice_%s.png":
            focus_mask True
            action [Hide("map_screen"),Jump("s2_4_kazuma")]
    else:
        imagebutton idle "kazuma_choice_disable"

    if not risa_mall_pass:
        imagebutton auto "screen_new/choice_mall/risa_choice_%s.png":
            focus_mask True
            action [Hide("map_screen"),Jump("s2_4_risa")]
    else:
        imagebutton idle "risa_choice_disable"
label mall_map:
    $ preferences.afm_enable = False
    $ old_afm_time = renpy.game.preferences.afm_time
    $ renpy.game.preferences.afm_time = 0
    
    if akane_mall_pass and reika_mall_pass and kazuma_mall_pass and risa_mall_pass:
        $ renpy.game.preferences.afm_time = old_afm_time
        jump s2_4_2

    $ renpy.config.skipping = False
    $ _skipping = False
    # window hide
    show screen map_screen with dissolve
    
    $ renpy.pause(hard=True)

