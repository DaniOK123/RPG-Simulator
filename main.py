import random 
import time

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
   


def main():
   
    while True:
        
        utente = input("Scegli => ")

        if utente == mago.name:
            mage()
            break
        
        elif utente == guerriero.name:
            figther()
            break

        else:
            print("Scegli un personaggio tra quelli proposti!!!")
            
            


def mage():

    print(f'Combattimento tra {mago.name} e {nemico.name}')

    while True:

        if mago.vita > 0 or nemico.vita > 0:
            attackM = random.randint(3,10)
            print(f'Il tuo attacco ha fatto {attackM} danni!')
            nemico.vita -= attackM 
            print(f'La tua vita è: {mago.vita}')
            print(f'La vita del nemico è: {nemico.vita}')
            print("--------------")
            

            if nemico.vita <= 0: 
                print('Hai vinto!!!')
                break

            time.sleep(2)

            attackN = random.randint(3,10)
            print(f"L'attacco del nemico ha fatto {attackN} danni!")
            mago.vita -= attackN
            print(f'La tua vita è: {mago.vita}')
            print(f'La vita del nemico è: {nemico.vita}')
            print("--------------")
            

            if mago.vita <= 0:
                print('Sei morto!!!')
                break
        
            time.sleep(2)



def figther():
    
    print(f'Combattimento tra {guerriero.name} e {nemico.name}')

    while True:

        if guerriero.vita > 0 or nemico.vita > 0:
            attackG = random.randint(3,10)
            print(f'Il tuo attacco ha fatto {attackG} danni!')
            nemico.vita -= attackG 
            print(f'La tua vita è: {guerriero.vita}')
            print(f'La vita del nemico è: {nemico.vita}')
            print("--------------")
           

            if nemico.vita <= 0: 
                print('Hai vinto!!!')
                break

            time.sleep(2)


            attackN = random.randint(3,10)
            print(f"'L'attacco del nemico ha fatto {attackN} danni!")
            guerriero.vita -= attackN
            print(f'La tua vita è: {guerriero.vita}')
            print(f'La vita del nemico è: {nemico.vita}')
            print("--------------")
            time.sleep(2)

            if guerriero.vita <= 0:
                print('Sei morto!!!')
                break

            time.sleep(2)



def partita():
    menu()
    main() 

if __name__ == '__main__':
    partita()