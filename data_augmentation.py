import torch
import torchvision


'''
v2.Compose(transforms)
Composes several transforms together.

v2.RandomApply(transforms[, p])
Apply randomly a list of transformations with a given probability.

v2.RandomChoice(transforms[, p])
Apply single transformation randomly picked from a list.

v2.RandomOrder(transforms)
Apply a list of transformations in a random order.
'''

transforms = torchvision.transforms.v2.Compose([
    torchvision.transforms.RandomHorizontalFlip(),
    torchvision.transforms.RandomVerticalFlip(),
    torchvision.transforms.RandomRotation(180)
])


#out_img, out_mask = transforms(img, mask)
#plot([(img, mask), (out_img, out_mask)])
dataset = torchvision.datasets.ImageFolder('pytorch-examples/data/', transform=transforms)