import bpy
import csv
import os

# ============================================================================ #
# CONFIGURATION & CORE FUNCTIONS
# ============================================================================ #

# Scaling factors:
# - X-axis: 1 meter = 1 minute (60 seconds)
# - Y-axis: 1 meter = 100 BPM
X_SCALE = 1 / 60.0
Y_SCALE = 1 / 100.0

def read_csv_points(file_path):
    """Read CSV and return list of (x, y, z) coordinates."""
    points = []
    try:
        with open(file_path, 'r', newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)  # Skip header: "Time (s),Average BPM"
            
            for row in csvreader:
                if len(row) != 2:
                    continue
                    
                try:
                    time_sec = float(row[0])
                    bpm = float(row[1])
                    x = time_sec * X_SCALE
                    y = bpm * Y_SCALE
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
# OPERATOR WITH FILE SELECTOR
# ============================================================================ #

class BPM_OT_Import_Curve(bpy.types.Operator):
    """Import BPM data from CSV and create a curve"""
    bl_idname = "bpm.import_curve"
    bl_label = "Import BPM Curve"
    bl_description = "Select CSV file and create a curve with proper scaling"
    bl_options = {'REGISTER', 'UNDO'}
    
    # File selector properties
    filepath: bpy.props.StringProperty(subtype="FILE_PATH")
    filename_ext = ".csv"
    filter_glob: bpy.props.StringProperty(default="*.csv", options={'HIDDEN'})
    
    # Operator properties (shown in file browser)
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
        
        curve_name = os.path.splitext(os.path.basename(self.filepath))[0]
        self.curve_name = curve_name
        curve = create_curve_from_points(points, curve_name)
        
        if curve:
            # Try to select and frame the curve, but don't fail if context is wrong
            try:
                # Only perform these operations if we have a 3D view context
                if bpy.context.area and bpy.context.area.type == 'VIEW_3D':
                    bpy.ops.object.select_all(action='DESELECT')
                    curve.select_set(True)
                    bpy.context.view_layer.objects.active = curve
                    bpy.ops.view3d.view_selected(use_all_regions=False)
            except RuntimeError:
                # Context isn't right for view operations, but curve was still created
                pass
            
            self.report({'INFO'}, f"Created '{self.curve_name}' with {len(points)} points")
            return {'FINISHED'}
        else:
            self.report({'ERROR'}, "Failed to create curve")
            return {'CANCELLED'}
    
    def invoke(self, context, event):
        # Open file browser
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}
    
    def draw(self, context):
        # Show properties in file browser
        layout = self.layout
        layout.prop(self, "curve_name")

# ============================================================================ #
# UI PANEL
# ============================================================================ #

class BPM_PT_Panel(bpy.types.Panel):
    """Panel for BPM curve import"""
    bl_label = "BPM Curve Import"
    bl_idname = "BPM_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "BPM Curve"
    
    def draw(self, context):
        layout = self.layout
        
        # Scaling info
        box = layout.box()
        box.label(text="Scaling:", icon="INFO")
        box.label(text="  X: 1m = 1 minute")
        box.label(text="  Y: 1m = 100 BPM")
        
        # Import button
        layout.separator()
        layout.operator(BPM_OT_Import_Curve.bl_idname, icon="FILE_FOLDER")

# ============================================================================ #
# REGISTRATION
# ============================================================================ #

classes = (BPM_OT_Import_Curve, BPM_PT_Panel)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()