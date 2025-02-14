from concurrent import futures
import grpc
import calculadora_pb2
import calculadora_pb2_grpc

class Greeter(calculadora_pb2_grpc.GreeterServicer):
    def Calculadora(self, request, context):
        print(f"Mensagem do cliente: {request.operacao}")

        n1 = request.numero1
        n2 = request.numero2

        match request.operacao:
            case 1:
                resultado = n1 + n2
            case 2:
                resultado = n1 - n2
            case 3:
                resultado = n1 * n2
            case 4:
                resultado = n1 / n2
            case _:
                resultado = 0
            
        return calculadora_pb2.MsgServidor( resultado=resultado )

endereco = "[::]:50051"
servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
calculadora_pb2_grpc.add_GreeterServicer_to_server(Greeter(), servidor)

servidor.add_insecure_port(endereco)
servidor.start()
print(f"Servidor escutando em {endereco}")
servidor.wait_for_termination()