# RNN Notebook
RNN is a great method to process and learn from sequential data. The key difference between RNN and other neural network architecture is that the output connection of an RNN cell is linked to the input of itself. This design is meant to feed the output at time *t-1* back into the cell at time *t*. This mechanism allows us to consider past result while processing the current input.

Essentially, any function involving recurrence can be considered a recurrent neural network.

## Advantages
- Ability to process variable-length of sequential data.
- Same transition function with the same parameters at every time step.


## Disadvantages
- Prone to exploding or vanishing gradient.

## Details


## Applications
Speech recognition, language modeling, translation, image captioning, etc.

## Tutorials
- [A friendly introduction to Recurrent Neural Networks](https://www.youtube.com/watch?v=UNmqTiOnRfg)
- [Recurrent Neural Networks by Example in Python](https://towardsdatascience.com/recurrent-neural-networks-by-example-in-python-ffd204f99470)
- [Standford RNN Lecture](https://www.youtube.com/watch?v=6niqTuYFZLQ)
