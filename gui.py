# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 15:09:34 2019

@author: bhaskaraby
"""

import pandas as pd
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Tk, Frame, Label, Entry, StringVar, Canvas, Scrollbar, Button, OptionMenu, filedialog, messagebox

dataTraining = np.array(pd.read_excel('Data Skripsi.xlsx'))
# ************************
# Scrollable Frame Class
# ************************
class ScrollFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent) # create a frame (self)

        self.canvas = Canvas(self, borderwidth=0)          #place canvas on self
        self.viewPort = Frame(self.canvas)                    #place a frame on the canvas, this frame will hold the child widgets 
        self.vsb = Scrollbar(self, orient="vertical", command=self.canvas.yview) #place a scrollbar on self 
        self.canvas.configure(yscrollcommand=self.vsb.set)                          #attach scrollbar action to scroll of canvas

        self.vsb.pack(side="right", fill="y")                                       #pack scrollbar to right of self
        self.canvas.pack(side="left", fill="both", expand=True)                     #pack canvas to left of self and expand to fil
        self.canvas.create_window((4,4), window=self.viewPort, anchor="nw",            #add view port frame to canvas
                                  tags="self.viewPort")

        self.viewPort.bind("<Configure>", self.onFrameConfigure)                       #bind an event whenever the size of the viewPort frame changes.

    def onFrameConfigure(self, event):                                              
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))                 #whenever the size of the frame changes, alter the scroll region respectively.

class Main(Frame):
    def __init__(self, root):

        Frame.__init__(self, root)
        self.root = root
        self.root.title(" Penerapan LVQ2 pada jenis penyalahgunaan Narkoba")
        self.scrollFrame = ScrollFrame(self) # add a new scrollable frame.
        
        # Now add some controls to the scrollframe. 
        # NOTE: the child controls are added to the view port (scrollFrame.viewPort, NOT scrollframe itself)
#        for row in range(100):
#            a = row
#            tk.Label(self.scrollFrame.viewPort, text="%s" % row, width=3, borderwidth="1", 
#                     relief="solid").grid(row=row, column=0)
#            t="this is the second column for row %s" %row
#            tk.Button(self.scrollFrame.viewPort, text=t, command=lambda x=a: self.printMsg("Hello " + str(x))).grid(row=row, column=1)
    
        # when packing the scrollframe, we pack scrollFrame itself (NOT the viewPort)
        self.scrollFrame.pack(side="top", fill="both", expand=True)
        self.header = ['No.', 'Pendidikan', 'Pekerjaan', 'Usia', 
                       'G1', 'G2', 'G3', 'G4', 
                       'G5', 'G6', 'G7', 'G8', 
                       'G9', 'G10', 'G11', 'G12', 'G13', 'G14', 'Indikasi']
        self.w = []
        self.bestWTesting = []
        
        self.mainFrame()
        
    def mainFrame(self):
        lblCoba = Label(self.scrollFrame.viewPort, text="Coba")
        lblCoba.grid(row=0, column=0)
        self.pendidikan = StringVar(value="Pend")
        optPendidikan = OptionMenu(self.scrollFrame.viewPort, self.pendidikan, "SD", "SMP", "SMA", "Kuliah")
        optPendidikan.grid(row=0, column=1)
        self.pekerjaan = StringVar(value="Pek.")
        optPekerjaan = OptionMenu(self.scrollFrame.viewPort, self.pekerjaan, "TNI/POLRI", "PNS", "Swasta", "Petani", "Buruh", "Non")
        optPekerjaan.grid(row=0, column=2)
        self.umur = StringVar(value="Umur")
        entUmur = Entry(self.scrollFrame.viewPort, textvariable=self.umur, width="5")
        entUmur.grid(row=0, column=3)
        self.g1 = StringVar(value="G1")
        optG1 = OptionMenu(self.scrollFrame.viewPort, self.g1, "Yes", "No")
        optG1.grid(row=0, column=4)
        self.g2 = StringVar(value="G2")
        optG2 = OptionMenu(self.scrollFrame.viewPort, self.g2, "Yes", "No")
        optG2.grid(row=0, column=5)
        self.g3 = StringVar(value="G3")
        optG3 = OptionMenu(self.scrollFrame.viewPort, self.g3, "Yes", "No")
        optG3.grid(row=0, column=6)
        self.g4 = StringVar(value="G4")
        optG4 = OptionMenu(self.scrollFrame.viewPort, self.g4, "Yes", "No")
        optG4.grid(row=0, column=7)
        self.g5 = StringVar(value="G5")
        optG5 = OptionMenu(self.scrollFrame.viewPort, self.g5, "Yes", "No")
        optG5.grid(row=0, column=8)
        self.g6 = StringVar(value="G6")
        optG6 = OptionMenu(self.scrollFrame.viewPort, self.g6, "Yes", "No")
        optG6.grid(row=0, column=9)
        self.g7 = StringVar(value="G7")
        optG7 = OptionMenu(self.scrollFrame.viewPort, self.g7, "Yes", "No")
        optG7.grid(row=0, column=10)
        self.g8 = StringVar(value="G8")
        optG8 = OptionMenu(self.scrollFrame.viewPort, self.g8, "Yes", "No")
        optG8.grid(row=0, column=11)
        self.g9 = StringVar(value="G9")
        optG9 = OptionMenu(self.scrollFrame.viewPort, self.g9, "Yes", "No")
        optG9.grid(row=0, column=12)
        self.g10 = StringVar(value="G10")
        optG10 = OptionMenu(self.scrollFrame.viewPort, self.g10, "Yes", "No")
        optG10.grid(row=0, column=13)
        self.g11 = StringVar(value="G11")
        optG11 = OptionMenu(self.scrollFrame.viewPort, self.g11, "Yes", "No")
        optG11.grid(row=0, column=14)
        self.g12 = StringVar(value="G12")
        optG12 = OptionMenu(self.scrollFrame.viewPort, self.g12, "Yes", "No")
        optG12.grid(row=0, column=15)
        self.g13 = StringVar(value="G13")
        optG13 = OptionMenu(self.scrollFrame.viewPort, self.g13, "Yes", "No")
        optG13.grid(row=0, column=16)
        self.g14 = StringVar(value="G14")
        optG14 = OptionMenu(self.scrollFrame.viewPort, self.g14, "Yes", "No")
        optG14.grid(row=0, column=17)
        #btnBrowse = Button(self.scrollFrame.viewPort, text="Browse", command=self.browse)
        #btnBrowse.grid(row=0, column=19, sticky="N")
        btnCek = Button(self.scrollFrame.viewPort, text="Cek", command=self.cek)
        btnCek.grid(row=0, column=18)
        btnTraining = Button(self.scrollFrame.viewPort, text="Training", command=self.training)
        btnTraining.grid(row=1, column=19, sticky="N")
        btnTesting = Button(self.scrollFrame.viewPort, text="Testing", command=self.testing)
        btnTesting.grid(row=2, column=19, sticky="N")
        btnSaveW = Button(self.scrollFrame.viewPort, text="Save\nWeight", command=self.saveWeight)
        btnSaveW.grid(row=3, column=19, sticky="N")
        tblHeader = []
        for i in range(len(self.header)):
            tblHeader.append(Label(self.scrollFrame.viewPort, text=self.header[i], borderwidth=1, relief="solid"))
            tblHeader[i].grid(row=1, column=i)
        lblData = []
        for i in range(20):
            temp = []
            data = dataTraining[i, 1:]
            temp.append(Label(self.scrollFrame.viewPort, text=str(1+i)))
            temp[0].grid(row=i+2, column=0)
            for j in range(data.size):
                temp.append(Label(self.scrollFrame.viewPort, text=data[j]))
                temp[j+1].grid(row=i+2, column=j+1)
            lblData.append(temp)
    
    def browse(self):
        self.path = filedialog.askopenfilename()
        
    def olahData(self, fitur, n):
        if fitur == 'Pendidikan':
            if n == 'Non':
                return 0
            elif n == 'SD':
                return 0.25
            elif n == 'SMP':
                return 0.5
            elif n == 'SMA':
                return 0.75
            elif n == 'Kuliah':
                return 1
        elif fitur == 'Pekerjaan':
            if n == 'TNI/POLRI':
                return 0
            elif n == 'PNS':
                return 0.2
            elif n == 'Swasta':
                return 0.4
            elif n == 'Petani':
                return 0.6
            elif n == 'Buruh':
                return 0.8
            elif n == 'Non':
                return 1
        elif fitur == 'Usia':
            return n
        else:
            if n == 'Yes':
                return 1
            else:
                return 0
    
    def cek(self):
        if len(self.bestWTesting) > 0:
            w = self.bestWTesting
            Xtest = []
            data = [self.pendidikan.get(), self.pekerjaan.get(), self.umur.get(), 
                    self.g1.get(), self.g2.get(), self.g3.get(), self.g4.get(),
                     self.g5.get(), self.g6.get(), self.g7.get(),
                     self.g8.get(), self.g9.get(), self.g10.get(),
                     self.g11.get(), self.g12.get(), self.g13.get(), self.g14.get()
                     ]
            i = 0
            for h in self.header[1:-1]:
                Xtest.append(self.olahData(h, data[i]))
                i+=1
            Xtest = np.array(Xtest, dtype=float)
            temp = np.append(dataTraining[:, 1:-1], [Xtest], axis=0)
            temp = self.normalisasi(temp)
            Xtest = temp[-1]
            X = Xtest
            f1 = np.sqrt(np.sum(np.square(X - w[0])))
            f2 = np.sqrt(np.sum(np.square(X - w[1])))
            f3 = np.sqrt(np.sum(np.square(X - w[2])))
            distances = [f1, f2, f3]
            result = np.argmin(distances) + 1
            if result == 1:
                messagebox.showinfo("Message", "Narkotika")
            elif result == 2:
                messagebox.showinfo("Message", "Psikotropika")
            else:
                messagebox.showinfo("Message", "Zat Adiktif")
        else:
            messagebox.showinfo("Message", "Belum ada bobot yang telah di training dan di testing.")
        
    def normalisasi(self, x):
        newx = np.copy(x)
        for i in range(x.shape[1]):
            if i == 2:
                nmin = np.min(x[:, i])
                nmax = np.max(x[:, i])
                newx[:, i] = (x[:, i] - nmin) / (nmax - nmin)
        return newx
    
    def saveWeight(self):
        if len(self.w) > 0:
            for i in range(len(self.w)):
                df = pd.DataFrame(self.w[i])
                df.to_excel('Bobot Fold %s Training GUI.xlsx' % str(i+1))
        
    def training(self):
        self.w = []
        lblAccFold = []
        target = np.copy(dataTraining[:,-1])
        normalized = self.normalisasi(dataTraining[:, 1:-1])
        for i in range(target.size):
            if target[i].lower() == 'narko':
                target[i] = 1
            elif target[i].lower() == 'psiko':
                target[i] = 2
            elif target[i].lower() == 'zat adiktif':
                target[i] = 3
        akurasies = []
        p = np.random.permutation(normalized.shape[0])
        normalized = normalized[p]
        target = target[p]
        val_w = []
        for val in range(3):
            learning_rate = 0.1
            penurun = 0.01
            window = 0.5
            max_epoh = 10
            min_lr = 1e-20
            if val == 0:
                Xval = normalized[:20]
                yval = target[:20]
                Xtrain = normalized[20:]
                ytrain = target[20:]
            elif val == 1:
                Xval = normalized[94:114]
                yval = target[94:114]
                Xtrain = np.append(normalized[:94], normalized[114:], axis=0)
                ytrain = np.append(target[:94], target[114:], axis=0)
            else:
                Xval = normalized[-40:]
                yval = target[-40:]
                Xtrain = normalized[:-40]
                ytrain = target[:-40]
            val_accs = []
            
            w = np.random.random((3, 17))
            continue_training = True
            min_e = 0
            min_i = 0
            for e in range(max_epoh):
                jml_benar = 0
                for i in range(Xval.shape[0]):
                    X = Xval[i]
                    f1 = np.sqrt(np.sum(np.square(X - w[0])))
                    f2 = np.sqrt(np.sum(np.square(X - w[1])))
                    f3 = np.sqrt(np.sum(np.square(X - w[2])))
                    distances = [f1, f2, f3]
                    result = np.argmin(distances) + 1
                    if yval[i] == result:
                        jml_benar += 1
                
                akurasi = jml_benar / yval.size * 100
                print("akurasi fold %s: %.3f" % (val, akurasi))
                val_accs.append(akurasi)
                if continue_training == True:
                    for i in range(Xtrain.shape[0]):
                        X = Xtrain[i]
                        f1 = np.sqrt(np.sum(np.square(X - w[0])))
                        f2 = np.sqrt(np.sum(np.square(X - w[1])))
                        f3 = np.sqrt(np.sum(np.square(X - w[2])))
                        distances = [f1, f2, f3]
                        result = np.argmin(distances) + 1
                        if ytrain[i] == result:
                            j = result - 1
                            w[j] = X + learning_rate * (X - w[j])
                        else:
                            temp = np.argsort(distances)
                            if distances[temp[0]] > (1-window) * distances[temp[1]] and distances[temp[1]] < (1+window) * distances[temp[0]]:
                                w[temp[0]] = w[temp[0]] - learning_rate * (X - w[temp[0]])
                                w[temp[1]] = w[temp[1]] + learning_rate * (X - w[temp[1]])
                        learning_rate -= penurun * learning_rate
                        if learning_rate < min_lr:
                            continue_training = False
                            min_e = e
                            min_i = i
                            break
                else:
                    print("Training dihentikan pada epoh = %s dan i = %s karena learning rate mencapai minimum." % (min_e, min_i))
                    
            val_w.append(w)
            akurasies.append(val_accs)
        self.w = val_w
        i = 1
        for a in akurasies:
            lblAccFold.append(Label(self.scrollFrame.viewPort, text=("Akurasi Fold %s : %.2f %s" % (i, a[-1], "%"))))
            lblAccFold[i-1].grid(row=22, column=5*(i-1), columnspan=5)
            i+=1
        f = Figure(figsize=(6, 3.5), dpi=100)
        self.canvas = FigureCanvasTkAgg(f, master=self.scrollFrame.viewPort)
        self.canvas.get_tk_widget().grid(row=23, column=0, padx=30, pady=20, columnspan=18)
        p = f.gca()
        p.plot(akurasies[0])
        p.plot(akurasies[1])
        p.plot(akurasies[2])
        p.set_xlabel("Epoh")
        p.set_ylabel("Akurasi")
        self.canvas.draw()
        
    def testing(self):
        accs = []
        self.bestWTesting = []
        if len(self.w) > 0:
            for w in self.w:
                jml_benar = 0
                Xtest = self.normalisasi(dataTraining[:, 1:-1])
                target = np.copy(dataTraining[:, -1])
                for i in range(target.size):
                    if target[i].lower() == 'narko':
                        target[i] = 1
                    elif target[i].lower() == 'psiko':
                        target[i] = 2
                    elif target[i].lower() == 'zat adiktif':
                        target[i] = 3
                ytest = target
                for i in range(Xtest.shape[0]):
                    X = Xtest[i]
                    f1 = np.sqrt(np.sum(np.square(X - w[0])))
                    f2 = np.sqrt(np.sum(np.square(X - w[1])))
                    f3 = np.sqrt(np.sum(np.square(X - w[2])))
                    distances = [f1, f2, f3]
                    result = np.argmin(distances) + 1
                    if ytest[i] == result:
                        jml_benar += 1
                akurasi = jml_benar / ytest.size * 100
                print("Akurasi testing: %.2f" % akurasi)
                accs.append(akurasi)
            self.bestWTesting = self.w[np.argmax(accs)]
        else:
            messagebox.showinfo("Message", "Belum ada bobot yang telah di training.")
        
if __name__ == "__main__":
    root = Tk()
    root.geometry("1200x500")
    Main(root).pack(side="top", fill="both", expand=True)
    root.mainloop()