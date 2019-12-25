This repository contains the code files to identify the presence of human beings in Earthquake debris images using CNN models. The dataset has been synthetically expanded using augmentation techniques - rotation, translation, rescaling, flipping, shearing, stretching and adding random noise.

CNN models - Resnet50 and InceptionV3 have been applied on the dataset.

The models have been compared on various metrics -

Overall accuracy
Class wise accuracy
Precision
Recall
AUC Score
F1 score
The files should be executed in the following order -

data_augmentation.py
Resnet_Training.py / InceptionV3_Training.py
Model_Predictions.py
