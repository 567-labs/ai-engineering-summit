def process_taxonomy_file(yaml_path: str) -> dict:
    """
    Process a taxonomy YAML file and extract taxonomy map, occasions, materials, and other relevant data.

    Args:
        yaml_path (str): Path to the taxonomy YAML file

    Returns:
        dict: Dictionary containing:
            - taxonomy_map: Nested dictionary mapping categories -> subcategories -> attributes
            - occasions: List of valid occasions
            - materials: List of valid materials
            - taxonomy: Raw taxonomy data
    """
    import yaml

    # Load the YAML file
    with open(yaml_path, "r") as f:
        taxonomy = yaml.safe_load(f)

    # Create taxonomy map
    taxonomy_map = {}
    for category in taxonomy["categories"]:
        subcat_name = category["name"]
        taxonomy_map[subcat_name] = {}

        # Add product types
        taxonomy_map[subcat_name]["product_type"] = category.get("types", [])

        # Add attributes and their values
        taxonomy_map[subcat_name]["attributes"] = {}
        for attr in category.get("attributes", []):
            for attr_name, values in attr.items():
                taxonomy_map[subcat_name]["attributes"][attr_name] = values

    return taxonomy_map
