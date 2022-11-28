from ipdb import set_trace
from rest_framework.views import APIView, Response

from .models import Clientes
from .serializers import CNABSerializer


class ConversorCNAB(APIView):

    def get(self, request):
        lista = Clientes.objects.all()
        serializer = CNABSerializer(lista, many=True)
        return Response(serializer.data)

    def post(self, request):
        dados_do_cliente = request.FILES["file"]
        

        linhas = dados_do_cliente.readlines()

        for linha in linhas:

            tipo_convertido = linha.decode("utf-8")[0:1]
            natureza = "Entrada"
            sinal = "+"

            if (tipo_convertido == "1"):
                tipo_convertido = "Débito"

            if (tipo_convertido == "2"):
                natureza = "Saída"
                sinal = "-"
                tipo_convertido = "Boleto"

            if (tipo_convertido == "3"):
                natureza = "Saída"
                sinal = "-"
                tipo_convertido = "Financiamento"

            if (tipo_convertido == "4"):
                tipo_convertido = "Crédito"

            if (tipo_convertido == "5"):
                tipo_convertido = "Recebimento Empréstimo"

            if (tipo_convertido == "6"):
                tipo_convertido = "Vendas"

            if (tipo_convertido == "7"):
                tipo_convertido = "Recebimento TED"

            if (tipo_convertido == "8"):
                tipo_convertido = "Recebimento DOC"

            if (tipo_convertido == "9"):
                natureza = "Saída"
                sinal = "-"
                tipo_convertido = "Aluguel"

            data_convertida = linha.decode("utf-8")[1:9]
            data_formatada = f"{data_convertida[6:8]}/{data_convertida[4:6]}/{data_convertida[0:4]}"
            valor_convertido = linha.decode("utf-8")[9:19]
            valor_formatado = int(valor_convertido)/100.00
            cpf_convertido = linha.decode("utf-8")[19:30]
            cartao_convertido = linha.decode("utf-8")[30:42]
            hora_convertida = linha.decode("utf-8")[42:48]
            hora_formatada = f"{hora_convertida[0:2]}:{hora_convertida[2:4]}:{hora_convertida[4:6]}"
            dono_nome_convertido = linha.decode("utf-8")[48:62]
            nome_loja_convertida = linha.decode("utf-8")[62:81]

            data_clientes_convertida = {"tipo": tipo_convertido, "data": data_formatada,"valor": valor_formatado, 
                                  "cpf": cpf_convertido,"cartao": cartao_convertido, "hora": hora_formatada,
                                  "dono_nome": dono_nome_convertido, "nome_loja": nome_loja_convertida,"natureza": natureza, 
                                  "sinal": sinal}

           
            Serializer = CNABSerializer(data=data_clientes_convertida)
            Serializer.is_valid(raise_exception=True)
            Serializer.save()

        return Response({"mensagen": "sucesso dados foram colocados no banco"})
