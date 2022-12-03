import argparse
import bpy
import sys
import os
import time

import bpy
import bmesh
from random import randint

file_loc = 'D:\\Program Files\\Pixologic\\ZBrush 2022\\ZScripts\\PluginDev\\blenderheadless\\obj.obj'
file_loc_exp = 'D:\\Program Files\\Pixologic\\ZBrush 2022\\ZScripts\\PluginDev\\blenderheadless\\obj_export.obj'
file_loc_exp_mlt = 'D:\\Program Files\\Pixologic\\ZBrush 2022\\ZScripts\\PluginDev\\blenderheadless\\obj_export.mtl'


def random_face(bm):
    bm.faces.ensure_lookup_table()
    return bm.faces[randint(0, len(bm.faces) - 1)]


print("###################### delete obj and obj_export #############################")

if os.path.exists(file_loc_exp):
    print(" obj file exist - removing ")
    os.remove(file_loc_exp) 
if os.path.exists(file_loc_exp_mlt):
    print(" obj.mlt file exist - removing ")
    os.remove(file_loc_exp_mlt) 
time_duration = 1
time.sleep(time_duration)
print("################# Executing script #########################")
argv = sys.argv
print(argv)
argv = argv[argv.index("--") + 1:]  # get all args after "--"
print(argv)
#delete cube
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False, confirm=False)
#import object
imported_object = bpy.ops.import_scene.obj(filepath=file_loc)
bpy.context.selected_objects[0] ####<--Fixs
#select obj
obj = bpy.context.window.scene.objects[0]
bpy.context.view_layer.objects.active = obj 
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.uv.reset()
bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.001)
bpy.ops.export_scene.obj(filepath=file_loc_exp)
#
print("exporting"+file_loc_exp)
bpy.ops.wm.save_as_mainfile(filepath="e:\\test\\blbb.blend")
print("################Python script ended #########################")



