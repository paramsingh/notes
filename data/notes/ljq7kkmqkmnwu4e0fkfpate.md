
https://github.com/fastai/fastbook/blob/master/05_pet_breeds.ipynb

https://www.kaggle.com/iliekpython/fastai-chapter-5-manual-runthrough

> One important piece of this DataBlock call that we haven't seen before is in these two lines:

> item_tfms=Resize(460),
> batch_tfms=aug_transforms(size=224, min_scale=0.75)
> These lines implement a fastai data augmentation strategy which we call presizing. Presizing is a particular way to do image augmentation that is designed to minimize data destruction while maintaining good performance.

Presizing adopts two strategies:

- Resize images to relatively "large" dimensions—that is, dimensions significantly larger than the target training dimensions.
- Compose all of the common augmentation operations (including a resize to the final target size) into one, and perform the combined operation on the GPU only once at the end of processing, rather than performing the operations individually and interpolating multiple times.

> Please include a transform in `after_item` that ensures all data of type TensorImage is the same size

The summary error can tell you what transformations you forgot to apply etc.

- [[machine-learning.cross-entropy-loss]]
