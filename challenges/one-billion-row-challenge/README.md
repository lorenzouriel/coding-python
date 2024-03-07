# Um Bilhão de Linhas: Desafio de Processamento de Dados com Python

## Introdução

O objetivo deste projeto é demonstrar como processar eficientemente um arquivo de dados massivo contendo 1 bilhão de linhas (~14GB), especificamente para calcular estatísticas (Incluindo agregação e ordenação que são operações pesadas) utilizando Python.

Este desafio foi inspirado no [The One Billion Row Challenge](https://github.com/gunnarmorling/1brc), originalmente proposto para Java.

E eu conheci o mesmo e me inspirei atráves do [Luciano Galvão](https://github.com/lvgalvao/One-Billion-Row-Challenge-Python/tree/main?tab=readme-ov-file)

O arquivo de dados consiste em medições de temperatura de várias estações meteorológicas. Cada registro segue o formato <string: nome da estação>;<double: medição>, com a temperatura sendo apresentada com precisão de uma casa decimal.

Aqui estão dez linhas de exemplo do arquivo:
```
Hamburg;12.0
Bulawayo;8.9
Palembang;38.8
St. Johns;15.2
Cracow;12.6
Bridgetown;26.9
Istanbul;6.2
Roseau;34.4
Conakry;31.2
Istanbul;23.0
```

O desafio é desenvolver um programa Python capaz de ler esse arquivo e calcular a temperatura mínima, média (arredondada para uma casa decimal) e máxima para cada estação, exibindo os resultados em uma tabela ordenada por nome da estação.


| station      | min_temperature | mean_temperature | max_temperature |
|--------------|-----------------|------------------|-----------------|
| Abha         | -31.1           | 18.0             | 66.5            |
| Abidjan      | -25.9           | 26.0             | 74.6            |
| Abéché       | -19.8           | 29.4             | 79.9            |
| Accra        | -24.8           | 26.4             | 76.3            |
| Addis Ababa  | -31.8           | 16.0             | 63.9            |
| Adelaide     | -31.8           | 17.3             | 71.5            |
| Aden         | -19.6           | 29.1             | 78.3            |
| Ahvaz        | -24.0           | 25.4             | 72.6            |
| Albuquerque  | -35.0           | 14.0             | 61.9            |
| Alexandra    | -40.1           | 11.0             | 67.9            |
| ...          | ...             | ...              | ...             |
| Yangon       | -23.6           | 27.5             | 77.3            |
| Yaoundé      | -26.2           | 23.8             | 73.4            |
| Yellowknife  | -53.4           | -4.3             | 46.7            |
| Yerevan      | -38.6           | 12.4             | 62.8            |
| Yinchuan     | -45.2           | 9.0              | 56.9            |
| Zagreb       | -39.2           | 10.7             | 58.1            |
| Zanzibar City| -26.5           | 26.0             | 75.2            |
| Zürich       | -42.0           | 9.3              | 63.6            |
| Ürümqi       | -42.1           | 7.4              | 56.7            |
| İzmir        | -34.4           | 17.9             | 67.9            |

## Dependências

Para executar os scripts deste projeto, instale as dependências:
```
pip install -r requirements.txt
```

## Meus Resultados
Os testes foram realizados em um notebook Acer, 16 GB RAM e SSD de 500 GB. As implementações utilizaram abordagens puramente Python, Pandas, Dask, Polars e DuckDB. 

Os resultados de tempo de execução para processar o arquivo de 1 bilhão de linhas são apresentados abaixo:

| Implementação | Tempo |
| --- | --- |
| Bash + awk | +30 minutos |
| Python | +30 minutos |
| Python + Pandas | 955.75 sec |
| Python + Dask | sec |
| Python + Polars | 244.60 sec |
| Python + Duckdb | 175.26 sec |

## Como Executar

Para executar este projeto e reproduzir os resultados:

1. Clone esse repositório
2. Definir a versao do Python usando o `pyenv local 3.12.1`
2. `poetry env use 3.12.1`, `poetry install --no-root` e `poetry lock --no-update`
3. Execute o comando `python src/create_measurements.py` para gerar o arquivo de teste
4. Tenha paciência e vá fazer um café, vai demorar uns 10 minutos para gerar o arquivo
5. Certifique-se de instalar as versões especificadas das bibliotecas Dask, Polars e DuckDB
6. Execute os scripts `python src/using_python.py`, `python src/using_pandas.py`, `python src/using_dask.py`, `python src/using_polars.py` e `python src/using_duckdb.py` através de um terminal ou ambiente de desenvolvimento que suporte Python.

Este projeto destaca a versatilidade do ecossistema Python para tarefas de processamento de dados, oferecendo valiosas lições sobre escolha de ferramentas para análises em grande escala.

## Agradecimentos e Recomendação

Eu descobri esse desafio atráves do bootcamp do [Luciano Vasconcelos Filho](https://www.linkedin.com/in/lucianovasconcelosf/), recomendo o bootcamp para todos que desejam aprender mais sobre Python e Data Engineering.

E esse é o [repositório](https://github.com/lvgalvao/One-Billion-Row-Challenge-Python) dele com os desafios 
