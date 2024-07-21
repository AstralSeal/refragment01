#set PYTHONIOENCODING=utf-8
#set PYTHONLEGACYWINDOWSSTDIO=utf-8
#python gen.py > s1_1.rpy
import pandas as pd
FILE_NAME = "s1_1.csv"
data = pd.read_csv(FILE_NAME,encoding="utf-8")
data = data.fillna("")

def show_charector(charector1,charector2,zoom=False):

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
        print(f'show {character2} normal at righ with Dissolve(1.0) t')
        return
        
    # One character Case
    print(f'show {character1} normal at center with Dissolve(1.0) ')

    return


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
        print(f'play music "audio/bgm/{bgm}.mp3 volume 0.5')
    
    if(bgm =='stop'):
        print(f"stop music")

    show_charector(character1, character2)
        


    if(voice):
        print(f'play sound "audio/voice/{voice}"')
    
    # if(bg_effect):
    #     print(f'show {bg_effect}')


    #Todo 
    
    if(talk):
        if(who_talk):
            print(f'{who_talk} {face} "{talk}" with dissolve')
        else:
            print(f'"{talk}" with dissolve')


    # if(bg_effect):
    #     print(f'hide {bg_effect}')


    ### Post ####################################