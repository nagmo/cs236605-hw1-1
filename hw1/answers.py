r"""
Use this module to write your answers to the questions in the notebook.

Note: Inside the answer strings you can use Markdown format and also LaTeX
math (delimited with $$).
"""

# ==============
# Part 2 answers

part2_q1 = r"""
**Your answer:**


Increasing K will lead to improved generalization for unseen data,
because it lets us take into consideration the class of the majority
of the samples "neighbours" and by that protect the result from being vulnerable to outliers.
The best K can be found using cross validation as we have seen.
The edge cases are when K=1 in that case the class of the sample will be determined by the closest neighbour
that can have an error in it's prediction (makes out model over fitted), the other case is when K=N_samples
in that case for each sample we will get the most common class with no regards to the real value of the sample.

"""
# ==============

# ==============
# Part 3 answers

part3_q1 = r"""
**Your answer:**


The selection of $\Delta > 0$ is arbitrary because we derive L(w) by w to find it's minimum,
and because $\Delta$ is constant it's derivative is 0. 

"""

part3_q2 = r"""
**Your answer:**


1. We can interpret the images we have created as the visual representation of the "template" the model
 have created for a given class (in our case a number). We can see that for numbers that are more similar
 in their shape we get a more similar image, this can explain why the model can be "confused" by them.
2. the KNN model looks at the K most similar images by looking at each pixel at a time while the SVM loss 
 model only looks at the images which have an effect on the separating hyper-plane.  
   

"""

part3_q3 = r"""
**Your answer:**


1. The training set loss graph looks Good, Because it descends fast and is monotonic. 
 If it was too low we were expecting a slow descending of the loss graph,
 and If it was too high we were expecting a fast descending, but also fast increasings and non-monotonic loss graph. 
2. The model is slightly under-fitted because the accuracy of both the train and validation are increasing together.
 If it was in a state of over-fit we would expect the training accuracy
 to keep improving while the validation accuracy starts to decrease. 

"""

# ==============

# ==============
# Part 4 answers

part4_q1 = r"""
**Your answer:**


The ideal pattern ot the residual plot will be close to a straight line, with the point being concentrated
near the straight line at zero, having standard distribution with zero mean.
In the first plot we can see a lot of points far away from the zero line because of the non-linear relationship.
After CV we can still see some outliers but most of the pints are close to the zero line. 

"""

part4_q2 = r"""
**Your answer:**


1. The use of the 'np.logspace' function, as opposed to the 'np.linspace' function, is allowing us to search over
 lambdas in different orders of magnitudes, without sampling extremely large number of points.
 We assume that for close lambda values, the accuracy of the model won't change much.
2. Overall, the model is fitted K_folds * len(degree_range) * len(lambda_range) times,
 not including the final fit over the entire training data.

"""

# ==============
