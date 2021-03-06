# big-data-analytics

### Useful Links

[Project Report](https://docs.google.com/document/d/14SnZ_6uk6oxmgjR6I7VQr0qOu1YXDGigYqDEVj2ZFw0/edit)

[Data Footnotes](http://www.nyc.gov/html/nypd/downloads/pdf/analysis_and_planning/nypd_incident_level_data_footnotes.pdf)

[NYPD Crime Data](https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Historic/qgea-i56i)

### Responsibilities

#### Xiaohang Su
-------------
Columns:

1. CMPLNT_NUM
	* Data Type: Number
	* Randomly generated persistent ID for each complaint

2. CMPLNT\_FR_DT
	* Data Type: Date & Time
	* Exact date of occurrence for the reported event (or starting date of occurrence, if CMPLNT_TO_DT exists)

3. CMPLNT\_FR_TM
	* Data Type: Plain Text
	* Exact time of occurrence for the reported event (or starting time of occurrence, if CMPLNT_TO_TM exists)

4. CMPLNT\_TO_DT
	* Data Type: Date & Time
	* Ending date of occurrence for the reported event, if exact time of occurrence is unknown

5. CMPLNT\_TO_TM
	* Data Type: Plain Text
	* Ending time of occurrence for the reported event, if exact time of occurrence is unknown

6. RPT_DT
	* Data Type: Date & Time
	* Date event was reported to police

7. BORO_NM
	* Data Type: Plain Text
	* The name of the borough in which the incident occurred

8. ADDR\_PCT_CD
	* Data Type: Number
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

#### Zebin Xu
---------------
Columns:

1. KY_CD
    * Data Type: Number
    * Three digit offense classification code
2. OFNS_DESC
    * Data Type: Plain Text
    * Description of offense corresponding with key code
3. PD_CD
    * Data Type: Number
    * Three digit internal classification code (more granular than Key Code)
4. PD_DESC
    * Data Type: Plain Text
    * Description of internal classification corresponding with PD code (more granular than Offense Description)
5. CRM_ATPT_CPTD_CD
    * Data Type: Plain Text
    * Indicator of whether crime was successfully completed or attempted, but failed or was interrupted prematurely
6. LAW_CAT_CD
    * Data Type: Plain Text
    * Level of offense: felony, misdemeanor, violation
7. JURIS_DESC
    * Data Type: Plain Text
    * Jurisdiction responsible for incident. Either internal, like Police, Transit, and Housing; or external, like Correction, Port Authority, etc.

### Assumption

*	There are connections between festivals and crimes.
*	There are more crimes happened in night than daylight.
