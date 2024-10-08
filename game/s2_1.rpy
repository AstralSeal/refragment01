label s2_1:
    scene home_yuumabedroom_morning with Dissolve(1.0)
    stop music
    play music "audio/bgm/Sunrise.mp3" volume 0.5
    voice "audio/voice/yuno/chapter2/chapter2_1/yuno_2_1_001.mp3"
    $ achievement.grant("START_CH02")
    $ achievement.sync()
    show wakeup24 with dissolve
    yuno_th  "ยู…มะ…" with dissolve
    yuno_en  "Yuu... ma..." with dissolve
    voice "audio/voice/yuno/chapter2/chapter2_1/yuno_2_1_002.mp3"
    yuno_th  "ยูมะ ตื่นได้แล้ว!" with dissolve
    yuno_en  "Yuuma, time to wake up!" with dissolve
    play sound "audio/voice/yuno/chapter2/chapter2_1/yuno_2_1_003.mp3"
    hide wakeup24
    show wakeup01 with dissolve
    yuno_th  "ได้เวลาไปโรงเรียนแล้ว!" with dissolve
    yuno_en  "It's time for school!" with dissolve
    th "สิ่งแรกที่ผมพบเห็นในตอนเช้าคือใบหน้ายิ้มแย้มแจ่มใสของยูโนะ" with dissolve
    en "The first thing I see in the morning is Yuno's bright, smiling face." with dissolve
    th "วันนี้ยูโนะก็นั่งทับตัวผมอีกแล้ว" with dissolve
    en "Today, Yuno is sitting on top of me again." with dissolve
    yuma_th  "ยูโนะ ช่วยลุกหน่อย พี่ขยับตัวไม่ได้แล้วเนี่ย" with dissolve
    yuma_en  "Yuno, can you get off? I can't move." with dissolve
    voice "audio/voice/yuno/chapter2/chapter2_1/yuno_2_1_004.mp3"
    hide wakeup01
    show wakeup03 with dissolve
    yuno_th  "ไม่! หนูไม่ลุกจนกว่าพี่จะตื่น" with dissolve
    yuno_en  "No! I won't get up until you wake up." with dissolve
    yuma_th  "ก็ได้ ตื่นแล้ว ลุกออกไปที" with dissolve
    yuma_en  "Fine, I'm awake. Now get off." with dissolve
    voice "audio/voice/yuno/chapter2/chapter2_1/yuno_2_1_005.mp3"
    hide wakeup03
    show wakeup04 with dissolve
    yuno_th  "ก็ได้" with dissolve
    yuno_en  "Okay." with dissolve
    th "ยูโนะยอมลุกขึ้นแต่โดยดี" with dissolve
    en "Yuno obediently gets up." with dissolve
    voice "audio/voice/yuno/chapter2/chapter2_1/yuno_2_1_006.mp3"
    hide wakeup04
    show wakeup07 with dissolve
    yuno_th  "วันนี้เกม Seal Impact มีอัพเดตใหม่ หนูไม่ว่างมาปลุกพี่ซ้ำหรอกนะ " with dissolve
    yuno_en  "There's a new update for Seal Impact today. I won't have time to wake you up again." with dissolve
    voice "audio/voice/yuno/chapter2/chapter2_1/yuno_2_1_007.mp3"
    yuno_th  "ห้ามนอนเด็ดขาด ขืนหลับต่อละก็ไปโรงเรียนสายแน่" with dissolve
    yuno_en  "Don't even think about going back to sleep, or you'll end up being late for school." with dissolve
    scene home_yuumabedroom_morning with Dissolve(1.0)
    play sound "audio/sfx/ドアを閉める2.mp3"
    th "นี่เรามีน้องสาวหรือแม่คนที่สองกันแน่เนี่ย…" with dissolve
    en "You're sounding way too much like a mom!" with dissolve
    th "ยูโนะพูดทิ้งท้ายก่อนเดินออกจากห้อง" with dissolve
    en "Yuno says as she walks out of the room." with dissolve
    yuma_th  "ง่วงจัง ถ้านอนต่ออีกสัก 5 นาทีก็คงไม่เป็นอะไรหรอกมั้ง" with dissolve
    yuma_en  "I'm so sleepy. Surely another 5 minutes won't hurt." with dissolve
    play sound "audio/sfx/家の階段を駆け上る.mp3"
    th "พอพูดจบ ผมก็ดำดิ่งเข้าสู่ห้วงนิทรา" with dissolve
    en "As soon as I say that, I drift back into sleep," with dissolve
    th "โดยที่ไม่ได้ตระหนักว่าการนอนต่อรอบท่ีสองคือจุดเริ่มต้นของหายนะ" with dissolve
    en "Unaware that this second nap marks the beginning of disaster." with dissolve
    yuma_th  "zzz" with dissolve
    yuma_en  "zzz" with dissolve
    scene black with Dissolve(1.0)
    th "…" with dissolve
    en "..." with dissolve
    th "……" with dissolve
    en "......" with dissolve
    scene home_yuumabedroom_morning with Dissolve(1.0)
    yuma_th  "หืม? กี่โมงแล้วเนี่ย" with dissolve
    yuma_en  "Hm? What time is it?" with dissolve
    th "ผมมองนาฬิกา พบว่าเวลาไม่ได้ผ่านไปแค่ห้านาที แต่เป็นสามสิบห้านาที" with dissolve
    en "I look at the clock and realize that not five, but thirty-five minutes have passed." with dissolve
    stop music
    play music "audio/bgm/MusMus-BGM-087.mp3" volume 0.5
    yuma_th  "แย่แล้ว สายแล้ว" with dissolve
    yuma_en  "Oh no, I'm late." with dissolve
    th "ด้วยเหตุนี้ผมรีบแต่งตัวและวิ่งพรวดออกจากห้องนอน" with dissolve
    en "With that, I hurriedly get dressed and dash out of my bedroom." with dissolve
    scene home_livingroom_morning with Dissolve(1.0)
    show yuno_c normal at center with Dissolve(0.2) 
    yuma_th  "ยูโนะ ทำไมไม่เข้ามาปลุกพี่อีกรอบล่ะ" with dissolve
    yuma_en  "Yuno, why didn't you come wake me up again?" with dissolve
    voice "audio/voice/yuno/chapter2/chapter2_1/yuno_2_1_008.mp3"
    yuno_c_th pout2_2 "หนูเข้าไปปลุกพี่อีกรอบแล้ว แต่พี่เป็นคนตอบเองว่าโอเค" with dissolve
    yuno_c_en pout2_2 "I did come to wake you up again, but you said you were okay." with dissolve
    yuma_th  "จริงเหรอ ไม่รู้ตัวเลย" with dissolve
    yuma_en  "Really? I don't remember at all." with dissolve
    voice "audio/voice/yuno/chapter2/chapter2_1/yuno_2_1_009.mp3"
    yuno_c_th hee "จริงสิ หนูจะโกหกทำไม" with dissolve
    yuno_c_en hee "Of course. Why would I lie?" with dissolve
    voice "audio/voice/yuno/chapter2/chapter2_1/yuno_2_1_010.mp3"
    yuno_c_th teehee "อีกอย่าง รู้มั้ยว่าวันนี้เกม Seal Impact มีอัพเดตใหม่ หนูต้องรีบเล่นก่อนคนอื่น" with dissolve
    yuno_c_en teehee "Besides, I did told you Seal Impact has a new update today. I need to play before everyone else." with dissolve
    th "ช่วงหลังมานี้น้องสาวของผมเริ่มรักเกมมากกว่าผมแล้วหรือเปล่าเนี่ย…" with dissolve
    en "I wonder if my little sister has started to love games more than me lately..." with dissolve
    yuma_th  "ช่างเถอะ พี่ไปก่อนละนะ" with dissolve
    yuma_en  "Anyway, I'm heading out." with dissolve
    voice "audio/voice/yuno/chapter2/chapter2_1/yuno_2_1_011.mp3"
    yuno_c_th ah_2 "ไม่กินข้าวเช้าก่อนเหรอ" with dissolve
    yuno_c_en ah_2 "Aren't you going to have breakfast?" with dissolve
    yuma_th  "โทษที แต่วันนี้ไม่ทันแล้ว" with dissolve
    yuma_en  "Sorry, but there's no time today." with dissolve
    hide yuno_c
    scene home_entrance_noon with Dissolve(1.0)
    stop music
    play music "audio/bgm/MusMus-BGM-103.mp3" volume 0.5
    show yuno_c normal at center with Dissolve(0.2) 
    th "ขณะที่ผมกำลังเดินออกจากบ้าน ยูโนะก็เดินมาหาผมที่บริเวณทางเข้าหน้าประตูบ้าน" with dissolve
    en "As I'm about to leave the house, Yuno walks up to me near the front door." with dissolve
    voice "audio/voice/yuno/chapter2/chapter2_1/yuno_2_1_012.mp3"
    yuno_c_th  "เดี๋ยวก่อน" with dissolve
    yuno_c_en  "Wait a second." with dissolve
    yuma_th  "มีอะไรเหรอ" with dissolve
    yuma_en  "What is it?" with dissolve
    voice "audio/voice/yuno/chapter2/chapter2_1/yuno_2_1_013.mp3"
    show shine
    yuno_c_th wow "พี่ไม่ลองคาบขนมปังแล้ววิ่งไปโรงเรียนดูล่ะ" with dissolve
    yuno_c_en wow "Why don't you try running to school with a piece of toast in your mouth?" with dissolve
    hide shine
    th "ยูโนะพูดด้วยท่าทีขี้เล่น ดวงตาเป็นประกาย" with dissolve
    en "Yuno says playfully, her eyes sparkling." with dissolve
    yuma_th  "พี่ไม่ใช่นางเอกการ์ตูนตาหวานสักหน่อย" with dissolve
    yuma_en  "I'm not some wide-eyed anime heroine." with dissolve
    play sound "audio/voice/yuno/chapter2/chapter2_1/yuno_2_1_014.mp3"
    yuno_c_th crymeme2 "ชิ พี่ไม่รักหนูแล้วใช่มั้ย หนูอุตส่าห์เตรียมอาหารเช้าไว้แล้ว" with dissolve
    yuno_c_en crymeme2 "Hmph. Don't you love me anymore? I even prepared breakfast for you." with dissolve
    yuma_th  "เอาไว้วันหลังน่า ตอนนี้สายแล้ว" with dissolve
    yuma_en  "Maybe next time. I'm late now." with dissolve
    voice "audio/voice/yuno/chapter2/chapter2_1/yuno_2_1_015.mp3"
    yuno_c_th smile_2 "ไปดีมาดีนะ" with dissolve
    yuno_c_en smile_2 "Take care!" with dissolve
    hide yuno_c
    th "พอพูดจบ ผมก็รีบวิ่งพรวดออกจากบ้านทันที" with dissolve
    en "With that, I dash out of the house." with dissolve
    th "ลองคิดดูแล้วแอบเสียดายอาหารเช้าฝีมือน้องสาวเหมือนกันนะ" with dissolve
    en "Now that I think about it, I do regret missing my little sister's home-cooked breakfast." with dissolve
    th "………" with dissolve
    en "........" with dissolve
    scene neighborhood_noon with Dissolve(1.0)
    stop music
    play music "audio/bgm/MusMus-BGM-087.mp3" volume 0.5
    play sound "audio/sfx/run.mp3"
    th "ผมรีบวิ่งสุดกำลังเพื่อไปโรงเรียนให้ทัน" with dissolve
    en "" with dissolve
    scene back_street_noon with Dissolve(1.0)
    play sound "audio/sfx/ロボットを殴る1.mp3"
    th "ผมสะดุดหกล้มเพราะเผลอไปเตะถังเหล็กเข้าโดยบังเอิญ" with dissolve
    en "I trip and fall because I accidentally kicked a metal bin." with dissolve
    yuma_th  "โอ๊ย!" with dissolve
    yuma_en  "Ouch!" with dissolve
    yuma_th  "ให้ตายสิ คนยิ่งรีบอยู่" with dissolve
    yuma_en  "Damn it, I'm in such a hurry." with dissolve
    th "ตอนนี้ชุดนักเรียนของผมเปรอะเปื้อนฝุ่นตามถนน แถมเนคไทก็หลุดลุ่ย" with dissolve
    en "My school uniform is covered in street dust, and my tie is all messed up." with dissolve
    th "ช่างมัน ตอนนี้ยังไม่จำเป็นต้องใส่ใจเรื่องเล็กๆ น้อยๆ แบบนี้" with dissolve
    en "Never mind. There's no need to worry about little things like this right now." with dissolve
    th "รีบไปโรงเรียนก่อนดีกว่า" with dissolve
    en "I'd better hurry to school." with dissolve
    scene school_front_noon with Dissolve(1.0)
    stop music
    play music "audio/bgm/MusMus-BGM-107.mp3" volume 0.5
    yuma_th  "ในที่สุด… ก็… มา… ถึง… โรงเรียน… แล้ว" with dissolve
    yuma_en  "Finally... I've... made it... to... school..." with dissolve
    th "แม้ว่าบ้านของผมอยู่ห่างจากโรงเรียนไม่มาก" with dissolve
    en "Although my house isn't far from school," with dissolve
    th "แต่ถ้ามัวแต่เดินเอ้อระเหยเหมือนทุกที สายแน่นอนหนึ่งร้อยเปอร์เซ็นต์" with dissolve
    en "If I had dawdled like usual, I'd be late for sure." with dissolve
    th "ด้วยเหตุนี้ผมจึงวิ่งอย่างสุดกำลัง จนมาถึงโรงเรียนในเวลา 8:29 น. ทันเวลาอย่างฉิวเฉียด" with dissolve
    en "That's why I sprinted with all my might and made it to school at 8:29 AM, just in time." with dissolve
    th "หากมาช้ากว่านี้เพียงแค่หนึ่งนาทีจะถือว่ามาสาย" with dissolve
    en "If I had been even a minute slower, I would have been considered late." with dissolve
    stop music
    play music "audio/bgm/MusMus-BGM-125.mp3" volume 0.5
    hide wakeup07
    show border with dissolve
    th "เมื่อหันไปดูบรรยากาศรอบข้าง พบว่าหน้าโรงเรียนตอนนี้มีแต่ความวุ่นวาย" with dissolve
    en "Looking around, I see the school entrance is in chaos." with dissolve
    show akane normal at center with Dissolve(0.2) 
    voice "audio/voice/akane/chapter2/chapter2_1/akane_2_1_001.mp3"
    akane_th angry "นี่เธอ กระโปรงสั้นไปหรือเปล่า" with dissolve
    akane_en angry "Hey, isn't your skirt too short?" with dissolve
    student_f_a_th  "คิดว่าไม่...นะคะ" with dissolve
    student_f_a_en  "I don't... think so..." with dissolve
    voice "audio/voice/akane/chapter2/chapter2_1/akane_2_1_002.mp3"
    akane_th serious "นั่นสินะ ถ้างั้นฉันขอตรวจสอบสักหน่อยละกัน" with dissolve
    akane_en serious "Is that so? Well then, let me check." with dissolve
    th "พอพูดจบ อากาเนะก็หยิบไม้บรรทัดออกมาทาบบริเวณชายกระโปรงของนักเรียนหญิงคนนั้น" with dissolve
    en "As soon as she finishes speaking, Akane pulls out a ruler and places it against the girl's skirt hem." with dissolve
    hide akane
    show akane normal at center with Dissolve(0.2) 
    voice "audio/voice/akane/chapter2/chapter2_1/akane_2_1_003.mp3"
    akane_th serious "16.6 เซนติเมตร… กฎของโรงเรียนอนุญาตให้นักเรียนหญิงสวมกระโปรงสั้นเหนือเข่าได้แค่ 15 เซนติเมตร" with dissolve
    akane_en serious "16.6 centimeters... School rules only allow girls' skirts to be 15 centimeters above the knee." with dissolve
    student_f_a_th  "สั้นว่าแค่ไม่กี่เซนติเมตรเอง แกล้งปล่อยผ่านไปเถอะ" with dissolve
    student_f_a_en  "It's just a few centimeters, can't you let it slide?" with dissolve
    voice "audio/voice/akane/chapter2/chapter2_1/akane_2_1_004.mp3"
    akane_th angry "ไม่ได้ค่ะ กฎต้องเป็นกฎ" with dissolve
    akane_en angry "No, rules are rules." with dissolve
    hide border with dissolve
    th "นักเรียนหญิงอ้อนวอนขอให้อะลุ่มอล่วย แต่อากาเนะปฏิเสธเสียงแข็ง" with dissolve
    en "The girl pleads for leniency, but Akane firmly refuses." with dissolve
    hide akane
    th "ทันใดนั้นผมเผลอสบตาอากาเนะเข้า เธอเดินมาทางผมอย่างไม่รอช้า" with dissolve
    en "Just then, I accidentally make eye contact with Akane. She walks towards me without delay." with dissolve
    th "ให้ความรู้สึกราวกับปีศาจที่กำลังย่างกรายเข้ามา" with dissolve
    en "It feels like a demon approaching." with dissolve
    scene akane with Dissolve(1.0)
    th "อิวาโนะ อากาเนะ กรรมการฝ่ายระเบียบวินัย เธออยู่มัธยมปลายชั้นปีหนึ่ง" with dissolve
    en "Iwano Akane, member of the Disciplinary Committee. She's a first-year high school student." with dissolve
    th "ทำหน้าที่สอดส่องดูแลความเรียบร้อยภายในโรงเรียน" with dissolve
    en "She adheres strictly to every single rule." with dissolve
    th "เธอเป็นยึดมั่นในกฎระเบียบตามตัวอักษรทุกกระเบียดนิ้ว" with dissolve
    en "She adheres strictly to every letter of the rules." with dissolve
    th "ถ้าเห็นคนทำผิดกฎก็จะพุ่งเข้าไปตักเตือนทันที ไม่ว่าอีกฝ่ายเป็นใครก็ตาม" with dissolve
    en "If she sees anyone breaking a rule, she'll rush over to scold them, no matter who they are." with dissolve
    th "แม้กระทั่งรุ่นพี่ปีสองและปีสามต่างก็เกรงกลัวและยอมสยบให้กับเธอ" with dissolve
    en "Even second and third-year students fear and submit to her." with dissolve
    voice "audio/voice/akane/chapter2/chapter2_1/akane_2_1_005.mp3"
    akane_th  "รุ่นพี่ยูมะ พอไม่มีงานสภานักเรียนก็มาสายเลยนะ!" with dissolve
    akane_en  "Yuuma-senpai, when there's no student council work, you're late!" with dissolve
    th "อากาเนะตะโกนเสียงดังลั่น นักเรียนทุกคนที่อยู่บริเวณหน้าโรงเรียนต่างมองมาที่พวกเรา" with dissolve
    en "Akane shouts loudly. Every student at the school entrance turns to look at us." with dissolve
    yuma_th  "อากาเนะ ใจเย็นๆ ก่อน" with dissolve
    yuma_en  "Akane, calm down for a second." with dissolve
    voice "audio/voice/akane/chapter2/chapter2_1/akane_2_1_006.mp3"
    akane_th  "จะให้ใจเย็นได้ยังไงกัน" with dissolve
    akane_en  "How can I be calm?" with dissolve
    voice "audio/voice/akane/chapter2/chapter2_1/akane_2_1_007.mp3"
    akane_th  "เป็นคนจากสภานักเรียน อย่าริอ่านมาสายเด็ดขาด เข้า-ใจ-ไหม" with dissolve
    akane_en  "As a member of the student council, don't you dare be late, un-der-stand?" with dissolve
    yuma_th  "ไม่นับสิ ฉันมาทันเวลาแบบฉิวเฉียดเลยนะ ยังไม่ถึง 8:30 น. สักหน่อย" with dissolve
    yuma_en  "No way, I made it just in time. It's not even 8:30 AM yet." with dissolve
    scene school_front_noon with Dissolve(1.0)
    stop music
    play music "audio/bgm/MusMus-BGM-029.mp3" volume 0.5
    show akane normal at zoom_in,center with Dissolve(0.2) 
    voice "audio/voice/akane/chapter2/chapter2_1/akane_2_1_008.mp3"
    akane_th look2 "ก็ได้ รอบนี้ถือว่ารุ่นพี่ยูมะมาทันเวลา แต่อย่าให้มีครั้งถัดไปอีกนะ เข้า-ใจ-ไหม" with dissolve
    akane_en look2 "Fine, this time I'll consider Yuuma-senpai on time. But don't let there be a next time, un-der-stand?" with dissolve
    yuma_th  "ครับ เข้าใจแล้วครับ" with dissolve
    yuma_en  "Yes, I understand." with dissolve
    voice "audio/voice/akane/chapter2/chapter2_1/akane_2_1_009.mp3"
    akane_th onegai "เห้อ นอกจากมาเกือบสายแล้วยังแต่งตัวไม่เรียบร้อยอีก เนคไทหลุดลุ่ยหมดแล้ว" with dissolve
    akane_en onegai "Sigh, not only are you almost late, but you're not even dressed properly. Your tie is all messed up." with dissolve
    yuma_th  "ช่วยไม่ได้นี่นา เมื่อกี้รีบวิ่งมาสุดชีวิต เนคไทเลยหลุดกลางทาง" with dissolve
    yuma_en  "I couldn't help it. I was running here at full speed, so my tie came loose on the way." with dissolve
    voice "audio/voice/akane/chapter2/chapter2_1/akane_2_1_010.mp3"
    akane_th  "ให้ตายสิ ช่วงหลังมานี้พวกนักเรียนชายชอบคิดว่าสวมเนคไทหลุดลุ่ยเป็นเรื่องเท่กันอยู่ด้วย" with dissolve
    akane_en  "Good grief. Lately, the male students seem to think wearing a loose tie looks cool." with dissolve
    voice "audio/voice/akane/chapter2/chapter2_1/akane_2_1_011.mp3"
    akane_th serious "เสื้อผ้าที่ไม่เรียบร้อยเปรียบเสมือนจิตใจที่ยุ่งเหยิง" with dissolve
    akane_en serious "Untidy clothes reflect a chaotic mind." with dissolve
    play sound "audio/voice/akane/chapter2/chapter2_1/akane_2_1_012.mp3"
    akane_th  "รุ่นพี่เป็นสมาชิกสภานักเรียน ต้องเป็นตัวอย่างที่ดีให้กับนักเรียนคนอื่นสิ" with dissolve
    akane_en  "You're a member of the student council. You should set a good example for other students." with dissolve
    yuma_th  "รู้แล้วล่ะน่า " with dissolve
    yuma_en  "I know, I know. I'm fixing my tie now." with dissolve
    th "ทันใดนั้น อากาเนะก็คว้าเนคไทในมือผมไป" with dissolve
    en "Suddenly, Akane grabs the tie from my hand." with dissolve
    voice "audio/voice/akane/chapter2/chapter2_1/akane_2_1_013.mp3"
    akane_th angry "ไม่ต้อง เดี๋ยวฉันจะผูกให้เอง" with dissolve
    akane_en angry "No need, I'll tie it for you." with dissolve
    th "เอ๊ะ วันนี้มาแปลกนะเนี่ย" with dissolve
    en "Huh? This is unusual." with dissolve
    th "คุณกรรมการระเบียบวินัยสุดโหดอย่างอากาเนะเนี่ยจะผูกเนคไทให้ ...ไม่อยากเชื่อเลย" with dissolve
    en "The super-strict disciplinary committee member Akane is going to tie my tie? ...Impossible" with dissolve
    th "ไอ้นั่นสินะ ที่เขาเรียกกันว่าแฟนเซอร์วิส" with dissolve
    en "Isn't this what they call fan service?" with dissolve
    yuma_th  "เธอผูกเนคไทเป็นด้วยเหรอเนี่ย" with dissolve
    yuma_en  "Do you even know how to tie a tie?" with dissolve
    voice "audio/voice/akane/chapter2/chapter2_1/akane_2_1_014.mp3"
    akane_th look "ผูกเป็นเพราะมีคนที่แต่งตัวไม่เรียบร้อยอย่างรุ่นพี่อยู่ไงคะ" with dissolve
    akane_en look "I learned because there are people like you who can't dress properly." with dissolve
    play sound "audio/voice/akane/chapter2/chapter2_1/akane_2_1_015.mp3"
    akane_th s2 "…แล้วก็ถือโอกาสไว้ลงโทษคนทำผิดกฏในเวลาเดียวกันด้วย!" with dissolve
    akane_en s2 "...And it's also a chance to punish rule-breakers at the same time!" with dissolve
    th "ทันใดนั้น เนคไทที่คอผมก็รัดแน่นขึ้นมาอย่างกะทันหัน" with dissolve
    en "Suddenly, the tie around my neck tightens abruptly." with dissolve
    yuma_th  "โอ๊ยๆ หายใจไม่ออก จะตายแล้ว พอก่อน" with dissolve
    yuma_en  "Ow, ow! I can't breathe. I'm dying. Stop, please!" with dissolve
    th "หลังจากผมร้องขอชีวิตอยู่สักพักหนึ่ง ในที่สุดอากาเนะก็ยอมปล่อยมือออก" with dissolve
    en "After I plead for my life for a while, Akane finally lets go." with dissolve
    show akane normal at center with Dissolve(0.2) 
    voice "audio/voice/akane/chapter2/chapter2_1/akane_2_1_016.mp3"
    akane_th normal "จำไว้ คราวหน้าอย่าให้มีเหตุการณ์แบบนี้เกิดขึ้นอีกนะ" with dissolve
    akane_en normal "Remember, don't let this happen again." with dissolve
    show akane normal at center with Dissolve(0.2) 
    voice "audio/voice/akane/chapter2/chapter2_1/akane_2_1_017.mp3"
    play sound "audio/sfx/escape.mp3"
    akane_th angry "ถ้ารุ่นพี่ยูมะตื่นเช้าตั้งแต่แรก ก็ไม่ต้องรีบวิ่งจนกระเซอะกระเซิงและเนคไทหลุดลุ่ยแบบนี้" with dissolve
    akane_en angry "If Yuuma-senpai woke up early in the first place, you wouldn't have to rush and end up all disheveled with a loose tie like this." with dissolve
    play sound "audio/voice/akane/chapter2/chapter2_1/akane_2_1_018.mp3"
    akane_th  "จำไว้ นกที่ตื่นเช้าจับหนอนกินได้ก่อนใคร" with dissolve
    akane_en  "Remember, the early bird catches the worm." with dissolve
    yuma_th  "หนอนที่ตื่นสายจะรอดจากการถูกนกกิน" with dissolve
    yuma_en  "The late worm avoids being caught by the bird." with dissolve
    show akane normal at zoom_in,center with Dissolve(0.2) 
    voice "audio/voice/akane/chapter2/chapter2_1/akane_2_1_019.mp3"
    show angry
    akane_th angrymeme "รุ่น~พี่~ยู~ มะ~" with dissolve
    akane_en angrymeme "Sen~ pai~!!!" with dissolve
    hide angry
    voice "audio/voice/akane/chapter2/chapter2_1/akane_2_1_020.mp3"
    akane_th  "บางทีโรงเรียนในนรกอาจจะอนุญาตให้มาสายก็ได้นะ สนใจลองดูสักหน่อยมั้ย" with dissolve
    akane_en  "Maybe schools in hell allow tardiness. Want me to send you there?" with dissolve
    th "อากาเนะกำเนคไทของผมไว้แน่น ผมสัมผัสได้ว่าเธอพร้อมออกแรงอย่างเต็มที่" with dissolve
    en "Akane grips my tie tightly. I can feel she's ready to use her full strength." with dissolve
    yuma_th  "ขอโทษ! เข้าใจแล้วค้าบ รอบหน้าจะไม่มาสายอีกแล้ว" with dissolve
    yuma_en  "I'm sorry! I understand! I won't be late again!" with dissolve
    voice "audio/voice/akane/chapter2/chapter2_1/akane_2_1_021.mp3"
    akane_th serious "เข้าใจก็ดีแล้ว… อ๊ะ!" with dissolve
    akane_en serious "Good that you understand... Ah!" with dissolve
    play sound "audio/sfx/squeeze.mp3"
    th "ทันใดนั้น อากาเนะทำสายตาเหมือนแมวที่เจอหนูวิ่งผ่านต่อหน้าต่อตา" with dissolve
    en "Suddenly, Akane's eyes look like a cat that's just spotted a mouse running by." with dissolve
    voice "audio/voice/akane/chapter2/chapter2_1/akane_2_1_022.mp3"
    akane_th s2 "หยุดก่อน นักเรียนชายตรงนั้น จะรีบไปไหน นายมาโรงเรียนสายนะ" with dissolve
    akane_en s2 "Stop right there, boy! Where are you rushing to? You're late for school." with dissolve
    hide akane
    student_m_a_th  "งานเข้า นึกว่าจะรอดแล้วเชียว" with dissolve
    student_m_a_en  "Dammit. I thought I was in the clear." with dissolve
    th "พอพูดจบ อากาเนะก็วิ่งไปขวางนักเรียนที่มาสาย" with dissolve
    en "As soon as she finishes speaking, Akane runs to block the late student." with dissolve
    th "ขืนอยู่ต่อผมอาจจะโดนลูกหลงไปด้วย ด้วยเหตุนี้ผมจึงอาสัยจังหวะชุลมุนรีบเดินเข้าอาคารเรียน" with dissolve
    en "If I stay any longer, I might get caught in the crossfire. So, I take advantage of the commotion to quickly enter the school building." with dissolve
    scene black with Dissolve(1.0)
    jump s2_2
    return