# 🧠 CNN - FashionMNIST

Este projeto implementa uma **rede neural convolucional (CNN)** para classificar imagens do dataset **FashionMNIST**, utilizando **PyTorch**.  
O objetivo é demonstrar um fluxo completo de Machine Learning — desde o carregamento dos dados até o treinamento e avaliação do modelo.

---

## 📁 Estrutura do Projeto

projeto/
├── data/ # Dados brutos e processados
│ ├── raw/
│ └── processed/
├── src/ # Código-fonte principal
│ ├── dataset.py # Carregamento e pré-processamento dos dados
│ ├── model.py # Definição da CNN
│ ├── train.py # Loop de treinamento e validação
│ ├── utils.py # Funções auxiliares
├── outputs/ # Resultados do modelo
│ ├── checkpoints/ # Pesos salvos
│ └── logs/ # Logs de execução
├── config.yaml # Arquivo de configuração
├── main.py # Script principal
└── requirements.txt # Dependências do projeto
---

## ⚙️ Requisitos

Antes de rodar, instale as dependências:

```bash
pip install -r requirements.txt

🚀 Execução

Para treinar o modelo, execute:
```bash
python main.py

Os logs de treinamento serão salvos automaticamente na pasta runs/ para visualização com o TensorBoard:
```bash
tensorboard --logdir=runs

🧩 Tecnologias Utilizadas

Python 3.10+

PyTorch

Torchvision

TensorBoard

PyYAML

## 📊 Resultados Esperados

Após o treinamento, o modelo alcançou uma **acurácia superior a 90%** no conjunto de teste, mostrando boa capacidade de generalização no dataset FashionMNIST.

🧑‍💻 Autoria

Desenvolvido por Larissa Silva de Morais Batista