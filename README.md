# neural network potentials
When we want to take advantage of a neural network to construct a potential energy surface (how atoms see their neighbors! and interact with them), we should consider the physical system symmetries. We already know that translation, rotation, permutation, and reflection symmetry for a problem such as potential energy should be considered.People already did different works for tackling these symmetry things. Still, the problem is already out there (and that is the reason why we every day see a lot of creative ways of representing molecular configurations for machine learning).

In this repository, we aim to reproduce those representations (which from now on, we will use the name fingerprints for them), and we will try to use different architectures of neural networks to get good accuracy and generalization.
##image method
We will start with the image representation of an atomistic environment, implemented in the below article:

in Ryczko K, Mills K, Luchak I, Homenick C, Tamblyn I. Convolutional neural networks for atomistic systems. Computational Materials Science. 2018 Jun 15;149:134-42.

![Alt text](images/graphene_image.png?raw=true "Title")
