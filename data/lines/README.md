# lines

This directory contains data for the image lines used in the training of the OMR
models.

- `splits/` — Files with the list of lines used for train/test/val for each
dataset (EIN and SAL).
- `transcriptions/` — GT transcriptions provided for each split according to the
distribution in `splits`.
- `IMAGES/` — This folder should contain the images of the lines extracted from each
image of the real manuscripts. We do not own the rights for distributing the 
images, so this folder is empty. It has been created only for reproductibilty 
purposes.
