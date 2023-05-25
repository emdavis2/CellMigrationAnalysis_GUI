.PHONY: clean
.PHONY: d3-vis
.PHONY: visualization
.PHONY: 

clean:
	rm -rf sentinels
	rm -rf .created-dirs

.created-dirs:
	mkdir -p sentinels
	touch .created-dirs

# Create the autocorrelation figures for glass data
sentinels/ACF_figures_glass.txt: .created-dirs 2023_03_30_Data/glass_data\
 functions/acf_functions.py functions/compile_data_tracks_function.py\
 functions/libraries/track_functions.py
	python3 GenerateDataACF.py '2023_03_30_Data/glass_data' 30 'glass' 'GUI_test_figures'

# Create the autocorrelation figures for soft gel data
sentinels/ACF_figures_soft_gel.txt: .created-dirs 2023_03_30_Data/soft_gel_data\
 functions/acf_functions.py functions/compile_data_tracks_function.py\
 functions/libraries/track_functions.py
	python3 GenerateDataACF.py '2023_03_30_Data/soft_gel_data' 30 'soft_gel' 'GUI_test_figures'

# Create the autocorrelation figures for stiff gel data
sentinels/ACF_figures_stiff_gel.txt: .created-dirs 2023_03_30_Data/stiff_gel_data\
 functions/acf_functions.py functions/compile_data_tracks_function.py\
 functions/libraries/track_functions.py
	python3 GenerateDataACF.py '2023_03_30_Data/stiff_gel_data' 30 'stiff_gel' 'GUI_test_figures'

# Create the boxplot and histogram figures for both glass and gel data
sentinels/histogram_boxplot.txt: .created-dirs 2023_03_30_Data/glass_data\
 2023_03_30_Data/soft_gel_data 2023_03_30_Data/stiff_gel_data functions/compile_data_tracks_function.py\
 functions/libraries/track_functions.py
	python3 GenerateDataHistogramBoxplot.py '2023_03_30_Data/glass_data' '2023_03_30_Data/soft_gel_data' '2023_03_30_Data/stiff_gel_data' 60 'glass' 'soft_gel' 'stiff_gel' 'GUI_test_figures'

# Create the boxplot and histogram figures for both glass and gel data
sentinels/cellshape_histogram.txt: .created-dirs 2023_03_30_Data/glass_data\
 2023_03_30_Data/soft_gel_data 2023_03_30_Data/stiff_gel_data functions/compile_data_tracks_function.py\
 functions/libraries/track_functions.py
	python3 CellShapeOverTrack.py '2023_03_30_Data/glass_data' '2023_03_30_Data/soft_gel_data' '2023_03_30_Data/stiff_gel_data' 60 'glass' 'soft_gel' 'stiff_gel' 'GUI_test_figures'