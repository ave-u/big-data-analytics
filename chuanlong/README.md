## Columns Description

 
1. Column15 - LOC_OF_OCCUR_DESC
	* Data Type:Plain Text
	* Description: Specific location of occurrence in or around the premises(inside, opposite of, front of, rear of)
	* Data quality: 
		- Valid Value: 3973890 rows
			* The most frequently values: 'INSIDE', 'FRONT OF', 'OPPOSITE OF', 'REAR OF', 'OUTSIDE'
		- Null Value: 1127128 rows
		- Invalid Value: 213 rows (" ")
	

2. Column16 - PREM_TYP_DESC
	* Data Type:Plain Text
    * Specific description of premises; grocery store, residence, street, etc. 
	* Data quality
		- Valid Value: 5067952 rows
			* The most frequently values: 'STREET', 'RESIDENCE - APT. HOUSE', 'RESIDENCE-HOUSE', 'RESIDENCE - PUBLIC HOUSING', 'OTHER', etc.
		- Null Value: 33279 rows 
		- Invalid Value: 0 row

3. Column17 - PARKS_NM
	* Data Type:Plain Text
	* Name of NYC park, playground or greenspace of occurrence, if applicable (state parks are not included)
	* Data quality
		- Valid Value: 7599 rows
			* 'CENTRAL PARK', 'FLUSHING MEADOWS CORONA PARK', 'RIVERSIDE PARK', "ST. MARY'S PARK BRONX", 'MARCUS GARVEY PARK', 'CONEY ISLAND BEACH & BOARDWALK', etc.
		- Null Value: 0 row
		- Invalid Value: 5093632 rows

4. Column18 - HADEVELOPT
	* Data Type:Plain Text
    * Name of NYCHA housing development of occurrence, if applicable
	* Data quality
		- Valid Value: 253205 rows
			* 'CASTLE HILL', 'VAN DYKE I', 'MARCY', 'LINCOLN', 'BUTLER', 'GRANT', 'DOUGLASS', 'LINDEN', 'FARRAGUT', 'PINK'
		- Null Value: 0 row
		- Invalid Value: 4848026 rows

5. Column19 - X_COORD_CD
	* Data Type:Number
    * X-coordinate for New York State Plane Coordinate System, Long Island Zone, NAD 83, units feet (FIPS 3104)
		- Valid Value: 4913085 rows
		- Null Value: 0 row
		- Invalid Value: 188146 rows

6. Column20 - Y_COORD_CD
	* Data Type:Number
	* Y-coordinate for New York State Plane Coordinate System, Long Island Zone, NAD 83, units feet (FIPS 3104)
		- Valid Value: 4913085 rows
		- Null Value: 0
		- Invalid Value: 188146 rows 

7. Column21 - Latitude
	* Data Type:Number
	* Latitude coordinate for Global Coordinate System, WGS 1984, decimal degrees (EPSG 4326)
		- Valid Value: 4913085 rows
		- Null Value: 0 rows
		- Invalid Value: 188146 rows

8. Column22 - Longitude
	* Data Type:Number
	* Longitude coordinate for Global Coordinate System, WGS 1984, decimal degrees (EPSG 4326)
		- Valid Value: 4813085 rows
		- Null Value: 0 row
		- Invalid Value: 188146 rows

