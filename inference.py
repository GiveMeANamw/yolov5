import torch
from torch.utils import tensorboard

print(torch.__version__)
print(torch.cuda.is_available())
print(torch.backends.cudnn.is_available())
print(torch.cuda_version)
print(torch.backends.cudnn.version())
print(tensorboard.__version__)