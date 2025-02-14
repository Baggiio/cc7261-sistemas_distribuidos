import grpc
import calculadora_pb2
import calculadora_pb2_grpc

print("Cliente conectando com servidor")

porta = "50051"
endereco = "localhost"

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

print("Seleciona a operação desejada:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("0 - Sair")

operacao = int(input("Digite a operação desejada: "))
if operacao == 0:
    exit()
elif operacao in range(1, 5):
    with grpc.insecure_channel(f"{endereco}:{porta}") as channel:
        stub = calculadora_pb2_grpc.GreeterStub(channel)
        resposta = stub.Calculadora(calculadora_pb2.MsgCliente(operacao=operacao, numero1=n1, numero2=n2))
        print(f"Resposta do servidor: {resposta.resultado}")
else:
    print("Operação inválida")