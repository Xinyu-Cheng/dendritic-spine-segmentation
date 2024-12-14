from model import *
from utils import *
from tensorflow.keras.models import load_model
from tensorflow.keras.callbacks import ModelCheckpoint
import os

def file_exists(directory, filename):
    file_path = os.path.join(directory, filename)
    return os.path.isfile(file_path)

directory = "../demo" 
filename = "unet_trained_model.keras" 

if file_exists(directory, filename):
    model = load_model(os.path.join(directory, filename))
    print("Model loaded successfully.")
    model.summary()
    gen = testGenerator("../demo/test")
    results = model.predict(gen, steps=30, verbose=1)
    saveResult("../results/demo",results)

else:
    data_gen_args = dict(rotation_range=0.2,
                        width_shift_range=0.05,
                        height_shift_range=0.05,
                        shear_range=0.05,
                        zoom_range=0.05,
                        horizontal_flip=True,
                        fill_mode='nearest')
    dir = '../data'
    myGene = trainGenerator(2,dir,'images','labels',data_gen_args,save_to_dir = None)
    model = unet()
    model_checkpoint = ModelCheckpoint('../checkpoints/unet_dendrite.keras', monitor='loss', verbose=1, save_best_only=True)
    model.fit(myGene, steps_per_epoch=100, epochs=10, callbacks=[model_checkpoint])
    model.save('../data/model/unet_trained_model.keras')
    gen = testGenerator("../demo/test")
    results = model.predict(gen, steps=16, verbose=1)
    saveResult("../results/demo",results)
