print("--------------------------------Keyframe Interval Generator for Deforum-v1-------------------------------------------")
print("------------------------------------------Created by MushieKings-------------------------------------------------------")
import customtkinter
import threading
import os
import random

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

#--------------------------------------------------------GLOBAL VARIABLES----------------------------------------------------------
startframe = 0
framecount = int
totalframes = 0
startinterval = 15
startframe_cfg = 0.65
randonoff = 0
rfval = 0
randsetting1 = ""
randsetting2 = ""
randval = int
cfg1 = 0
cfg2 = 0
cfg3 = 0
cfg4 = 0
cfg5 = 0
cfg6 = 0
cfg7 = 0
cfg8 = 0
cfg9 = 0
cfg10 = 0
fi_cfg1 = 15
fi_cfg2 = 0
fi_cfg3 = 0
fi_cfg4 = 0
fi_cfg5 = 0
fi_cfg6 = 0
fi_cfg7 = 0
fi_cfg8 = 0
fi_cfg9 = 0
fi_cfg10 = 0
string = ""
newline = ""
filename = ""
file_ext = 1
newlineval = 0
quotesval = 0
addquotes = ''
leftbracket = "("
rightbracket = ")"

framerate = 15
minutes = 0
seconds = 0
totalseconds = 0
kf_answer = 0
#-------------------------------------------------------Initialize settings--------------------------------------------------------
def calc_keyframe():
    global framerate, minutes, seconds, totalseconds, kf_answer
    framerate = app.fps_entry.get()
    framerate = int(framerate)
    minutes = app.minutes_entry.get()
    minutes = int(minutes)
    seconds = app.seconds_entry.get()
    seconds = int(seconds)
    totalseconds = (minutes * 60) + seconds
    kf_answer = (totalseconds * framerate)
    return

def get_settings():
    global startframe, startframe_cfg, framecount, startinterval, totalframes, cfg1, cfg2, cfg3, cfg4, cfg5, cfg6, cfg7, cfg8, cfg9, cfg10, fi_cfg1, fi_cfg2, fi_cfg3, fi_cfg4, fi_cfg5, fi_cfg6, fi_cfg7, fi_cfg8, fi_cfg9, fi_cfg10, string, newline, quotesval, filename, file_ext, leftbracket, rightbracket, randsetting1, randsetting2, randval, randonoff
    randsetting1 = app.randframes_entry1.get()
    randsetting1 = int(randsetting1)
    randsetting2 = app.randframes_entry2.get()
    randsetting2 = int(randsetting2)
    framecount = 0
    startframe = app.sf_entry1.get()
    startframe = int(startframe)
    startframe_cfg = app.sf_entry2.get()
    totalframes = app.tf_entry.get()
    totalframes = int(totalframes)
    startinterval = app.sf_entry3.get()
    startinterval = int(startinterval)
    fi_cfg1 = app.cfg1_entry2.get()
    fi_cfg1 = int(fi_cfg1)
    fi_cfg2 = app.cfg2_entry2.get()
    fi_cfg2 = int(fi_cfg2)
    fi_cfg3 = app.cfg3_entry2.get()
    fi_cfg3 = int(fi_cfg3)
    fi_cfg4 = app.cfg4_entry2.get()
    fi_cfg4 = int(fi_cfg4)
    fi_cfg5 = app.cfg5_entry2.get()
    fi_cfg5 = int(fi_cfg5)
    fi_cfg6 = app.cfg6_entry2.get()
    fi_cfg6 = int(fi_cfg6)
    fi_cfg7 = app.cfg7_entry2.get()
    fi_cfg7 = int(fi_cfg7)
    fi_cfg8 = app.cfg8_entry2.get()
    fi_cfg8 = int(fi_cfg8)
    fi_cfg9 = app.cfg9_entry2.get()
    fi_cfg9 = int(fi_cfg9)
    fi_cfg10 = app.cfg10_entry2.get()
    fi_cfg10 = int(fi_cfg10)
    try: 
        startframe_cfg = float(startframe_cfg)
    except:
        startframe_cfg = startframe_cfg
    cfg1 = app.cfg1_entry1.get()
    try: 
        cfg1 = float(cfg1)
    except:
        cfg1 = cfg1
    cfg2 = app.cfg2_entry1.get()
    try: 
        cfg2 = float(cfg2)
    except:
        cfg2 = cfg2
    cfg3 = app.cfg3_entry1.get()
    try: 
        cfg3 = float(cfg3)
    except:
        cfg3 = cfg3
    cfg4 = app.cfg4_entry1.get()
    try: 
        cfg4 = float(cfg4)
    except:
        cfg4 = cfg4
    cfg5 = app.cfg5_entry1.get()
    try: 
        cfg5 = float(cfg5)
    except:
        cfg5 = cfg5
    cfg6 = app.cfg6_entry1.get()
    try: 
        cfg6 = float(cfg6)
    except:
        cfg6 = cfg6
    cfg7 = app.cfg7_entry1.get()
    try: 
        cfg7 = float(cfg7)
    except:
        cfg7 = cfg7
    cfg8 = app.cfg8_entry1.get()
    try: 
        cfg8 = float(cfg8)
    except:
        cfg8 = cfg8
    cfg9 = app.cfg9_entry1.get()
    try: 
        cfg9 = float(cfg9)
    except:
        cfg9 = cfg9
    cfg10 = app.cfg10_entry1.get()
    try: 
        cfg10 = float(cfg10)
    except:
        cfg10 = cfg10
    string = ""
    filename = app.entry10.get()
    file_ext = int(file_ext)
    print("Settings Loaded")
    if randonoff == 1:
        randval = random.randint(randsetting1, randsetting2)
    elif randonoff == 0:
        randval = 0
    if quotesval == 1:
        quotesval = '"'
    elif quotesval == 0:
        quotesval = ''
    if newlineval == 1:
###########---Remove indent here if you so choose-----#####################################################################
        newline = "\n    "
    elif newlineval == 0:
        newline = ""
    return

#--------------------------------------------------------Main-------------------------------------------------------------
def append():
    global startframe, framecount, totalframes, cfg1, cfg2, cfg3, cfg4, cfg5, cfg6, cfg7, cfg8, cfg9, cfg10, fi_cfg1, fi_cfg2, fi_cfg3, fi_cfg4, fi_cfg5, fi_cfg6, fi_cfg7, fi_cfg8, fi_cfg9, fi_cfg10, string, leftbracket, rightbracket, startframe_cfg, randval
    if startframe == startframe: #runs once at begining
        framecount += startframe
        leftbracket = "("
        rightbracket = ")"
        try: 
            startframe_cfg = float(startframe_cfg) #check if int-return exception if string, use quotes if string
        except:
            leftbracket = ""
            rightbracket = ""
        string = string + (quotesval + str(framecount) + quotesval + ": " + leftbracket + quotesval + str(startframe_cfg) + quotesval + rightbracket + ", " + newline) #append
        framecount += startinterval + randval #adjust frame count
        startframe += framecount

    while framecount <= totalframes:
        if randonoff == 1:
            randval = random.randint(randsetting1, randsetting2)
        if cfg1 != "s":
            if framecount <= totalframes:
                leftbracket = "("
                rightbracket = ")"
                try:
                    cfg1 = float(cfg1)
                except:
                    leftbracket = ""
                    rightbracket = ""
                string = string + (quotesval + str(framecount) + quotesval + ": " + leftbracket + quotesval + str(cfg1) + quotesval + rightbracket + ", " + newline)
                if fi_cfg1 != 0:
                    framecount += fi_cfg1 + randval
                else:
                    framecount += startinterval + randval
            else:
                string = string[0:-2]
                if newlineval == 1:
                    string = string[0:-5]
                return string
            
        if randonoff == 1:
            randval = random.randint(randsetting1, randsetting2)
        if cfg2 != "s":
            if framecount <= totalframes:
                leftbracket = "("
                rightbracket = ")"
                try:
                    cfg2 = float(cfg2)
                except:
                    leftbracket = ""
                    rightbracket = ""
                string = string + (quotesval + str(framecount) + quotesval + ": " + leftbracket + quotesval + str(cfg2) + quotesval + rightbracket + ", " + newline)
                if fi_cfg2 != 0:
                    framecount += fi_cfg2 + randval
                else:
                    framecount += startinterval + randval
            else:
                string = string[0:-2]
                if newlineval == 1:
                    string = string[0:-5]
                return string
            
        if randonoff == 1:
            randval = random.randint(randsetting1, randsetting2)
        if cfg3 != "s":
            if framecount <= totalframes:
                leftbracket = "("
                rightbracket = ")"
                try:
                    cfg3 = float(cfg3)
                except:
                    leftbracket = ""
                    rightbracket = ""
                string = string + (quotesval + str(framecount) + quotesval + ": " + leftbracket + quotesval + str(cfg3) + quotesval + rightbracket + ", " + newline)
                if fi_cfg3 != 0:
                    framecount += fi_cfg3 + randval
                else:
                    framecount += startinterval + randval
            else:
                string = string[0:-2]
                if newlineval == 1:
                    string = string[0:-5]
                return string

        if randonoff == 1:
            randval = random.randint(randsetting1, randsetting2)
        if cfg4 != "s":
            if framecount <= totalframes:
                leftbracket = "("
                rightbracket = ")"
                try:
                    cfg4 = float(cfg4)
                except:
                    leftbracket = ""
                    rightbracket = ""
                string = string + (quotesval + str(framecount) + quotesval + ": " + leftbracket + quotesval + str(cfg4) + quotesval + rightbracket + ", " + newline)
                if fi_cfg4 != 0:
                    framecount += fi_cfg4 + randval
                else:
                    framecount += startinterval + randval
            else:
                string = string[0:-2]
                if newlineval == 1:
                    string = string[0:-5]
                return string

        if randonoff == 1:
            randval = random.randint(randsetting1, randsetting2)
        if cfg5 != "s":
            if framecount <= totalframes:

                leftbracket = "("
                rightbracket = ")"
                try:
                    cfg5 = float(cfg5)
                except:
                    leftbracket = ""
                    rightbracket = ""
                string = string + (quotesval + str(framecount) + quotesval + ": " + leftbracket + quotesval + str(cfg5) + quotesval + rightbracket + ", " + newline)
                if fi_cfg5 != 0:
                    framecount += fi_cfg5 + randval
                else:
                    framecount += startinterval + randval
            else:
                string = string[0:-2]
                if newlineval == 1:
                    string = string[0:-5]
                return string

        if randonoff == 1:
            randval = random.randint(randsetting1, randsetting2)
        if cfg6 != "s":
            if framecount <= totalframes:
                leftbracket = "("
                rightbracket = ")"
                try:
                    cfg6 = float(cfg6)
                except:
                    leftbracket = ""
                    rightbracket = ""
                string = string + (quotesval + str(framecount) + quotesval + ": " + leftbracket + quotesval + str(cfg6) + quotesval + rightbracket + ", " + newline)
                if fi_cfg6 != 0:
                    framecount += fi_cfg6 + randval
                else:
                    framecount += startinterval + randval
            else:
                string = string[0:-2]
                if newlineval == 1:
                    string = string[0:-5]
                return string

        if randonoff == 1:
            randval = random.randint(randsetting1, randsetting2)
        if cfg7 != "s":
            if framecount <= totalframes:
                leftbracket = "("
                rightbracket = ")"
                try:
                    cfg7 = float(cfg7)
                except:
                    leftbracket = ""
                    rightbracket = ""
                string = string + (quotesval + str(framecount) + quotesval + ": " + leftbracket + quotesval + str(cfg7) + quotesval + rightbracket + ", " + newline)
                if fi_cfg7 != 0:
                    framecount += fi_cfg7 + randval
                else:
                    framecount += startinterval + randval
            else:
                string = string[0:-2]
                if newlineval == 1:
                    string = string[0:-5]
                return string

        if randonoff == 1:
            randval = random.randint(randsetting1, randsetting2)
        if cfg8 != "s":
            if framecount <= totalframes:
                leftbracket = "("
                rightbracket = ")"
                try:
                    cfg8 = float(cfg8)
                except:
                    leftbracket = ""
                    rightbracket = ""
                string = string + (quotesval + str(framecount) + quotesval + ": " + leftbracket + quotesval + str(cfg8) + quotesval + rightbracket + ", " + newline)
                if fi_cfg8 != 0:
                    framecount += fi_cfg8 + randval
                else:
                    framecount += startinterval + randval
            else:
                string = string[0:-2]
                if newlineval == 1:
                    string = string[0:-5]
                return string
            
        if randonoff == 1:
            randval = random.randint(randsetting1, randsetting2)
        if cfg9 != "s":
            if framecount <= totalframes:
                leftbracket = "("
                rightbracket = ")"
                try:
                    cfg9 = float(cfg9)
                except:
                    leftbracket = ""
                    rightbracket = ""
                string = string + (quotesval + str(framecount) + quotesval + ": " + leftbracket + quotesval + str(cfg9) + quotesval + rightbracket + ", " + newline)
                if fi_cfg9 != 0:
                    framecount += fi_cfg9 + randval
                else:
                    framecount += startinterval + randval
            else:
                string = string[0:-2]
                if newlineval == 1:
                    string = string[0:-5]
                return string
        if randonoff == 1:
            randval = random.randint(randsetting1, randsetting2)
        if cfg10 != "s":
            if framecount <= totalframes:
                leftbracket = "("
                rightbracket = ")"
                try:
                    cfg10 = float(cfg10)
                except:
                    leftbracket = ""
                    rightbracket = ""
                string = string + (quotesval + str(framecount) + quotesval + ": " + leftbracket + quotesval + str(cfg10) + quotesval + rightbracket + ", " + newline)
                if fi_cfg10 != 0:
                    framecount += fi_cfg10 + randval
                else:
                    framecount += startinterval + randval
            else:
                string = string[0:-2]
                if newlineval == 1:
                    string = string[0:-5]
                return string
    string = string[0:-2]
    if newlineval == 1:
            string = string[0:-5]
    return string

#-------------------------------------Save File----------------------------------------------------
#--------------check if file exist or not. Adds +1 to file # text entry and saves------------------
def save_file():
    global file_ext, string
    print(newline)
    file_ext = app.entry11.get()
    file_ext = int(file_ext)
    if os.path.isfile((str(filename) + str(file_ext) + ".txt"), ):
        print("file already exists. File not saved")
    else:
        txt_file = open((str(filename) + str(file_ext) + ".txt"), "w")
        txt_file.close()
        txt_file = open((str(filename) + str(file_ext) + ".txt"), "w")
        txt_file.write(string)
        txt_file.close()
        app.entry11.delete(0, 'end')
        file_ext = file_ext + 1
        app.entry11.insert(0, file_ext)
        print(string)
        print("Saved")
        return
    
#Start threading/kill thread-------------------------------------------------------------------------
def append_thread():
    global string
    thread1 = threading.Thread(target=append)
    thread1.start()
    save_file()
    thread1.join()
#-----------------------------------------------------GUI-------------------------------------------------------------------------------
class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("510x960")
        self.title("Keyframe Interval Generator")
        self.frame = customtkinter.CTkFrame(master=self)
        self.frame.grid(padx=10, pady=10, row=20, column=3, rowspan=4, sticky="nsew")
#-------Start Frame Setting---------------------------------------------------
        self.sf_label1 = customtkinter.CTkLabel(master=self.frame, text="Start Frame\nRuns Once", font=("Impact", 18), text_color="white")
        self.sf_label1.grid(row=1, column=1, pady=0, padx=6)
        self.sf_entry1 = customtkinter.CTkEntry(master=self.frame, placeholder_text="start frame")
        self.sf_entry1.insert(0, 0)
        self.sf_entry1.grid(row=2, column=1, pady=0, padx=6)
        self.sf_label2 = customtkinter.CTkLabel(master=self.frame, text="Start Frame CFG", font=("Impact", 18), text_color="white")
        self.sf_label2.grid(row=3, column=1, pady=0, padx=6)
        self.sf_entry2 = customtkinter.CTkEntry(master=self.frame, placeholder_text="start frame setting")
        self.sf_entry2.insert(0, 0.65)
        self.sf_entry2.grid(row=4, column=1, pady=0, padx=6)
        self.sf_label3 = customtkinter.CTkLabel(master=self.frame, text="Start Interval", font=("Impact", 18), text_color="White")
        self.sf_label3.grid(row=5, column=1, pady=0, padx=6)
        self.sf_entry3 = customtkinter.CTkEntry(master=self.frame, placeholder_text="15")
        self.sf_entry3.insert(0, 15)
        self.sf_entry3.grid(row=6, column=1, pady=0, padx=6)

#-------Total Frames setting--------------------------------------------------
        self.tf_label = customtkinter.CTkLabel(master=self.frame, text="Total Frames", font=("Impact", 18), text_color="deep sky blue")
        self.tf_label.grid(row=7, column=1, pady=0, padx=6)
        self.tf_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="total frames")
        self.tf_entry.insert(0, 150)
        self.tf_entry.grid(row=8, column=1, pady=0, padx=6)
#-------Random Frame Add------------------------------------------------------
        self.randframes_button = customtkinter.CTkButton(master=self.frame, hover=False, fg_color="red", text="RandFrames is off", command=self.randframes_on)
        self.randframes_button.grid(row=9, column=1, pady=12, padx=6)

        self.randframes_entry1 = customtkinter.CTkEntry(master=self.frame, placeholder_text="0, 100")
        self.randframes_entry1.insert(0, 1)
        self.randframes_entry1.grid(row=10, column=1, pady=6, padx=6)
        self.rf_label = customtkinter.CTkLabel(master=self.frame, text="Random # Between", font=("Impact", 18), text_color="teal")
        self.rf_label.grid(row=11, column=1, pady=0, padx=6)
        self.randframes_entry2 = customtkinter.CTkEntry(master=self.frame, placeholder_text="0, 100")
        self.randframes_entry2.insert(0, 100)
        self.randframes_entry2.grid(row=12, column=1, pady=6, padx=6)
#-------CFG Entries-----------------------------------------------------------
        self.cfg1_label1 = customtkinter.CTkLabel(master=self.frame, text='CFG1 # or "Text"', font=("Impact", 18), text_color="deep sky blue")
        self.cfg1_label1.grid(row=1, column=2, pady=0, padx=6)
        self.cfg1_entry1 = customtkinter.CTkEntry(master=self.frame, placeholder_text="cfg1")
        self.cfg1_entry1.insert(0, 0.65)
        self.cfg1_entry1.grid(row=2, column=2, pady=0, padx=6)
        self.cfg2_label1 = customtkinter.CTkLabel(master=self.frame, text="CFG2 s=Skip", font=("Impact", 18), text_color="deep sky blue")
        self.cfg2_label1.grid(row=3, column=2, pady=0, padx=6)
        self.cfg2_entry1 = customtkinter.CTkEntry(master=self.frame, placeholder_text="cfg2")
        self.cfg2_entry1.insert(0, "s")
        self.cfg2_entry1.grid(row=4, column=2, pady=0, padx=6)
        self.cfg3_label1 = customtkinter.CTkLabel(master=self.frame, text="CFG3 s=Skip", font=("Impact", 18), text_color="deep sky blue")
        self.cfg3_label1.grid(row=5, column=2, pady=0, padx=6)
        self.cfg3_entry1 = customtkinter.CTkEntry(master=self.frame, placeholder_text="cfg3")
        self.cfg3_entry1.insert(0, "s")
        self.cfg3_entry1.grid(row=6, column=2, pady=0, padx=6)
        self.cfg4_label1 = customtkinter.CTkLabel(master=self.frame, text="CFG4 s=Skip", font=("Impact", 18), text_color="deep sky blue")
        self.cfg4_label1.grid(row=7, column=2, pady=0, padx=6)
        self.cfg4_entry1 = customtkinter.CTkEntry(master=self.frame, placeholder_text="cfg4")
        self.cfg4_entry1.insert(0, "s")
        self.cfg4_entry1.grid(row=8, column=2, pady=0, padx=6)
        self.cfg5_label1 = customtkinter.CTkLabel(master=self.frame, text="CFG5 s=Skip", font=("Impact", 18), text_color="deep sky blue")
        self.cfg5_label1.grid(row=9, column=2, pady=0, padx=6)
        self.cfg5_entry1 = customtkinter.CTkEntry(master=self.frame, placeholder_text="cfg5")
        self.cfg5_entry1.insert(0, "s")
        self.cfg5_entry1.grid(row=10, column=2, pady=0, padx=6)
        self.cfg6_label1 = customtkinter.CTkLabel(master=self.frame, text="CFG6 s=Skip", font=("Impact", 18), text_color="deep sky blue")
        self.cfg6_label1.grid(row=11, column=2, pady=0, padx=6)
        self.cfg6_entry1 = customtkinter.CTkEntry(master=self.frame, placeholder_text="cfg6")
        self.cfg6_entry1.insert(0, "s")
        self.cfg6_entry1.grid(row=12, column=2, pady=0, padx=6)
        self.cfg7_label1 = customtkinter.CTkLabel(master=self.frame, text="CFG7 s=Skip", font=("Impact", 18), text_color="deep sky blue")
        self.cfg7_label1.grid(row=13, column=2, pady=0, padx=6)
        self.cfg7_entry1 = customtkinter.CTkEntry(master=self.frame, placeholder_text="cfg7")
        self.cfg7_entry1.insert(0, "s")
        self.cfg7_entry1.grid(row=14, column=2, pady=0, padx=6)
        self.cfg8_label1 = customtkinter.CTkLabel(master=self.frame, text="CFG8 s=Skip", font=("Impact", 18), text_color="deep sky blue")
        self.cfg8_label1.grid(row=15, column=2, pady=0, padx=6)
        self.cfg8_entry1 = customtkinter.CTkEntry(master=self.frame, placeholder_text="cfg8")
        self.cfg8_entry1.insert(0, "s")
        self.cfg8_entry1.grid(row=16, column=2, pady=0, padx=6)
        self.cfg9_label1 = customtkinter.CTkLabel(master=self.frame, text="CFG9 s=Skip", font=("Impact", 18), text_color="deep sky blue")
        self.cfg9_label1.grid(row=17, column=2, pady=0, padx=6)
        self.cfg9_entry1 = customtkinter.CTkEntry(master=self.frame, placeholder_text="cfg9")
        self.cfg9_entry1.insert(0, "s")
        self.cfg9_entry1.grid(row=18, column=2, pady=0, padx=6)
        self.cfg10_label1 = customtkinter.CTkLabel(master=self.frame, text="CFG10 s=Skip", font=("Impact", 18), text_color="deep sky blue")
        self.cfg10_label1.grid(row=19, column=2, pady=0, padx=6)
        self.cfg10_entry1 = customtkinter.CTkEntry(master=self.frame, placeholder_text="cfg10")
        self.cfg10_entry1.insert(0, "s")
        self.cfg10_entry1.grid(row=20, column=2, pady=0, padx=6)
#-------Frame Interval Entries-----------------------------------------------------
        self.cfg1_label2 = customtkinter.CTkLabel(master=self.frame, text="Frame Interval 1", font=("Impact", 18), text_color="teal")
        self.cfg1_label2.grid(row=1, column=3, pady=0, padx=6)
        self.cfg1_entry2 = customtkinter.CTkEntry(master=self.frame, placeholder_text="15")
        self.cfg1_entry2.insert(0, 15)
        self.cfg1_entry2.grid(row=2, column=3, pady=0, padx=6)
        self.cfg2_label2 = customtkinter.CTkLabel(master=self.frame, text='Frame Interval 2', font=("Impact", 18), text_color="teal")
        self.cfg2_label2.grid(row=3, column=3, pady=0, padx=6)
        self.cfg2_entry2 = customtkinter.CTkEntry(master=self.frame, placeholder_text="15")
        self.cfg2_entry2.insert(0, 0)
        self.cfg2_entry2.grid(row=4, column=3, pady=0, padx=6)
        self.cfg3_label2 = customtkinter.CTkLabel(master=self.frame, text='Frame Interval 3', font=("Impact", 18), text_color="teal")
        self.cfg3_label2.grid(row=5, column=3, pady=0, padx=6)
        self.cfg3_entry2 = customtkinter.CTkEntry(master=self.frame, placeholder_text="15")
        self.cfg3_entry2.insert(0, 0)
        self.cfg3_entry2.grid(row=6, column=3, pady=0, padx=6)
        self.cfg4_label2 = customtkinter.CTkLabel(master=self.frame, text='Frame Interval 4', font=("Impact", 18), text_color="teal")
        self.cfg4_label2.grid(row=7, column=3, pady=0, padx=6)
        self.cfg4_entry2 = customtkinter.CTkEntry(master=self.frame, placeholder_text="15")
        self.cfg4_entry2.insert(0, 0)
        self.cfg4_entry2.grid(row=8, column=3, pady=0, padx=6)
        self.cfg5_label2 = customtkinter.CTkLabel(master=self.frame, text='Frame Interval 5', font=("Impact", 18), text_color="teal")
        self.cfg5_label2.grid(row=9, column=3, pady=0, padx=6)
        self.cfg5_entry2 = customtkinter.CTkEntry(master=self.frame, placeholder_text="15")
        self.cfg5_entry2.insert(0, 0)
        self.cfg5_entry2.grid(row=10, column=3, pady=0, padx=6)
        self.cfg6_label2 = customtkinter.CTkLabel(master=self.frame, text='Frame Interval 6', font=("Impact", 18), text_color="teal")
        self.cfg6_label2.grid(row=11, column=3, pady=0, padx=6)
        self.cfg6_entry2 = customtkinter.CTkEntry(master=self.frame, placeholder_text="15")
        self.cfg6_entry2.insert(0, 0)
        self.cfg6_entry2.grid(row=12, column=3, pady=0, padx=6)
        self.cfg7_label2 = customtkinter.CTkLabel(master=self.frame, text='Frame Interval 7', font=("Impact", 18), text_color="teal")
        self.cfg7_label2.grid(row=13, column=3, pady=0, padx=6)
        self.cfg7_entry2 = customtkinter.CTkEntry(master=self.frame, placeholder_text="15")
        self.cfg7_entry2.insert(0, 0)
        self.cfg7_entry2.grid(row=14, column=3, pady=0, padx=6)
        self.cfg8_label2 = customtkinter.CTkLabel(master=self.frame, text='Frame Interval 8', font=("Impact", 18), text_color="teal")
        self.cfg8_label2.grid(row=15, column=3, pady=0, padx=6)
        self.cfg8_entry2 = customtkinter.CTkEntry(master=self.frame, placeholder_text="15")
        self.cfg8_entry2.insert(0, 0)
        self.cfg8_entry2.grid(row=16, column=3, pady=0, padx=6)
        self.cfg9_label2 = customtkinter.CTkLabel(master=self.frame, text='Frame Interval 9', font=("Impact", 18), text_color="teal")
        self.cfg9_label2.grid(row=17, column=3, pady=0, padx=6)
        self.cfg9_entry2 = customtkinter.CTkEntry(master=self.frame, placeholder_text="15")
        self.cfg9_entry2.insert(0, 0)
        self.cfg9_entry2.grid(row=18, column=3, pady=0, padx=6)
        self.cfg10_label2 = customtkinter.CTkLabel(master=self.frame, text='Frame Interval 10', font=("Impact", 18), text_color="teal")
        self.cfg10_label2.grid(row=19, column=3, pady=0, padx=6)
        self.cfg10_entry2 = customtkinter.CTkEntry(master=self.frame, placeholder_text="15")
        self.cfg10_entry2.insert(0, 0)
        self.cfg10_entry2.grid(row=20, column=3, pady=0, padx=6)
#-------Timecode to frame calculator-----------------------------------------
        self.fps_label = customtkinter.CTkLabel(master=self.frame, text='Frames Per Second', font=("Impact", 18), text_color="deep sky blue")
        self.fps_label.grid(row=13, column=1, pady=0, padx=6)
        self.fps_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="15")
        self.fps_entry.insert(0, 15)
        self.fps_entry.grid(row=14, column=1, pady=0, padx=6)
        self.minutes_label = customtkinter.CTkLabel(master=self.frame, text='Minutes', font=("Impact", 18), text_color="deep sky blue")
        self.minutes_label.grid(row=15, column=1, pady=0, padx=6)
        self.minutes_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="15")
        self.minutes_entry.insert(0, 0)
        self.minutes_entry.grid(row=16, column=1, pady=0, padx=6)
        self.minutes_label = customtkinter.CTkLabel(master=self.frame, text='Seconds', font=("Impact", 18), text_color="deep sky blue")
        self.minutes_label.grid(row=17, column=1, pady=0, padx=6)
        self.seconds_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="15")
        self.seconds_entry.insert(0, 0)
        self.seconds_entry.grid(row=18, column=1, pady=0, padx=6)    
        self.keyframe_label = customtkinter.CTkLabel(master=self.frame, text='answer', font=("Impact", 18), text_color="green")
        self.keyframe_label.grid(row=19, column=1, pady=0, padx=6)    

        self.calculate_button = customtkinter.CTkButton(master=self.frame, hover=False, fg_color="green", text="Calculate", command=self.calc_start)
        self.calculate_button.grid(row=20, column=1, pady=12, padx=10)
#-------File Name------------------------------------------------------------
        self.label10 = customtkinter.CTkLabel(master=self.frame, text="File Name", font=("Impact", 18), text_color="deep sky blue")
        self.label10.grid(row=21, column=2, pady=10, padx=10)
        self.entry10 = customtkinter.CTkEntry(master=self.frame, placeholder_text="output")
        self.entry10.insert(0, "output")
        self.entry10.grid(row=22, column=2, pady=0, padx=10)
#-------File Extension-------------------------------------------------------
        self.label11 = customtkinter.CTkLabel(master=self.frame, text="File #", font=("Impact", 18), text_color="deep sky blue")
        self.label11.grid(row=23, column=2, pady=0, padx=10)
        self.entry11 = customtkinter.CTkEntry(master=self.frame, placeholder_text="#")
        self.entry11.insert(0, 1)
        self.entry11.grid(row=24, column=2, pady=0, padx=10)
#-------Button for adding quotes around the frame number---------------------------
        self.label11 = customtkinter.CTkLabel(master=self.frame, text="Add Keyframe Quotes", font=("Impact", 18), text_color="deep sky blue")
        self.label11.grid(row=25, column=2, pady=0, padx=10)
        self.quotesbutton = customtkinter.CTkButton(master=self.frame, hover=False, fg_color="red", text="Add Quotes off", command=self.addquotes_on)
        self.quotesbutton.grid(row=26, column=2, pady=6, padx=10)
#-------Button for newline setting---------------------------------------------
        self.returnbutton = customtkinter.CTkButton(master=self.frame, hover=False, fg_color="red", text="Newlines is off", command=self.returnbutton_on)
        self.returnbutton.grid(row=27, column=2, pady=6, padx=10)
#-------startstop button--------------------------------------------------------
        self.button = customtkinter.CTkButton(master=self.frame, hover=False, fg_color="green", text="Start", command=self.button_start)
        self.button.grid(row=28, column=2, pady=12, padx=10)

#---------------------------------------------------------BUTTONS---------------------------------------------------------------------
    def randframes_on(self):
        global randonoff
        self.randframes_button.configure(fg_color="green", text="RandFrames is on", command=self.randframes_off)
        randonoff = 1
        print("Add random frames on")
        return
    def randframes_off(self):
        global randonoff
        self.randframes_button.configure(fg_color="red", text="RandFrames is off", command=self.randframes_on)
        randonoff = 0
        print("Add random frames off")
        return

    def addquotes_on(self):
        global quotesval
        self.quotesbutton.configure(fg_color="green", text="Add Quotes is on", command=self.addquotes_off)
        quotesval = 1
        print("quotes on")
        return
    def addquotes_off(self):
        global quotesval
        self.quotesbutton.configure(fg_color="red", text="Add Quotes is off", command=self.addquotes_on)
        quotesval = 0
        print("quotes off")
        return

    def returnbutton_on(self):
        global newlineval
        self.returnbutton.configure(fg_color="green", text="Newlines is on", command=self.returnbutton_off)
        newlineval = 1
        print("newlines on")
        return
    def returnbutton_off(self):
        global newlineval
        self.returnbutton.configure(fg_color="red", text="Newlines is off", command=self.returnbutton_on)
        newlineval = 0
        print("newlines off")
        return

    def button_start(self):
        self.button.configure(fg_color="red", text="Reset", command=self.button_stop)
        print("Started")
        get_settings()
        append_thread()
        return

    def button_stop(self):
        self.button.configure(fg_color="green",text="Start", command=self.button_start)
        print("Reset")
        return

    def calc_start(self):
        self.calculate_button.configure(fg_color="red", text="Reset", command=self.calc_stop)
        calc_keyframe()
        self.keyframe_label.configure(text = kf_answer)
        return

    def calc_stop(self):
        self.calculate_button.configure(fg_color="green",text="Calculate", command=self.calc_start)
        return

if __name__ == "__main__":
    app = App()   
    app.mainloop()