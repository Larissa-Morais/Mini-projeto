#carregamento e pré-processamento de dados

#importações necessárias
from src.imports import transforms, datasets, DataLoader

#definição das transformações e carregamento dos datasets
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])
#carregamento dos datasets FashionMNIST
trainset = datasets.FashionMNIST(root='./data', train=True, download=True, transform=transform)
testset = datasets.FashionMNIST(root='./data', train=False, download=True, transform=transform)

trainloader = DataLoader(trainset, batch_size=128, shuffle=True, num_workers=2)
testloader = DataLoader(testset, batch_size=128, shuffle=False, num_workers=2)

print('Train size(tamanho do conjunto de treino):', len(trainset), 'Test size(tamanho do conjunto de teste):', len(testset))