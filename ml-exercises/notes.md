# ML Crash Course Notes

## 1. Introduction
- Topics going to be covered: Supervised, Unsupervised, Recco, Ranking and DL

## 2. Supervised Learning Algorithms
- Naive Bayes
    1. Naive Bayes is a probabilistic classifier based on applying Bayes' theorem with strong (naive) independence assumptions between the features.
    2. Naive Bayes classifiers are highly scalable, requiring a number of parameters linear in the number of variables (features/predictors) in a learning problem.
    3. Bayes' theorem is given by:
    $$
    P(Spam | W) = \frac{P(W | Spam) \cdot P(Spam)}{P(W)}
    $$
    - $P(Spam | W)$ is the posterior probability of msg being spam containing words (W) .
    - $P(Spam)$ is the probability of any msg being `Spam`.
    - $P(W | Spam)$ is the liklihood of finding these words (W) when there was a Spam msg.
    - $P(W)$ is the total probability of finding these words (W) in any msg (spam or not).
    - Its calculated as: $P(W) = P(W | Spam) * P(Spam) + P(W | Not Spam) * P(Not Spam)$