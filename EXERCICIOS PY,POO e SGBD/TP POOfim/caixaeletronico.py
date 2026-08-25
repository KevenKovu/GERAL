from Banco.contas import*
import os
if __name__== "__main__":
    listaCarteiras = []
    while True:
        print("Bem-vindo ao Bank POOdle \U0001F916 \n")
        print("(1) Cadastrar uma nova carteira \U0001F4AB")
        print("(2) Listar as contas de uma carteira existente \U0001F440")
        print("(3) Sair do programa \U0001F6B6 \n")
        opcao = int (input("Informe a opção desejada\U0001F432: "))

        if opcao==1:
            inv= input("Qual o tipo de investimento? \U0001F432	")
            car = Carteira(inv)
            resposta =input("Deseja cadastrar uma conta? (s/n)\U0001F916 ")
            while (resposta =="s"):
                num =input("Informe o numero daconta\U0001F916: ")
                tit = input("Informe o nome do titular \U0001F916: ")
                sld = float(input("Qual o valor do saldo iniacial?\U0001F4B0"))
                tip = input("Conta Normal(N), Conta Corrente (C) ou Conta Poupança(P)?\U0001F4BC")
                if tip =="N":
                    car.addConta (Conta(num,tit,sld))
                elif tip=="C":
                    car.addConta (ContaCorrente(num,tit,sld))
                else:
                    ren =float(input("Qual o rendimento mensal?\U0001F9FE	"))
                    car.addConta (ContaPoupanca(num,tit,sld))
                resposta =input("Deseja cadastrar uma conta? (s/n) \U0001F4BC")

            listaCarteiras+= [car]
            print(f"Cadastro da carteira {inv} realizado com sucesso!=)\U0001F973 \n")
        elif opcao==2:
            inv=input("Informe o investimento desejado: \U0001F4C8	")
            achou=False
            for carteirinha in listaCarteiras:
                if carteirinha.investimento ==inv:
                    achou=True
                    if carteirinha.listaContas == []:
                        print("Essa carteira " + inv+ " não possui contas cadastradas!\U0001F612		\n")
                    else:
                        for continha in carteirinha.listaContas:
                            print(continha.retornaDados())
            if not achou:
                print("Não existe carteira do tipo informado!\U0001F612	")
            print("\n")
        elif opcao==3:
            break
        else:
            print("Opção inválida! \U0001F62C	\n")
        input()
        os.system("cls" if os.name == "nt" else "clear")
    print("Volte sempre ao Bank POOdle\U0001FAE1	")
    
