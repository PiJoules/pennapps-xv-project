import cv2
import numpy as np
from matplotlib import pyplot as plt
from convert2d import getBinaryEdges
import os, os.path, time

def convert_original_2D(directory_path):
	files = {}  # dict[str, binary]
 	for filename in os.listdir(directory_path):
	    if filename.endswith(".jpg"):
		    img_as_2d = getBinaryEdges(os.path.join(directory_path, filename))
		    #final_edges_binary=final_dges_binary.append(img_as_2d)
		    files[filename] = img_as_2d

	return files
