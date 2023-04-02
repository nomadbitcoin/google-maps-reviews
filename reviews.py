import googlemaps
import csv
from dotenv import load_dotenv
import os

# carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# lista de enderecos dos estabelecimentos
enderecos = [
    'Vila D\'Água, Santa Catarina, Brasil'
    ]

# cabeçalhos para o arquivo CSV
headers = ['Nome', 'Endereço', 'Telefone', 'Avaliação', 'Comentário', 'Autor do comentário']

# criar um cliente para acessar a API do Google Places
client = googlemaps.Client(os.getenv('API_GOOGLE_MAPS'))

# criar um arquivo CSV e escrever os cabeçalhos
with open('estabelecimentos.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()

    # percorrer a lista de enderecos e extrair os dados de cada um
    for endereco in enderecos:
        # extrair o Place ID da URL
        # fazer uma requisição à API do Google Maps para buscar o Place ID
        resultado = client.find_place(
            input=endereco,
            input_type='textquery',
            fields=['place_id']
        )

        # extrair o Place ID do resultado da API
        place_id = resultado['candidates'][0]['place_id']

        # fazer uma requisição à API do Google Places para buscar as informações do lugar, incluindo as avaliações
        place = client.place(place_id, fields=['name', 'formatted_address', 'formatted_phone_number', 'rating', 'reviews'], language='pt-BR')['result']

        # extrair os dados do estabelecimento
        nome = place['name']
        endereco = place['formatted_address']
        telefone = place['formatted_phone_number'] if 'formatted_phone_number' in place else ''
        avaliacao = place['rating'] if 'rating' in place else ''

        # extrair os comentários das avaliações
        comentarios = []
        autores = []
        if 'reviews' in place:
            for review in place['reviews']:
                comentario = review['text']
                comentarios.append(comentario)

                autor = review['author_name']
                autores.append(autor)

        # escrever os dados no arquivo CSV
        writer.writerow({'Nome': nome, 'Endereço': endereco, 'Telefone': telefone, 'Avaliação': avaliacao, 'Comentário': comentarios, 'Autor do comentário': autores})
