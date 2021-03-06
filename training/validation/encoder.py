import torch.nn as nn

class AutoEncoder(nn.Module):
    def __init__(self, dataset):
        self._loss_func = nn.MSELoss
        self._dataset = dataset
        self._img_size = 28 if dataset == 'mnist' else 32
        super(AutoEncoder, self).__init__()

        self.encoder = nn.Sequential(
            nn.Linear(self._img_size**2, 128),
            nn.Tanh(),
            nn.Linear(128, 64),
            nn.Tanh(),
            nn.Linear(64, 12),
            nn.Tanh(),
            nn.Linear(12, 3),   # compress to 3 features which can be visualized in plt
        )
        self.decoder = nn.Sequential(
            nn.Linear(3, 12),
            nn.Tanh(),
            nn.Linear(12, 64),
            nn.Tanh(),
            nn.Linear(64, 128),
            nn.Tanh(),
            nn.Linear(128, 28*28),
            nn.Sigmoid(),       # compress to a range (0, 1)
        )

    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return encoded, decoded

