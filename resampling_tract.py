from __future__ import division
import os
import sys
import argparse
import nibabel as nib
import numpy as np
import dipy
from dipy.tracking.utils import length
from dipy.tracking.streamline import set_number_of_points


def resample_tract(tract, step_size):
    """Resample the tract with the given step size.
    """
    lengths=list(length(tract))
    tract_res = []
    for i, f in enumerate(tract):
	nb_res_points = np.int(np.floor(lengths[i]/step_size))
	tmp = set_number_of_points(f, nb_res_points)
	tract_res.append(tmp)
    tract_res = nib.streamlines.array_sequence.ArraySequence(tract_res)
    return tract_res


def resample_tract_nb_points(tract, nb_res_points):
    """Resample the tract with the given number of points.
    """
    tract_res = []
    for i, f in enumerate(tract):
	tmp = set_number_of_points(f, nb_res_points)
	tract_res.append(tmp)
    tract_res = nib.streamlines.array_sequence.ArraySequence(tract_res)
    return tract_res


def save_tck_res(tract, hdr, step_size, out_filename):
	"""Save the tract in tck format.
	"""
	hdr['step_size'] = step_size
	t = nib.streamlines.tractogram.Tractogram(tract, affine_to_rasmm=np.eye(4))
	nib.streamlines.save(t, out_filename, header=hdr)
	print("Tract saved in %s" % out_filename)
	

def save_tck_res_nb_points(tract, hdr, out_filename):
	"""Save the tract in tck format.
	"""
	t = nib.streamlines.tractogram.Tractogram(tract, affine_to_rasmm=np.eye(4))
	nib.streamlines.save(t, out_filename, header=hdr)
	print("Tract saved in %s" % out_filename)


if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('-tract', nargs='?', const=1, default='',
	                    help='The tract filename')    
	parser.add_argument('-type', nargs='?', const=1, default='',
	                    help='Type of resampling (step_size or nb_points')  
	parser.add_argument('-new_param', nargs='?', const=1, default='',
	                    help='The new step_size (in mm) or nb_points for resampling')    
	parser.add_argument('-out', nargs='?', const=1, default='',
	                    help='The output filename')                                           
	args = parser.parse_args()

	tract = nib.streamlines.load(args.tract)
	hdr = tract.header
	tract = tract.streamlines
	res_type = args.type
	new_param = np.asarray(args.new_param, dtype='float64')
	if res_type == 'step_size':
		print("Resampling tract with step_size = %s" % new_param)
		tract_res = resample_tract(tract, new_param)
		save_tck_res(tract_res, hdr, new_param, args.out)
	elif res_type == 'nb_points':	
		print("Resampling tract with %i number of points" % new_param)
		tract_res = resample_tract_nb_points(tract, new_param)
		save_tck_res_nb_points(tract_res, hdr, new_param, args.out)

	sys.exit() 
