import os
import tkinter as tk
from tkinter import ttk


LARGE_FONT = ("Impact", 12)
LARGE_FONT2 = ("Impact", 18)
SMALL_FONT = ("Impact", 14)
file = open("settings.txt", "r+")
Directory = file.read()
file.close()
pic=1



def comingsoon():
     coming=tk.Tk()
     coming.geometry("300x50")
     coming.title("Coming Soon!")
     coming.mainloop()
     
def SAVE(file, Directory, entry):
     os.remove("settings.txt")
     file = open("settings.txt", "w+")
     file.write(entry.get())
     Directory = entry.get()
     file.close()

def change_pic(HUBPIC, button5):
     global pic
     pic += 1
     if pic == 6:
         pic = 1
     if pic == 1:
         HUBPIC = tk.PhotoImage(file="hubpic1.png")
     if pic == 2:
         HUBPIC = tk.PhotoImage(file="hubpic2.png")
     if pic == 3:
         HUBPIC = tk.PhotoImage(file="hubpic3.png")
     if pic == 4:
         HUBPIC = tk.PhotoImage(file="hubpic4.png")      
     if pic == 5:
         HUBPIC = tk.PhotoImage(file="hubpic5.png")  
              
     button5.configure(image = HUBPIC)
     button5.image = HUBPIC


class LauncherApp(tk.Tk):
     def __init__(self, *args, **kwargs):
         
         
         tk.Tk.__init__(self, *args, **kwargs)
         
         tk.Tk.iconbitmap(self, default="Icon.ico")
         
         container = tk.Frame(self, bg="#525252")
         container.pack(side="top", fill="both", expand=True)
         container.grid_rowconfigure(0, weight=1)
         container.grid_columnconfigure(0, weight=1)

         
         
         self.frames = {}
         
         for F in(StartPage, GamesPage, InstalledPage, SettingsPage, AboutPage):
         
             frame = F(container, self)
             
             self.frames[F] = frame
             
             frame.grid(row=0, column=0, sticky="nsew")
             
         
         self.show_frame(StartPage)

         
     def show_frame(self, cont):
         
         frame = self.frames[cont]
         frame.tkraise()
         
class StartPage(tk.Frame):
     
     def __init__(self, parent, controller):
         tk.Frame.__init__(self, parent)
         label = tk.Label(self, text="Stealth Launcher", font=LARGE_FONT2, fg="#c90808", bg="#4f4f4f")
         label.place(height=35, width=173)
         label = tk.Label(self, text="Hub", font=LARGE_FONT2, fg="#c90808", bg="#4f4f4f")
         label.place(x=536, width=76, height=35, anchor="nw")
         button5 = tk.Button(self, text="Hub", command=lambda: controller.show_frame(StartPage), relief="groove", bg = "#4f4f4f")
         button5.place(y=5, x=172, width=76, height=25)
         button1 = tk.Button(self, text="Games",command=lambda: controller.show_frame(GamesPage), relief="groove", bg = "#4f4f4f")
         button1.place(y=5, x=248, width=76, height=25)
         button2 = tk.Button(self, text="Installed",command=lambda: controller.show_frame(InstalledPage), relief="groove", bg = "#4f4f4f")
         button2.place(y=5, x=324, width=76, height=25)
         button3 = tk.Button(self, text="Settings",command=lambda: controller.show_frame(SettingsPage), relief="groove", bg = "#4f4f4f")
         button3.place(y=5, x=400, width=76, height=25)
         button4 = tk.Button(self, text="About",command=lambda: controller.show_frame(AboutPage), relief="groove", bg = "#4f4f4f")
         button4.place(y=5, x=476, width=76, height=25)
         
         HUBPIC = tk.PhotoImage(file="hubpic1.png")
         button5 = tk.Button(self, image = HUBPIC, bd=0, relief="flat", command=lambda:change_pic(HUBPIC, button5))
         button5.image = HUBPIC
         button5.place(y=80, x=40, width=640, height=360)
         
         tk.Frame.configure(self, bg="#4f4f4f")
         
         
         
class GamesPage(tk.Frame):
     
     def __init__(self, parent, controller):
        
         tk.Frame.__init__(self, parent)
         label = tk.Label(self, text="Stealth Launcher", font=LARGE_FONT2, fg="#c90808", bg="#4f4f4f")
         label.place(height=35, width=173)
         label = tk.Label(self, text="Games", font=LARGE_FONT2, fg="#c90808", bg="#4f4f4f")
         label.place(x=551, width=76, height=35)
         button5 = tk.Button(self, text="Hub",command=lambda: controller.show_frame(StartPage), relief="groove", bg = "#4f4f4f")
         button5.place(y=5, x=172, width=76, height=25)
         button1 = tk.Button(self, text="Games",command=lambda: controller.show_frame(GamesPage), relief="groove", bg = "#4f4f4f")
         button1.place(y=5, x=248, width=76, height=25)
         button2 = tk.Button(self, text="Installed",command=lambda: controller.show_frame(InstalledPage), relief="groove", bg = "#4f4f4f")
         button2.place(y=5, x=324, width=76, height=25)
         button3 = tk.Button(self, text="Settings",command=lambda: controller.show_frame(SettingsPage), relief="groove", bg = "#4f4f4f")
         button3.place(y=5, x=400, width=76, height=25)
         button4 = tk.Button(self, text="About",command=lambda: controller.show_frame(AboutPage), relief="groove", bg = "#4f4f4f")
         button4.place(y=5, x=476, width=76, height=25)
         
         tk.Frame.configure(self, bg="#4f4f4f")
     
class InstalledPage(tk.Frame):
     
     def __init__(self, parent, controller):
        
         tk.Frame.__init__(self, parent)
         label = tk.Label(self, text="Stealth Launcher", font=LARGE_FONT2, fg="#c90808", bg="#4f4f4f")
         label.place(height=35, width=173)
         label = tk.Label(self, text="Installed", font=LARGE_FONT2, fg="#c90808", bg="#4f4f4f")
         label.place(x=555, width=86, height=35)
         button5 = tk.Button(self, text="Hub",command=lambda: controller.show_frame(StartPage), relief="groove", bg = "#4f4f4f")
         button5.place(y=5, x=172, width=76, height=25)
         button1 = tk.Button(self, text="Games",command=lambda: controller.show_frame(GamesPage), relief="groove", bg = "#4f4f4f")
         button1.place(y=5, x=248, width=76, height=25)
         button2 = tk.Button(self, text="Installed",command=lambda: controller.show_frame(InstalledPage), relief="groove", bg = "#4f4f4f")
         button2.place(y=5, x=324, width=76, height=25)
         button3 = tk.Button(self, text="Settings",command=lambda: controller.show_frame(SettingsPage), relief="groove", bg = "#4f4f4f")
         button3.place(y=5, x=400, width=76, height=25)
         button4 = tk.Button(self, text="About",command=lambda: controller.show_frame(AboutPage), relief="groove", bg = "#4f4f4f")
         button4.place(y=5, x=476, width=76, height=25)
         
         tk.Frame.configure(self, bg="#4f4f4f")
         
class SettingsPage(tk.Frame):
     
     def __init__(self, parent, controller):
        
         tk.Frame.__init__(self, parent)
         label = tk.Label(self, text="Stealth Launcher", font=LARGE_FONT2, fg="#c90808", bg="#4f4f4f")
         label.place(height=35, width=173)
         label = tk.Label(self, text="Settings", font=LARGE_FONT2, fg="#c90808", bg="#4f4f4f")
         label.place(x=553, width=86, height=35)
         button5 = tk.Button(self, text="Hub",command=lambda: controller.show_frame(StartPage), relief="groove", bg = "#4f4f4f")
         button5.place(y=5, x=172, width=76, height=25)
         button1 = tk.Button(self, text="Games",command=lambda: controller.show_frame(GamesPage), relief="groove", bg = "#4f4f4f")
         button1.place(y=5, x=248, width=76, height=25)
         button2 = tk.Button(self, text="Installed",command=lambda: controller.show_frame(InstalledPage), relief="groove", bg = "#4f4f4f")
         button2.place(y=5, x=324, width=76, height=25)
         button3 = tk.Button(self, text="Settings",command=lambda: controller.show_frame(SettingsPage), relief="groove", bg = "#4f4f4f")
         button3.place(y=5, x=400, width=76, height=25)
         button4 = tk.Button(self, text="About",command=lambda: controller.show_frame(AboutPage), relief="groove", bg = "#4f4f4f")
         button4.place(y=5, x=476, width=76, height=25)
         
         
         labe2 = tk.Label(self, text="Directory:", font=SMALL_FONT, fg="#c90808", bg="#4f4f4f")
         labe2.place(x=200, y=40, width=86, height=35)
         entry = tk.Entry(self, exportselection=0, textvariable = "StringVar", font=SMALL_FONT, fg="#c90808", bg="#5f5f5f", bd=3)
         entry.insert(0, Directory)
         entry.place(x=290, y=47, width=300, height=25)
         
         button5 = ttk.Button(self, text="save", command=lambda: SAVE(file, Directory, entry))
         button5.place(x=360, y=400, width=76, height=25, anchor="center")
         
         tk.Frame.configure(self, bg="#4f4f4f")
         
     
         
         
class AboutPage(tk.Frame):
     
     def __init__(self, parent, controller):
        
         tk.Frame.__init__(self, parent)
         label = tk.Label(self, text="Stealth Launcher", font=LARGE_FONT2, fg="#c90808", bg="#4f4f4f")
         label.place(height=35, width=173)
         label = tk.Label(self, text="About", font=LARGE_FONT2, fg="#c90808", bg="#4f4f4f")
         label.place(x=546, width=76, height=35)
         button5 = tk.Button(self, text="Hub",command=lambda: controller.show_frame(StartPage), relief="groove", bg = "#4f4f4f")
         button5.place(y=5, x=172, width=76, height=25)
         button1 = tk.Button(self, text="Games",command=lambda: controller.show_frame(GamesPage), relief="groove", bg = "#4f4f4f")
         button1.place(y=5, x=248, width=76, height=25)
         button2 = tk.Button(self, text="Installed",command=lambda: controller.show_frame(InstalledPage), relief="groove", bg = "#4f4f4f")
         button2.place(y=5, x=324, width=76, height=25)
         button3 = tk.Button(self, text="Settings",command=lambda: controller.show_frame(SettingsPage), relief="groove", bg = "#4f4f4f")
         button3.place(y=5, x=400, width=76, height=25)
         button4 = tk.Button(self, text="About",command=lambda: controller.show_frame(AboutPage), relief="groove", bg = "#4f4f4f")
         button4.place(y=5, x=476, width=76, height=25)
         
         label1 = tk.Label(self, text="This is a game downloader and launcher made by RedStealthAlix#6969", font=SMALL_FONT, fg="#fa87f0", bg="#4f4f4f")
         label1.place(y=200, x=70)
         label1 = tk.Label(self, text="on discord", font=SMALL_FONT, fg="#fa87f0", bg="#4f4f4f")
         label1.place(y=230, x=315)
         
         tk.Frame.configure(self, bg="#4f4f4f")
         

app = LauncherApp()
app.geometry("720x480")
app.title("Stealth Launcher")
app.resizable(0, 0)
app.mainloop()


















