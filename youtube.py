from selenium import webdriver
import pafy,vlc,playsound,time
import cv2

def formatter(img):
    w,h,d=img.shape
    wi=(w//2)-60
    hi=(h//2)-100
    return img[wi:,hi:]

driver=webdriver.Chrome('C:\Users\peddy\Downloads\chromedriver_win32\chromedriver.exe')
driver.get('https://www.youtube.com')
time.sleep(20)
run=True
start=True
time_frame=0
fn=0
while True:
    cururl=driver.current_url
    video=pafy.new(cururl)
    best_video = video.getbestvideo()
    best_audio = video.getbestaudio()

    x=vlc.MediaPlayer(best_audio.url)

    cap=cv2.VideoCapture(best_video.url)
    while True:
        filhal_ka_url=driver.current_url
        if cururl==filhal_ka_url:
            if time_frame%1.5==0 and run==True:
                print (time_frame)
                ret,img=cap.read()
                if ret:
                    if start==True:
                        x.play()
                        start=False
                    #img=formatter(img)
                    img = cv2.resize(img, (640, 480))
                    img=cv2.Canny(img,100,200)

                    cv2.imshow('image',img)
            if cv2.waitKey(1)==ord('p'):
                if run==True:
                    run=False
                    x.pause()
                else:
                    run=True
                    x.play()
            elif cv2.waitKey(2)==ord('q'):
                fn=1
                break
        else:
            break
        time_frame+=1
        print (time_frame)
    if fn==1:
        break
driver.close()