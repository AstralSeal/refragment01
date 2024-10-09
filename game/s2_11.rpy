init python:
    import webbrowser

    def open_survey_url():
        webbrowser.open("https://docs.google.com/forms/d/e/1FAIpQLSec9GmgjlqDV818dcfMdirdv9F5J7gd_kgz-3Ac-nq5uwYlgQ/viewform")

label s2_11:
    scene white with Dissolve(1.0)
    scene home_livingroom_morning with Dissolve(4.0)
    show yuno_c smile_2 at center with Dissolve(0.2)
    play music "audio/bgm/MusMus-BGM-162.mp3" volume 0.5 
    voice "audio/voice/yuno/chapter2/chapter2_12/yuno_2_12_001.mp3"
    yuno_c_th smile_2 "จบเกมเวอร์ชั่นทดลองเล่นแล้ว เป็นไงบ้างพี่จ๋า สนุกหรือเปล่า" with Dissolve(0.2)
    yuno_c_en smile_2 "What did you think of the trial version, Onii-chan. Did you have fun?" with Dissolve(0.2)

    voice "audio/voice/yuno/chapter2/chapter2_12/yuno_2_12_002.mp3"
    yuno_c_th smile "อย่าลืมทำแบบสอบถามให้หนูด้วยน้าา~" with Dissolve(0.2)
    yuno_c_en smile "Don't forget to fill out the questionnaire for me." with Dissolve(0.2)
    
    menu :
        '[get_choice("ทำแบบสอบถาม","Fill out a survey")]':
            $ open_survey_url()
        '[get_choice("ทำแบบสอบถามเหมือนกันแต่อยู่ข้างล่าง","Fill out a survey but at the bottom")]':
            $ open_survey_url()

    show yuno_c teehee at zoom_in
    voice "audio/voice/yuno/chapter2/chapter2_12/yuno_2_12_003.mp3"
    yuno_c_th teehee "แล้วก็อย่าลืมโหวตให้หนูด้วยนะ!" with Dissolve(0.2) 
    yuno_c_en teehee "Don't forget to vote for me!"
    scene black with Dissolve(2.0)
    scene white with Dissolve(4.0)
    return 
