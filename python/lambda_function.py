# -*- coding: utf-8 -*-
import json
import requests

def lambda_handler(event, context):
    # URL da API Go para onde os dados serão enviados.
    api_url = "http://192.168.0.101:5000/receptor"
    
    # Exemplo de objeto JSON que será enviado para a API Go
    payload = {
        "id_credito": "01JBCNGYZWDVMYN7NQ3QPGT6FGJOAOMARIA",
        "id_produto": "00129",
        "id_cliente": "12345",
        "eventos": [
            {
                "id_evento": "SK1",
                "descricao": "Solicitação de crédito recebida",
                "data": "2024-01-01",
                "status": "Processado"
            },
            {
                "id_evento": "SK2",
                "descricao": "Análise de crédito em andamento",
                "data": "2024-01-02",
                "status": "Processado"
            },
            {
                "id_evento": "SK3",
                "descricao": "Crédito aprovado",
                "data": "2024-01-03",
                "status": "Processado"
            },
            {
                "id_evento": "SK4",
                "descricao": "Documentação verificada",
                "data": "2024-01-04",
                "status": "Processado"
            },
            {
                "id_evento": "SK5",
                "descricao": "Crédito liberado",
                "data": "2024-01-05",
                "status": "Processado"
            }
        ]
    }
    
    # Definir os headers da requisição
    headers = {
        'Content-Type': 'application/json'
    }
    
    # Enviando o payload JSON via POST para a API Go
    try:
        print("Enviando dados para a API Go:", payload)  # Debug: Imprime o payload que está sendo enviado
        
        response = requests.post(api_url, data=json.dumps(payload), headers=headers)
        
        # Verifica o status da resposta
        print("Código de status da resposta:", response.status_code)  # Debug: Imprime o código de status da resposta
        
        if response.status_code == 200:
            print("Resposta bem-sucedida!")  # Debug: Imprime uma mensagem de sucesso
            return {
                'statusCode': 200,
                'body': json.dumps('Dados enviados com sucesso!')
            }
        else:
            print("Erro ao enviar os dados:", response.text)  # Debug: Imprime o erro ao enviar os dados
            return {
                'statusCode': response.status_code,
                'body': json.dumps(f"Erro ao enviar os dados: {response.text}")
            }
    except Exception as e:
        print("Erro de execução:", str(e))  # Debug: Imprime a exceção capturada
        return {
            'statusCode': 500,
            'body': json.dumps(f"Erro de execução: {str(e)}")
        }

# Simulando a execução local
if __name__ == "__main__":
    event = {}  # Você pode personalizar esse evento de teste
    context = None
    result = lambda_handler(event, context)
    print("Resultado da execução da Lambda:", result)
