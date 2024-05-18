import math
import matplotlib.pyplot as mpl
import pandas as pd

class KNNClassifier:
    def __init__(self, claseA, claseB):
        self.claseA = claseA
        self.claseB = claseB
        self.datos = []

    def calcular_distancia(self, punto1, punto2):
        try:
            x1, y1 = punto1
            x2, y2 = punto2
            distancia = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
            return distancia
        except TypeError:
            print("Error: Coordenadas inválidas.")
            return None

    def cargar_datos(self, puntoClasificar):
        for tipoClase, puntos in [("Billete_Falso", self.claseA), ("Billete_Verdadero", self.claseB)]:
            for punto in puntos:
                distancia = self.calcular_distancia(puntoClasificar, punto)
                if distancia is not None:
                    self.datos.append((tipoClase, distancia))

#k numero limite 
    def determinar_KNN(self, k):
        contadorA = contadorB = 0
        for tipoClase, _ in self.datos[:k]:
            if tipoClase == "Billete_Falso":
                contadorA += 1
            else:
                contadorB += 1
        return contadorA, contadorB

    def determinar_clase(self,k):
        self.datos.sort(key=lambda dato: dato[1])
        for tipoClase, distancia in self.datos:
            print(f"Tipo de clase: {tipoClase}, Distancia: {distancia:.2f}")
        intentos = False
        while intentos == False:
            contadorA, contadorB = self.determinar_KNN(k)
            if contadorA > contadorB:
                intentos = True
                return "Es un billete falso"
            elif contadorB > contadorA:
                intentos = True 
                return "Es un billete real"
            else:
                print(f"No se puede determinar la clase con k={k}. Incrementando k...")
                k += 1
                intentos = False 
        


# Read the CSV file, omitting the index by default (since Pandas 0.24)
df = pd.read_csv("billete_falso.csv", index_col=None)
# Access the columns by their correct names
# Obtener valores de las columnas y convertirlos en listas planas
valor_x_Fake = df['height_left fake'].tolist()
valor_y_Fake = df['height_right Fake'].tolist()

valor_x_True = df['height_left TRUE'].tolist()
valor_y_True = df['height_right TRUE'].tolist()

# Combina los valores de las listas en tuplas
claseA = list(zip(valor_x_Fake, valor_y_Fake))
claseB = list(zip(valor_x_True, valor_y_True))
puntoClasificar = (103.2, 104.3)

knn = KNNClassifier(claseA, claseB)

knn.cargar_datos(puntoClasificar)

resultado = knn.determinar_clase(10)
print(resultado)

mpl.title("k-nearest neighbors")

x1 = [pnt[0] for pnt in claseA]
x2 = [pnt[0] for pnt in claseB]
y1 =[pnt[1] for pnt in claseA]
y2 = [pnt[1] for pnt in claseB]

#claseA
mpl.scatter(x1,y1,color='orange', label='Billete Falso', marker='v')
#claseB
mpl.scatter(x2,y2, color='blue', label='Billete verdadero', marker='v')
#nunevo punto
mpl.scatter(puntoClasificar[0], puntoClasificar[1], color = 'g', marker='x', label="Punto a clasificar")
mpl.legend()
mpl.xlabel("ancho")
mpl.ylabel("alto")
mpl.grid()
mpl.show()


