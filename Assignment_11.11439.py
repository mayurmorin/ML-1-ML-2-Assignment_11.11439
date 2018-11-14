
# coding: utf-8

# <h4>Task 2.1. What are the three stages to build the hypotheses or model in machine learning?</h4>

# <h4>Answer 2.1:</h4>
# The three stages to build the hypotheses or model in machine learning are:
# <h4>1. Model building:</h4> The model building process involves setting up ways of collecting data, understanding and paying attention to what is important in the data to answer the questions you are asking, finding a statistical, mathematical or a simulation model to gain understanding and make predictions.
# <h4>2. Model testing:</h4> In machine learning, model testing is referred to as the process where the performance of a fully trained model is evaluated on a testing set. The testing set consisting of a set of testing samples should be separated from the both training and validation sets, but it should follow the same probability distribution as the training set. A better test to check accuracy of model is to see its performance on data which was not used at all during model build.
# <h4>3. Applying the model:</h4> This stage involves choosing a different model altogether or introducing more variables to augment the efficiency.

# <h4>Task 2.2. What is the standard approach to supervised learning?</h4>

# <h4>Answer 2.2:</h4> The standard approach to supervised learning is to split the set of example into the training set and the test.
# 
# <h4>1. Determine the type of training examples.</h4> User should decide what kind of data is to be used as a training set. In case of handwriting analysis, for example, this might be a single handwritten character, an entire handwritten word, or an entire line of handwriting.
# <h4>2. Gather a training set.</h4> The training set needs to be representative of the real-world use of the function. Thus, a set of input objects is gathered and corresponding outputs are also gathered, either from human experts or from measurements.
# <h4>3. Determine the input feature representation of the learned function.</h4> The accuracy of the learned function depends strongly on how the input object is represented. Typically, the input object is transformed into a feature vector, which contains a number of features that are descriptive of the object. The number of features should not be too large, because of the curse of dimensionality; but should contain enough information to accurately predict the output.
# <h4>4. Determine the structure of the learned function and corresponding learning algorithm.</h4> For example, the engineer may choose to use support vector machines or decision trees.
# <h4>5. Complete the design.</h4> Run the learning algorithm on the gathered training set. Some supervised learning algorithms require the user to determine certain control parameters. These parameters may be adjusted by optimizing performance on a subset (called a validation set) of the training set, or via cross-validation.
# <h4>6. Evaluate the accuracy of the learned function.</h4> After parameter adjustment and learning, the performance of the resulting function should be measured on a test set that is separate from the training set.

# <h4>Task 2.3. What is Training set and Test set?</h4>

# <h4>Asnwer 2.3:</h4>
# 
# <h4>Training:</h4> A training set is a dataset used to train a model. In training the model, specific features are picked out from the training set. These features are then incorporated into the model. Thereby, if the training set is labeled correctly, the model should be able to learn something from these features.
# **********************
# <h4>Test:</h4>The test set is a dataset used to measure how well the model performs at making predictions on that test set.
# If the prediction scores for the test set are unreasonable, we’ll have to make some adjustments to our model and try again.
# **********************
# Training set is an examples given to the learner, while Test set is used to test the accuracy of the hypotheses generated by the learner, and it is the set of example held back from the learner. Training set are distinct from Test set.

# <h4>Task 2.4. What is the general principle of an ensemble method and what is bagging and
# boosting in ensemble method?</h4>

# <h4>Answer: 2.4</h4>
# 
# The general principle of an ensemble method is to combine the predictions of several models built with a given learning 
# algorithm in order to improve robustness over a single model. They typically reduce overfitting in models and make the model more robust (unlikely to be influenced by small changes in the training data). 
#   
# <h4>Example:</h4>
# 
# A: You may ask one of your friends to rate the movie for you.
# Now it’s entirely possible that the person you have chosen loves you very much and doesn’t want to break your heart by providing a 1-star rating to the horrible work you have created.
# 
# B: Another way could be by asking 5 colleagues of yours to rate the movie.
# This should provide a better idea of the movie. This method may provide honest ratings for your movie. But a problem still exists. These 5 people may not be “Subject Matter Experts” on the topic of your movie. Sure, they might understand the cinematography, the shots, or the audio, but at the same time may not be the best judges of dark humour.
# 
# C: How about asking 50 people to rate the movie?
# Some of which can be your friends, some of them can be your colleagues and some may even be total strangers.
# 
# With these examples, you can infer that a diverse group of people are likely to make better decisions as compared to individuals. Similar is true for a diverse set of models in comparison to single models. This diversification in Machine Learning is achieved by a technique called Ensemble Learning.
# 
# <h4>Bagging</h4>
# Bagging is a method in ensemble for improving unstable estimation or classification schemes.
# 1. Multiple subsets are created from the original dataset, selecting observations with replacement.
# 2. A base model (weak model) is created on each of these subsets.
# 3. The models run in parallel and are independent of each other.
# 4. The final predictions are determined by combining the predictions from all the models.
# 
# <h4>Boosting</h4>
# Boosting method are used sequentially to reduce the bias of the combined model. It is a sequential process, where each subsequent model attempts to correct the errors of the previous model. The succeeding models are dependent on the previous model. Let’s understand the way boosting works in the below steps.
# 
# 1. A subset is created from the original dataset.
# 2. Initially, all data points are given equal weights.
# 3. A base model is created on this subset.
# 4. This model is used to make predictions on the whole dataset.
# 5. Errors are calculated using the actual values and predicted values.
# 6. The observations which are incorrectly predicted, are given higher weights.
# 7. Another model is created and predictions are made on the dataset.
# 8. Similarly, multiple models are created, each correcting the errors of the previous model.
# 9 .The final model (strong learner) is the weighted mean of all the models (weak learners).
# 
# Thus, the boosting algorithm combines a number of weak learners to form a strong learner. The individual models would not perform well on the entire dataset, but they work well for some part of the dataset. Thus, each model actually boosts the performance of the ensemble.
# 
# Boosting and Bagging both can reduce errors by reducing the variance term.
# 
# 

# <h4>Task 2.5. How can you avoid overfitting ?</h4>

# <h4>Answer: 2.5</h4>
# 
# Overfitting happens relatively as you have a small dataset, and you try to learn from it. But if you have a small database and you are forced to come with a model based on that. In such situation, you can use a technique known as cross validation. In this method the dataset splits into two section, testing and training datasets, the testing dataset will only test the model while, in training dataset, the data points will come up with the model.
# 
# Following are the commonly used methodologies to avoid overfitting:
# 
# <h4>1. Cross-Validation :</h4> Cross Validation in its simplest form is a one round validation, where we leave one sample as in-time validation and rest for training the model. But for keeping lower variance a higher fold cross validation is preferred.
# In this technique, a model is usually given a dataset of a known data on which training (training data set) is run and a dataset of unknown data against which the model is tested. The idea of cross validation is to define a dataset to "test" the model in the training phase.
# <h4>2. Early Stopping :</h4> Early stopping rules provide guidance as to how many iterations can be run before the learner begins to over-fit.
# <h4>3. Pruning :</h4> Pruning is used extensively while building CART models. It simply removes the nodes which add little predictive power for the problem in hand.
# <h4>4. Regularization :</h4> This is the technique we are going to discuss in more details. Simply put, it introduces a cost term for bringing in more features with the objective function. Hence, it tries to push the coefficients for many variables to zero and hence reduce cost term.
