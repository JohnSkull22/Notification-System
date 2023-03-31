def physical():
    import time
    from datetime import datetime
    from pygame import mixer



    def Physical_function():
        mixer.init()
        mixer.music.load("C:\\Users\\nisch\OneDrive\Desktop\Python_Docs\Healthy_Programmer_File\physical.mp3")
        print("You need to perform Physical Activity Now! \n ")
        mixer.music.set_volume(0.5)
        mixer.music.play()
        while True:
            
            ip=input("Enter\"ExDone\" once you have done some Physical Activity\n")
            if ip=="ExDone":
                f=open("C:\\Users\\nisch\OneDrive\Desktop\Python_Docs\Healthy_Programmer_File\Physical_log.txt","a")
                f.write("["+str(dt)+"]"+ip+"\n")
                f.close()
                break
            else:
                print("Enter the command correctly")
                continue
        mixer.music.stop()

    while True:
        dt=datetime.now()
        s2=datetime.now().hour
        s3=datetime.now().weekday()    
        if s2>9 and s2<17 and s3<5:
            Physical_function()
            time.sleep(2700)
            continue
        else:
            print("You don't need to work Now! Go and Chill!")
            exit()
