import Tkinter as tk
import tkFileDialog as tkfd
import cv2
import MMCorePy
from PIL import Image, ImageTk

# Initializing the microscope. ------------------------------

#DEVICE = ['Camera', 'DemoCamera', 'DCam']

DEVICE = ['Camera', 'Andor', 'Andor']

mmc = MMCorePy.CMMCore()
mmc.enableStderrLog(False)
mmc.enableDebugLog(False)
mmc.loadDevice(*DEVICE)
mmc.initializeDevice(DEVICE[0])
mmc.setCameraDevice(DEVICE[0])
mmc.setProperty(DEVICE[0], 'PixelType', '16bit')
mmc.setProperty(DEVICE[0], 'AD_Converter', '2. 14bit')
mmc.setProperty(DEVICE[0], 'Binning', '1')

#print(mmc.getDevicePropertyNames(DEVICE[0]))

mmc.setExposure(20)

mmc.startContinuousSequenceAcquisition(1)

# OOP ------------------------------------------------------------

class App:
    
    def __init__(self, root, title):
        
        self.root = root
        self.root.title(title)
        
        # checkbutton 1 & label 1 & button 1 --------------------
        
        self.var1 = tk.BooleanVar()
        self.var1.set(True)
        
        self.label_1 = tk.Label(self.root, text = str((348,260)), font='12', 
                                 height = 2, width = 16, 
                                 relief = tk.FLAT)
        self.label_1.grid(row = 0, column=1)
        
        self.btn_1 = tk.Button(self.root, text = 'Set', font = '12', fg = 'orange', 
                               height = 1, width = 6, 
                               disabledforeground = 'grey', 
                               state = tk.NORMAL, command = self.setbutton_1)
        self.btn_1.grid(row = 0, column=2)
        
        self.cbtn_1 = tk.Checkbutton(self.root, relief = tk.GROOVE, 
                                     height = 2, width = 8, 
                                     text='Trap A', font='12', 
                                     variable = self.var1, 
                                     disabledforeground = 'black',
                                     state = tk.DISABLED)
        self.cbtn_1.grid(row = 0, column = 0, padx = 5)
        
        # checkbutton 2 & label 2 & button 2 --------------------
        
        self.var2 = tk.BooleanVar()
        
        self.label_2 = tk.Label(self.root, text = 'None', font='12', 
                         height = 2, width = 16, 
                         relief = tk.FLAT)
        self.label_2.grid(row = 1, column=1)
 
        self.btn_2 = tk.Button(self.root, text = 'Set', font = '12', fg = 'orange', 
                               height = 1, width = 6, 
                               disabledforeground = 'grey',
                               state = tk.DISABLED, command = self.setbutton_2)
        self.btn_2.grid(row = 1, column=2)
        
        self.cbtn_2 = tk.Checkbutton(self.root, relief = tk.GROOVE,
                             height = 2, width = 8,
                             text='Trap B', font='12', 
                             variable = self.var2,  
                             command = self.enable_2)
        self.cbtn_2.grid(row = 1, column = 0, padx = 5)
        
        # checkbutton 3 & label 3 & button 3 --------------------
        
        self.var3 = tk.BooleanVar()
        
        self.label_3 = tk.Label(self.root, text = 'None', font='12', 
                         height = 2, width = 16, 
                         relief = tk.FLAT)
        self.label_3.grid(row = 2, column=1)
 
        self.btn_3 = tk.Button(self.root, text = 'Set', font = '12', fg = 'orange', 
                               height = 1, width = 6, 
                               disabledforeground = 'grey',
                               state = tk.DISABLED, command = self.setbutton_3)
        self.btn_3.grid(row = 2, column=2)
        
        self.cbtn_3 = tk.Checkbutton(self.root, relief = tk.GROOVE,
                             height = 2, width = 8,
                             text='Trap C', font='12', 
                             variable = self.var3, 
                             command = self.enable_3)
        self.cbtn_3.grid(row = 2, column = 0, padx = 5)
        
        # checkbutton 2 & label 2 & button 2 --------------------
        
        self.var4 = tk.BooleanVar()
        
        self.label_4 = tk.Label(self.root, text = 'None', font='12', 
                         height = 2, width = 16, 
                         relief = tk.FLAT)
        self.label_4.grid(row = 3, column=1)
 
        self.btn_4 = tk.Button(self.root, text = 'Set', font = '12', fg = 'orange', 
                               height = 1, width = 6, 
                               disabledforeground = 'grey',
                               state = tk.DISABLED, command = self.setbutton_4)
        self.btn_4.grid(row = 3, column=2)
        
        self.cbtn_4 = tk.Checkbutton(self.root, relief = tk.GROOVE,
                             height = 2, width = 8,
                             text='Trap D', font='12', 
                             variable = self.var4, 
                             command = self.enable_4)
        self.cbtn_4.grid(row = 3, column = 0, padx = 5)
        
        # real-time coords ----------------------------------------
        
        self.word_label = tk.Label(self.root, text = "Position : ",
                                  font = '12', relief = tk.FLAT)
        self.word_label.grid(row = 4, column = 0, 
                             sticky=tk.E)
        
        self.cur_label = tk.Label(self.root, font = '12', text = '--', 
                                  height = 2, width = 10, 
                                  relief = tk.FLAT)
        self.cur_label.grid(row = 4, column = 1, padx = 5, sticky=tk.W)
        
        # unset button ----------------------------------------
        
        self.btn_unset = tk.Button(self.root, text='Done setting', 
                                   font = '12', fg = 'blue',
                                   height = 2,
                                   command = self.unset)
        
        self.btn_unset.grid(row = 4, column = 2, padx = 5, sticky=tk.W)
        
        # snapshot button ----------------------------------------
        
        self.btn_snapshot = tk.Button(self.root,
                                      text='Snapshot', font='12',
                                      foreground = 'darkgreen', 
                                      height = 2,
                                      command = self.snapshot)
        
        self.btn_snapshot.grid(row = 5, column = 0, columnspan = 3, 
                               sticky=tk.W+tk.E+tk.N+tk.S, pady=10, padx = 5)
        
        # canvas --------------------------------------------------
        
        self.canvas = tk.Canvas(self.root, width = 696-3, height = 520-3)
        
        self.canvas.grid(column = 4, row = 0, rowspan = 6,
                         sticky=tk.W+tk.E+tk.N+tk.S, 
                         padx = 5, pady = 10)
        
        self.update()
        
        # exposure time ----------------------------------------
        
        self.exp_label = tk.Label(self.root, text = "Exp time [ms]", 
                                  font = '12', relief = tk.FLAT)
        self.exp_label.grid(row = 6, column = 0, sticky=tk.E)
        
        self.exp_scale = tk.Scale(self.root, from_=20, to=1000, 
                                  orient = tk.HORIZONTAL, length = 900, 
                                  command = self.brightness)
        self.exp_scale.grid(row = 6, column = 1, columnspan = 4, sticky=tk.E+tk.N, 
                            padx = 20, pady = 5)
        
        # mouse stuff --------------------------------------------------
        
        self.in_var = False
        
        self.canvas.bind('<Enter>', self.enter)
        self.canvas.bind('<Leave>', self.leave)
        self.root.bind('<Motion>', self.motion)
        
        # shutdown --------------------------------------------------
         
        self.root.wm_protocol("WM_DELETE_WINDOW", self.out)
        
    # -------------------------------------------------------
        
    def update(self):
        
        if mmc.getRemainingImageCount() > 0:
            img = mmc.getLastImage()
            img = img/257
        else:
            img = cv2.imread('blank.png')
        
        self.canvas.photo = ImageTk.PhotoImage(Image.fromarray(img).resize((696,520)), img.shape)
        
        self.canvas.create_image(0, 0, image = self.canvas.photo, anchor = tk.NW)
        
        self.root.after(1, self.update)
        
    # -------------------------------------------------------
        
    def snapshot(self):
        
        if mmc.getRemainingImageCount() > 0:
            snap = mmc.getLastImage()
        else:
            snap = cv2.imread('blank.png')
            
        output = tkfd.asksaveasfilename(initialdir = "/", 
                                title = "Save PNG file only", 
                                defaultextension='.png', 
                                filetypes = (("PNG","*.png"),
                                             ("","*.??")))
        
        cv2.imwrite(output, snap)

    # -------------------------------------------------------
    
    def brightness(self, t):
        mmc.setExposure(self.exp_scale.get())

    # -------------------------------------------------------

    def enable(self, whichvar, whichlabel, whichbutton):
        if whichvar.get() == True:
            whichbutton.config(state=tk.NORMAL)
            whichlabel.config(text = str((348,260)))
        elif whichvar.get() == False:
            whichbutton.config(state=tk.DISABLED)
            whichlabel.config(text = 'None')
        
    def enable_2(self):
        self.enable(self.var2, self.label_2, self.btn_2)
        self.root.config(cursor = 'arrow')
        self.root.unbind('<Button-1>')
        
    def enable_3(self):
        self.enable(self.var3, self.label_3, self.btn_3)
        self.root.config(cursor = 'arrow')
        self.root.unbind('<Button-1>')
    
    def enable_4(self):
        self.enable(self.var4, self.label_4, self.btn_4)
        self.root.config(cursor = 'arrow')
        self.root.unbind('<Button-1>')

    # -------------------------------------------------------

    def setbutton_1(self):
        self.root.config(cursor = 'plus')
        self.root.bind('<Button-1>', self.click_1)

    def setbutton_2(self):
        self.root.config(cursor = 'plus')
        self.root.bind('<Button-1>', self.click_2)
        
    def setbutton_3(self):
        self.root.config(cursor = 'plus')
        self.root.bind('<Button-1>', self.click_3)
        
    def setbutton_4(self):
        self.root.config(cursor = 'plus')
        self.root.bind('<Button-1>', self.click_4)
        
    def unset(self):
        self.root.config(cursor = 'arrow')
        self.root.unbind('<Button-1>')

    # -------------------------------------------------------

    def click_1(self, event):
        if self.in_var == True:
            self.tx, self.ty = event.x, event.y
            self.label_1.config(text = '({}, {})'.format(self.tx, self.ty))

    def click_2(self, event):
        if self.in_var == True:
            self.tx, self.ty = event.x, event.y
            self.label_2.config(text = '({}, {})'.format(self.tx, self.ty))
        
    def click_3(self, event):
        if self.in_var == True:
            self.tx, self.ty = event.x, event.y
            self.label_3.config(text = '({}, {})'.format(self.tx, self.ty))
        
    def click_4(self, event):
        if self.in_var == True:
            self.tx, self.ty = event.x, event.y
            self.label_4.config(text = '({}, {})'.format(self.tx, self.ty))

    # -------------------------------------------------------

    def enter(self, event):
        self.in_var = True
        
    def leave(self, event):
        self.in_var = False

    def motion(self, event):
        if self.in_var == True:
            self.x, self.y = event.x, event.y
            self.cur_label.config(text = '({}, {})'.format(self.x, self.y))
        if self.in_var == False:
            self.cur_label.config(text = '--')

    # -------------------------------------------------------
        
    def out(self):
        mmc.stopSequenceAcquisition()
        self.root.destroy()
        
# ------------------------------------------------------------
        
pba = App(tk.Tk(), "The Optical Tweezer Program")
pba.root.mainloop()
