import torch
import numpy as np
a = torch.FloatTensor(3,2)

a.zero_()
print(a)

n = np.zeros(shape = (3,2), dtype = np.float16)
n_tensor = torch.tensor(n)
print(n_tensor)

a = torch.tensor([1,2,3])
print(a)
s = a.sum()
print(s)
print(s.item())

torch.tensor(1)

v1 = torch.tensor([1.0,1.0], requires_grad=True)
v2 = torch.tensor([2.0,2.0])

v_sum = v1+ v2
v_res = (v_sum * 2).sum()
print(v_res)
v_res.backward()
print(v1.grad)

import torch.nn as nn
l = nn.Linear(2,5)
v = torch.FloatTensor([1,2])
print(l(v))