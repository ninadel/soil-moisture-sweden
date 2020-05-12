Variables stored in separate files (Header+values)

Filename

	Data_seperate_files_header_startdate(YYYYMMDD)_enddate(YYYYMMDD)_userid_randomstring_currrentdate(YYYYMMDD).zip
	
	e.g., Data_seperate_files_header_20050316_20050601.zip

	
Folder structure

	Networkname
		Stationname

		
Dataset Filename

	CSE_Network_Station_Variablename_depthfrom_depthto_startdate_enddate.ext

	CSE	- Continental Scale Experiment (CSE) acronym, if not applicable use Networkname
	Network	- Network abbreviation (e.g., OZNET)
	Station	- Station name (e.g., Widgiewa)
	Variablename - Name of the variable in the file (e.g., Soil-Moisture)
	depthfrom - Depth in the ground in which the variable was observed (upper boundary)
	depthto	- Depth in the ground in which the variable was observed (lower boundary)
	startdate -	Date of the first dataset in the file (format YYYYMMDD)
	enddate	- Date of the last dataset in the file (format YYYYMMDD)
	ext	- Extension .stm (Soil Temperature and Soil Moisture Data Set see CEOP standard)
	
	e.g., OZNET_OZNET_Widgiewa_Soil-Temperature_0.150000_0.150000_20010103_20090812.stm

	
File Content Sample
	
	REMEDHUS   REMEDHUS        Zamarron          41.24100    -5.54300  855.00    0.05    0.05  (Header)
	2005/03/16 00:00    10.30 U	M	(Records)
	2005/03/16 01:00     9.80 U M

	
Header

	CSE Identifier - Continental Scale Experiment (CSE) acronym, if not applicable use Networkname
	Network	- Network abbreviation (e.g., OZNET)
	Station	- Station name (e.g., Widgiewa)
	Latitude - Decimal degrees. South is negative.
	Longitude - Decimal degrees. West is negative.
	Elevation - Meters above sea level
	Depth from - Depth in the ground in which the variable was observed (upper boundary)
	Depth to - Depth in the ground in which the variable was observed (lower boundary)

	
Record

	UTC Actual Date and Time
	yyyy/mm/dd HH:MM
	Variable Value
	ISMN Quality Flag
	Data Provider Quality Flag, if existing


Network Information

	HOBE
		Abstract: Soil moisture and soil temperature network with 30 stations within the area of major signal contribution of one selected SMOS grid node in the Skjern River Catchment
		Continent: Europe
		Country: Denmark
		Stations: 32
		Status: running
		Data Range: from 2009-09-08
		Type: project
		Url: http://www.hobe.dk/
		Reference: Bircher, S., Skou, N., Jensen, K.H., Walker, J.P., and Rasmussen, L. (2011): A soil moisture and temperature network for SMOS validation in Western Denmark. Hydrology and Earth System Sciences Discussions, 8, 9961-10006, doi:10.5194/hessd-8-9961
		Variables: soil moisture, soil temperature, 
		Soil Moisture Depths: 0.00 - 0.05 m , 0.20 - 0.25 m , 0.50 - 0.55 m , 
		Soil Moisture Sensors: Decagon 5TE, 

