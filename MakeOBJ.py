import numpy as np
from skimage import measure

def load_orbital(fname):
 F = open(fname,'r').read().split('\n')[23:-1]
 F = ' '.join(F)
 F = np.array(list(map(float,F.split())))
 F = F.reshape(178,109,89)
 return F

Initial_State = load_orbital('HOMO.cube')
Final_State = load_orbital('LUMO.cube')

N_frames = 250 # Number of frames
for t in range(0,N_frames):  
 Psi_squared = abs(np.cos(t*np.pi/(2*N_frames)) * Initial_State + np.sin(t*np.pi/(2*N_frames)) * Final_State * np.exp(-1j*t*2*np.pi/25))**2  
 verts, faces, normals, values = measure.marching_cubes(Psi_squared, 0.0005) 
 verts = (verts*0.148345)*0.52918
 o = open('OBJ/%s.obj' % t,'w')
 o.write('o Wavefunction\n')
 for i in verts:
  o.write('v %s %s %s \n' %(i[0],i[1],i[2]))
 for i in normals:
  o.write('vn %s %s %s \n' %(i[0],i[1],i[2]))
 for i in faces:
  o.write('f %s %s %s \n' %(i[0]+1,i[1]+1,i[2]+1))
 o.close()

