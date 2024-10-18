import tkinter as tk
from tkinter import colorchooser
class FillPoly:
    lista_intersecoess = {}
    cores_poligino = []
    vertices_poliginos = []
    def __init__(self, poligino,tela,corPreenchimento,indicePoligino,Poligino_controle,x,y):
        self.controle = Poligino_controle
        if (self.controle == 4) :
           FillPoly.lista_intersecoess = {}
           FillPoly.cores_poligino = [] 
           FillPoly.vertices_poliginos = []
           return
        else:            
            self.tela = tela
            self.corA,self.cor = corPreenchimento[(0)]
            self.indicePoligino = indicePoligino
            self.controle = Poligino_controle
            self.xPonto = x
            self.yPonto = y 
            self.y_min = 600
            self.y_max = 0
            self.num_Scanlines = 0
            self.yP = []
            self.xP = []
            if self.controle == 1 :     
                self.poligino = poligino       
                FillPoly.vertices_poliginos.append((self.poligino)) 
                FillPoly.cores_poligino.append((self.corA, self.cor))            
                self.scanlines()
                self.calc_intersecoes()
                self.FillPoly_pinta()                
                return
            elif self.controle == 2:
                self.poligino = FillPoly.vertices_poliginos 
                self.mudarCor()
                return 
            else:
                self.poligino = FillPoly.vertices_poliginos 
                self.ApagaPoligino()
                return
            
    def scanlines(self):
        if self.indicePoligino not in FillPoly.lista_intersecoess:
            FillPoly.lista_intersecoess[self.indicePoligino] = {}
            
        for i in range(len(self.poligino)):
            x , y = self.poligino[(i)]             
            if y > self.y_max :
                self.y_max = y
            if y < self.y_min :
                self.y_min = y
        self.num_Scanlines = self.y_max - self.y_min 
        
        if self.controle == 1:
            for i in range(self.num_Scanlines+1):
                FillPoly.lista_intersecoess[self.indicePoligino][self.y_min + i] = []                
        return                  

    def calc_intersecoes(self):

        for i in range(len(self.poligino)):             
            if (i != len(self.poligino)-1):
                x_ver1, y_ver1 = self.poligino[(i)]
                x_ver2, y_ver2 = self.poligino[(i+1)]
                if (y_ver1 <= y_ver2):
                    x_Ini, y_ini =  self.poligino[(i)]
                    x_Fin, y_Fin =  self.poligino[(i+1)]
                else:
                    x_Ini, y_ini =  self.poligino[(i+1)]
                    x_Fin, y_Fin =  self.poligino[(i)]
            else:
                x_ver1, y_ver1 = self.poligino[(i)]
                x_ver2, y_ver2 = self.poligino[(0)]
                if (y_ver1 <= y_ver2):
                    x_Ini, y_ini =  self.poligino[(i)]
                    x_Fin, y_Fin =  self.poligino[(0)]
                else:
                    x_Ini, y_ini =  self.poligino[(0)]
                    x_Fin, y_Fin =  self.poligino[(i)]
                
            if (y_ini != y_Fin):                    
                if(x_Fin == x_Ini):
                    coeficienteAngular =  (y_Fin -y_ini)
                else:
                    coeficienteAngular =  (y_Fin -y_ini)/(x_Fin-x_Ini)
                Tx = 1 / coeficienteAngular
                YInter  = y_ini
                XInter =  x_Ini 
                FillPoly.lista_intersecoess[self.indicePoligino][y_ini].append((x_Ini))
                self.xP.append(x_Ini + Tx)
                while (YInter < (y_Fin-1)):                        
                    YInter = YInter + 1
                    XInter = XInter + Tx
                    FillPoly.lista_intersecoess[self.indicePoligino][YInter].append((XInter))
        return    

    def FillPoly_pinta(self):
        corAresta, CorPoligino = FillPoly.cores_poligino[self.indicePoligino]
        i = self.y_min   
        for i in range((len(self.poligino)-1)):
            x_inicial , y_inicial = self.poligino[(i)] 
            x_final , y_final = self.poligino[(i+1)] 
            self.tela.create_line(x_inicial, y_inicial, x_final, y_final, fill=corAresta, width=3)
        i = len(self.poligino)              
        x_inicial, y_inicial = self.poligino[(0)]  
        x_final, y_final = self.poligino[(i-1)]
        self.tela.create_line(x_inicial, y_inicial, x_final, y_final, fill=corAresta, width=3)

        while (i < self.y_max):
            pontos_Intersecoess = sorted(FillPoly.lista_intersecoess[self.indicePoligino].get(i, []))
            if len(pontos_Intersecoess) > 1 :
                j = 0
                while j < (len(pontos_Intersecoess)):
                    x_ini =  pontos_Intersecoess[(j)]
                    x_fim =  pontos_Intersecoess[(j+1)]
                    j = j + 2
                    X = x_ini
                    while X < x_fim:
                        self.tela.create_oval(X, i, X+1, i+1, fill=CorPoligino, outline= CorPoligino)
                        
                        X += 1
            i+=1
        return    

    def encontraPoligino(self):
        ind = self.indicePoligino    
        while ind >= 0:
            pontos_Intersecoess = sorted(FillPoly.lista_intersecoess[ind].get(self.yPonto, []))
            if len(pontos_Intersecoess) > 1:
                j = 0
                while j < len(pontos_Intersecoess):
                    if self.xPonto >= pontos_Intersecoess[j] and self.xPonto <= pontos_Intersecoess[j+1]:
                        return ind                        
                    else:
                        j += 2
            elif len(pontos_Intersecoess) == 1:
                if self.xPonto == pontos_Intersecoess[0]:
                    return ind         
            ind -= 1
        return -1

    def atualizaTela(self):    
        self.tela.delete("all")
        poliginos = self.poligino
        self.poligino = []
        ind = self.indicePoligino                  
        i = 0
        while i <= ind:
            self.poligino = poliginos[i]
            poliginoOrdenadoY = sorted(poliginos[i], key=lambda x: x[1])
            x_min, self.y_min = poliginoOrdenadoY[0]  
            x_min, self.y_max = poliginoOrdenadoY[-1]  
            self.indicePoligino = i
            self.corA, self.cor = FillPoly.cores_poligino[i]  
            for vertice in range(len(self.poligino)):
                x,y = self.poligino[(vertice)]
                self.tela.create_oval(x, y, x+3, y+3, fill=self.cor)

            self.FillPoly_pinta() 
            self.poligino = []
            i += 1
        return

    def mudarCor(self):
        ind = self.encontraPoligino()
        if (ind != -1):
            corAresta, CorPoliginoAntiga = FillPoly.cores_poligino[ind]
            cor = colorchooser.askcolor(title="Escolha uma cor")
            _, hex_color = cor                  
            corPoligino = hex_color        
            FillPoly.cores_poligino[ind] = (corAresta, corPoligino)
            self.atualizaTela()   
        
        
    def ApagaPoligino(self):
        ind = self.encontraPoligino()
        if (ind != -1):
            self.tela.delete("all")
            del FillPoly.lista_intersecoess[ind] 
            del FillPoly.cores_poligino[ind]
            del FillPoly.vertices_poliginos[ind]
            j = 0
            for i in sorted(FillPoly.lista_intersecoess):
                FillPoly.lista_intersecoess[j] = FillPoly.lista_intersecoess[i]
                j += 1
            
            self.indicePoligino -= 1
            self.atualizaTela()
            return 

    

    

