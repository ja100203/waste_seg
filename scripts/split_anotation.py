import os
import json
import random
import copy

# Fixed values
dataset_dir = "TACO/data"  # Replace with your dataset path
test_percentage = 10  # Percentage of images used for the testing set
val_percentage = 10   # Percentage of images used for the validation set
nr_trials = 10        # Number of splits

ann_input_path = "TACO/data/annotations.json"

# Load annotations
with open(ann_input_path, 'r') as f:
    dataset = json.loads(f.read())

anns = dataset['annotations']
scene_anns = dataset['scene_annotations']
imgs = dataset['images']
nr_images = len(imgs)

# Calculate the number of testing and non-training images
nr_testing_images = int(nr_images * test_percentage * 0.01 + 0.5)
nr_nontraining_images = int(nr_images * (test_percentage + val_percentage) * 0.01 + 0.5)

# Start trials for dataset splitting
for i in range(nr_trials):
    random.shuffle(imgs)

    # Initialize train, val, test sets
    train_set = {
        'info': dataset['info'],
        'images': [],
        'annotations': [],
        'scene_annotations': [],
        'licenses': dataset['licenses'],
        'categories': dataset['categories'],
        'scene_categories': dataset['scene_categories'],
    }

    # Create deep copies of the sets for validation and test
    val_set = copy.deepcopy(train_set)
    test_set = copy.deepcopy(train_set)

    # Split images for train, val, test
    test_set['images'] = imgs[:nr_testing_images]
    val_set['images'] = imgs[nr_testing_images:nr_nontraining_images]
    train_set['images'] = imgs[nr_nontraining_images:]

    # Create image IDs for splitting annotations
    test_img_ids = [img['id'] for img in test_set['images']]
    val_img_ids = [img['id'] for img in val_set['images']]
    train_img_ids = [img['id'] for img in train_set['images']]

    # Split instance annotations
    for ann in anns:
        if ann['image_id'] in test_img_ids:
            test_set['annotations'].append(ann)
        elif ann['image_id'] in val_img_ids:
            val_set['annotations'].append(ann)
        elif ann['image_id'] in train_img_ids:
            train_set['annotations'].append(ann)

    # Split scene annotations
    for ann in scene_anns:
        if ann['image_id'] in test_img_ids:
            test_set['scene_annotations'].append(ann)
        elif ann['image_id'] in val_img_ids:
            val_set['scene_annotations'].append(ann)
        elif ann['image_id'] in train_img_ids:
            train_set['scene_annotations'].append(ann)

    # Write the split annotations to new JSON files
    ann_train_out_path = os.path.join(dataset_dir, f'annotations_{i}_train.json')
    ann_val_out_path = os.path.join(dataset_dir, f'annotations_{i}_val.json')
    ann_test_out_path = os.path.join(dataset_dir, f'annotations_{i}_test.json')

    with open(ann_train_out_path, 'w') as f:
        json.dump(train_set, f, indent=4)

    with open(ann_val_out_path, 'w') as f:
        json.dump(val_set, f, indent=4)

    with open(ann_test_out_path, 'w') as f:
        json.dump(test_set, f, indent=4)

    print(f"Trial {i + 1} split complete: Train, Val, Test sets saved.")
