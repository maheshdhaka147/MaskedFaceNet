In the wake of Covid-19, an increasing number of individuals are not following the face mask guidelines issued by authorities. The research paper focuses on detecting whether people are wearing face masks properly or not. The experiment uses three different datasets to train a Convolution Neural Network model for the classification of Correctly and Incorrectly worn face masks. The CNN model performs a total of 5 different experiments on various combinations of data obtained from these datasets. The experiments also use Generative Adversarial Networks to generate more images to deal with the issue of class imbalance. The first three experiments involve applying a CNN model on these datasets one by one, where only one dataset got used for each experiment. In the fourth experiment, all three datasets got merged and, a CNN model got applied to them. In the last experiment, along with merging all three datasets, a GAN model got used to resolve the class imbalance issue. There is a plethora of research on face mask detection, recognition, or even on detection whether people are wearing face masks or not but this research is unique in a way that it focuses on whether subjects are wearing face masks correctly or not.


Folder Name                            : Summary
#################################### BEGIN ###################################################
Code                                   : Contains all the programs and their outputs
Experiment                             : Contains code of 5 different experiments performed in the research. 
MSProjectDataStoreInArray              : Containes 3 different datasets with image size 16X16 stored in array format
Preprocessing                          : Contains 3 programs to preprocess 3 differnt datasets
TrainedModels                          : Contains 5 trained models from 5 different experiments
RunDemo                                : The folder contains code to run a live demo using trained models
##################################### END ##################################################





File Name                              : Summary
#################################### BEGIN ##################################################
Experiment1MaskedFaceNetModel          : Contains program to perform experiment1 on MaskedFaceNet Dataset(Dataset1)
Experiment2KaggleModel                 : Contains program to perform experiment2 on Kaggle Dataset(Dataset2)
Experiment3SCFaceModel                 : Contains program to perform experiment3 on SCFace Dataset(Dataset3)
Experiment4Merge3Datasets              : Contains program to perform experiment4 on the merger on all three datasets
Experiment5Merge3DatasetsAndUseGAN     : Contains program to perform experiment5 on the merger on all three datasets and on additional images generated using GAN
CreateDataset1MaskedFaceNet            : MaskedFaceNet(Dataset1) Preprocessing
CreateDataset2Kaggle                   : Kaggle(Dataset2) Preprocessing
CreateDataset3SCFace                   : SCFace(Dataset3) Preprocessing. The program imposes face mask on SCFace dataset's faces
MaskedFaceNetModel.h5                  : Trained model from experiment1
KaggleModel.h5                         : Trained model from experiment2
SCFaceModel.h5                         : Trained model from experiment3
Experiment4Merge3Datasets.h5           : Trained model from experiment4
Experiment5Merge3DatasetsAndUseGAN.h5  : Trained model from experiment5
RunThisFile                            : The file can be used to run a live demo. Please view Requirements.txt in the same folder to install required libraries before running this file.
###################################### END #################################################






Original Dataset: Link
#################################### BEGIN ##################################################
Dataset1: Correctly Masked Faces (https://drive.google.com/file/d/1upkkdJ8x4QKivBqmhIrsAeLf2sR2A2_v/view?usp=sharing)
Dataset1: Incorrectly Masked Faces (https://drive.google.com/file/d/1h8hXuLYDIVupV3u80sd8CIdsTWDgExb3/view?usp=sharing)
Dataset2: Kaggle (https://www.kaggle.com/andrewmvd/face-mask-detection)
Dataset3: SCFace Link Not available due to legal agreement
###################################### END #################################################
