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
print("##############################################")
print("################ end #########################")
print("##############################################")
print("################# Executing script #########################")
argv = sys.argv
print(argv)
argv = argv[argv.index("--") + 1:]  # get all args after "--"
print(argv)
#delete cube
print("################# remove cube #########################")
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False, confirm=False)
#import object
print("################# import object #########################")
imported_object = bpy.ops.import_scene.obj(filepath=file_loc)
bpy.context.selected_objects[0] ####<--Fixs
#select obj
print("################# select object #########################")
obj = bpy.context.window.scene.objects[0]
print("################# execute script #########################")
bpy.context.view_layer.objects.active = obj 
bpy.ops.object.modifier_add(type='DECIMATE')
bpy.context.object.modifiers["Decimate"].decimate_type = 'UNSUBDIV'
bpy.context.object.modifiers["Decimate"].iterations = 1
bpy.ops.object.apply_all_modifiers()
#
print("exporting "+file_loc_exp)
bpy.ops.export_scene.obj(filepath=file_loc_exp)
print("###################### delete obj and obj_export #############################")
if os.path.exists(file_loc):
    print(" obj file exist - removing ")
    os.remove(file_loc) 
print("##############################################")
print("################ end #########################")
print("##############################################")


#bpy.ops.wm.save_as_mainfile(filepath="e:\\test\\blbb.blend")
print("################Python script ended #########################")



