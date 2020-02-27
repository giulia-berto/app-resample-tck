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


def save_tck_res(tract, hdr, step_size, out_filename):
	"""Save the tract in tck format.
	"""
	hdr['step_size'] = step_size
	t = nib.streamlines.tractogram.Tractogram(tract, affine_to_rasmm=np.eye(4))
	nib.streamlines.save(t, out_filename, header=hdr)
	print("Tract saved in %s" % out_filename)


if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('-tract', nargs='?', const=1, default='',
	                    help='The tract filename')     
	parser.add_argument('-step_size', nargs='?', const=1, default='',
	                    help='The step size to use for resampling (in mm)')    
	parser.add_argument('-out', nargs='?', const=1, default='',
	                    help='The output filename')                                           
	args = parser.parse_args()

	tract = nib.streamlines.load(args.tract)
	hdr = tract.header
	tract = tract.streamlines
	step_size = np.asarray(args.step_size, dtype='float64')
	tract_res = resample_tract(tract, step_size)
	save_tck_res(tract_res, hdr, step_size, args.out)

	sys.exit() 
