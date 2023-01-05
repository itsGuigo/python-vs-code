#este agente soft para retornar o pagamento com parcela iguais
#atraves da entrada: pagamento a vista ou emprestimo
#ou numero de meses
#valor de juro (ou taxa do banco)

#um subprograma para mensagens de abertura
import string

def mensagens():
    print("*******************************************")
    print("Bem vindo ao Sistema de Financeiro")
    print("*******************************************")
    
#subprograma (função) para calcular o termo comum
def formulaComum(N_mes, taxa) : #(1+1)^n
    Resultado = 1.0 #uma variavel como acumulador
    expressao = 1 + taxa/100 # -> (1+i)
    for i in range (N_mes) :
        Resultado *= expressao # Resultado = Resultado * expressao
    return Resultado

#um subprograma (função) para calcular parcelamento igual
def calcularParcelamentos(Pgavista, termo,taxa) :
    par_iguais = Pgavista * ((termo*taxa/100)/(termo-1))
    return par_iguais

#um subprograma (procedimento) para mostrar resultado
def mostrarResultado(par_iguais,N_mes,Pgavista) :
    print(f"As parcelas iguais será R$ {par_iguais:.2f}")
    total_pago = par_iguais*N_mes
    print(f"O valor total será pago R$ {total_pago:.2f}")
    juro_pago = total_pago - Pgavista
    print(f"O juro será pago R$ {juro_pago:.2f}")
    
#programa principal
mensagens()

#entrada de dados
Pgavista = float(input("Informe o valor emprestimo ou pagamento a vista R$ "))
N_mes = int(input("Digite quantos meses gostaria de pagar: "))
taxa = float(input("Informe qual é a taxa por mês (%) "))

#operações de calculos
termo = formulaComum(N_mes,taxa)
parcelamentosIguais = calcularParcelamentos(Pgavista,termo,taxa)

#mostrar os resultados
mostrarResultado(parcelamentosIguais,N_mes,Pgavista)
print("Finalizando o programa!!")