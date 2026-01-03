import bpy
import csv
import os
import datetime

# ============================================================================ #
# CONFIGURATION
# ============================================================================ #

# Import scaling factors
IMPORT_X_SCALE = 1 / 60.0  # 1m = 1 minute (60 seconds)
IMPORT_Y_SCALE = 1 / 100.0 # 1m = 100 BPM

# Export scaling factors
EXPORT_X_SCALE = 60.0  # X-axis: multiply by 60 for time in seconds

# ============================================================================ #
# CORE FUNCTIONS - IMPORT
# ============================================================================ #

def read_csv_points(file_path):
    """Read CSV and return list of (x, y, z) coordinates."""
    points = []
    try:
        with open(file_path, 'r', newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)  # Skip header row
            
            for row in csvreader:
                if len(row) != 2:
                    continue
                    
                try:
                    time_sec = float(row[0])
                    value = float(row[1])
                    x = time_sec * IMPORT_X_SCALE
                    y = value * IMPORT_Y_SCALE
                    points.append((x, y, 0.0))
                except ValueError:
                    print(f"Skipping invalid row: {row}")
                    
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return []
    
    return points

def create_curve_from_points(point_list, curve_name):
    """Create a Blender curve object from list of 3D points."""
    if not point_list:
        return None
    
    # Remove existing curve with same name
    if curve_name in bpy.data.objects:
        bpy.data.objects.remove(bpy.data.objects[curve_name])
    
    # Create curve data
    curve_data = bpy.data.curves.new(name=curve_name, type='CURVE')
    curve_data.dimensions = '3D'
    
    # Create object
    curve_object = bpy.data.objects.new(curve_name, curve_data)
    bpy.context.collection.objects.link(curve_object)
    
    # Create poly spline (direct point mapping, no smoothing)
    spline = curve_data.splines.new(type='POLY')
    spline.points.add(len(point_list) - 1)
    
    # Set point coordinates (x, y, z, weight)
    for i, (x, y, z) in enumerate(point_list):
        spline.points[i].co = (x, y, z, 1.0)
    
    return curve_object

# ============================================================================ #
# CORE FUNCTIONS - EXPORT
# ============================================================================ #

def append_to_csv(filepath, x, y, header_name):
    """Append a single row to CSV file with dynamic header."""
    file_exists = os.path.isfile(filepath)
    
    with open(filepath, 'a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['time (s)', header_name])
        writer.writerow([x, y])

def export_mesh_data(mesh_data, original_object_name, data_file_path):
    """Export mesh vertices to CSV with conditional Y-axis scaling."""
    
    # Determine Y-Axis Header and Scaling based on object name
    y_header = "y_scaled"
    scale_factor_y = 1.0
    
    if "BPM" in original_object_name:
        y_header = "BPM"
        scale_factor_y = 100.0
    elif "Velocity" in original_object_name:
        y_header = "Speed m/s"
        scale_factor_y = 3.6
    elif "SpO2" in original_object_name:
        y_header = "SpO2"
        scale_factor_y = 100.0

    # Main export loop
    print(f"\nExporting vertices of '{original_object_name}' to: {data_file_path}")
    print(f"X-Axis Scale Factor (Time): {EXPORT_X_SCALE}")
    print(f"Y-Axis Scale Factor ({y_header}): {scale_factor_y}")

    for v in mesh_data.vertices:
        co = v.co

        # Apply scaling
        x_scaled = co[0] * EXPORT_X_SCALE
        y_scaled = co[1] * scale_factor_y
        
        # Clamp to zero (time and metrics shouldn't be negative)
        x_clamped = max(0.0, x_scaled)
        y_clamped = max(0.0, y_scaled)
        
        # Format to exactly 2 decimal places
        x_formatted = float("{:.2f}".format(x_clamped))
        y_formatted = float("{:.2f}".format(y_clamped))

        # Append to CSV
        append_to_csv(data_file_path, x_formatted, y_formatted, y_header)

    print(f"Successfully exported {len(mesh_data.vertices)} vertices.")

def get_export_file_path(object_name):
    """Generate export file path based on blend file location and timestamp."""
    if not bpy.data.filepath:
        raise Exception("The current Blender file has not been saved. Please save before exporting.")
    
    blend_dir = os.path.dirname(bpy.data.filepath)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H%M%S%z")
    csv_filename = f"{object_name}_{timestamp}.csv"
    return os.path.join(blend_dir, csv_filename)

# ============================================================================ #
# OPERATORS
# ============================================================================ #

class BPM_OT_Import_Curve(bpy.types.Operator):
    """Import BPM data from CSV and create a curve"""
    bl_idname = "bpm.import_curve"
    bl_label = "Import CSV as Curve"
    bl_description = "Select CSV file and create a curve with proper scaling"
    bl_options = {'REGISTER', 'UNDO'}
    
    filepath: bpy.props.StringProperty(subtype="FILE_PATH")
    filename_ext = ".csv"
    filter_glob: bpy.props.StringProperty(default="*.csv", options={'HIDDEN'})
    
    curve_name: bpy.props.StringProperty(
        name="Curve Name",
        description="Name for the created curve object",
        default="BPM_Curve"
    )
    
    def execute(self, context):
        if not self.filepath:
            self.report({'ERROR'}, "No file selected")
            return {'CANCELLED'}
        
        points = read_csv_points(self.filepath)
        
        if not points:
            self.report({'ERROR'}, "Failed to read CSV or no valid data")
            return {'CANCELLED'}
        
        # Use filename as curve name if default is unchanged
        if self.curve_name == "BPM_Curve":
            self.curve_name = os.path.splitext(os.path.basename(self.filepath))[0]
        
        curve = create_curve_from_points(points, self.curve_name)
        
        if curve:
            try:
                if context.area and context.area.type == 'VIEW_3D':
                    bpy.ops.object.select_all(action='DESELECT')
                    curve.select_set(True)
                    context.view_layer.objects.active = curve
                    bpy.ops.view3d.view_selected(use_all_regions=False)
            except RuntimeError:
                pass
            
            self.report({'INFO'}, f"Created '{self.curve_name}' with {len(points)} points")
            return {'FINISHED'}
        else:
            self.report({'ERROR'}, "Failed to create curve")
            return {'CANCELLED'}
    
    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}
    
    def draw(self, context):
        layout = self.layout
        layout.prop(self, "curve_name")

class BPM_OT_Export_Curve(bpy.types.Operator):
    """Export selected curve or mesh to CSV"""
    bl_idname = "bpm.export_curve"
    bl_label = "Export Selected Object"
    bl_description = "Export active mesh or curve to CSV with auto-scaling"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        obj = context.object
        
        if not obj:
            self.report({'ERROR'}, "No object selected")
            return {'CANCELLED'}
        
        if obj.type not in {'MESH', 'CURVE'}:
            self.report({'ERROR'}, f"Object type '{obj.type}' not supported. Select a mesh or curve.")
            return {'CANCELLED'}
        
        try:
            # Generate export file path
            object_name = obj.name.replace(" ", "_")
            data_file_path = get_export_file_path(object_name)
            
            # Process object based on type
            mesh_to_export = None
            temp_object = None
            
            if obj.type == 'MESH':
                print(f"Selected object is a MESH. Exporting directly.")
                eval_obj = obj.evaluated_get(context.evaluated_depsgraph_get())
                mesh_to_export = eval_obj.to_mesh()
                
            elif obj.type == 'CURVE':
                print(f"Selected object is a CURVE. Duplicating and converting to mesh...")
                
                # Duplicate the curve object
                bpy.ops.object.duplicate(linked=False)
                temp_object = context.object
                
                # Convert to mesh
                bpy.ops.object.convert(target='MESH')
                mesh_to_export = temp_object.data
            
            # Export the data
            if mesh_to_export:
                export_mesh_data(mesh_to_export, obj.name, data_file_path)
                
                # Cleanup
                if obj.type == 'MESH':
                    eval_obj.to_mesh_clear()
                
                if temp_object:
                    print(f"Deleting temporary object: {temp_object.name}")
                    context.view_layer.objects.active = obj
                    bpy.data.objects.remove(temp_object, do_unlink=True)
                
                self.report({'INFO'}, f"Exported: {os.path.basename(data_file_path)}")
                return {'FINISHED'}
            else:
                self.report({'ERROR'}, "Failed to get mesh data")
                return {'CANCELLED'}
                
        except Exception as e:
            self.report({'ERROR'}, f"Export failed: {str(e)}")
            return {'CANCELLED'}

# ============================================================================ #
# UI PANEL
# ============================================================================ #

class BPM_PT_Panel(bpy.types.Panel):
    """Panel for BPM curve import and export tools"""
    bl_label = "BPM Curve Tools"
    bl_idname = "BPM_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Animation"
    
    def draw(self, context):
        layout = self.layout
        
        # Import Section
        box = layout.box()
        
        # Import scaling info
        box.label(text="Scaling:", icon="INFO")
        box.label(text="  X: 1m = 1 minute")
        box.label(text="  Y: 1m = 100 BPM")
        
        layout.operator(BPM_OT_Import_Curve.bl_idname, icon="FILE_FOLDER")
        
        layout.separator()
        
        # Selection status and export button
        if context.object:
            col = layout.column(align=True)
            col.label(text=f"Selected: {context.object.name}", icon="OBJECT_DATA")
            if context.object.type in {'MESH', 'CURVE'}:
                col.operator(BPM_OT_Export_Curve.bl_idname, icon="FILE_TICK")
            else:
                col.label(text="Select a mesh or curve", icon="ERROR")
        else:
            layout.label(text="No object selected", icon="ERROR")

# ============================================================================ #
# REGISTRATION
# ============================================================================ #

classes = (
    BPM_OT_Import_Curve,
    BPM_OT_Export_Curve,
    BPM_PT_Panel
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()