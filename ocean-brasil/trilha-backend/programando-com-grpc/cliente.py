import grpc
import calcula_pb2
import calcula_pb2_grpc

def main():
    canal = grpc.insecure_channel("localhost:50004")
    stub = calcula_pb2_grpc.CalcularServiceStub(canal)
    a = int(input("x: "))
    b = int(input("y: "))
    r = calcula_pb2.operandos(x=a, y=b)
    resp = stub.Somar(r)
    print(f"{a}+{b} = {resp.res}")

if __name__ == "__main__":
    main()