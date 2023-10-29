import cv2
import dropbox
import time
import random

start_time=time.time()
#captures the time when the code first gets executed like it's 11:58 when i executed the code

def take_snapshot():
    number = random.randint(0,100)
    #genereates a random number between 0 and 100 for picture names
    #initializing cv2
    videoCaptureObject = cv2.VideoCapture(0)
    #it opens the camera, 0 meaning camera
    result = True 
    #result is a variable that will decide whether loop executes or not
    while(result):
        #while (result) means till the time result is true while will execute
        #read the frames while the camera is on
        ret,frame = videoCaptureObject.read()
        #read function takes the pictures and stores in frame
        #ret tells you whether if the picture is taken or not
        #cv2.imwrite() method is used to save an image to any storage device
        img_name = "img"+str(number)+".png"
        #img23.png
        #img87.png
        cv2.imwrite(img_name, frame)
        #it saves the image
        start_time = time.time
        result = False
    return img_name
    print("snapshot taken")
    # releases the camera
    videoCaptureObject.release()
    #closes all the window that might be opened while this process
    cv2.destroyAllWindows()



def upload_file(img_name):
    access_token = "sl.BobrPZsgY_8KlV-YnDUt40WY81GhWlxrUsYjjkM5Y_iOwZRiP_rcn_LJ5eCnsq5kWbcgV86t9TvFMOWea6SvNDFboPZlDNGCaubAkDofy35REFpPF6eTyhkrqngaW7ijhPAYG2ZwyZGKyR-Bk41FzqQ"
    file =img_name
    file_from = file
    file_to="/coding_byjus/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")


def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=take_snapshot()
            upload_file(name)

main()
