# Algoritmo de Recomendação Musical com Grafos

Este projeto apresenta um sistema de recomendação baseado na estrutura de dados de grafos, 
conectando usuarios e suas preferencias musicais para sugerir novos conteudos.

## Estrutura de Pastas

* data: Contem o arquivo setup_grafo.cypher com os comandos para o banco de dados Neo4j.
* docs: Armazena a representacao visual do grafo de recomendacao.
* notebooks: Espaco destinado a testes preliminares e prototipos.
* scr: Contem o codigo fonte principal (main.py) em Python.

## Tecnologias Utilizadas

* Linguagem Python para a logica de recomendacao.
* Biblioteca NetworkX para manipulacao de grafos.
* Linguagem Cypher para estruturacao no banco de dados Neo4j.

## Como Funciona

O sistema utiliza o conceito de filtragem colaborativa baseada em grafos. Ele identifica usuarios 
que possuem gostos em comum (ouviram as mesmas musicas) e sugere musicas que esses "vizinhos" 
gostaram, mas que o usuario alvo ainda nao conhece.

