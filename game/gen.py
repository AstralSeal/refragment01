#set PYTHONIOENCODING=utf-8
#set PYTHONLEGACYWINDOWSSTDIO=utf-8
#python gen.py > s2_6.rpy

#todo reika normal_2 
#maya smile
#yuno smile_2
import pandas as pd
FILE_NAME = "s2_3.csv"
VOICE_BASE_PATH="audio/voice"
VOICE_PATH = "chapter2/chapter2_3"
SFX_BASE_PATH="audio/sfx"
data = pd.read_csv(FILE_NAME,encoding="utf-8")
data = data.fillna("")
zoom_in_cha = ""
shortcut_charector_1 = ""
def show_charector(charector1,charector2,zoom=False):

    if ("hide" in charector1) :
        return
    if("hide" in charector2):
        return 
    
    global shortcut_charector_1 
    global zoom_in_cha 
    
    if(  charector1 != ""):
        zoom_in_cha = charector1

    if(shortcut_charector_1 != "" and character1 != ""):
        print(f'hide {shortcut_charector_1}')
        print(f'show {charector1} normal at center with Dissolve(0.2) ')




    if (zoom == "1" or zoom == 1) :
        print(f'show {zoom_in_cha} normal at zoom_in,center with Dissolve(0.2) ')
        return
    
    if (zoom == "0" or zoom == 0):
        print(f'show {zoom_in_cha} normal at center with Dissolve(0.2) ')
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
        print(f'show {character1} normal at left')
        print(f'show {character2} normal at right with Dissolve(0.2) ')
        return
        
    # One character Case
    print(f'show {character1} normal at center with Dissolve(0.2) ')
    return

def preprocess_dialog(s):
    if (s == None):
        return None
    return s.replace("[", "")\
            .replace("”", "")\
            .replace("“","")\
            .replace("]","")\
            .replace("%","\%")

def preprocess_face(s,who):
    if (who == 'yuma'):
        return s
    if( s == "sadistic2_2_s" or s == "sadistic2_2_s" or s == "s2_s" or s =="sadistic_s" or s =="sadistic2_2" ):
        return "normal"
    return s

def hide_charector(charector1,charector2) :
    if ("hide" in charector1) :
        print(charector1)
    if("hide" in charector2):
        print(charector2)


def get_cloth(past_cloth,s) :
    if not isinstance(s, str):
        s = ""

    if("hide" in s):
        return ""
    
    if(past_cloth != "" and s == ""):
        return past_cloth
    if "_" in s:
        s = "_"+s.split("_")[-1]
    else:
        s = ""
    return s

cloth_dict = {}

def get_origin_charector(charector):
    if ("_" in charector):
        return charector.split("_")[0]
    return charector


def remove_cloth(charector) :
    cloth_dict[charector] = ""


def set_cloth(charector,cloth):
    cloth_dict[charector] = cloth

def apply_cloth(charector):
    if cloth_dict.get(charector):
        return cloth_dict.get(charector)
    else:
        return ""
    

cloth1=""
cloth2=""
for i,c in data.iterrows():
    ### Assign ##############################

    bg = c['bg']
    bg_effect = c['bg_effect']
    bgm = c['bgm']
    zoom = c['zoom']

    character1 = c['character1']
    cloth1 = get_cloth(cloth1,c['character1'])

    if(not "hide" in character1 ) :
        set_cloth(get_origin_charector(character1),cloth1)
    else :
        remove_cloth(get_origin_charector(character1))


    
    character2 = c['character2']
    cloth2 = get_cloth(cloth2,c['character2'])

    
    if(not "hide" in character2 ) :
        set_cloth(get_origin_charector(character2),cloth2)
    else :
        remove_cloth(get_origin_charector(character2))
    
    # character3 = c['character3']

    face = c['face']
    
    # effect = c['effect']
    who_talk = c['who_talk']
    talk = c['talk']
    talk_en = c['talk_en']
    voice = c['voice']
    sfx = c['sfx']
    
    ### Action ###############################


    if(bg):
        print(f'scene {bg} with Dissolve(1.0)')

    if(bgm and bgm != 'stop'):
        print(f"stop music")
        print(f'play music "audio/bgm/{bgm}.mp3" volume 0.5')
    
    if(bgm =='stop'):
        print(f"stop music")
    show_charector(character1, character2, zoom)
        
    if(sfx):
        print(f'play sound "{SFX_BASE_PATH}/{sfx}.mp3"')

    if(voice):
        print(f'#---- play sound "{VOICE_BASE_PATH}/{who_talk}/{VOICE_PATH}/{voice}.mp3"')
    
    if(bg_effect):
        if("hide" in bg_effect):
            print(f'{bg_effect} with dissolve')
        else:
            print(f'show {bg_effect} with dissolve')


    #Todo 
    
    if(talk):
        if(who_talk):
            print(f'{who_talk}{apply_cloth(who_talk)}_th {preprocess_face(face,who_talk)} "{preprocess_dialog(talk)}" with dissolve')
            print(f'{who_talk}{apply_cloth(who_talk)}_en {preprocess_face(face,who_talk)} "{preprocess_dialog(talk_en)}" with dissolve')
        else:
            print(f'th "{preprocess_dialog(talk)}" with dissolve')
            print(f'en "{preprocess_dialog(talk_en)}" with dissolve')
    
    if( character1 != "" and ("hide" not in character1)):
        shortcut_charector_1 = character1
    else:
        shortcut_charector_1 = ""
    hide_charector(character1,character2)
    # if(bg_effect):
    #     print(f'hide {bg_effect}')


    ### Post ####################################