from functions.compile_data_tracks_function import *

import ntpath
import os
import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
#from scipy.stats import ttest_ind
from scipy.stats import f_oneway

data_path1 = str(sys.argv[1])

data_path2 = str(sys.argv[2])

data_path3 = str(sys.argv[3])

min_track_length = int(sys.argv[4])

region1 = str(sys.argv[5])

region2 = str(sys.argv[6])

region3 = str(sys.argv[7])

save_path = str(sys.argv[8])

pixel_size = 1.54 #pixels/micron

tracks_region1, tracks_geo_region1, region1_cells, region1_endpointcells = compile_data_tracks(data_path1, min_track_length, region1, pixel_size)

tracks_region2, tracks_geo_region2, region2_cells, region2_endpointcells = compile_data_tracks(data_path2, min_track_length, region2, pixel_size)

tracks_region3, tracks_geo_region3, region3_cells, region3_endpointcells = compile_data_tracks(data_path3, min_track_length, region3, pixel_size)


#clears out sentinel file if it exists
open('sentinels/cellshape_histogram.txt','w').close()
#create new sentinel file to write to
hist_boxplot_figs = open('sentinels/cellshape_histogram.txt','w')
file_lines = [] 

#where acf figures are saved
figure_path = save_path + '/cellshape_histogram'

#check to see if the path exists, if not make the directory
if not os.path.exists(figure_path):
  os.mkdir(figure_path)

var_area_region1 = []
area_region1 = []
for df in tracks_geo_region1:
  area = df['area'].iloc[:,0]/(pixel_size**2)
  area_region1.append(area)
  var_area_region1.append(np.var(area))
plt.title('Variance of cell area over track in {}'.format(region1))
plt.hist(var_area_region1, bins=30)
plt.savefig(figure_path + '/var_area_hist_{}.png'.format(region1))
plt.clf()
file_lines.append('{}/var_area_hist_{}.png \n'.format(figure_path, region1))
plt.title('Cell area over track in {}'.format(region1))
plt.hist(np.concatenate(area_region1).ravel(), bins=30)
plt.savefig(figure_path + '/area_hist_{}.png'.format(region1))
plt.clf()
file_lines.append('{}/area_hist_{}.png \n'.format(figure_path, region1))

var_area_region2 = []
area_region2 = []
for df in tracks_geo_region2:
  area = df['area'].iloc[:,0]/(pixel_size**2)
  area_region2.append(area)
  var_area_region2.append(np.var(area))
plt.title('Variance of cell area over track on {}'.format(region2))
plt.hist(var_area_region2, bins=30)
plt.savefig(figure_path + '/var_area_hist_{}.png'.format(region2))
plt.clf()
file_lines.append('{}/var_area_hist_{}.png \n'.format(figure_path, region2))
plt.title('Cell area over track in {}'.format(region2))
plt.hist(np.concatenate(area_region2).ravel(), bins=30)
plt.savefig(figure_path + '/area_hist_{}.png'.format(region2))
plt.clf()
file_lines.append('{}/area_hist_{}.png \n'.format(figure_path, region2))

var_area_region3 = []
area_region3 = []
for df in tracks_geo_region3:
  area = df['area'].iloc[:,0]/(pixel_size**2)
  area_region3.append(area)
  var_area_region3.append(np.var(area))
plt.title('Variance of cell area over track on {}'.format(region3))
plt.hist(var_area_region3, bins=30)
plt.savefig(figure_path + '/var_area_hist_{}.png'.format(region3))
plt.clf()
file_lines.append('{}/var_area_hist_{}.png \n'.format(figure_path, region3))
plt.title('Cell area over track in {}'.format(region3))
plt.hist(np.concatenate(area_region3).ravel(), bins=30)
plt.savefig(figure_path + '/area_hist_{}.png'.format(region3))
plt.clf()
file_lines.append('{}/area_hist_{}.png \n'.format(figure_path, region3))

var_perim_region1 = []
perim_region1 = []
for df in tracks_geo_region1:
  perim = df['perimeter']/pixel_size
  perim_region1.append(perim)
  var_perim_region1.append(np.var(perim))
plt.title('Variance of cell perimeter over track on {}'.format(region1))
plt.hist(var_perim_region1, bins=30)
plt.savefig(figure_path + '/var_perim_hist_{}.png'.format(region1))
plt.clf()
file_lines.append('{}/var_perim_hist_{}.png \n'.format(figure_path, region1))
plt.title('Cell perimeter over track on {}'.format(region1))
plt.hist(np.concatenate(perim_region1).ravel(), bins=30)
plt.savefig(figure_path + '/perim_hist_{}.png'.format(region1))
plt.clf()
file_lines.append('{}/perim_hist_{}.png \n'.format(figure_path, region1))

var_perim_region2 = []
perim_region2 = []
for df in tracks_geo_region2:
  perim = df['perimeter']/pixel_size
  perim_region2.append(perim)
  var_perim_region2.append(np.var(perim))
plt.title('Variance of cell perimeter over track on {}'.format(region2))
plt.hist(var_perim_region2, bins=30)
plt.savefig(figure_path + '/perim_hist_{}.png'.format(region2))
plt.clf()
file_lines.append('{}/perim_hist_{}.png \n'.format(figure_path, region2))
plt.title('Cell perimeter over track on {}'.format(region2))
plt.hist(np.concatenate(perim_region2).ravel(), bins=30)
plt.savefig(figure_path + '/perim_hist_{}.png'.format(region2))
plt.clf()
file_lines.append('{}/perim_hist_{}.png \n'.format(figure_path, region2))

var_perim_region3 = []
perim_region3 = []
for df in tracks_geo_region3:
  perim = df['perimeter']/pixel_size
  perim_region3.append(perim)
  var_perim_region3.append(np.var(perim))
plt.title('Variance of cell perimeter over track on {}'.format(region3))
plt.hist(var_perim_region3, bins=30)
plt.savefig(figure_path + '/perim_hist_{}.png'.format(region3))
plt.clf()
file_lines.append('{}/perim_hist_{}.png \n'.format(figure_path, region3))
plt.title('Cell perimeter over track on {}'.format(region3))
plt.hist(np.concatenate(perim_region3).ravel(), bins=30)
plt.savefig(figure_path + '/perim_hist_{}.png'.format(region3))
plt.clf()
file_lines.append('{}/perim_hist_{}.png \n'.format(figure_path, region3))

###########PERCENT CHANGE#######################


perchange_area_region1 = []
perchange_perim_region1 = []
for df in tracks_geo_region1:
  area = df['area'].iloc[:,0]/(pixel_size**2)
  perim = df['perimeter']/pixel_size
  max_area = np.max(area)
  min_area = np.min(area)
  perchange_area_region1.append((max_area-min_area)/max_area)
  max_perim = np.max(perim)
  min_perim = np.min(perim)
  perchange_perim_region1.append((max_perim-min_perim)/max_perim)
plt.title('Percent change of cell area over track in {}'.format(region1))
plt.hist(perchange_area_region1)
plt.savefig(figure_path + '/perchange_area_hist_{}.png'.format(region1))
plt.clf()
file_lines.append('{}/perchange_area_hist_{}.png \n'.format(figure_path, region1))
plt.title('Percent change of cell perimeter over track in {}'.format(region1))
plt.hist(perchange_perim_region1)
plt.savefig(figure_path + '/perchange_perim_hist_{}.png'.format(region1))
plt.clf()
file_lines.append('{}/perchange_perim_hist_{}.png \n'.format(figure_path, region1))

perchange_area_region2 = []
perchange_perim_region2 = []
for df in tracks_geo_region2:
  area = df['area'].iloc[:,0]/(pixel_size**2)
  perim = df['perimeter']/pixel_size
  max_area = np.max(area)
  min_area = np.min(area)
  perchange_area_region2.append((max_area-min_area)/max_area)
  max_perim = np.max(perim)
  min_perim = np.min(perim)
  perchange_perim_region2.append((max_perim-min_perim)/max_perim)
plt.title('Percent change of cell area over track in {}'.format(region2))
plt.hist(perchange_area_region2)
plt.savefig(figure_path + '/perchange_area_hist_{}.png'.format(region2))
plt.clf()
file_lines.append('{}/perchange_area_hist_{}.png \n'.format(figure_path, region2))
plt.title('Percent change of cell perimeter over track in {}'.format(region2))
plt.hist(perchange_perim_region2)
plt.savefig(figure_path + '/perchange_perim_hist_{}.png'.format(region2))
plt.clf()
file_lines.append('{}/perchange_perim_hist_{}.png \n'.format(figure_path, region2))

perchange_area_region3 = []
perchange_perim_region3 = []
for df in tracks_geo_region1:
  area = df['area'].iloc[:,0]/(pixel_size**2)
  perim = df['perimeter']/pixel_size
  max_area = np.max(area)
  min_area = np.min(area)
  perchange_area_region3.append((max_area-min_area)/max_area)
  max_perim = np.max(perim)
  min_perim = np.min(perim)
  perchange_perim_region3.append((max_perim-min_perim)/max_perim)
plt.title('Percent change of cell area over track in {}'.format(region3))
plt.hist(perchange_area_region3)
plt.savefig(figure_path + '/perchange_area_hist_{}.png'.format(region3))
plt.clf()
file_lines.append('{}/perchange_area_hist_{}.png \n'.format(figure_path, region3))
plt.title('Percent change of cell perimeter over track in {}'.format(region3))
plt.hist(perchange_perim_region3)
plt.savefig(figure_path + '/perchange_perim_hist_{}.png'.format(region3))
plt.clf()
file_lines.append('{}/perchange_perim_hist_{}.png \n'.format(figure_path, region3))

#write lines to text file 
hist_boxplot_figs.writelines(file_lines)
hist_boxplot_figs.close() 