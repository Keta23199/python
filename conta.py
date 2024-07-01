def cria_conta(numero, titular, saldo, limite):
    conta={"numero": numero,"titular": titular,"saldo":saldo,"limite":limite
}
    return conta

def saldo(conta):
    print("conta numero:{}".format(conta["numero"]))

conta00= cria_conta(1234, "Ketlin", 50.0, 100.0)
conta01= cria_conta(4321, "bolett", 50.0, 100.0)
saldo(conta00)
saldo(conta01)
