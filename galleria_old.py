


class Quadro:
    def __init__(self, artista,titolo, materiali, anno):
        self.__artista = artista
        self.__titolo = titolo
        self.__materiali = materiali
        self.__anno = anno    #1853 e 1890

    def imposta_anno(self, nuovo_anno):
        if nuovo_anno > 1853 and nuovo_anno < 1890:
            self.__anno = nuovo_anno
        else:
            print("L'anno inserito non è valido")

    def leggi_anno(self):
        return self.__anno


q1 = Quadro("Van Gogh", "autoritratto","olio su tela", 1870)
#print(f"{q1.__artista} {q1.__titolo} {q1.__materiali} {q1.__anno}")

#q1.anno = 1945  #Non posso farlo così perchè l'attributo è privato/nascosto

# Per accedere all'attributo devo usare i metodi/le funzioni

q1.imposta_anno(1800)

#print(f"{q1.__artista} {q1.__titolo} {q1.__materiali} {q1.__anno}")

print("Anno:"+str(q1.leggi_anno()))