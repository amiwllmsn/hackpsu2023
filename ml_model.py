import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import cv2
from PIL import Image
from sklearn.metrics import accuracy_score

data = pd.read_csv('image_dataset.csv')

def load_and_preprocess_images(df, image_column):
    for i in df[image_column]:
        image = Image.open(i)
        image = image.resize((64, 64))
        image_array = np.array(image)
        flattened_array = image_array.ravel() #should make array 1D
        return np.array(flattened_array)

numerical_data = load_and_preprocess_images(data, 'Image')
print(numerical_data.shape)
print(numerical_data)
data['NumericalImage']=[numerical_data]

x = data['NumericalImage']  
y = data['DirectoryName']  

x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.30,random_state=42)

x_train= np.array(x_train).reshape(-1,1)
x_test= np.array(x_test).reshape(-1,1)
y_train= np.array(y_train).reshape(-1,1)
y_test= np.array(y_test).reshape(-1,1)

classifier = RandomForestClassifier()
classifier.fit(x_train,y_train)

y_pred=classifier.predict(x_test)
accuracy=accuracy_score(y_test,y_pred)

'''Once the model has been trained and evaluated, we can make predictions using new data. 
I would just reshuffle my dataframe once again to create a new dataset and test it out
'''
#new_data = pd.read_csv('new_data.csv')
#new_predictions = classifier.predict(new_data['NumericalImageData'])