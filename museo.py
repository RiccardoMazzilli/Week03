# Se voglio utilizzare una classe definita in un altro file (o modulo)
# devo utilizzare le parole chiave import e from

from quadro import Quadro

# Ora posso utilizzare la classe Quadro, es. per creare oggetti)
q = Quadro("Monet", "...", "...", "...")

print(q.__str__())

print(q)  # Se ho definito la funzione __str__ per l'oggetto
          # quando lo vado a stampare python capisce che deve
          # utilizzare quella funzione anzichè stampare l'indirizzo memoria

lista_di_quadri = []
lista_di_quadri.append(q)
lista_di_quadri.append(Quadro("Cezanne", "...", "...", "..."))
lista_di_quadri.append(Quadro("Pollock", "...", "...", "..."))

print("Lista di quadri:")
for quadro in lista_di_quadri:
    print(quadro.__str__())

# 1) CON LE CLASSI POSSO DEFINIRE I MIEI TIPI DI DATO (ES. QUADRO)
# 2) POSSO DOTARLI DI DEI DATI/ATTRIBUTI CHE LI CARATTERIZZANO (NASCOSTI)
# 3) POSSO DOTARLI DELLE FUNZIONI/DEI METODI PER OPERARE SU QUEI DATI

