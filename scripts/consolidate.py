import os
import shutil

def move_and_rename_files(src_dir, dest_dir, prefix="batch_"):
    """
    Moves and renames files from the source directory (which contains batch subfolders)
    to the destination directory (train, val, or test) while ensuring unique file names.
    
    Args:
    - src_dir (str): The source directory containing batches.
    - dest_dir (str): The destination directory (train, val, or test).
    - prefix (str): Prefix to add to each file to ensure uniqueness.
    """
    for batch_name in os.listdir(src_dir):
        batch_path = os.path.join(src_dir, batch_name)
        if os.path.isdir(batch_path):
            for file in os.listdir(batch_path):
                file_path = os.path.join(batch_path, file)
                
                if file.endswith(('.jpg', '.png')):  # Image files
                    # Ensure destination directory exists
                    os.makedirs(dest_dir, exist_ok=True)
                    # Rename the image file with batch name prefix
                    new_image_name = f"{prefix}{batch_name}_{file}"
                    shutil.move(file_path, os.path.join(dest_dir, new_image_name))
                
                elif file.endswith('.txt'):  # Label annotation files
                    # Ensure destination directory exists
                    os.makedirs(dest_dir, exist_ok=True)
                    # Rename the label file with batch name prefix
                    new_label_name = f"{prefix}{batch_name}_{file}"
                    shutil.move(file_path, os.path.join(dest_dir, new_label_name))

# Paths for the source directories (yolo/yolo_images and yolo/yolo_annotations)
base_path = 'yolo'  # Replace with the actual path to your yolo folder

# Define the paths for images and labels
image_base_path = os.path.join(base_path, 'yolo_images')
label_base_path = os.path.join(base_path, 'yolo_annotations')

# Define the destination paths for images and labels (inside yolov5 folder)
yolov5_path = os.path.join(base_path, 'yolov5')  # yolov5 directory where images and labels should go
images_dest_path = os.path.join(yolov5_path, 'images')
labels_dest_path = os.path.join(yolov5_path, 'labels')

# Consolidate and rename files for training, validation, and testing datasets
for dataset_type in ['train', 'val', 'test']:
    # For images
    move_and_rename_files(os.path.join(image_base_path, dataset_type),
                          os.path.join(images_dest_path, dataset_type))
    # For labels
    move_and_rename_files(os.path.join(label_base_path, dataset_type),
                          os.path.join(labels_dest_path, dataset_type))
