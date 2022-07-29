from tkinter import *
import pyscreenrec

main = Tk()
main.geometry('600x800')
main.title('Screen Recorder')
main.config(bg='#fff')
main.resizable(False, False)

def start_rec():
    file = Filename.get()
    rec.start_recording(str('Recordes\\'+file+'.mp4'), 5)

def pause_rec():
    rec.pause_recording()

def stop_rec():
    rec.stop_recording()

def resume_rec():
    rec.resume_recording()

rec = pyscreenrec.ScreenRecorder()

icon = PhotoImage(file='Images\\icon.png')
main.iconphoto(False, icon)

image1 = PhotoImage(file='Images\\yellow.png')
Label(main, image=image1, bg='#fff').place(x=-2, y=35)

image2 = PhotoImage(file='Images\\blue.png')
Label(main, image=image2, bg='#fff').place(x=223, y=200)



lab = Label(main, text='Screen Recorder', bg='#fff', font='arial 15 bold')
lab.pack(pady=20)

image3 = PhotoImage(file='Images\\recording.png')
Label(main, image=image3, bd=0).pack(pady=30)


Filename = StringVar()
entry = Entry(main, textvariable=Filename, width=18, font='arial 15')
entry.place(x=100, y=350)
Filename.set('recorded')
entry.pack()


start = Button(main, text='Start', font='arial 22', bd=0, command=start_rec)
start.place(x=140, y=250)
start.pack()

image4 = PhotoImage(file='Images\\pause.png')
pause = Button(main, image=image4, bd=0, bg='#fff', command=pause_rec)
pause.place(x=50, y=450)
pause.pack()

image5 = PhotoImage(file='Images\\resume.png')
resume = Button(main, image=image5, bd=0, bg='#fff', command=resume_rec)
resume.place(x=150, y=450)
resume.pack()

image6 = PhotoImage(file='Images\\stop.png')
stop = Button(main, image=image6, bd=0, bg='#fff', command=stop_rec)
stop.place(x=250, y=450)
stop.pack()


main.mainloop()
