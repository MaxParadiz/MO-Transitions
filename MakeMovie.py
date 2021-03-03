import bpy


path = '/home/max/Projects/TransitionDipole/OMeOMe-S0/S0S1/OBJ/'
renderpath='/home/max/Projects/TransitionDipole/OMeOMe-S0/S0S1/Render/'

for i in range(0,250):
 bpy.ops.import_scene.obj(filepath=path+"%s.obj" % i) # Import OBJ
 D = bpy.data
 WF = bpy.context.selected_objects[0].name
 o = D.objects[WF]
 edens = bpy.data.materials['ElectronDensity']
 o.material_slots[o.active_material_index].material = edens
 bpy.data.scenes['Scene'].render.filepath = renderpath+'%s.png' % (i) # Render image
 bpy.ops.render.render(write_still=True)
 bpy.ops.object.select_all(action='DESELECT')
 bpy.data.objects[WF].select_set(True)
 bpy.ops.object.delete()   # Delete the object


