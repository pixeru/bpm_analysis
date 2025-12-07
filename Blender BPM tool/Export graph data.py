import bpy
import csv
import os

current_datetime_str = "2025-09-22T212300-0500"

# Set the active object
obj = bpy.context.object

# --- Helper Function for Exporting Mesh Data ---
# Note: The original_object_name is used for conditional Y-axis scaling and header naming
def export_mesh_data(mesh_data, original_object_name, data_file_path):
    
    # --- Determine Y-Axis Header and Scaling ---
    y_header = "y_scaled" # Default fallback
    scale_factor_y = 1.0
    
    # Apply conditional logic for scaling and naming
    if "BPM" in original_object_name:
        y_header = "BPM"
        scale_factor_y = 100.0
    elif "Velocity" in original_object_name:
        y_header = "Speed m/s"
        scale_factor_y = 3.6
    # --- ADDED LOGIC FOR SpO2 ---
    elif "SpO2" in original_object_name: # Check if "SpO2" is in the object name
        y_header = "SpO2"              # Set the header to "SpO2"
        scale_factor_y = 100.0          # Set a suitable scale factor (assuming Blender data is 0-1)
    # ----------------------------

    # --- CSV Writer Function ---
    # Only needs to write x and y data
    def append_to_csv(filepath, x, y):
        # Check if the file exists
        file_exists = os.path.isfile(filepath)

        # Open the file in append mode
        with open(filepath, 'a', newline='') as file:
            writer = csv.writer(file)

            # If the file doesn't exist, write the updated header
            if not file_exists:
                writer.writerow(['time (s)', y_header])

            # Write the values to the file (x and y only)
            writer.writerow([x, y])

    # --- Main Export Loop ---
    print(f"Exporting vertices of '{original_object_name}' to: {data_file_path}")
    print(f"X-Axis Scale Factor (Time): 60.0")
    print(f"Y-Axis Scale Factor ({y_header}): {scale_factor_y}")


    for v in mesh_data.vertices:
        co = v.co

        # 1. Apply Scaling
        x_scaled = co[0] * 60.0 # Always scale X by 60
        # Z-axis is ignored/removed from further processing

        y_scaled = co[1] * scale_factor_y # Apply determined Y scale factor
        
        # --- ADDED CLAMPING TO ZERO ---
        # Ensure neither value goes below 0.0, as time and derived metrics shouldn't be negative
        x_clamped = max(0.0, x_scaled)
        y_clamped = max(0.0, y_scaled)
        # ------------------------------

        # 2. Format the scaled coordinates to exactly 3 decimal places
        x_formatted = float("{:.2f}".format(x_clamped)) # Use x_clamped
        y_formatted = float("{:.2f}".format(y_clamped)) # Use y_clamped

        # 3. Append to CSV (x and y only)
        append_to_csv(data_file_path, x_formatted, y_formatted)

    print(f"Successfully exported and scaled data for '{original_object_name}'.")

# --- Main Script Execution ---

# 1. Check if an object is selected
if not obj:
    print("Error: No object selected.")
# 2. Check if the object is a MESH or a CURVE (or other types that can be converted)
elif obj.type != 'MESH' and obj.type != 'CURVE':
    print(f"Error: Selected object type is '{obj.type}'. Only MESH or CURVE objects are supported.")
else:
    # --- File Path Construction ---
    # Get the name of the selected object, replacing spaces with underscores for a clean filename
    object_name = obj.name.replace(" ", "_")

    # Construct the CSV filename
    csv_filename = f"{object_name}_{current_datetime_str}.csv"

    # Get the path to the current Blender file
    blend_file_path = bpy.data.filepath
    if not blend_file_path:
        print("Error: The current Blender file has not been saved. Please save the file before running the export script.")
        raise Exception("Blend file not saved.")

    # Get the directory of the Blender file
    blend_dir = os.path.dirname(blend_file_path)

    # Construct the absolute path to the CSV file
    data_file_path = os.path.join(blend_dir, csv_filename)


    # --- Object Processing ---

    mesh_to_export = None
    temp_object = None

    if obj.type == 'MESH':
        print(f"Selected object is a MESH. Exporting directly.")
        mesh_to_export = obj.evaluated_get(bpy.context.evaluated_depsgraph_get()).to_mesh()

    elif obj.type == 'CURVE':
        print(f"Selected object is a CURVE. Duplicating and converting to mesh for export.")

        try:
            # Duplicate the curve object (to preserve the original)
            bpy.ops.object.duplicate(linked=False)
            temp_object = bpy.context.object # The duplicate is now the active object

            # Convert the duplicate to a mesh
            bpy.ops.object.convert(target='MESH')
            # The converted mesh object is now the active object again

            # Get the mesh data
            mesh_to_export = temp_object.data

        except RuntimeError as e:
            print(f"Error during curve conversion: {e}")
            if temp_object:
                bpy.data.objects.remove(temp_object, do_unlink=True)
            raise

    # --- Export & Cleanup ---
    if mesh_to_export:
        # Pass the original object name to export_mesh_data for conditional scaling/naming
        export_mesh_data(mesh_to_export, obj.name, data_file_path)

        # Free the temporary mesh data (good practice in Blender scripting)
        if obj.type == 'MESH':
            obj.evaluated_get(bpy.context.evaluated_depsgraph_get()).to_mesh_clear()

        # Clean up the temporary object if one was created (e.g., from a curve)
        if temp_object:
            print(f"Deleting temporary mesh object: {temp_object.name}")
            bpy.context.view_layer.objects.active = obj
            bpy.data.objects.remove(temp_object, do_unlink=True)