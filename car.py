

#Definisco un nuovo tipo di dato, la classe Car
class Car: #per convenzione le classi hanno iniziale maiuscola
    wheels = 4 # Variabile di classe identica per tute le istanze di quella classe

    def __init__(self, license_plate, color):        #costruttore della classe
        self.license_plate = ""    #  Attributi o Variabili di istanza
        self.color = "White"
        self.turned_on = False

    def paint(self, color):
        self.color = color

    def turn_on(self):
        self.turned_on = True

#c1 = Car()          #creo un oggetto di classe/tipo Car

c1 = Car("AA123EB", "Red")    #Invoco il costruttore passando due argomenti

print(c1)

c1.license_plate = "GE888EG"

print("License plate: "+str(c1.license_plate))
print("color: "+str(c1.color))
print("Turned on: "+str(c1.turned_on))

c2 = Car("ZZ666ZZ", "Black")

# Come si accede alle variabili di istanza
c1.color = "Green"

# Come si accede alla variabili di classe
Car.wheels = 7

# Come faccio a cambiare il colore di un oggetto Car? O lo stato di accensione?

c1.color = "Pink"
c2.turned_on = True

#Anziche accedere direttamente agli attributi posso usare le funzioni

c1.paint("Violet")
c2.turn_on()