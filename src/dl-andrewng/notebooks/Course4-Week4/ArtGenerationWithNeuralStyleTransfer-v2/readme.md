View Project -

Residual Network Tutorial
http://htmlpreview.github.io/?https://github.com/manas-mukherjee/MLTools/blob/master/src/dl-andrewng/notebooks/Course4-Week4/ArtGenerationWithNeuralStyleTransfer-v2/ArtGenerationwithNeuralStyleTransfer-v2.html

** What we should remember **:

- Neural Style Transfer is an algorithm that given a content image C and a style image S can generate an artistic image
- It uses representations (hidden layer activations) based on a pretrained ConvNet.
- The content cost function is computed using one hidden layer's activations.
- The style cost function for one layer is computed using the Gram matrix of that layer's activations. The overall style cost function is obtained using several hidden layers.
- Optimizing the total cost function results in synthesizing new images.
