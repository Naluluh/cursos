from concurrent import futures
import grpc
import calcula_pb2
import calcula_pb2_grpc

def soma(a: int, b: int) -> int:
    return a + b

class CalcularService(calcula_pb2_grpc.CalcularServiceServicer):
    def Somar(self, request, context):
        resultado = soma(request.x, request.y)
        print("Calculando soma requisitada...")
        return calcula_pb2.resposta(res=resultado)

def main():
    servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calcula_pb2_grpc.add_CalcularServiceServicer_to_server(CalcularService(), servidor)
    servidor.add_insecure_port("[::]:50004")
    print("Servidor escutando na porta 50004")
    servidor.start()
    servidor.wait_for_termination()
if __name__ == "__main__":
    main()