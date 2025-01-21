import json
import os
import cv2

# Paths
annotations_dir = 'TACO/data'  # Folder containing 'train', 'val', 'test'
yolo_annotation_dir = 'yolo/yolo_annotations'  # Output directory for YOLO annotations

# Ensure that the output directory exists
os.makedirs(yolo_annotation_dir, exist_ok=True)

# Category mapping (COCO ID to YOLO class_id)
category_map = {
    'biodegradable': [
        "Food waste", "Toilet tube", "Egg carton", "Drink carton", "Corrugated carton", "Meal carton", 
        "Pizza box", "Paper cup", "Normal paper", "Paper bag", "Plastified paper bag", "Wrapping paper", 
        "Tissues", "Magazine paper", "Rope & strings"
    ],
    'non_biodegradable': [
        "Aluminium foil", "Battery", "Aluminium blister pack", "Carded blister pack", "Other plastic bottle", 
        "Clear plastic bottle", "Glass bottle", "Plastic bottle cap", "Metal bottle cap", "Broken glass", "Food Can", 
        "Aerosol", "Drink can", "Disposable plastic cup", "Foam cup", "Glass cup", "Other plastic cup", "Plastic lid", 
        "Metal lid", "Other plastic", "Plastic film", "Six pack rings", "Garbage bag", "Other plastic wrapper", 
        "Single-use carrier bag", "Polypropylene bag", "Crisp packet", "Spread tub", "Tupperware", 
        "Disposable food container", "Foam food container", "Other plastic container", "Plastic glooves", 
        "Plastic utensils", "Pop tab", "Scrap metal", "Shoe", "Squeezable tube", "Plastic straw", 
        "Paper straw", "Styrofoam piece", "Unlabeled litter", "Cigarette"
    ]
}

# Flatten the category map to get the object name and its class_id
category_to_class_id = {}
for idx, category in enumerate(category_map['biodegradable']):
    category_to_class_id[category] = idx
for idx, category in enumerate(category_map['non_biodegradable']):
    category_to_class_id[category] = len(category_map['biodegradable']) + idx

# Load COCO annotations for train, val, and test datasets
def convert_annotations_to_yolo_format(coco_annotation_file, img_dir, output_dir):
    with open(coco_annotation_file, 'r') as f:
        coco_data = json.load(f)
    
    # Map to get images by image_id
    images_map = {img['id']: img for img in coco_data['images']}
    
    # Convert annotations to YOLO format for each image
    for ann in coco_data['annotations']:
        # Get image info based on image_id from annotation
        image_id = ann['image_id']
        img_info = images_map.get(image_id)
        
        if img_info is None:
            continue
        
        img_file = img_info['file_name']
        image_path = os.path.join(img_dir, img_file)
        
        # Read the image to get its dimensions
        img = cv2.imread(image_path)
        if img is None:
            continue
        
        height, width, _ = img.shape
        
        # Ensure the directory exists for this image
        yolo_annotation_file = os.path.join(output_dir, img_file.replace('.jpg', '.txt'))
        yolo_annotation_dir_for_image = os.path.dirname(yolo_annotation_file)
        os.makedirs(yolo_annotation_dir_for_image, exist_ok=True)
        
        # Create YOLO annotation file for this image
        with open(yolo_annotation_file, 'w') as f:
            # Get category name and map to class_id
            category_id = ann['category_id']
            category_name = coco_data['categories'][category_id - 1]['name']
            class_id = category_to_class_id.get(category_name)
            
            if class_id is None:
                continue
            
            # Get bounding box and convert to YOLO format
            bbox = ann['bbox']
            x_min, y_min, box_width, box_height = bbox
            x_center = (x_min + box_width / 2) / width
            y_center = (y_min + box_height / 2) / height
            box_width = box_width / width
            box_height = box_height / height
            
            # Write in YOLO format
            f.write(f"{class_id} {x_center} {y_center} {box_width} {box_height}\n")

# Convert annotations for train, val, and test datasets
convert_annotations_to_yolo_format('TACO/data/annotations_0_train.json', 'TACO/split_data/train', 'yolo/yolo_annotations/train')
convert_annotations_to_yolo_format('TACO/data/annotations_0_val.json', 'TACO/split_data/val', 'yolo/yolo_annotations/val')
convert_annotations_to_yolo_format('TACO/data/annotations_0_test.json', 'TACO/split_data/test', 'yolo/yolo_annotations/test')

print("COCO to YOLO conversion complete!")
