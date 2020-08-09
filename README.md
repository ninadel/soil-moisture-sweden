# Soil Moisture Sweden Project

This project aims to evaluate satellite and model soil moisture products for Sweden. 

Analyses include:

* Statistical evaluation against in-situ soil moisture data from [ICOS network ecosystem stations](https://www.icos-cp.eu/observations/ecosystem/stations)
* Statistical evaluation against the [ERA5-Land reanalysis dataset](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-land)
* Triple collocation analysis

## Data Sources

### ESA ASCAT 12.5 H115

* http://hsaf.meteoam.it/documents/H115_ASCAT_SSM_CDR_v5_PUM_v0.1.pdf

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

### SMAP
* https://search.earthdata.nasa.gov/projects?projectId=6586843843

* SMAP L3 (SPL3SMP) https://nsidc.org/data/SPL3SMP

* SMAP L3 Enhanced (SPL3SMP_E) https://nsidc.org/data/SPL3SMP_E

* SMAP L4 (SPL4SMAU)

### Sentinel-1

* https://land.copernicus.eu/global/products/ssm

### SMOS
* SMOS-BEC
* SMOS-IC


## Tools/Packages

In addition to standard data analysis packages (e.g. pandas), the following packages are used to process and analyze data:

* [pytesmo](https://pytesmo.readthedocs.io/en/latest) for traditional statistical evaluation and triple collocation analysis
* [xarray](http://xarray.pydata.org/) for NetCDF reading, processing, and conversion
* [xesmf](https://xesmf.readthedocs.io/en/latest/) for NetCDF regridding

## Credits

Nina del Rosario

MSc student in GIS at Lund University