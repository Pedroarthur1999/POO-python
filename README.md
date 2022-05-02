# POO-python

## Prática 1.1 - Classe `ContaBancaria`

Considere a classe `ContaBancaria`, para representar uma conta em um banco.

Todo objeto da classe `ContaBancaria` deve ter como atributos:
- O número da conta
- O número da agência
- O saldo em reais na conta

Como comportamento, toda `ContaBancaria` deve conter:
- Um método para realizar um `deposito`, que recebe a quantia a ser depositada como parâmetro. Este método deve checar se o valor passado como parâmetro é válido (maior do que 0) e caso não seja, deve imprimir a mensagem `Valor inválido para depósito.`.
- Um método para realizar um `saque`, que recebe a quantia a ser sacada como parâmetro. Este método deve checar se o valor passado como parâmetro é válido (maior do que 0) e caso não seja, deve imprimir a mensagem `Valor inválido para saque.` Além disso, o método também deve checar se há saldo suficiente na conta e caso não haja, imprimir a mensagem `Saldo insuficiente na conta.`
- Um método chamado `mesma_agencia`, que recebe um objeto `ContaBancaria` como parâmetro. Este método deve imprimir uma mensagem informando se a conta que chamou o método e a conta contida no parâmetro fazem parte da mesma agência ou não
- O método especial `__str__` para imprimir o objeto `ContaBancaria` no formato `Ag: X, conta: Y, saldo: Z`

Utilize o código a seguir para testar o seu programa e observe a saída esperada.

Saída esperada:

```
Valor para depósito inválido.
Valor inválido para saque.
Ag: 2, conta: 100, saldo: R$1000.00
Saldo insuficiente na conta.
Ag: 2, conta: 100, saldo: R$500.00
Contas 100 e 200 não são da mesma agência
Contas 100 e 300 são da mesma agência
```
