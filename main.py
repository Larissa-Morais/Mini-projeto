#carregar configurações e preparar o ambiente

import yaml
from src.train import train_model
from src.imports import torch

#carrega o arquivo config
def main():
    with open("config.yaml", "r") as file:
     config = yaml.safe_load(file)

    train_model()

if __name__ == "__main__": 
    main()