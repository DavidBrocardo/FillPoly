import tkinter as tk
from tkinter import colorchooser
from tkinter import messagebox
from FillPoly import FillPoly


class Interface:

    def __init__(self, tela):
        self.tela = tela
        self.tela.title("FillPoly")
        self.vertices = []      
        self.cores_poliginos = []         
        self.corPoligino = "#000000"
        self.corAresta = "#FFFF00"
        self.Poligino_controle = 0
        self.indicePoligino  = 0 

        self.canvas = tk.Canvas(tela, width=600, height=400, bg="white")
        self.canvas.pack(pady=10)
        self.button_frame = tk.Frame(tela)
        self.button_frame.pack()

        self.btn_poligino = tk.Button(self.button_frame, text="Gerar Polígono", command=self.gerar_poligino, bg="cyan")
        self.btn_poligino.grid(row=0, column=0, padx=5)

        self.btn_limpar = tk.Button(self.button_frame, text="Limpar Tela", command=self.limpar_tela, bg="cyan")
        self.btn_limpar.grid(row=0, column=1, padx=5)   

        self.btn_sair = tk.Button(self.button_frame, text="Sair", command=tela.destroy, bg="red")
        self.btn_sair.grid(row=0, column=2, padx=5)           

        self.btn_mudarCor = tk.Button(self.button_frame, text="Alterar cor", command=self.Mudar_Cor_Poligino, bg="gray")
        self.btn_mudarCor.grid(row=1, column=0,padx=5, pady=5)   

        self.btn_apagaPoligino = tk.Button(self.button_frame, text="Apagar Poligino", command=self.Apagar_Poligino, bg="gray")
        self.btn_apagaPoligino.grid(row=1, column=1,padx=5, pady=5)   

        self.btn__corPoligino = tk.Button(self.button_frame, text="Escolher Cor do Polígono", command=self.determina_corPoligino)
        self.btn__corPoligino.grid(row=2, column=0, padx=5, pady=5)
        
        self.label_corPoligino = tk.Label(self.button_frame, width=7, bg=self.corPoligino)
        self.label_corPoligino.grid(row=2, column=1, padx=5, pady=5)

        self.btn_corAresta = tk.Button(self.button_frame, text="Escolher Cor da Aresta", command=self.determina_corAresta)
        self.btn_corAresta.grid(row=3, column=0, padx=5, pady=5)
        self.label_corAresta = tk.Label(self.button_frame, width=7, bg=self.corAresta)
        self.label_corAresta.grid(row=3, column=1, padx=5, pady=5)        

        self.canvas.bind("<Button-1>", self.onclick)

    def gerar_poligino(self):
        if self.Poligino_controle == 0: 
            if len(self.vertices) >= 3:
                self.cores_poliginos.append((self.corAresta, self.corPoligino))
                i = len(self.vertices)
                x_inicial, y_inicial = self.vertices[(0)] 
                x_final, y_final = self.vertices[(i-1)]  
                
                FillPoly(self.vertices,self.canvas,self.cores_poliginos,self.indicePoligino,1,0,0)
                self.indicePoligino += 1
                self.vertices = []
                self.cores_poliginos = []
            self.Poligino_controle = 0

    def limpar_tela(self):
        self.cores_poliginos = []
        self.indicePoligino = 0
        self.canvas.delete("all") 
        self.vertices = []
        FillPoly(0,0,0,0,4,0,0)
        
    def Mudar_Cor_Poligino(self):
        if len(self.vertices) == 0:
            self.Poligino_controle = 2
        else:
            messagebox.showinfo("Atenção", "Finalize o polígono atual antes de realizar outra ação!")        

    def Apagar_Poligino(self):
        if len(self.vertices) == 0:
            self.Poligino_controle = 3
        else:
            messagebox.showinfo("Atenção", "Finalize o polígono atual antes de realizar outra ação!")


    def onclick(self, event):
        if self.Poligino_controle == 0:
            x, y = event.x, event.y
            self.vertices.append((x,y))
            self.canvas.create_oval(x, y, x+2, y+2, fill=self.corPoligino)

        else:
            x, y = event.x, event.y
            cor = []  
            cor.append((self.corAresta, self.corPoligino))
                     
            if self.indicePoligino >= 1:
                if self.Poligino_controle == 2:
                    FillPoly(0,self.canvas,cor,(self.indicePoligino-1),self.Poligino_controle, x , y)
                elif self.Poligino_controle == 3:
                    FillPoly(0,self.canvas,cor,(self.indicePoligino-1),self.Poligino_controle, x , y)
                    self.indicePoligino -= 1

            self.Poligino_controle = 0   
            
    def determina_corPoligino(self):
        cor = colorchooser.askcolor(title="Escolha uma cor")
        _, hex_color = cor
        if (len(self.vertices)==0):
            self.corPoligino = hex_color
            self.label_corPoligino.config(bg=self.corPoligino)
    
    def determina_corAresta(self):
        cor = colorchooser.askcolor(title="Escolha uma cor")
        _, hex_color = cor
        if (len(self.vertices)==0):
            self.corAresta = hex_color
            self.label_corAresta.config(bg=self.corAresta)

tkk = tk.Tk()
app = Interface(tkk)
tkk.mainloop()


