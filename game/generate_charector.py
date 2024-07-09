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

##########################################################################################################

###########NANAMI##################################################################################

mypath = r"D:\renpy-8.0.3-sdk\renpy-8.0.3-sdk\project3rd\game\images\Sprite\nanami01"

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
    print(f'image nanami {get_emotion_from_file(c)}:')
    print(f'    zoom 0.75')
    print(f'    xoffset 25')
    print(f'    im.Composite((1433,3100), (0,2000), "Sprite/nanami01/nanami01_body.png" ,(0,2000), "Sprite/nanami01/{c}" )')

for c in onlyfiles:
    print(f'image nanami_p {get_emotion_from_file(c)}:')
    print(f'    zoom 0.75')
    print(f'    xoffset 25')
    print(f'    im.Composite((1433,3100), (0,2000), "Sprite/nanami01/nanami01_p_body.png" ,(0,2000), "Sprite/nanami01/{c}" )')



mypath = r"D:\renpy-8.0.3-sdk\renpy-8.0.3-sdk\project3rd\game\images\Sprite\nanami02"

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
    print(f'image nanami {get_emotion_from_file(c)}_2:')
    print(f'    zoom 0.75')
    print(f'    xoffset 25')
    print(f'    im.Composite((1433,3100), (0,2000), "Sprite/nanami02/nanami02_body.png" ,(0,2000), "Sprite/nanami02/{c}" )')

for c in onlyfiles:
    print(f'image nanami_p {get_emotion_from_file(c)}_2:')
    print(f'    zoom 0.75')
    print(f'    xoffset 25')
    print(f'    im.Composite((1433,3100), (0,2000), "Sprite/nanami02/nanami02_p_body.png" ,(0,2000), "Sprite/nanami02/{c}" )')



#################################################################################################

#############################################################################################

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



#################################################################################################