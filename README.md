# Script Python para exportar dados de estabelecimentos do Google Maps
Este script Python utiliza a API do Google Maps para extrair informações de estabelecimentos a partir de uma lista de endereços e exportá-los em um arquivo CSV. As informações extraídas incluem o nome, endereço, telefone, avaliação e comentários do estabelecimento.

## Requisitos
Antes de utilizar este script, é necessário ter uma chave de API do Google Maps. Você pode obter uma chave gratuitamente na página de desenvolvedores do Google Maps.

## Como usar
Clone este repositório ou faça o download do script google_maps_api.py.

Crie um arquivo .env na mesma pasta do script Python e adicione a variável API_GOOGLE_MAPS com o valor da sua chave de API do Google Maps:

```
API_GOOGLE_MAPS=SUA_CHAVE_DE_API
```

Abra o terminal ou prompt de comando e navegue até a pasta do script Python.

Execute o seguinte comando para instalar as dependências necessárias:

```
pip install googlemaps python-dotenv
```
Edite a lista enderecos no script Python com os endereços dos estabelecimentos que você deseja extrair informações.

Execute o script Python com o seguinte comando:

```
python reviews.py
```
O script irá extrair as informações dos estabelecimentos e salvá-las em um arquivo CSV chamado estabelecimentos.csv na mesma pasta do script Python.

## Como funciona
O script utiliza a biblioteca googlemaps para acessar a API do Google Maps. Primeiro, ele extrai o Place ID de cada endereço na lista enderecos fazendo uma requisição à API do Google Maps. Em seguida, ele utiliza o Place ID para fazer uma nova requisição à API do Google Maps para buscar as informações do estabelecimento, incluindo as avaliações. O script então extrai os dados do estabelecimento, incluindo o nome, endereço, telefone, avaliação e comentários, e os salva em um arquivo CSV.

O script também utiliza a biblioteca python-dotenv para carregar a chave de API do Google Maps a partir do arquivo .env.

# Observações
Este script é apenas um exemplo e pode ser adaptado para atender às suas necessidades específicas. Respeite os Termos de Serviço da API do Google Maps.