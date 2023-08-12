import torch
from unbalanced_loss.focal_loss import MultiFocalLoss

batch_size, num_class = 64, 10
Loss_Func = MultiFocalLoss(num_class=num_class, gamma=2.0, reduction='mean')

logits = torch.rand(batch_size, num_class, requires_grad=True)  # (batch_size, num_classes)
targets = torch.randint(0, num_class, size=(batch_size,))  # (batch_size, )

loss = Loss_Func(logits, targets)
loss.backward()