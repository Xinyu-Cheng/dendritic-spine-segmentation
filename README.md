# Project Overview: 
This project focuses on developing a U-Net-based convolutional neural network for image segmentation. The goal is to automate the identification and segmentation of regions of interest in fluorescence image. The project aims to create a reliable segmentation pipeline for fluorescent antibodies staining synapses. 

# Setup Instructions:
Install packages using 
```bash
pip install -r requirements.txt
```
The test data for demo code is located in the data/test folder, the pre-trained model will be downloaded from google drive once you run the demo.ipynb file and stored as demo/unet_trained_model.keras. The model can also be found at https://drive.google.com/file/d/1hWLFNcZ3ZZDAz6vgVBQN4HUzVAU9kLnf/view?usp=sharing. If you wish to train the model, you have to delete the pre-trained model from demo/unet_trained_model.keras and download the [images] (https://drive.google.com/drive/folders/11PbAfyUD3BAdCtU7HhzHOPSQIAjuzkKE?usp=sharing) and [labels] (https://drive.google.com/drive/folders/1C4YmZhHXd3ejqz44S5Ib6yLFEYJD8mNT?usp=sharing) and store them under the data/images and data/labels folder respectively. 

# How to Run:
Find the demo/demo.ipynb file and start running it. It will load the pre-trained model and run on demo test data. 

# Expected Output: 
The predicted images should appear under results/demo folder. 

# Pre-trained Model Link
Download from [Google Drive](https://drive.google.com/file/d/1hWLFNcZ3ZZDAz6vgVBQN4HUzVAU9kLnf/view?usp=sharing)

# hyperparameters and training setup
steps_per_epoch=100, epochs=10, optimizer=Adam, learning rate=1e-4, loss function: binary crossentropy. 

# Acknowledgments:
https://lmb.informatik.uni-freiburg.de/people/ronneber/u-net/
https://github.com/zhixuhao/unet/tree/master

(I am having trouble installing the packages on my local computer so I used colab to run my code. There could be some mistakes I made for the setup.)