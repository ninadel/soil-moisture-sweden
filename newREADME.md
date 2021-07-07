# Soil Moisture Sweden Project

## Overview 
* Description
* Motivation
* Who is involved

## Data selection & acquisition
* Based on existing literature (what products work best), temporal availability, spatial availability, spatial resolution
* Special considerations for Northern Europe (gaps in data)
* Independence of products for triple collocation analysis (active, passive, model)
* NetCDF

### In-situ data
* ICOS

### Satellite data


## Data processing
* Regrid from native => common resolution
* Based on GLDAS cells for easy reference, also has land use codes
* Temporal matching
* NetCDF => CSV

### Scripts


## Data analysis

### Station evaluation

### Grid-based evaluation

### Triple collocation analysis


This project aims to evaluate satellite and model soil moisture products for Sweden. 

Analyses include:

* Statistical evaluation against in-situ soil moisture data from [ICOS network ecosystem stations](https://www.icos-cp.eu/observations/ecosystem/stations)

* Statistical evaluation against the [ERA5-Land reanalysis dataset](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-land)

* Triple collocation analysis

## Scripts

* [Python scripts](https://github.com/ninadel/soil-moisture-sweden/tree/master/python) (documentation in progress)

## Data Sources

### Metop ASCAT 12.5 H115

* http://hsaf.meteoam.it/documents/H115_ASCAT_SSM_CDR_v5_PUM_v0.1.pdf
* ASCAT Surface Soil Moisture Climate Data Record v5 12.5 km (H115)

### ESA Climate Change Initiative

* https://www.esa-soilmoisture-cci.org/

* CCI Active

* CCI Passive

* CCI Combined
### ERA5-Land

* https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-land

* ERA5-Land, 0.1 degree resolution
* ERA5-Land 0.25 degree resolution

### GLDAS Noah

* https://search.earthdata.nasa.gov/search?projectId=8364534388
* GLDAS Noah Land Surface Model 3 hourly v2.1

### SMAP
* https://search.earthdata.nasa.gov/projects?projectId=6586843843

* SMAP L3 (SPL3SMP) https://nsidc.org/data/SPL3SMP

* SMAP L3 Enhanced (SPL3SMP_E) https://nsidc.org/data/SPL3SMP_E

* SMAP L4 (SPL4SMAU) https://nsidc.org/data/SPL4SMAU/versions/4

### Sentinel-1

* https://land.copernicus.eu/global/products/ssm
* CGLOPS-1 SSM 1km v1 https://land.copernicus.eu/global/sites/cgls.vito.be/files/products/CGLOPS1_PUM_SSM1km-V1_I1.30.pdf

### SMOS-BEC

* http://bec.icm.csic.es/

* SMOS-BEC L4 http://bec.icm.csic.es/doc/BEC_SMOS_PD_SM_L3v3_L4v5.pdf

### SMOS-IC

* https://www.catds.fr/Products/Available-products-from-CEC-SM/SMOS-IC
* SMOS-IC L3 Soil Moisture [ftp://ext-catds-cecsm:catds2010@ftp.ifremer.fr/Land_products/L3_SMOS_IC_Soil_Moisture/ASC/](ftp://ext-catds-cecsm:catds2010@ftp.ifremer.fr/Land_products/L3_SMOS_IC_Soil_Moisture/ASC/)


## Tools/Packages

In addition to standard data analysis packages (e.g. pandas), the following packages are used to process and analyze data:

* [pytesmo](https://pytesmo.readthedocs.io/en/latest) for traditional statistical evaluation and triple collocation analysis
* [xarray](http://xarray.pydata.org/) for NetCDF reading, processing, and conversion
* [xesmf](https://xesmf.readthedocs.io/en/latest/) for NetCDF regridding

## Credits

Nina del Rosario - MSc student in GIS at Lund University

Supervised by Dr. Zheng Duan at Lund University