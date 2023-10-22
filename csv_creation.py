import os
import pandas as pd

root_directory = "random_color_images"

image_paths = []
directory_names = []

for directory_name in os.listdir(root_directory):
    if os.path.isdir(os.path.join(root_directory, directory_name)):
        for image_name in os.listdir(os.path.join(root_directory, directory_name)):
            print(image_name)
            if image_name.endswith(".png"):
                image_paths.append(os.path.join(root_directory, directory_name, image_name))
                directory_names.append(directory_name)
            data = pd.DataFrame({"Image": image_paths, "DirectoryName": directory_names})

shuffled_df = data.sample(frac=1, random_state=42) 
shuffled_df.reset_index(drop=True, inplace=True)

print(data.head())
shuffled_df.to_csv("image_dataset.csv", index=False)

