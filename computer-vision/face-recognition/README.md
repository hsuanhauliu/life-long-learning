# Face Recognition Notebook
## Goal
Verify one's identity by extracting features and comparing the feature vector with ground truth in the database.

## Challenges
Regular CNN is not flexible enough when it comes to expanding the number of classes for the output. If one wishes to verify the identities of new people for example, a new network will have to be trained. This also requires a lot of data for training for each class. Therefore, we need a better way that requires less training data (for each individual class) and expandable method.

## Vocabularies
- Face embedding: a rich low-dimensional feature representation (vector) of the a face.
- One-shot learning: a classification task where one example (or a very small number of examples) is given for each class
- Comparative loss: a type of loss calculated by comparing the output of multiple network.
- Triplet loss: loss calculated using output from three networks.
- Dimensionality reduction: aims to translate high dimensional data to a low dimensional representation such that similar input objects are mapped to nearby points on a manifold.
- Anchor: the ground truth image used to verify one's identity.

## One-Shot Learning Approach
- [One-Shot Learning for Face Recognition by Jason Brownlee](https://machinelearningmastery.com/one-shot-learning-with-siamese-networks-contrastive-and-triplet-loss-for-face-recognition/)
- [Siamese Network Tutorial by Andrew Ng](https://www.youtube.com/watch?v=6jfw8MuKwpI)
- [Triplet Loss Tutorial by Andrew Ng](https://www.youtube.com/watch?v=d2XB5-tuCWU)
- [More on Triplet Loss](https://omoindrot.github.io/triplet-loss)
- [FaceNet Paper Discussion](https://youtu.be/w--c0qG9MCc)

## Papers
- [FaceNet: A Unified Embedding for Face Recognition and Clustering](https://arxiv.org/abs/1503.03832)
- [DeepFace: Closing the Gap to Human-Level Performance in Face Verification](https://www.cs.toronto.edu/~ranzato/publications/taigman_cvpr14.pdf)

## Resources
- [Pre-trained FaceNet Implemented using TensorFlow](https://github.com/davidsandberg/facenet)
- [VGGFace2: a large-scale face recognition dataset](https://www.robots.ox.ac.uk/~vgg/data/vgg_face2/)
