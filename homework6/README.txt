Uriel (Shaun) Stoll
uds2104
homework6

1. One-Hot Encoding is a binary string of zeros with exactly one '1'. For example: 0001, 0010, 0100, 1000. In keras, it is used for simpler labeling than standard binary. It is implemented in keras by using the to_categorical function. It is used to categorize data.

2. Dropout is a regularization method. Dropout helps prevent overfitting by randomly deleting nodes in the Neural Network during training.

3. ReLU is linear in the positive region. Negative values will all be set to zero, but as the positive values increase, the output will follow it linearly. The sigmoid function is capped from 0~1. Therefore, for large positive and negative values, the distinction is small because the sigmoid function converges.

4. softmax is necessary to get useful data from the output layer. It converts the outputs into probabilities totalling 1.

5. Convolution output = 96x96x16, Max-Pool output = 48x48x16
