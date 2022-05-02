class ContaBancaria:

    def __init__(self, n_conta, n_agencia, saldo):
        self.n_conta = n_conta
        self.n_agencia = n_agencia
        self.saldo = saldo

    def __str__(self):
         return f'Ag:{self.n_agencia}, conta:{self.n_conta}, saldo:{self.saldo}'

    def deposito(self, valor):
        if valor <= 0:
            print(f'Valor inválido para depósito!')
            return 
        
        self.saldo+=valor
    
    def saque(self, retirada):
        if retirada<0:
            print(f'Valor invalido para saque')
            return
        elif retirada>self.saldo:
            print(f'Saldo insuficiente na conta')
            return
        
        self.saldo -= retirada;
        

        
    def mesma_agencia(self, outra):
        if self.n_agencia == outra.n_agencia:
            print(f'Contas {self.n_conta} e {outra.n_conta} são da mesma agência')
        else:
            print(f'Contas {self.n_conta} e {outra.n_conta}'
                   ' não são da mesma agência')
        
def main():
    c1 = ContaBancaria(100, 2, 1000.0)
    c2 = ContaBancaria(200, 8, 500.0)
    c3 = ContaBancaria(300, 2, 2000.0)

    c1.deposito(-5) # valor inválido para depósito
    c1.saque(-5) # valor inválido para saque
    print(c1)

    c1.deposito(100)
    c1.saque(1200) # saldo insuficiente
    c1.saque(600)
    print(c1)

    c1.mesma_agencia(c2) # não têm mesma agência
    c1.mesma_agencia(c3) # têm mesma agência

if __name__ == '__main__':
    main()
