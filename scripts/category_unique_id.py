import json

# The category map you provided
category_map = {
    "biodegradable": [
        "Food waste", "Toilet tube", "Egg carton", "Drink carton", "Corrugated carton", "Meal carton",
        "Pizza box", "Paper cup", "Normal paper", "Paper bag", "Plastified paper bag", "Wrapping paper",
        "Tissues", "Magazine paper", "Rope & strings"
    ],
    "non_biodegradable": [
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

# Create a mapping for each object with a unique ID based on the original COCO format
def generate_object_id_mapping(category_map):
    object_id_mapping = {}
    id_counter = 0

    # Add biodegradable category objects
    for obj in category_map['biodegradable']:
        object_id_mapping[obj] = id_counter
        id_counter += 1

    # Add non_biodegradable category objects
    for obj in category_map['non_biodegradable']:
        object_id_mapping[obj] = id_counter
        id_counter += 1

    return object_id_mapping

# Get the unique IDs for each object
object_id_mapping = generate_object_id_mapping(category_map)

# Print the object_id_mapping as a JSON
with open("category_object_ids.json", "w") as f:
    json.dump(object_id_mapping, f, indent=4)

# Print the object_id_mapping
for obj, obj_id in object_id_mapping.items():
    print(f"Object: {obj}, Unique ID: {obj_id}")
