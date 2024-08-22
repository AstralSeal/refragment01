# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define en = Character(None, condition='persistent.language == "eng"')
define th = Character(None, condition='persistent.language == "thai"')


define yume = Character("เรา",color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])
define cat0 = Character("???",color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])
define cat = Character("แมว", image ="cat" ,color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])

define yume_th = Character("เรา",color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")] , condition='persistent.language == "thai"')
define cat0_th = Character("???",color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")] , condition='persistent.language == "thai"' )
define cat_th = Character("แมว", image ="cat" ,color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")] , condition='persistent.language == "thai"')

define yume_en = Character("I",color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")],condition='persistent.language == "eng"')
define cat0_en = Character("???",color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")] , condition='persistent.language == "eng"')
define cat_en = Character("Cat", image ="cat" ,color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")] , condition='persistent.language == "eng"')


define mary0 = Character("???",color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")] )
define mary = Character("แมรี่",color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])
define father = Character("พ่อของแมรี่",color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])


define mary0_th = Character("???",color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")], condition='persistent.language == "thai"')
define mary_th = Character("แมรี่",color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")], condition='persistent.language == "thai"')
define father_th = Character("พ่อของแมรี่",color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")], condition='persistent.language == "thai"')

define mary0_en = Character("???",color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")] , condition='persistent.language == "eng"')
define mary_en = Character("Mary",color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")] , condition='persistent.language == "eng"')
define father_en = Character("Mary's Father",color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")] , condition='persistent.language == "eng"')


define yuma = Character("ยูมะ", color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])
define yuno_0 = Character("???", color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])


define maya_0 = Character("???", color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])
define student_m_a = Character("นักเรียนชาย A", color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])
define student_m_b = Character("นักเรียนชาย B", color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])
define student_m_c = Character("นักเรียนชาย C", color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])

define student_f_a = Character("นักเรียนหญิง A", color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])
define student_f_b = Character("นักเรียนหญิง B", color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])
define student_f_c = Character("นักเรียนหญิง C", color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])



define reika = Character("เรย์กะ", image ="reika" , color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])
define yuno = Character("ยูโนะ", image ="yuno" , color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])
define maya = Character("มายะ", image ="maya" , color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])

define akane = Character("อาคาเนะ", image ="akane" , color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])
define kazuma = Character("คาซึมะ", image ="kazuma" , color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])
define risa = Character("ริซะ", image ="risa" , color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])

image moonlight3 = im.Scale("bg/moonlight3.png",1920,1080)
image sky_cloudy = im.Scale("bg/sky_cloudy.png",1920,1080)
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
    if persistent.true_end_pass == True:
        jump title2
    if persistent.common_end_pass == True:
        jump title3

    jump title1
    return

label title1:
    scene white with Dissolve(1.0)
    scene main01_01 with Dissolve(1)
    scene main01_02 with Dissolve(1)
    scene main01_03 with Dissolve(0.5)
    scene main01_04 with Dissolve(0.5)
    scene main01_05 with Dissolve(0.5)

    return

label title2:
    scene white with Dissolve(1.0)
    scene main02_01 with Dissolve(1)
    scene main02_02 with Dissolve(1)
    scene main02_03 with Dissolve(0.5)
    scene main02_04 with Dissolve(0.5)
    scene main02_05 with Dissolve(0.5)
    return


label title3:
    scene white with Dissolve(1.0)
    scene main03_01 with Dissolve(1)
    scene main03_02 with Dissolve(1)
    scene main03_03 with Dissolve(0.5)
    scene main03_04 with Dissolve(0.5)
    return



style default:
    line_spacing 10
init python:
    def prepare(s):
        return s.lower().replace(" ", "").replace("_","").replace("-","")
label start:
    jump s1_1_2
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
