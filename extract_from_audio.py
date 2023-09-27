import whisper
import os
import sys
import cv2
import numpy as np


def extract_text(file):   
    #convert video to audio 
    os.system("ffmpeg -i "+file+" -map 0:a -acodec copy audio.mp4")
    model = whisper.load_model("base")
    result = model.transcribe("audio.mp4", verbose = False)
    os.system("rm audio.mp4")
    return result["segments"]

def mse(img1, img2):
   h, w = img1.shape
   diff = cv2.subtract(img1, img2)
   err = np.sum(diff**2)
   mse = err/(float(h*w))
   return mse

def extract_images(file):
    #clean
    os.system('rm -r Data')
    cap=cv2.VideoCapture(file)
    fps = cap.get(cv2.CAP_PROP_FPS)
    images=[0]
    times=[0]
    # Read the video from specified path
    cam = cv2.VideoCapture(file)
    
    try:
        # creating a folder named data
        if not os.path.exists('data'):
            os.makedirs('data')
    
    # if not created then raise error
    except OSError:
        print ('Error: Creating directory of data')
    
    # frame
    #inti time
    currentframe = 0
    res=0
    
    while(True):
        
        # reading from frame
        ret,frame = cam.read()

        if ret:
            # if video is still left continue creating images
            time=float(currentframe/fps)
            name = './data/frame' + str(time) + '.jpg'
            path ='/data/frame' + str(time) + '.jpg'    
            if(currentframe>0):
                img1 = cv2.cvtColor(frame_old, cv2.COLOR_BGR2GRAY)
                img2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                res=mse(img1,img2)
                if (res>=5.0):
                    #print ('Creating...' + name+" "+str(res))
                    # writing the extracted images
                    cv2.imwrite(name, frame)
                    times.append(time)
                    images.append("![]"+"("+path+")")           

            else:
                #print ('Creating...' + name+" "+str(res))
                # writing the extracted images
                cv2.imwrite(name, frame)
                times.append(time)
                images.append("![]"+"("+path+")")

       
            currentframe += 1
            frame_old=frame
        else:
            break
    
    # Release all space and windows once done
    cam.release()
    cv2.destroyAllWindows()
    return times,images

#file = sys.argv[1]
os.system("rm TEST.md")
#print(file)
file = "test.mp4"
array=extract_images(file)
data=extract_text(file)
end_old=0.0

for i, seg in enumerate(data):
    print(i+1, "- ", seg['text'],file=open('TEST.md', 'a'))
    count=0    
    for time in array[0]:
        if time >=end_old and time <= seg['end']:
            print(array[1][count],file=open('TEST.md', 'a'))
        
        count+=1
    
    end_old=seg['end']