import os

# Define the paths to the image and label folders
image_folder = r"C:\Users\PRATYUSH\Desktop\waste seg\yolo\yolov5\images\test"
label_folder = r"C:\Users\PRATYUSH\Desktop\waste seg\yolo\yolov5\labels\test"

# Supported image extensions
image_extensions = ['.jpg', '.JPG', '.jpeg', '.JPEG']

# Get all image filenames (ensure they are sorted sequentially)
image_files = sorted([f for f in os.listdir(image_folder) if any(f.lower().endswith(ext) for ext in image_extensions)])

# Open a test file to write the paths
with open('test.txt', 'w') as file:
    for image_file in image_files:
        # Construct the label file name by replacing the image extension with .txt
        label_file = os.path.splitext(image_file)[0] + '.txt'
        
        # Construct the full paths
        image_path = os.path.join(image_folder, image_file)
        label_path = os.path.join(label_folder, label_file)
        
        # Write the paths to the text file
        file.write(f"{image_path}\n{label_path}\n")

print("text.txt created successfully!")
