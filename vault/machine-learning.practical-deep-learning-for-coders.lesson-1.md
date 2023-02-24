---
id: aape7dhzwahxzd51op95nlt
title: "Lesson 1"
desc: ""
updated: 1677167986692
created: 1676289393239
---

https://transcribe.param.codes/result/tr-39307ea1-c9e0-42e9-96eb-0ce615efa30f

https://www.kaggle.com/code/iliekpython/deep-learning-chapter-1

- Overfitting is the single most important and challenging issue when training.
- It's easy to create a model that does a good job at making predictions on the exact data
  it has been trained on, but it's much harder to make accurate predictions on data the model has
  never seen before.

- When using a pretrained model, `cnn_learner` will remove the last layer, since that is
  always specifically customized to the original training task, and replace it with one or more
  new layers with randomized weights, of an appropriate size for the dataset we're working with.
  This last part of the model is called the _head_.

- Using a pretrained model for a task different from what it was originally trained for is known
  as _transfer learning_.

- Fine-tuning: A transfer learning technique that updates the parameters of a pre-trained model
  by training for additional epochs using a different task from that used for pre-training.
