g as _
import time
import _thread as a
class banco():
    def __init__(self,saldo=0):
        self.saldo=saldo

    def transferencia1(self,conta,numero,lock):

        if numero < conta1.saldo:
            lock.acquire()
            self.saldo -= numero
            conta.saldo += numero
            print('saldo1: ',self.saldo)
            print('saldo2: ',conta.saldo)
            lock.release()

    def transferencia2(self, conta, numero, lock):

        if numero < conta2.saldo:
            lock.acquire()
            self.saldo -= numero
            conta.saldo += numero
            print('saldo conta2: ', self.saldo)
            print('saldo conta1: ', conta.saldo)
            lock.release()
    def zero1 (self,conta,lock):
        lock.acquire()
        self.saldo -= 1
        conta.saldo += 1
        print('conta1: ', self.saldo,'     ','conta2: ',conta.saldo)
        lock.release()
    def zero2 (self,conta,lock):
        lock.acquire()
        self.saldo -= 1
        conta.saldo += 1
        print('conta2: ', self.saldo, '     ', 'conta1: ', conta.saldo)
        lock.release()


if __name__ == '__main__':
    lock = a.allocate_lock()
    thread_list = []
    conta1 = banco(100)
    conta2 = banco(100)

    while True:
        print('digite 0 para sair ')
        print('digite 3 para zera conta\ndigite 4 para zera conta 2')
        opçao = int(input('digite a conta a qual sera feita a transferencia 1 ou 2 : '))
        if opcao == 0 :
            break
        if opcao == 1:
            while True:
                time.sleep(0.4)
                print('saldo atual da conta :',conta1.saldo)
                numero = int(input('digite o valor a ser transferido :  '))
                thread=_.Thread(target=conta1.transferencia1,args=(conta2, numero, lock))
                thread_list.append(thread)
                thread.start()
                time.sleep(0.2)
                c=int(input('deseja continua a operacao?(1 para sim /npara nao ) '))
                if numero>conta1.saldo:
                    exit('error \nsaldo insuficiente ')
                if c != 1:
                    break
        if opcao == 2:
            while True:
                time.sleep(0.4)
                print('saldo atual da conta :', conta2.saldo)
                numero = int(input('digite o valor a ser transferido :  '))
                thread = _.Thread(target=conta2.transferencia2, args=(conta1, numero, lock))
                thread_list.append(thread)
                thread.start()
                time.sleep(0.2)
                c = int(input('deseja continua a operacao?(1 para sim /n2para nao ) '))
                if numero > conta2.saldo:
                    exit('error \nsaldo insuficiente ')
                if c != 1:
                    break
        if opcao == 3:
            while True:
                thread = _.Thread(target=conta1.zero1, args=(conta2, lock))
                thread_list.append(thread)
                thread.start()
                time.sleep(0.07)
                if conta1.saldo == 0:
                    break
        if opcao == 4:
            while True:
                thread = _.Thread(target=conta2.zero2, args=(conta1, lock))
                thread_list.append(thread)
                thread.start()
                time.sleep(0.07)
                if conta2.saldo == 0:
                    break
