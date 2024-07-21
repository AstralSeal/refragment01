#python .\generate_charector.py > charector.rpy
import os

# Print the current working directory
#print("Current working directory:", os.getcwd())

# Use the absolute path to the images directory
###########REIKA###########################################################
mypath = r"D:\renpy-8.0.3-sdk\renpy-8.0.3-sdk\project3rd\game\images\Sprite\reika01"

# /reika02_shy.png -> shy
def get_emotion_from_file(file_name):
    return c.split(".")[0].split("_")[-1]
    

# Check if the path exists
if not os.path.exists(mypath):
    print(f"The directory {mypath} does not exist.")
else:
    # List files in the directory
    onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
    #print(onlyfiles)

for c in onlyfiles:
    print(f'image reika {get_emotion_from_file(c)}:')
    print(f'    zoom 0.75')
    print(f'    xoffset 25')
    print(f'    im.Composite((1433,3100), (0,2000), "Sprite/reika01/reika01_body.png" ,(0,2000), "Sprite/reika01/{c}" )')

for c in onlyfiles:
    print(f'image reika_p {get_emotion_from_file(c)}:')
    print(f'    zoom 0.75')
    print(f'    xoffset 25')
    print(f'    im.Composite((1433,3100), (0,2000), "Sprite/reika01/reika01_p_body.png" ,(0,2000), "Sprite/reika01/{c}" )')

for c in onlyfiles:
    print(f'image side reika {get_emotion_from_file(c)}:')
    print(f'    zoom 0.25')
    print(f'    xoffset 100')
    print(f'    yoffset 0')
    print(f'    im.Composite((1433,3100), (0,2000), "Sprite/reika01/reika01_body.png" ,(0,2000), "Sprite/reika01/{c}" )')

for c in onlyfiles:
    print(f'image side reika_p {get_emotion_from_file(c)}:')
    print(f'    zoom 0.25')
    print(f'    xoffset 100')
    print(f'    yoffset 0')
    print(f'    im.Composite((1433,3100), (0,2000), "Sprite/reika01/reika01_p_body.png" ,(0,2000), "Sprite/reika01/{c}" )')

mypath = r"D:\renpy-8.0.3-sdk\renpy-8.0.3-sdk\project3rd\game\images\Sprite\reika02"

# Check if the path exists
if not os.path.exists(mypath):
    print(f"The directory {mypath} does not exist.")
else:
    # List files in the directory
    onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
    #print(onlyfiles)

for c in onlyfiles:
    print(f'image reika {get_emotion_from_file(c)}_2:')
    print(f'    zoom 0.75')
    print(f'    xoffset 25')
    print(f'    im.Composite((1433,3100), (0,2000), "Sprite/reika02/reika02_body.png" ,(0,2000), "Sprite/reika02/{c}" )')

for c in onlyfiles:
    print(f'image reika_p {get_emotion_from_file(c)}_2:')
    print(f'    zoom 0.75')
    print(f'    xoffset 25')
    print(f'    im.Composite((1433,3100), (0,2000), "Sprite/reika02/reika02_p_body.png" ,(0,2000), "Sprite/reika02/{c}" )')

for c in onlyfiles:
    print(f'image side reika {get_emotion_from_file(c)}_2:')
    print(f'    zoom 0.25')
    print(f'    xoffset 100')
    print(f'    yoffset 0')
    print(f'    im.Composite((1433,3100), (0,2000), "Sprite/reika02/reika02_body.png" ,(0,2000), "Sprite/reika02/{c}" )')

for c in onlyfiles:
    print(f'image side reika_p {get_emotion_from_file(c)}_2:')
    print(f'    zoom 0.25')
    print(f'    xoffset 100')
    print(f'    yoffset 0')
    print(f'    im.Composite((1433,3100), (0,2000), "Sprite/reika02/reika02_p_body.png" ,(0,2000), "Sprite/reika02/{c}" )')

##########################################################################################################

###########Yuno##################################################################################

mypath = r"D:\renpy-8.0.3-sdk\renpy-8.0.3-sdk\project3rd\game\images\Sprite\yuno01"

# /reika02_shy.png -> shy
def get_emotion_from_file(file_name):
    return c.split(".")[0].split("_")[-1]
    

# Check if the path exists
if not os.path.exists(mypath):
    print(f"The directory {mypath} does not exist.")
else:
    # List files in the directory
    onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
    #print(onlyfiles)

for c in onlyfiles:
    print(f'image yuno {get_emotion_from_file(c)}:')
    print(f'    zoom 0.75')
    print(f'    xoffset 25')
    print(f'    im.Composite((1433,3100), (0,2000), "Sprite/yuno01/yuno01_body.png" ,(0,2000), "Sprite/yuno01/{c}" )')

for c in onlyfiles:
    print(f'image yuno_p {get_emotion_from_file(c)}:')
    print(f'    zoom 0.75')
    print(f'    xoffset 25')
    print(f'    im.Composite((1433,3100), (0,2000), "Sprite/yuno01/yuno01_p_body.png" ,(0,2000), "Sprite/yuno01/{c}" )')


for c in onlyfiles:
    print(f'image side yuno {get_emotion_from_file(c)}:')
    print(f'    zoom 0.25')
    print(f'    xoffset 100')
    print(f'    yoffset 0')
    print(f'    im.Composite((1433,3100), (0,2000), "Sprite/yuno01/yuno01_body.png" ,(0,2000), "Sprite/yuno01/{c}" )')

for c in onlyfiles:
    print(f'image side yuno_p {get_emotion_from_file(c)}:')
    print(f'    zoom 0.25')
    print(f'    xoffset 100')
    print(f'    yoffset 0')
    print(f'    im.Composite((1433,3100), (0,2000), "Sprite/yuno01/yuno01_p_body.png" ,(0,2000), "Sprite/yuno01/{c}" )')

mypath = r"D:\renpy-8.0.3-sdk\renpy-8.0.3-sdk\project3rd\game\images\Sprite\yuno02"

# /reika02_shy.png -> shy
def get_emotion_from_file(file_name):
    return c.split(".")[0].split("_")[-1]
    

# Check if the path exists
if not os.path.exists(mypath):
    print(f"The directory {mypath} does not exist.")
else:
    # List files in the directory
    onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
    #print(onlyfiles)

for c in onlyfiles:
    print(f'image yuno {get_emotion_from_file(c)}_2:')
    print(f'    zoom 0.75')
    print(f'    xoffset 25')
    print(f'    im.Composite((1433,3100), (0,2000), "Sprite/yuno02/yuno02_body.png" ,(0,2000), "Sprite/yuno02/{c}" )')

for c in onlyfiles:
    print(f'image yuno_p {get_emotion_from_file(c)}_2:')
    print(f'    zoom 0.75')
    print(f'    xoffset 25')
    print(f'    im.Composite((1433,3100), (0,2000), "Sprite/yuno02/yuno02_p_body.png" ,(0,2000), "Sprite/yuno02/{c}" )')

for c in onlyfiles:
    print(f'image side yuno {get_emotion_from_file(c)}_2:')
    print(f'    zoom 0.25')
    print(f'    xoffset 100')
    print(f'    yoffset 0')
    print(f'    im.Composite((1433,3100), (0,2000), "Sprite/yuno02/yuno02_body.png" ,(0,2000), "Sprite/yuno02/{c}" )')

for c in onlyfiles:
    print(f'image side yuno_p {get_emotion_from_file(c)}_2:')
    print(f'    zoom 0.25')
    print(f'    xoffset 100')
    print(f'    yoffset 0')
    print(f'    im.Composite((1433,3100), (0,2000), "Sprite/yuno02/yuno02_p_body.png" ,(0,2000), "Sprite/yuno02/{c}" )')

#################################################################################################

################Maya#################################################################

mypath = r"D:\renpy-8.0.3-sdk\renpy-8.0.3-sdk\project3rd\game\images\Sprite\maya01"

# /reika02_shy.png -> shy
def get_emotion_from_file(file_name):
    return c.split(".")[0].split("_")[-1]
    

# Check if the path exists
if not os.path.exists(mypath):
    print(f"The directory {mypath} does not exist.")
else:
    # List files in the directory
    onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
    #print(onlyfiles)

for c in onlyfiles:
    print(f'image maya {get_emotion_from_file(c)}:')
    print(f'    zoom 0.75')
    print(f'    xoffset 25')
    print(f'    im.Composite((1433,3100), (0,2000), "Sprite/maya01/maya01_body.png" ,(0,2000), "Sprite/maya01/{c}" )')

for c in onlyfiles:
    print(f'image maya_p {get_emotion_from_file(c)}:')
    print(f'    zoom 0.75')
    print(f'    xoffset 25')
    print(f'    im.Composite((1433,3100), (0,2000), "Sprite/maya01/maya01_p_body.png" ,(0,2000), "Sprite/maya01/{c}" )')

for c in onlyfiles:
    print(f'image side maya {get_emotion_from_file(c)}:')
    print(f'    zoom 0.25')
    print(f'    xoffset 100')
    print(f'    yoffset 0')
    print(f'    im.Composite((1433,3100), (0,2000), "Sprite/maya01/maya01_body.png" ,(0,2000), "Sprite/maya01/{c}" )')

for c in onlyfiles:
    print(f'image side maya_p {get_emotion_from_file(c)}:')
    print(f'    zoom 0.25')
    print(f'    xoffset 100')
    print(f'    yoffset 0')
    print(f'    im.Composite((1433,3100), (0,2000), "Sprite/maya01/maya01_p_body.png" ,(0,2000), "Sprite/maya01/{c}" )')

mypath = r"D:\renpy-8.0.3-sdk\renpy-8.0.3-sdk\project3rd\game\images\Sprite\maya02"

# /reika02_shy.png -> shy
def get_emotion_from_file(file_name):
    return c.split(".")[0].split("_")[-1]
    

# Check if the path exists
if not os.path.exists(mypath):
    print(f"The directory {mypath} does not exist.")
else:
    # List files in the directory
    onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
    #print(onlyfiles)

for c in onlyfiles:
    print(f'image maya {get_emotion_from_file(c)}_2:')
    print(f'    zoom 0.75')
    print(f'    xoffset 25')
    print(f'    im.Composite((1433,3100), (0,2000), "Sprite/maya02/maya02_body.png" ,(0,2000), "Sprite/maya02/{c}" )')

for c in onlyfiles:
    print(f'image maya_p {get_emotion_from_file(c)}_2:')
    print(f'    zoom 0.75')
    print(f'    xoffset 25')
    print(f'    im.Composite((1433,3100), (0,2000), "Sprite/maya02/maya02_p_body.png" ,(0,2000), "Sprite/maya02/{c}" )')

for c in onlyfiles:
    print(f'image side maya {get_emotion_from_file(c)}_2:')
    print(f'    zoom 0.25')
    print(f'    xoffset 100')
    print(f'    yoffset 0')
    print(f'    im.Composite((1433,3100), (0,2000), "Sprite/maya02/maya02_body.png" ,(0,2000), "Sprite/maya02/{c}" )')

for c in onlyfiles:
    print(f'image side maya_p {get_emotion_from_file(c)}_2:')
    print(f'    zoom 0.25')
    print(f'    xoffset 100')
    print(f'    yoffset 0')
    print(f'    im.Composite((1433,3100), (0,2000), "Sprite/maya02/maya02_p_body.png" ,(0,2000), "Sprite/maya02/{c}" )')

#################################################################################################