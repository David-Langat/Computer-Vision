<<<<<<< HEAD
<<<<<<< HEAD
import numpy as np

class MyClassifier():
    
    ''' Do not change the class name. Do not change any of the existing function names. You may add extra functions as you see fit.'''
    
    def __init__(self):
        self.class_labels = ['edible_1', 'edible_2', 'edible_3', 'edible_4', 'edible_5',
                            'poisonous_1', 'poisonous_2', 'poisonous_3', 'poisonous_4', 'poisonous_5']
        
        
    def setup(self):
        ''' This function will initialise your model. 
            You will need to load the model architecture and load any saved weights file your model relies on.
        '''

        pass
        
    def test_image(self, image):
        ''' This function will be given a PIL image, and should return the predicted class label for that image. 
            Currently the function is returning a random label.
                
        '''
              
        predicted_cls = np.random.choice(self.class_labels)
        
        return predicted_cls
=======
from PIL import Image
=======
import numpy as np
import torchvision
import torch
from torchvision import transforms
import torch.nn as nn
>>>>>>> 6f3a611 (Main project file.)

class LinearClassifier(nn.Module):
    '''Linear classifier setup'''
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(384, 10) # (input dimension, output dimension)

    def forward(self, x):
        '''Fully connected layers'''
        y = self.fc(x)

        return y

class MyClassifier():

    ''' A class to setup and test different classifier models. '''

    def __init__(self):
        self.class_labels = ['edible_1', 'edible_2', 'edible_3', 'edible_4', 'edible_5','poisonous_1', 'poisonous_2', 'poisonous_3', 'poisonous_4', 'poisonous_5']


    def setup(self):
        ''' This function will initialise the model.
            It will oad the model architecture and load any saved weights files the model relies on.
        '''
        imagenet_means = (0.485, 0.456, 0.406)
        imagenet_stds = (0.229, 0.224, 0.225)

        self.transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Resize((224,224)),
            transforms.Normalize(imagenet_means, imagenet_stds)])

        self.dino = torch.hub.load('facebookresearch/dinov2', 'dinov2_vits14')
        self.dino.eval()

        self.model = LinearClassifier()
        self.model.load_state_dict(torch.load('ModifiedLinear_Dino_LR0.003.pth'))
        self.model.eval()
        pass

    def test_image(self, image):
        '''Test each image'''
        input_image = self.transform(image).unsqueeze(0)
        feature = self.dino(input_image)
        output = self.model(feature)
        predicted_idx = torch.argmax(output)

        predicted_cls = self.class_labels[predicted_idx]

<<<<<<< HEAD
# You can add any additional helper methods or attributes to the class as needed
>>>>>>> de081b5 (Initializing new repository: First Upload)
=======
        return predicted_cls
>>>>>>> 6f3a611 (Main project file.)
