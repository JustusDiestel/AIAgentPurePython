import torch
import torch.nn as nn
import torch.optim as optim

'''Das hier macht noch keinen Sinn weil wir keine Daten zum lernen haben, hier am besten Reinforced learning um im nachhinein zu prüfen 
    ob die empfehlung was getaugt hat'''


class TradingNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.l1 = nn.Linear(2, 16)
        self.l2 = nn.Linear(16,3)

    def forward(self,x):
        x = torch.relu(self.l1(x))
        x = torch.softmax(self.l2(x), dim=1)
        return x

