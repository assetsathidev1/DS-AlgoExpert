# ML Crash Course Notes

## 1. Introduction
- Topics going to be covered: Supervised, Unsupervised, Recco, Ranking and DL

## 2. Supervised Learning Algorithms
- Naive Bayes
    1. Naive Bayes is a probabilistic classifier based on applying Bayes' theorem with strong (naive) independence assumptions between the features.
    2. Naive Bayes classifiers are highly scalable, requiring a number of parameters linear in the number of variables (features/predictors) in a learning problem.
    3. Bayes' theorem is given by: $P(Spam | W) = \frac{P(W | Spam) \cdot P(Spam)}{P(W)}$
    - $P(Spam | W)$ is the posterior probability of msg being spam containing words (W) .
    - $P(Spam)$ is the probability of any msg being `Spam`.
    - $P(W | Spam)$ is the liklihood of finding these words (W) when there was a Spam msg.
    - $P(W)$ is the total probability of finding these words (W) in any msg (spam or not).
    - Its calculated as: $P(W) = P(W | Spam) * P(Spam) + P(W | Not Spam) * P(Not Spam)$
    
    4. If you have a feature set of 3 words, say `W1`, `W2`, and `W3`, then the probability of this set being a spam is given by chain rule:
    $P(W1, W2, W3 | Spam) = P(W1 | Spam) \cdot P(W2 | W1, Spam) \cdot P(W3 | W1, W2, Spam)$
    
    5. The above equation is not scalable to compute, so we make a naive assumption that all the words are independent of each other, so the above equation becomes: $P(W1, W2, W3 | Spam) = P(W1 | Spam) \cdot P(W2 | Spam) \cdot P(W3 | Spam)$
    
    6. The above equation is scalable and can be computed easily; because we just multiply the probability of each word being in a spam msg.
    7. To avoid a 0 probability, we use Laplace smoothing, which is adding 1 to the numerator and the number of words in the vocabulary to the denominator. 
    8. $P(Spam) and P(Not Spam)$ are called `Prior` probabilities.
    9. $P(W | Spam) and P(W | Not Spam)$ are called `Likelihood` probabilities.
    10. $P(Spam | W)$ is called `Posterior` probability.
    11. Denominator $P(W)$ is called `Evidence` probability.
    12. A Binary assumption is made that a word is either present or not present in a msg. This is called `Bernoulli` assumption. AKA `Bernoulli Distribution` AKA `Binomial` .
    13. And sometimes, it is assumed that a word can occur multiple times in a msg. This is called `Multinomial` assumption.

- Model Performance
    1. Validation Set is used to tune the model parameters.
    2. ROC Curve is a plot of True Positive Rate (TPR) vs False Positive Rate (FPR).
    3. AUC is the area under the ROC curve.
    4. AUC is a good metric to evaluate the model performance and decide which model to choose.
    5. Cross validation can happen in 2 ways, `K-Fold` and `Hold Out`.
    6. `K-Fold` is where the data is divided into K parts and each part is used as a validation set and the rest of the data is used as training set. This is repeated K times and the average of the K results is taken.


