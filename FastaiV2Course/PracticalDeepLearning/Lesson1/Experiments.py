# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/PracticalDeepLearning2019.Lesson1_Experiments.ipynb (unless otherwise specified).

__all__ = ['path', 'fname', 'pat', 'dblock', 'dls']

# Cell
from fastai2.data.all import *
from fastai2.vision.all import *
from nbdev.showdoc import *

# Cell
path = untar_data(URLs.PETS)
path_anno, path_img = [path/folder for folder in path.ls()]

fname = get_image_files(path_img)
fname[:5]

# Cell
pat = r'/(\w+)_\d+.jpg'

dblock = DataBlock((ImageBlock,CategoryBlock),
                    splitter=RandomSplitter(),
                    get_items=get_image_files,
                    item_tfms=Resize(224),
                    batch_tfms=aug_transforms(),
                    get_y=RegexLabeller(pat))

dls = dblock.dataloaders(path_img, bs=4)