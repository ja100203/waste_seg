import os
import json
import shutil

# Paths
dataset_dir = "TACO/data"  # Root dataset directory containing batch folders
output_dir = "TACO/split_data"  # Directory to save train/val/test images
annotation_files = {
    "train": "annotations_0_train.json",
    "val": "annotations_0_val.json",
    "test": "annotations_0_test.json",
}

# Create output directories
os.makedirs(output_dir, exist_ok=True)
for split in annotation_files.keys():
    os.makedirs(os.path.join(output_dir, split), exist_ok=True)

# Move images based on annotation files
for split, annotation_file in annotation_files.items():
    annotation_path = os.path.join(dataset_dir, annotation_file)
    
    # Load the annotation file
    with open(annotation_path, "r") as f:
        annotations = json.load(f)
    
    missing_images = []  # Track missing images
    
    # Loop through the images in the annotation file
    for image_info in annotations["images"]:
        image_name = image_info["file_name"]  # Get the file name (e.g., batch_13/000043.jpg)
        
        # Full path to the source image
        src_path = os.path.join(dataset_dir, image_name)
        
        if os.path.exists(src_path):
            # Destination path (preserve batch structure)
            dest_path = os.path.join(output_dir, split, image_name)
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)  # Create subfolders
            shutil.copy(src_path, dest_path)  # Copy the image
        else:
            missing_images.append(image_name)

    # Report missing images for this split
    if missing_images:
        print(f"Warning: Missing images in {split} split:")
        for img in missing_images:
            print(img)

print("Images moved successfully into train, val, and test folders!")
