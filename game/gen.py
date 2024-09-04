#set PYTHONIOENCODING=utf-8
#set PYTHONLEGACYWINDOWSSTDIO=utf-8
#python gen.py > s1_1.rpy
import pandas as pd
FILE_NAME = "s1_3.csv"
data = pd.read_csv(FILE_NAME,encoding="utf-8")
data = data.fillna("")
zoom_in_cha = ""
def show_charector(charector1,charector2,zoom=False):
    global zoom_in_cha 
    if(  charector1 != ""):
        zoom_in_cha = charector1

    if ("hide" in charector1) :
        print(charector1)
        if("hide" in charector2):
            print(charector2)
        return 

    if (zoom == "1" or zoom == 1) :
        print(f'show {zoom_in_cha} normal at zoom_in,center with Dissolve(1.0) ')
        return
    
    if (zoom == "0" or zoom == 0):
        print(f'show {zoom_in_cha} normal at center with Dissolve(1.0) ')
        return



    if ( charector1 == "" ):
        return
    
    #3 Charector Case
    # if ( charector3 != "" and charector2 != "" ):
    #     print(f'show {character1} normal with Dissolve(1.0) at center')
    #     print(f'show {character2} normal with Dissolve(1.0) at left')
    #     print(f'show {character3} normal with Dissolve(1.0) at right')
    #     return
    

    #2 Charector Case
    if ( charector2 != ""):
        print(f'show {character1} normal at left with Dissolve(1.0) ')
        print(f'show {character2} normal at right with Dissolve(1.0) ')
        return
        
    # One character Case
    print(f'show {character1} normal at center with Dissolve(1.0) ')
    return

def preprocess_dialog(s):
    if (s == None):
        return None
    return s.replace("[", "")\
            .replace("”", "")\
            .replace("“","")\
            .replace("]","")\
            .replace("%","\%")

def preprocess_face(s):
    if( s == "sadistic2_2_s" or s == "sadistic2_2_s" or s == "s2_s" ):
        return "normal"
    return s

for i,c in data.iterrows():
    ### Assign ##############################

    bg = c['bg']
    bg_effect = c['bg_effect']
    bgm = c['bgm']
    zoom = c['zoom']

    character1 = c['character1']
    
    character2 = c['character2']
    
    # character3 = c['character3']

    face = c['face']
    
    # effect = c['effect']
    who_talk = c['who_talk']
    talk = c['talk']
    voice = c['voice']
    
    ### Action ###############################


    if(bg):
        print(f'scene {bg} with Dissolve(1.0)')

    if(bgm and bgm != 'stop'):
        print(f"stop music")
        print(f'play music "audio/bgm/{bgm}.mp3" volume 0.5')
    
    if(bgm =='stop'):
        print(f"stop music")

    show_charector(character1, character2, zoom)
        


    # if(voice):
    #     print(f'play sound "audio/voice/{voice}"')
    
    if(bg_effect):
        if("hide" in bg_effect):
            print(f'{bg_effect} with dissolve')
        else:
            print(f'show {bg_effect} with dissolve')


    #Todo 
    
    if(talk):
        if(who_talk):
            print(f'{who_talk} {preprocess_face(face)} "{preprocess_dialog(talk)}" with dissolve')
        else:
            print(f'"{preprocess_dialog(talk)}" with dissolve')


    # if(bg_effect):
    #     print(f'hide {bg_effect}')


    ### Post ####################################