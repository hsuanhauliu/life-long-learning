# TensorFlow Study Guide
## High Level
### [Keras](https://www.tensorflow.org/guide/keras)
Keras is a high-level neural networks Python API that can run on top of either TensorFlow, CNTK, or Theano. TensorFlow library provides their own implementation of Keras (tensorflow.keras), which has direct support from TensorFlow.

#### Resources:
- [Keras documentation](https://keras.io/).
- [Youtube tutorial](https://www.youtube.com/watch?v=Y1-hQdgftMQ).

#### Benefits:
- Developed for easy and fast prototyping.
- User friendly: Keras has a simple, consistent interface optimized for common use cases. It provides clear and actionable feedback for user errors.
- Modular and composable: Keras models are made by connecting configurable building blocks together, with few restrictions.
- Easy to extend: Write custom building blocks to express new ideas for research. Create new layers, loss functions, and develop state-of-the-art models.
- Runs seamlessly on CPU and GPU.

#### Examples
Build a simple sequential (feed-forward) model:
```
model = keras.Sequential()

# Adds a densely-connected (fully-connected) layer with 64 nodes
model.add(keras.layers.Dense(64, activation='relu'), input_dim = 20)
model.add(keras.layers.Dense(64, activation='relu'))
model.add(keras.layers.Dense(10, activation='softmax'))
```

### [Estimator](https://www.tensorflow.org/guide/estimators)
Estimator is a high-level TensorFlow API that greatly simplifies machine learning programming. The API encapsulates the following actions:
1. training
2. evaluation
3. prediction
4. export for serving

## Save Models
### [TFRecord](https://medium.com/mostly-ai/tensorflow-records-what-they-are-and-how-to-use-them-c46bc4bbb564)
a binary file format for storage.

Benefits
- Less storage and memory space.
- Less loading time.
- Easy to combine multiple dataset.
  - This can be helpful when one dataset is too large to load.
- Possible to store sequence data.

## Visualization Tool
[Tensorboard](https://www.tensorflow.org/guide/summaries_and_tensorboard)
```
tensorboard --logdir=[path/to/log-directory]
```

## Notes
### Padding
"SAME": pad the image so that the output is the **same** size as the input.  
"VALID": don't pad the image since the output size is **valid**.  

Note: without padding, some pixels might not be covered. Consider a 5x5 image and a 4x4 filter. Without padding, the last pixel will be ignored.  

Reference:
[What is the difference between same and valid padding?](https://stackoverflow.com/questions/37674306/what-is-the-difference-between-same-and-valid-padding-in-tf-nn-max-pool-of-t)
