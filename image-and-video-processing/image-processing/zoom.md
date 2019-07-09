# Zooming
Zooming is a technique to enlarge an image in order to get a close-up look at the details of the image.

## Pixel Replication
Replicate/Copy pixels to interpolate middle pixels.

### Pros/Cons
Simple algorithm and easy to implement, but not very effective as the picture gets more blurry as we zoom in more times.

### Example
Below is an example of row-wise zooming.

Before:

| column1 | column 2 |
|---------|----------|
|    1    |     3    |
|    2    |     4    |

After:

| column 1 | column 2 | column 3 | column 4 |
|----------|----------|----------|----------|
|     1    |     1    |     3    |     3    |
|     2    |     2    |     4    |     4    |

## Zero order hold
Interpolate pixels twice (row-wise then column-wise) by taking the average of two adjacent pixels.


### Pros/Cons
Produce better result comparing to the previous method, but can only zoom in the power of 2.

### Example
Before:

| column1 | column 2 |
|---------|----------|
|    4    |     6    |
|    7    |     8    |

Intermediate:

| column1 | column 2 | column 2 |
|---------|----------|----------|
|    4    |     5    |     6    |
|    7    |     7    |     8    |

After:

| column1 | column 2 | column 2 |
|---------|----------|----------|
|    4    |     5    |     6    |
|    5    |     6    |     7    |
|    7    |     7    |     8    |

## K-Times Zooming
Calculate the difference of two neighbors and divide the difference by k-1, where k is the number of times we want to zoom in on the image. We divide the difference by k-1 because that's how many numbers we want to add to the gap. Add this value to the smaller value of the two neighbors and pad the new value next to that neighbor. Repeatedly add the value to the value previously padded until the gap between the two neighbors are filled.

### Pros/Cons
It is able to zoom by any factor and the resulting image is not as blurry. However, the computation cost increases.

### Example
Before:

| column1 | column 2 |
|---------|----------|
|    4    |     6    |
|    7    |     8    |

After:

| column1 | column 2 | column 3 | column 4 | column 5 |
|---------|----------|----------|----------|----------|
|   15    |    20    |    25    |    30    |    35    |
|   25    |    30    |    35    |    40    |    45    |
