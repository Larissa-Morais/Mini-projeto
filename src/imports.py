#todas as importações
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
import torchvision
from torchvision import transforms, datasets
from torch.utils.tensorboard import SummaryWriter

#verifica se CUDA está disponível, senão usa CPU
device = "cuda" if torch.cuda.is_available() else "cpu"
print('Device:', device)