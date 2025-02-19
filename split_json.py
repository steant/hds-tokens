import json
import os

def split_json(input_file):
    # Read the JSON file
    with open(input_file, "r") as file:
        data = json.load(file)

    # Extract the required sections based on new keys
    sections = {
        "primitives": data.get("primitives/primitives", {}),
        "semantics": data.get("semantics/semantics", {}),
        "light": data.get("themes/light", {}),
        "dark": data.get("themes/dark", {})
    }

    # Create an output directory
    output_dir = "output_json"
    os.makedirs(output_dir, exist_ok=True)

    # Save each section as a separate JSON file
    for name, content in sections.items():
        output_path = os.path.join(output_dir, f"{name}.json")
        with open(output_path, "w") as file:
            json.dump(content, file, indent=2)
        print(f"Saved: {output_path}")

    print("Splitting complete. JSON files saved in the 'output_json' folder.")

if __name__ == "__main__":
    input_file = "tokens.json"  # Ensure the file is in the same directory
    split_json(input_file)
