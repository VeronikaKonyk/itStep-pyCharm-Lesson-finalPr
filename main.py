import logging
import random

try:
    logging.basicConfig(
        level=logging.DEBUG,
        filename='testlog.log',
        filemode='w',
        format='%(message)s'
    )


    class Power:
        def __init__(self):
            self.energy = 120

        def consume_energy(self, amount):
            self.energy -= amount
            if self.energy < 0:
                self.energy = 0


    class Bee(Power):
        def __init__(self):
            super().__init__()
            self.flights = 0
            self.food = 0
            self.beauty = 0

        def fly(self):
            logging.debug('Flying...')
            self.flights += 1
            self.food += random.randint(1, 5)
            self.beauty += random.randint(1, 3)
            self.consume_energy(10)

        def dance(self):
            logging.debug('Dancing...')
            self.food -= random.randint(1, 3)
            self.beauty += random.randint(1, 2)
            self.consume_energy(5)

        def live_a_day(self, day):
            logging.info('''          
                            | \ | |                   | |            
                            |  \| |                   | | 
                            | . ` |/ _ \ \ /\ / /  / _` |/ _` | | | |
                            | |\  |  __/\ V  V /  | (_| | (_| | |_| |
                            |_| \_|\___| \_/\_/    \__,_|\__,_|\__, |
                                                                __/ |
                                                               |___/ 
                    ''')
            logging.debug(f'Day {day}:')
            self.fly()
            if self.energy > 0:
                self.fly()
                if self.food >= 10:
                    self.dance()
                self.status()
            else:
                logging.critical('Bee has died due to lack of energy.')


        def status(self):
            logging.debug(f'Flights: {self.flights}')
            logging.debug(f'Food: {self.food}')
            logging.debug(f'Beauty: {self.beauty}')
            logging.debug(f'Energy: {self.energy}')
            logging.debug('''                                             

                    ------:                      
                  ==      -+                     
                :+         =.                    
                #           .                    
                *          .=      .-----==      
                +.         :=    -=-       :     
                 +:        =:  -=.          :    
                  ==       * .+:            *    
                   .=-    .+==             --    
          .==++++-=+++*==:**.             -=     
         ++-=+-----------@@%+.        .-==.      
        *=--------------+@@@*=##------:          
        #---------------%@@@---@@=               
        *=-------------#@@@+--+@@@*              
         =+=---------=%@@@*--=@@@%=-             
           .-=:-:==+#@@@@+--=@@@@=-:             
                 .:=*%@*--=*@@@@=-=+             
                       -=*@@@@*--++              
                           .:----.               

         ''')


    bee = Bee()
    for day in range(1, 9):
        bee.live_a_day(day)


except ImportError:
    print("Помилка: Модуль не існує.")
except NameError:
    print("Помилка: Змінна не визначена.")
except ValueError:
    print("Помилка: Щось не то з числами.")
except IndexError:
    print("Помилка!")
