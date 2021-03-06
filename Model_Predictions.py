{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import json, os, re, sys, time\n",
    "import numpy as np\n",
    "from keras import backend as K\n",
    "from keras.applications.imagenet_utils import preprocess_input\n",
    "from keras.models import load_model\n",
    "from keras.preprocessing import image\n",
    "\n",
    "\n",
    "\n",
    "def predict(img_path, model):\n",
    "    img = image.load_img(img_path, target_size=(224, 224))\n",
    "    x = image.img_to_array(img)\n",
    "    x = np.expand_dims(x, axis=0)\n",
    "    preds = model.predict(x)\n",
    "    return preds\n",
    "\n",
    "\n",
    "import time\n",
    "model_path = \"C:/Users/abhij/Documents/Academics/Competitions/Earthquake/resnet50_final_v2.h5\"\n",
    "print('Loading model:', model_path)\n",
    "t0 = time.time()\n",
    "model = load_model(model_path)\n",
    "t1 = time.time()\n",
    "print('Loaded in:', t1-t0)\n",
    "\n",
    "\n",
    "##for creating the contingency table - \n",
    "root = 'C:/Users/abhij/Documents/academics big data/Earthquake/Test/Class1/'\n",
    "Test_v1_Class1 = []\n",
    "for root, _, filenames in os.walk(root):\n",
    "    for filename in filenames:\n",
    "        Test_v1_Class1.append(os.path.join(root, filename))\n",
    "\n",
    "preds_v1_Class1 = []\n",
    "for filename in Test_v1_Class1:\n",
    "    preds_v1_Class1.append(predict(filename,model))\n",
    "count = 0\n",
    "\n",
    "for i in range(len(preds_v1_Class1)):\n",
    "    if((preds_v1_Class1[i][0,0])>(preds_v1_Class1[i][0,1])):\n",
    "        count = count+1\n",
    "        \n",
    "print(\"Correct Predictions for Class 1 are\",count,\" and Total Images in Class 1 are\",len(preds_v1_Class1))\n",
    "\n",
    "root = 'C:/Users/abhij/Documents/academics big data/Earthquake/Test/Class2/'\n",
    "Test_v1_Class2 = []\n",
    "for root, _, filenames in os.walk(root):\n",
    "    for filename in filenames:\n",
    "        Test_v1_Class2.append(os.path.join(root, filename))\n",
    "\n",
    "preds_v1_Class2 = []\n",
    "for filename in Test_v1_Class2:\n",
    "    preds_v1_Class2.append(predict(filename,model))\n",
    "\n",
    "count = 0\n",
    "for i in range(len(preds_v1_Class2)):\n",
    "    if((preds_v1_Class2[i][0,0])<(preds_v1_Class2[i][0,1])):\n",
    "        count = count + 1\n",
    "        \n",
    "print(\"Correct Predictions for Class 2 are\",count,\" and Total Images in Class 2 are\",len(preds_v1_Class2))\n",
    "\n",
    "\n",
    "lst = [item2[0] for item2 in [item[0] for item in preds_v1_Class1]]\n",
    "lst.extend([item2[0] for item2 in [item[0] for item in preds_v1_Class2]])\n",
    "a = [(1 if item > 0.5 else 0) for item in lst]\n",
    "y_test = [1]*180\n",
    "y_test.extend([0]*190)\n",
    "print(y_test)\n",
    "\n",
    "##roc auc score\n",
    "from sklearn.metrics import roc_auc_score\n",
    "roc_auc_score(y_test,lst)\n",
    "\n",
    "##log loss\n",
    "from sklearn.metrics import log_loss\n",
    "log_loss(y_test,a)\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
