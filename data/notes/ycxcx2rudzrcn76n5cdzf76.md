
Often, it might be the case that the training set is
not large enough to be split into a training set and
validation set.

A simple but popular solution to this is cross-validation.

The idea is simple: we split the training data into $$K$$ __folds__; for each fold $$k \in \{1, \dots, K\}$$
we train on all the folds but the $$k$$th, and test on the $$k$$th in a round robin manner.

Then, we compute the error averaged over all the folds and use that.
