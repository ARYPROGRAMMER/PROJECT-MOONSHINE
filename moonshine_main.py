'''

TESTED ON :

Processor	AMD Ryzen 5 5600H with Radeon Graphics 3.30 GHz
Installed RAM	8.00 GB (7.36 GB usable)
System type	64-bit operating system, x64-based processor

Edition	Windows 11 Home Single Language
Version	21H2
OS build 22000.708
Experience Windows Feature Experience Pack 1000.22000.708.0

Python Version 3.7.9 64-bit 

MADE WITH LOVE
BY KARYA (KARTHIK & ARYA)

'''



import multiprocessing
import random

import os
try:
    os.system('pip install -q -r requirements.txt')
    ms=0
except:
    ms=1
import cv2
import os.path
import glob
import csv
import time as ti
from datetime import datetime
import subprocess
import sys
import psutil
from tkinter import *
import numpy as np
import moonshine_sunshine as htm
t=0
try:
    import autopy
except Exception as ImportError:
    print(ImportError)
    t=1

if t==0 and ms==0:
    try:
        class main_program(multiprocessing.Process):
            def run(self):
                global rad
                start_time = ti.time()
                Id = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
                location = os.getcwd()
                parent_dir = location 
                rad = (random.random())*100



                def delete1():
                    screen1.destroy()


                def delete2():
                    screen2.destroy()


                def delete3():
                    screen3.destroy()


                def delete4():
                    screen4.destroy()
                    
                def delete5():
                    screen5.destroy()

                def delete():
                    screen.destroy()

                def save_time():
                    global save_TIME
                    save_TIME = TIME.get()

                def save_fps():
                    global save_FPS
                    save_FPS = FPS.get()

                def save_webcam():
                    global save_WEBCAM
                    save_WEBCAM = WEBCAM.get()

                def save_play():
                    global save_PLAY
                    save_PLAY = PLAY.get()

                def save_save():
                    global save_SAVE
                    save_SAVE = SAVE.get()





                def time():


                    global screen1
                    screen1 = Toplevel(screen)
                    screen1.title("DURATION")
                    screen1.geometry("600x300")
                    
                    global TIME
                    global time_entry
                    TIME = StringVar()

                    Label(screen1, text = "PLEASE ENTER DURATION OF VIDEO",fg='red',font=("Times New Roman", 14,'bold')).pack()
                    Label(screen1, text = "").pack()
                    Label(screen1, text = "DURATION * ",fg='cyan',font=("Times New Roman", 12,'bold')).pack()

                    time_entry = Entry(screen1, textvariable = TIME)
                    time_entry.pack()
                    Button(screen1, text = "SAVE", width = 20, height = 2, fg='green',font=("Times New Roman", 12,'bold'),command = save_time).pack()
                    Label(screen1, text = "").pack()
                    Button(screen1, text = "PROCEED", width = 20, height = 2, fg='green',font=("Times New Roman", 12,'bold'),command = delete1).pack()
                    


                def fps():

                    global screen2
                    screen2 = Toplevel(screen)
                    screen2.title("FRAMES PER SECOND")
                    screen2.geometry("600x300")
                    
                    global FPS
                    global fps_entry
                    FPS = StringVar()

                    Label(screen2, text = "PLEASE ENTER REQUIRED FPS",fg='red',font=("Times New Roman", 14,'bold')).pack()
                    Label(screen2, text = "").pack()
                    Label(screen2, text = "FPS * ",fg='cyan',font=("Times New Roman", 12,'bold')).pack()
                    
                    fps_entry = Entry(screen2, textvariable = FPS)
                    fps_entry.pack()
                    Button(screen2, text = "SAVE", width = 20, height = 2, fg='green',font=("Times New Roman", 12,'bold'),command = save_fps).pack()
                    Label(screen2, text = "").pack()
                    Button(screen2, text = "PROCEED", width = 20, height = 2, fg='green',font=("Times New Roman", 12,'bold'),command = delete2).pack()

                    
                def webcam():
                
                    global screen3
                    screen3 = Toplevel(screen)
                    screen3.title("WEBCAM ACCESS")
                    screen3.geometry("600x300")
                    
                    global WEBCAM
                    global webcam_entry
                    WEBCAM = StringVar()

                    Label(screen3, text = "DO YOU HAVE EXTERNAL WEBCAM?",fg='red',font=("Times New Roman", 14,'bold')).pack()
                    Label(screen3, text = "").pack()
                    Label(screen3, text = "WEBCAM INFO * ",fg='cyan',font=("Times New Roman", 12,'bold')).pack()
                    
                    webcam_entry = Entry(screen3, textvariable = WEBCAM)
                    webcam_entry.pack()
                    Button(screen3, text = "SAVE", width = 20, height = 2, fg='green',font=("Times New Roman", 12,'bold'),command = save_webcam).pack()
                    Label(screen3, text = "").pack()
                    Button(screen3, text = "PROCEED", width = 20, height = 2, fg='green',font=("Times New Roman", 12,'bold'),command = delete3).pack()

                    
                def save():

                    global screen4
                    screen4 = Toplevel(screen)
                    screen4.title("KEEP OR NOT")
                    screen4.geometry("600x300")
                    
                    global SAVE
                    global save_entry
                    SAVE = StringVar()

                    Label(screen4, text = "DO YOU WISH TO KEEP CAPTURED IMAGES?",fg='red',font=("Times New Roman", 14,'bold')).pack()
                    Label(screen4, text = "").pack()
                    Label(screen4, text = "YOUR ANSWER * ",fg='cyan',font=("Times New Roman", 12,'bold')).pack()
                    
                    save_entry = Entry(screen4, textvariable = SAVE)
                    save_entry.pack()
                    Button(screen4, text = "SAVE", width = 20, height = 2, fg='green',font=("Times New Roman", 12,'bold'),command = save_save).pack()
                    Label(screen4, text = "").pack()
                    Button(screen4, text = "PROCEED", width = 20, height = 2, fg='green',font=("Times New Roman", 12,'bold'),command = delete4).pack()
                
                def playo():

                    global screen5
                    screen5 = Toplevel(screen)
                    screen5.title("PLAY OR NOT")
                    screen5.geometry("600x300")
                    
                    global PLAY
                    global play_entry
                    PLAY = StringVar()

                    Label(screen5, text = "ENTER 1 TO PLAY ANIMATED VIDEO",fg='red',font=("Times New Roman", 14,'bold')).pack()
                    Label(screen5, text = "").pack()
                    Label(screen5, text = "YOUR ANSWER * ",fg='cyan',font=("Times New Roman", 12,'bold')).pack()
                    
                    play_entry = Entry(screen5, textvariable = PLAY)
                    play_entry.pack()
                    Button(screen5, text = "SAVE", width = 20, height = 2, fg='green',font=("Times New Roman", 12,'bold'),command = save_play).pack()
                    Label(screen5, text = "").pack()
                    Button(screen5, text = "PROCEED", width = 20, height = 2, fg='green',font=("Times New Roman", 12,'bold'),command = delete5).pack()


                def main_screen():
                
                    global screen
                    screen = Tk()
                    screen.geometry("600x300")
                    screen.title("DETAILS")
                    screen.configure(background='black')
                    Label(text = "SUBMIT YOUR DETAILS", fg='black',bg='white', width = "600", height = "4", font = ("Times New Roman", 16)).pack()
                    Label(text = "").pack()


                    Button(text = "TIME", height = "4", width = "60", fg='white',bg='black',font=("Times New Roman", 14,'bold'),command = time).pack()
                    

                    Label(text = "").pack()

                    
                    Button(text = "FPS",height = "4", width = "60", fg='white',bg='black',font=("Times New Roman", 14,'bold'),command = fps).pack()


                    Label(text = "").pack()

                    
                    Button(text = "EXTERNAL WEBCAM", height = "4", width = "60", fg='white',bg='black',font=("Times New Roman", 14,'bold'),command = webcam).pack()
                        

                    Label(text = "").pack()

                    
                    Button(text = "REGARDING SAVING",height = "4", width = "60", fg='white',bg='black',font=("Times New Roman", 14,'bold'),command = save).pack()
                    

                    Label(text = "").pack()
                    
                    Button(text = "PLAY ON END" ,height = "4", width = "60", fg='white',bg='black',font=("Times New Roman", 14,'bold'),command = playo).pack()
                    

                    Label(text = "").pack()

                    Button(text = "PROCEED",height = "4", width = "60", fg='white',bg='black',font=("Times New Roman", 14,'bold'),command = delete).pack()
                    screen.attributes('-topmost',True)
                    screen.mainloop()



                main_screen()

                try:
                    frames = int(save_FPS)*int(save_TIME)
                except Exception as CriticalError:
                    pass

                try:
                    directory = f"RAW_IMAGES{rad}"  
                    path = os.path.join(parent_dir, directory)
                    os.mkdir(path)
                    directory = f"SKETCHED_IMAGES{rad}"
                    parent_dir = location
                    path = os.path.join(parent_dir, directory)
                    os.mkdir(path)
                    
                except Exception as error1:
                    pass

                try:
                    directory = f"RUNTIME_LOGS"
                    parent_dir = location
                    path = os.path.join(parent_dir, directory)
                    os.mkdir(path)
                except Exception as error2:
                    pass

                try:
                    key = cv2. waitKey(1)
                    if save_WEBCAM.lower() == 'no':
                        webcam = cv2.VideoCapture(0, apiPreference=cv2.CAP_ANY, params=[
                        cv2.CAP_PROP_FRAME_WIDTH, 100000,
                        cv2.CAP_PROP_FRAME_HEIGHT, 100000])

                        width = int(webcam.get(cv2.CAP_PROP_FRAME_WIDTH))
                        height = int(webcam.get(cv2.CAP_PROP_FRAME_HEIGHT))
                    else:
                        webcam = cv2.VideoCapture(1, apiPreference=cv2.CAP_ANY, params=[
                        cv2.CAP_PROP_FRAME_WIDTH, 100000,
                        cv2.CAP_PROP_FRAME_HEIGHT, 100000])

                        width = int(webcam.get(cv2.CAP_PROP_FRAME_WIDTH))
                        height = int(webcam.get(cv2.CAP_PROP_FRAME_HEIGHT))
                except Exception as error3:
                    pass

                ti.sleep(2)


                k = 0
                try:
                    while k<frames+1:
                        k += 1
                        try:
                            check, frame = webcam.read()
                            cv2.imshow("Capturing", frame)
                            key = cv2.waitKey(1)
                            os.chdir(f'{location}/RAW_IMAGES{rad}')
                            cv2.imwrite(filename=f'saved_img{k}.jpg', img=frame)
                            img = cv2.imread(f"saved_img{k}.jpg")
                            img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
                            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                            img_invert = cv2.bitwise_not(img_gray)
                            img_smoothing = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)
                            final = cv2.divide(img_gray, 255 - img_smoothing, scale=255)
                            os.chdir(f'{location}/SKETCHED_IMAGES{rad}')
                            cv2.imwrite(f'sketch{k}.jpg',final)
                            if key == ord('q'):
                                webcam.release()
                                cv2.destroyAllWindows()
                                break
                        
                        except(KeyboardInterrupt):
                            print("Turning off camera.")
                            webcam.release()
                            print("Camera off.")
                            print("Program ended.")
                            cv2.destroyAllWindows()
                            break
                except Exception as error4:
                    pass
                os.chdir(f'{parent_dir}/SKETCHED_IMAGES{rad}')
                fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
                video = cv2.VideoWriter('SKETCHED_ANIMATION.avi', fourcc, int(save_FPS), (width,height))


                try:
                
                    for i in range(1,frames+1):
                        img = cv2.imread(f'sketch{i}.jpg')
                        video.write(img)

                    cv2.destroyAllWindows()
                    video.release()

                    os.chdir(f'{parent_dir}/RAW_IMAGES{rad}')
                    fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
                    video = cv2.VideoWriter('RAW_ANIMATION.avi', fourcc, int(save_FPS), (width,height))

                    for i in range(1,frames+1):
                        img = cv2.imread(f'saved_img{i}.jpg')
                        video.write(img)

                    cv2.destroyAllWindows()
                    video.release()
                except Exception as error5:
                    pass

                try:
                    if save_SAVE != 'yes':
                        os.chdir(f'{parent_dir}/RAW_IMAGES{rad}')
                        for k in range(1,frames+2):
                            removing_files = glob.glob(f'saved_img{k}.jpg')
                            for i in removing_files:
                                os.remove(i)

                        os.chdir(f'{parent_dir}/SKETCHED_IMAGES{rad}')
                        for k in range(1,frames+2):
                            removing_files = glob.glob(f'sketch{k}.jpg')
                            for i in removing_files:
                                os.remove(i)
                                
                except Exception as error6:
                    pass

            
                try:
                    if int(save_PLAY) == 1:
                        os.chdir(f"{parent_dir}/SKETCHED_IMAGES{rad}")
                        cap = cv2.VideoCapture('SKETCHED_ANIMATION.avi')
                        ti.sleep(5)
                        if (cap.isOpened()== False):
                            print("Error opening video file")

                        while(cap.isOpened()):
                            
                            ret, frame = cap.read()
                            if ret == True:
                                
                                cv2.imshow('Frame', frame)

                                
                                if cv2.waitKey(25) & 0xFF == ord('q'):
                                    break

                        
                            else:
                                break

                        cap.release()


                        cv2.destroyAllWindows()

                    else:
                        print("THANK YOU")

                except Exception as error7:
                    pass


                end = ti.time()
                elap = end-start_time
                elap = "TOTAL ELAPSED TIME" + str(elap)

                os.chdir(f"{parent_dir}/RUNTIME_LOGS")
                myf = open(f'log{rad}.csv','a+') 
                csvwriter = csv.writer(myf,delimiter = " ") 

                p = "PYTHON VERSION" + sys.version
                Id.insert(0,"SYSTEM INFO.")
                for i in Id:
                    if i.isspace():
                        Id.remove(i)

                l = datetime.now()
                m = "DATE AND TIME" + str(l)

                csvwriter.writerow(Id)
                csvwriter.writerow(p)
                csvwriter.writerow(m)
                csvwriter.writerow(elap)


                p = psutil.Process()
                for i in range(20):
                    if i==19:
                        x = p.io_counters()
                csvwriter.writerow("READ AND WRITE SPEED "+ str(x))

                cam_info = f"CAMERA RESOLUTION : {width},{height}"

                csvwriter.writerow(cam_info)
                id1 = os.getpid()
                id3 = os.getppid()

                csvwriter.writerow(f"process id of main process is : {id1}")
                csvwriter.writerow(f"parent process id of main process is : {id3}")
                csvwriter.writerow(f"CPU CORE: {multiprocessing.cpu_count()}")
                
                # PREFERANCES
                csvwriter.writerow(f'FPS : {save_FPS}')
                csvwriter.writerow(f'PLAY ON END : {save_PLAY}')
                csvwriter.writerow(f'SAVE IMAGES : {save_SAVE}')
                csvwriter.writerow(f'TIME : {save_TIME}')
                csvwriter.writerow(f'EXTERNAL WEBCAM : {save_WEBCAM}')
                
                
                try:
                    csvwriter.writerow(error1) or csvwriter.writerow(error2) or csvwriter.writerow(error3) or csvwriter.writerow(error4) or csvwriter.writerow(error5) or csvwriter.writerow(error6) or csvwriter.writerow(error7) or csvwriter.writerow(CriticalError) or csvwriter.writerow(ImportError)
                except:
                    csvwriter.writerow("SUCCESSFULLY EXECUTED THE PROGRAM : ()")
                
                myf.close()

                print("CHECK LOGS FOR MORE INFORMATION")
                print("**IGNORE**")
                
                

        class virtual_mouse(multiprocessing.Process):
            
            def run(self):
                    
                try:
                    wCam, hCam = 640, 480
                    frameR = 100 
                    smoothening = 7
                    pTime = 0
                    plocX, plocY = 0, 0
                    clocX, clocY = 0, 0
                    
                    cap = cv2.VideoCapture(0)
                    cap.set(3, wCam)
                    cap.set(4, hCam)
                    detector = htm.handDetector(maxHands=2)
                    wScr, hScr = autopy.screen.size()
                    while True:
                    
                        success, img = cap.read()
                        img = detector.findHands(img)
                        lmList, bbox = detector.findPosition(img)
                        if len(lmList) != 0:
                            x1, y1 = lmList[8][1:]
                            x2, y2 = lmList[12][1:]
                        
                        fingers = detector.fingersUp()
                    
                        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR),
                        (255, 0, 255), 2)
                        
                        if fingers[1] == 1 and fingers[2] == 0:
                        
                            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
                            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
                        
                            clocX = plocX + (x3 - plocX) / smoothening
                            clocY = plocY + (y3 - plocY) / smoothening
                        
                        
                            autopy.mouse.move(wScr - clocX, clocY)
                            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
                            plocX, plocY = clocX, clocY
                        
                        if fingers[1] == 1 and fingers[2] == 1:
                            
                            length, img, lineInfo = detector.findDistance(8, 12, img)
                            
                            
                            if length < 30:
                                cv2.circle(img, (lineInfo[4], lineInfo[5]),
                                15, (0, 255, 0), cv2.FILLED)
                                autopy.mouse.click()
                        
                        cTime = ti.time()
                        fps = 1 / (cTime - pTime)
                        pTime = cTime
                        cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                        (255, 0, 0), 3)
                        
                        cv2.imshow("RC1 CAM", img)
                        cv2.setWindowProperty("RC1 CAM", cv2.WND_PROP_TOPMOST, 1)
                        
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            break
                    cv2.destroyAllWindows()
                except:
                    print("unhandled exception in virtual mouse")    

        t1 = main_program()
        t2 = virtual_mouse()

        if __name__ == "__main__":
            askng = input("WOULD YOU LIKE TO USE VIRTUAL MOUSE? : ").lower()
            t1.start()
            if askng == 'yes':
                print("WHILE ON CAM VIEW SCREEN , PRESS {q} TO QUIT VIRTUAL MOUSE")
                t2.start()
        
            try:
                t2.join()
            except:
                print("TRYNNA USE VIRTUAL MOUSE NEXT TIME")
            t1.join()
            exit()

    except:
        print("OPERATION ENDED")

else:
    print("autopy IMPORT ERROR")