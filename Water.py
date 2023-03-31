def water():
    import time
    from datetime import datetime
    from pygame import mixer
    def water_function():
        mixer.init()
        mixer.music.load("C:\\Users\\nisch\OneDrive\Desktop\Python_Docs\Healthy_Programmer_File\water.mp3")
        mixer.music.set_volume(0.5)
        mixer.music.play()
        print("Drink a 250 mL glass of water\n")
        while(True):
            
            ip=input("Enter\"Drank\" once you have drunk water \n")
        
            if ip=="Drank":
                f=open("C:\\Users\\nisch\OneDrive\Desktop\Python_Docs\Healthy_Programmer_File\Water_log.txt","a")
                f.write("["+str(dt)+"]  "+ip+"\n")
                f.close()
                break
            else :
                print("Enter the Log correctly")
                continue
        mixer.music.stop()
        
        
    while True:
        dt=datetime.now()
        s2=datetime.now().hour
        s3=datetime.now().weekday()    
        if s2>9 and s2<17 and s3<5:
            water_function()
            time.sleep(2100)
            continue
        else:
            print("You don't need to work right now! Go and Chill!")
            exit()
