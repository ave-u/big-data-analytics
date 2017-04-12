# big-data-analytics

### Useful Link
[Data Footnotes](http://www.nyc.gov/html/nypd/downloads/pdf/analysis_and_planning/nypd_incident_level_data_footnotes.pdf)

### Responsibility

#### Xiaohang Su
-------------
Columns:

1. CMPLNT_NUM
	* Randomly generated persistent ID for each complaint

2. CMPLNT\_FR_DT
	* Exact date of occurrence for the reported event (or starting date of occurrence, if CMPLNT_TO_DT exists)

3. CMPLNT\_FR_TM
	* Exact time of occurrence for the reported event (or starting time of occurrence, if CMPLNT_TO_TM exists)

4. CMPLNT\_TO_DT
	* Ending date of occurrence for the reported event, if exact time of occurrence is unknown

5. CMPLNT\_TO_TM
	* Ending time of occurrence for the reported event, if exact time of occurrence is unknown

6. RPT_DT
	* Date event was reported to police

7. BORO_NM
	* The name of the borough in which the incident occurred

8. ADDR\_PCT_CD
	* The precinct in which the incident occurred

#### Chuan Long
---------------
Columns:

1. LOC_OF_OCCUR_DESC
	* Data Type:Plain Text
	* Specific location of occurrence in or around the premises(inside, opposite of, front of, rear of)

2. PREM_TYP_DESC
	* Data Type:Plain Text
    * Specific description of premises; grocery store, residence, street, etc. 

3. PARKS_NM
	* Data Type:Plain Text
	* Name of NYC park, playground or greenspace of occurrence, if applicable (state parks are not included)

4. HADEVELOPT
	* Data Type:Plain Text
    * Name of NYCHA housing development of occurrence, if applicable

5. X_COORD_CD
	* Data Type:Number
    * X-coordinate for New York State Plane Coordinate System, Long Island Zone, NAD 83, units feet (FIPS 3104)

6. Y_COORD_CD
	* Data Type:Number
	* Y-coordinate for New York State Plane Coordinate System, Long Island Zone, NAD 83, units feet (FIPS 3104)

7. Latitude
	* Data Type:Number
	* Latitude coordinate for Global Coordinate System, WGS 1984, decimal degrees (EPSG 4326)

8. Longitude
	* Data Type:Number
	* Longitude coordinate for Global Coordinate System, WGS 1984, decimal degrees (EPSG 4326)
