import random 

class Personaggio:
    def __init__(self, name, qualita, range, vita):
        self.name = name
        self.qualita = qualita
        self.range = range
        self.vita = vita



class Guerriero(Personaggio):
    def __init__(self, name, qualita, range, vita):
        super().__init__(name, qualita, range, vita)

   


class Mago(Personaggio):
    def __init__(self, name, qualita, range, vita):
        super().__init__(name, qualita, range, vita)

    



class Nemico(Personaggio):
    def __init__(self, name, qualita, range, vita):
        super().__init__(name, qualita, range, vita)

   

personaggio = Personaggio('neutro', 'neutro', 'neutro', 0)
guerriero = Guerriero('Soul', 'Spada', 'Breve', 100)
mago = Mago('Sherron', 'Bacchetta', 'Lungo', 80 )
nemico = Nemico('Minion', 'Coltello', 'Breve', 90)



def menu():
    print(f"Quale personaggio vuoi scegliere tra {mago.name} e {guerriero.name}?")
    utente = input("Scegli => ")

    return utente  



def main(utente):
   if utente == mago.name:
        mage()


def mage():
    print(f'Combattimento tra {mago.name} e {nemico.name}')

    while True:

        if mago.vita > 0 or nemico.vita > 0:
            attackM = random.randint(3,10)
            print(f'Il tuo attacco ha fatto {attackM} danni!')
            nemico.vita -= attackM 
            print(f'La vita del nemico è: {nemico.vita}')

            attackN = random.randint(3,10)
            print(f"'L'attacco del nemico ha fatto {attackN} danni!")
            mago.vita -= attackN
            print(f'La tua vita è: {mago.vita}')

            if nemico.vita <= 0: 
                print('Hai vinto!!!')
                break

            elif mago.vita <= 0:
                print('Sei morto!!!')
                break
        
        



def partita():
    decisione = menu()
    main(decisione) 

if __name__ == '__main__':
    partita()