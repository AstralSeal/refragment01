#set PYTHONIOENCODING=utf-8
#set PYTHONLEGACYWINDOWSSTDIO=utf-8

import pandas as pd
FILE_NAME = "test.csv"
data = pd.read_csv(FILE_NAME,encoding="utf-8")
data = data.fillna("")

def show_charector(charector1,charector2,charector3,zoom=False):

    if ( charector1 == "" ):
        return
    
    #3 Charector Case
    if ( charector3 != "" and charector2 != "" ):
        print(f'show {character1} normal with Dissolve(1.0) at center')
        print(f'show {character2} normal with Dissolve(1.0) at left')
        print(f'show {character3} normal with Dissolve(1.0) at right')
        return
    

    #2 Charector Case
    if ( charector2 != ""):
        print(f'show {character1} normal with Dissolve(1.0) at left')
        print(f'show {character2} normal with Dissolve(1.0) at right')
        return
        
    # One character Case
    print(f'show {character1} normal with Dissolve(1.0) at center')

    return


for i,c in data.iterrows():
    ### Assign ##############################

    bg = c['bg']
    bg_effect = c['bg_effect']
    bgm = c['bgm']
    zoom = c['zoom']

    character1 = c['character1']
    
    character2 = c['character2']
    
    character3 = c['character3']

    emotion = c['emotion']
    
    effect = c['effect']
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

    show_charector(character1, character2, character3)
        


    if(voice):
        print(f'play sound "audio/voice/{voice}"')
    
    if(bg_effect):
        print(f'show {bg_effect}')


    #Todo 
    
    if(talk):
        if(who_talk):
            print(f'{who_talk} {emotion} "{talk}" with dissolve')
        else:
            print(f'"{talk}" with dissolve')


    if(bg_effect):
        print(f'hide {bg_effect}')


    ### Post ####################################