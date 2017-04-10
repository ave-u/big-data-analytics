# big-data-analytics


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