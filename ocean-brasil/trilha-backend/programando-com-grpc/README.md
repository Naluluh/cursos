# Exemplo de gRPC em Python: Soma

Projeto de estudo que mostra o básico do gRPC: um cliente envia dois números para um servidor, que devolve a soma. Tudo roda localmente, em dois terminais.

## Arquivos

| Arquivo | Função |
|---|---|
| `calcula.proto` | Define o serviço e as mensagens (contrato entre cliente e servidor) |
| `servidor.py` | Implementa o serviço e fica aguardando chamadas |
| `cliente.py` | Faz a chamada remota e mostra o resultado |

## Requisitos

- Python 3.8 ou superior
- `grpcio` e `grpcio-tools`

```bash
pip install grpcio grpcio-tools
```

## Como rodar

1. Gere o código Python a partir do arquivo `.proto`:

   ```bash
   python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calcula.proto
   ```

   Isso cria os arquivos `calcula_pb2.py` e `calcula_pb2_grpc.py`.

2. No **terminal 1**, inicie o servidor:

   ```bash
   python servidor.py
   ```

3. No **terminal 2**, execute o cliente:

   ```bash
   python cliente.py
   ```

O cliente deve exibir o resultado da soma.

## Como funciona

1. O `.proto` descreve o serviço (`Calcula`) e o formato das mensagens de entrada e saída.
2. O `protoc` gera as classes Python usadas pelo cliente e pelo servidor.
3. O servidor registra a implementação do serviço e escuta em `localhost`.
4. O cliente abre um canal até o servidor, chama o método como se fosse uma função local e recebe a resposta.

## Observações

- O exemplo usa conexão sem criptografia (`insecure_channel`), adequada apenas para estudo local. Em produção, use TLS.
- Os endereços e portas são locais (`localhost`); ajuste no código se precisar mudar.

## Objetivo

Subdiretório criado para fins de aprendizado de gRPC.
