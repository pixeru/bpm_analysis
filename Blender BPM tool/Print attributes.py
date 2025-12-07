import bpy
import pyperclip # You'll need to install this library in your Blender's Python environment for non-Blender-specific clipboard use.
import re # Import the regular expression module for numerical sorting

def get_attributes_containing_bpm():
    """
    Finds and returns a list of attribute names from the active object
    that contain the substring 'bpm' after duplicating and converting it to a mesh.

    Handles errors and cleans up the duplicated object.
    """
    orig_object = bpy.context.object

    # 1. Check for an active object
    if not orig_object:
        # Returning None or an empty list is often clearer for function output
        print("Error: No active object selected.")
        return []

    # 2. Check if the active object is allowed (e.g., non-camera/light)
    # This is a good robustness check, although conversion might fail anyway.
    if orig_object.type in ('CAMERA', 'LIGHT', 'ARMATURE', 'CURVE', 'LATTICE'):
        print(f"Error: Object type '{orig_object.type}' is not suitable for attribute checking via mesh conversion.")
        return []

    # Keep track of the selected state and active object for restoration
    original_selections = list(bpy.context.selected_objects)
    bpy.ops.object.select_all(action='DESELECT')
    orig_object.select_set(True)
    bpy.context.view_layer.objects.active = orig_object

    # --- Duplication and Conversion ---
    duplicated_object = None
    attribute_names = []

    try:
        # Duplicate the object
        bpy.ops.object.duplicate()
        # The duplicated object should now be the active one
        duplicated_object = bpy.context.object

        if not duplicated_object or duplicated_object is orig_object:
            # Should not happen, but a safe check
            raise RuntimeError("Object duplication failed.")

        # Convert the duplicate to a mesh
        bpy.ops.object.convert(target='MESH')

        # Check for successful conversion
        if duplicated_object.type != 'MESH':
            raise RuntimeError("Object conversion to MESH failed.")

        # --- Attribute Extraction ---
        # The object's data might be None if the conversion failed silently
        if not duplicated_object.data or not hasattr(duplicated_object.data, 'attributes'):
            raise RuntimeError("The converted object's data is invalid or lacks attributes.")

        for attr in duplicated_object.data.attributes:
            # --- Check for attributes containing "bpm" ---
            if attr.name and "bpm" in attr.name.lower():
                attribute_names.append(attr.name)

    except RuntimeError as e:
        print(f"A runtime error occurred during processing: {e}")
        # Attribute_names will be an empty list if an error occurs

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        # Attribute_names will be an empty list if an error occurs

    finally:
        # --- Cleanup and Restore ---
        
        # 1. Safely delete the duplicated object
        if duplicated_object:
            # Check if the object still exists in the scene before trying to remove it
            if duplicated_object.name in bpy.data.objects:
                try:
                    bpy.data.objects.remove(duplicated_object, do_unlink=True)
                    print(f"Cleaned up duplicated object: {duplicated_object.name}")
                except ReferenceError as e:
                    # Catch the error if the object was somehow removed earlier
                    print(f"Warning: Could not remove duplicated object cleanly: {e}")
            
            # CRITICAL: Clear the reference to the deleted object to prevent
            # future access attempts, even if we are past the point of error.
            duplicated_object = None 

        # 2. Restore the original selection and active object state
        bpy.ops.object.select_all(action='DESELECT')
        
        # Only select/set active for objects that still exist
        valid_selections = []
        for obj in original_selections:
            # Check if the object still exists in bpy.data
            if obj.name in bpy.data.objects:
                obj.select_set(True)
                valid_selections.append(obj)
        
        # Re-set the active object only if it still exists
        if orig_object and orig_object.name in bpy.data.objects:
            # Check if the original object is one of the valid selections
            if orig_object in valid_selections:
                bpy.context.view_layer.objects.active = orig_object
            else:
                # If the original object wasn't selected before, just make it active if possible
                bpy.context.view_layer.objects.active = orig_object
        elif valid_selections:
             # If the original object is gone, make one of the re-selected objects active
             bpy.context.view_layer.objects.active = valid_selections[0]

    return attribute_names

def send_to_clipboard(data):
    """
    Copies the provided string data to the operating system's clipboard
    using Blender's clipboard operator.
    """
    if not data:
        print("No data to copy to clipboard.")
        return

    # Blender has a built-in clipboard operator, which is more reliable
    # than external libraries within the Blender environment.
    bpy.context.window_manager.clipboard = data
    print(f"Successfully copied {len(data.splitlines())} attribute name(s) to clipboard.")

# --- Custom Sort Key Function ---
def numerical_sort_key(item):
    """
    Extracts the leading number from the string for numerical sorting.
    Uses regex to find a number at the start, optionally followed by a dot/space.
    Returns the number as an integer, or a large float if no number is found,
    to push non-matching items to the end.
    """
    # Look for one or more digits at the start of the string
    match = re.match(r'^\s*(\d+)', item)
    if match:
        return int(match.group(1))
    
    # Return a high value for items that don't start with a number
    return float('inf')


if __name__ == "__main__":
    found_attributes = get_attributes_containing_bpm()

    if found_attributes:
        # 1. Sort the attributes numerically
        found_attributes.sort(key=numerical_sort_key)
        
        # 2. Append "bpm/s" to each attribute name using a list comprehension
        final_attributes = [attr + "bpm/s" for attr in found_attributes]
        
        # 3. Join the modified list into a single string
        clipboard_content = "\n".join(final_attributes)
        send_to_clipboard(clipboard_content)
    else:
        print("No attributes containing 'bpm' were found.")