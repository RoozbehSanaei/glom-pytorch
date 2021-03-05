import torch
import torch.nn.functional as F
from torch import nn, einsum

from einops import rearrange, repeat

# helpers

def exists(val):
    return val is not None

# class

class Glom(nn.Module):
    def __init__(
    	self,
    	*,
    	dim = 512,
    	layers = 6
    ):
        super().__init__()
        self.embeddings = nn.Parameter(torch.randn(layers, dim))

    def forward(self, x):
        return x
