import nbformat
from nbformat import validate, ValidationError, writes
import uuid

notebook_path = "files/example.ipynb"

def add_missing_ids(notebook):
    """Add missing IDs to cells if they don't have one."""
    for cell in notebook.cells:
        if 'id' not in cell:
            cell['id'] = str(uuid.uuid4())  # Generate a unique ID for each cell

try:
    # Load the notebook
    with open(notebook_path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    # Add missing IDs
    add_missing_ids(nb)
    
    # Validate the updated notebook
    validate(nb)

    # Save the normalized notebook
    with open(notebook_path, "w", encoding="utf-8") as f:
        f.write(writes(nb))
    
    print("Notebook is normalized, IDs added, and validated successfully!")

except ValidationError as e:
    print(f"Notebook validation failed: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
