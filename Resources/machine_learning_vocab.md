[Gradient descent, how neural networks learn | Deep learning, part 2](https://youtu.be/IHZwWFHWa-w)

[But what *is* a Neural Network? | Deep learning, Part 1](https://www.youtube.com/watch?v=aircAruvnKk&t=0s)

[Tensor](https://www.tensorflow.org/api_docs/python/tf/Tensor) A Tensor is a symbolic handle to one of the outputs of an Operation. It does not hold the values of that operation's output, but instead provides a means of computing those values in a TensorFlow tf.Session.

`Shape`: size of each dimension of a matrix or "tensor" 

- 'NHWC' = Num_samples x Height x Width x Channels
- 'NCHW' = Num_samples x Channels x Height x Width

[tf.Session()](https://www.tensorflow.org/api_docs/python/tf/Session) - A Session object encapsulates the environment in which Operation objects are executed, and Tensor objects are evaluated.

[tf.placeholder](https://www.tensorflow.org/api_docs/python/tf/placeholder) Inserts a placeholder for a tensor that will be always fed.

[tf.argmax](https://www.tensorflow.org/api_docs/python/tf/argmax) Returns the index with the largest value across axes of a tensor. 

[tf.truncated_normal](https://www.tensorflow.org/api_docs/python/tf/truncated_normal) Outputs random values from a truncated normal distribution.

The generated values follow a normal distribution with specified mean and standard deviation, except that values whose magnitude is more than 2 standard deviations from the mean are dropped and re-picked.

[tf.Variable]() A variable maintains state in the graph across calls to run(). You add a variable to the graph by constructing an instance of the class Variable.

Just like any Tensor, variables created with Variable() can be used as inputs for other Ops in the graph. Additionally, all the operators overloaded for the Tensor class are carried over to variables, so you can also add nodes to the graph by just doing arithmetic on variables.

[tf.constant](https://www.tensorflow.org/versions/r0.12/api_docs/python/constant_op/constant_value_tensors) Creates a constant tensor.

[tf.nn.conv2d](https://www.tensorflow.org/api_docs/python/tf/nn/conv2d)

Computes a 2-D convolution given 4-D input and filter tensors.

Given an input tensor of shape [batch, in_height, in_width, in_channels] and a filter / kernel tensor of shape [filter_height, filter_width, in_channels, out_channels], this op performs the following:

Flattens the filter to a 2-D matrix with shape [filter_height * filter_width * in_channels, output_channels].
Extracts image patches from the input tensor to form a virtual tensor of shape [batch, out_height, out_width, filter_height * filter_width * in_channels].
For each patch, right-multiplies the filter matrix and the image patch vector.

#### Max Pooling
`pooling`: which is a form of non-linear down-sampling. There are several non-linear functions to implement pooling among which `max pooling` is the most common. It partitions the input image into a set of non-overlapping rectangles and, for each such sub-region, outputs the maximum.

Overview: http://ufldl.stanford.edu/tutorial/supervised/Pooling/


[tf.nn.max_pool](https://www.tensorflow.org/api_docs/python/tf/nn/max_pool) Performs the max pooling on the input.

Returns:
A Tensor with type tf.float32. The max pooled output tensor.

#### Activation Functions
- [Overview](https://theclevermachine.wordpress.com/2014/09/08/derivation-derivatives-for-common-neural-network-activation-functions/)
	
	- Functions:
		- ReLU
		- Tanh
		- Sigmoid
		- Linear

[tf.nn.relu](https://www.tensorflow.org/api_docs/python/tf/nn/relu) Activation Function

[tf.matmul](https://www.tensorflow.org/api_docs/python/tf/matmul) Multiplies matrix a by matrix b, producing a * b.

The inputs must, following any transpositions, be tensors of rank >= 2 where the inner 2 dimensions specify valid matrix multiplication arguments, and any further outer dimensions match.

Both matrices must be of the same type. The supported types are: float16, float32, float64, int32, complex64, complex128.

Either matrix can be transposed or adjointed (conjugated and transposed) on the fly by setting one of the corresponding flag to True. These are False by default.

[tf.nn.softmax](https://www.tensorflow.org/api_docs/python/tf/nn/softmax) Computes softmax activations.

[Logit](https://en.wikipedia.org/wiki/Logit) is a function that maps probabilities `([0, 1]) to R ((-inf, inf))`	
For Tensorflow: It's a name that it is thought to imply that this Tensor is the quantity that is being mapped to probabilities by the Softmax.

[tf.nn.softmax_cross_entropy_with_logits](https://www.tensorflow.org/api_docs/python/tf/nn/softmax_cross_entropy_with_logits) Computes softmax cross entropy between logits and labels.

[Gradient Descent Algorithms](http://ruder.io/optimizing-gradient-descent/) 

[tf.train.AdamOptimizer](https://www.tensorflow.org/api_docs/python/tf/train/AdamOptimizer) Optimizer that implements the [Adam algorithm](https://arxiv.org/pdf/1412.6980.pdf).

[tf.reduce_mean](https://www.tensorflow.org/api_docs/python/tf/reduce_mean) Computes the mean of elements across dimensions of a tensor.

Reduces input_tensor along the dimensions given in axis. Unless keep_dims is true, the rank of the tensor is reduced by 1 for each entry in axis. If keep_dims is true, the reduced dimensions are retained with length 1.

If axis has no entries, all dimensions are reduced, and a tensor with a single element is returned.
