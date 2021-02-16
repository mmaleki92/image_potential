# neural network potentials
When we want to take advantage of a neural network to construct a potential energy surface (how atoms see their neighbors! and interact with them), we should consider the physical system symmetries. We already know that we should take translation, rotation, permutation, and reflection symmetry for a problem such as potential energy into account. People already did different works for tackling these symmetry things. Still, the problem is already out there (and that is the reason why we every day see a lot of creative ways of representing molecular configurations for machine learning).

## image method

We will start with the image representation of an atomistic environment, implemented in the Ryczko et al article 
[[1]](#1). in order to convert atomistic systems to image, one can use this code:


```python
import numpy as np

a = 5
num = 2
pos_x = np.random.rand(num)
pos_y = np.random.rand(num)

grid = 256
points = np.linspace(0, a, grid)

pos_x,pos_y

X, Y = np.meshgrid(points, points)
image = np.zeros((grid, grid))

for p_x,p_y in zip(pos_x,pos_y):

    dx1 = X - p_x
    dy1 = Y - p_y

    dr1 = np.sqrt(dx1** 2 + dy1**2)

    image = image + np.exp(- (dr1**2 / (2 * (0.2 **2))))
```
and the result will be something like this image:
![Alt text](images/graphene_image.png?raw=true "Title")

Suppose that we had converted our atomistic environment to an image (in our case 2D image of graphene), and we already had a sufficient amount of that data. We can then feed those images to the neural network (in our case, Convolutional Neural Network or only CNN). We here take advantage of Keras (with TensorFlow backend). The NN model will be like the following:


{5:12}(codes/image.py)


## References
<a id="1">[1]</a> 
in Ryczko K, Mills K, Luchak I, Homenick C, Tamblyn I. Convolutional neural networks for atomistic systems. Computational Materials Science. 2018 Jun 15;149:134-42.

