## Environment Setup

```module load python/gnu/3.4.4
export PYSPARK_PYTHON=/share/apps/python/3.4.4/bin/python
export PYTHONHASHSEED=0
export SPARK_YARN_USER_ENV=PYTHONHASHSEED=0
alias hfs='/usr/bin/hadoop fs'
```
___

## How To Run

### To analyse the column description

	
`sh run_analyseColumns.sh	
`

 Then

	
`sh merge_analyseColumns.sh	
`

 To merge the formatting output of the analysed columns

### To get the data that we need to plot

	
`sh run_plotColumns.sh	
`

Then

	
`sh merge_plotColumns.sh	
`

To merge the dataset that we need to plot for the first part

> We are done!

___

## Columns Description

1. Column15 - LOC_OF_OCCUR_DESC
	* Data Type:Plain Text
	* Description: Specific location of occurrence in or around the premises(inside, opposite of, front of, rear of)
	* Data quality: 
		- Valid Value: 3973890 rows
			* The most frequently values: 'INSIDE', 'FRONT OF', 'OPPOSITE OF', 'REAR OF', 'OUTSIDE'
		- Null Value: 1127128 rows
		- Invalid Value: 213 rows, there are some rows that are blank spacing
	

2. Column16 - PREM_TYP_DESC
	* Data Type:Plain Text
    * Specific description of premises; grocery store, residence, street, etc. 
	* Data quality
		- Valid Value: 5067952 rows
			* The most frequently values: 'STREET', 'RESIDENCE - APT. HOUSE', 'RESIDENCE-HOUSE', 'RESIDENCE - PUBLIC HOUSING', 'OTHER', etc.
		- Null Value: 33279 rows. 
		- Invalid Value: 0 row

3. Column17 - PARKS_NM
	* Data Type:Plain Text
	* Name of NYC park, playground or green space of occurrence, if applicable (state parks are not included)
	* Data quality
		- Valid Value: 7599 rows
			* 'CENTRAL PARK', 'FLUSHING MEADOWS CORONA PARK', 'RIVERSIDE PARK', "ST. MARY'S PARK BRONX", 'MARCUS GARVEY PARK', 'CONEY ISLAND BEACH & BOARDWALK', etc.
		- Null Value: 5093632 rows, It is reasonable when there are many null values, because this value would exist only if applicable
		- Invalid Value: 0 row

4. Column18 - HADEVELOPT
	* Data Type:Plain Text
    * Name of NYCHA housing development of occurrence, if applicable
	* Data quality
		- Valid Value: 253205 rows
			* 'CASTLE HILL', 'VAN DYKE I', 'MARCY', 'LINCOLN', 'BUTLER', 'GRANT', 'DOUGLASS', 'LINDEN', 'FARRAGUT', 'PINK'
		- Null Value: 4848026 rows, It is reasonable when there are many null values, because this value would exist only if applicable
		- Invalid Value: 0 row

5. Column19 - X_COORD_CD
	* Data Type:Number
    * X-coordinate for New York State Plane Coordinate System, Long Island Zone, NAD 83, units feet (FIPS 3104)
		- Valid Value: 4913085 rows
		- Null Value: 188146 rows. The coordinate value should be exist anyway.
		- Invalid Value: 0 row

6. Column20 - Y_COORD_CD
	* Data Type:Number
	* Y-coordinate for New York State Plane Coordinate System, Long Island Zone, NAD 83, units feet (FIPS 3104)
		- Valid Value: 4913085 rows
		- Null Value: 188146 rows. The coordinate value should be exist anyway.
		- Invalid Value: 0 row

7. Column21 - Latitude
	* Data Type:Number
	* Latitude coordinate for Global Coordinate System, WGS 1984, decimal degrees (EPSG 4326)
		- Valid Value: 4913085 rows
		- Null Value: 188146 rows. The coordinate value should be exist anyway.
		- Invalid Value: 0 row

8. Column22 - Longitude
	* Data Type:Number
	* Longitude coordinate for Global Coordinate System, WGS 1984, decimal degrees (EPSG 4326)
		- Valid Value: 4813085 rows
		- Null Value: 188146 rows. The coordinate value should be exist anyway.
		- Invalid Value: 0 row

