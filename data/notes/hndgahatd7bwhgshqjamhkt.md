
- YouTube: https://www.youtube.com/watch?v=F4tvM4Vb3A0
- Transcription: https://transcribe.param.codes/result/tr-0a85d5e8-562c-4812-bf4f-a09f4c602075
- Book chapter: https://github.com/fastai/fastbook/blob/master/02_production.ipynb

## Things I actually learnt

- Clean data before training the model
- Gradio and huggingface are easy ways to deploy the model.

# Book notes

- Drivetrain approach to designing great data products: The basic idea is to start with considering your objective, then think about what actions you can take to meet that objective and what data you have (or can acquire) that can help, and then build a model that you can use to determine the best actions to take to get the best results in terms of your objective.

# Lecture notes

- https://aiquizzes.com

- damaged car vs normal car.
- beard or not
- food image classifier
- can squish images.
- also pad, pad with zeros.
- `RandomResizedCrop` - get different bits of the image.
- Data augmentation: creating more data from original data, `aug_transforms`
- Training the model before we clean it.
- Confusion matrix: shows what category errors the model is making.
- Plot top losses to see which images break.
- Before actually cleaning the data, train the model, plot top losses, use cleaner to clean the data.
