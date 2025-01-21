import os

def create_file_list(root_dir, output_file):
    """
    Generate a list of image paths from nested batch directories.

    Args:
    - root_dir (str): Root directory containing images in batch-wise subfolders.
    - output_file (str): Output text file to save image paths.
    """
    with open(output_file, 'w') as file:
        for root, _, files in os.walk(root_dir):
            for f in files:
                if f.endswith(('.jpg', '.jpeg', '.png')):
                    file.write(os.path.join(root, f) + '\n')

# Define directories
train_dir = "yolo/yolo_images/train"
val_dir = "yolo/yolo_images/val"
test_dir = "yolo/yolo_images/test"

# Create train.txt, val.txt, and test.txt
create_file_list(train_dir, "yolo/train.txt")
create_file_list(val_dir, "yolo/val.txt")
create_file_list(test_dir, "yolo/test.txt")
