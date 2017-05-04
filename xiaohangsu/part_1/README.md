### ENVIRONMENT SETUP
```
module load python/gnu/3.4.4
export PYSPARK_PYTHON=/share/apps/python/3.4.4/bin/python
export PYTHONHASHSEED=0
export SPARK_YARN_USER_ENV=PYTHONHASHSEED=0
```

start ```pyspark2```

### GETTING START
> Caveat: Do this in dumbo and start.sh might need chmod for excute


Simply as:

```
./start.sh &lt;argument group>
```
arugment group can be 1,2,3,4,5,6,14,15

For example, run col1.py col2.py col14.py do ```./start.sh 1 2 14```

Then it everything goes well, there would generate folders:

* **log/** all column script output logs
* **out/** all column script output
* **plotData/** all data generated for mathplotlib

### COLUMN DESCRIPTION
> Caveat: all column was analysed seperately during count null value and invalid.

#### Column 1
Description: Randomly generated persistent ID for each records.

* No **null** value
* Range form 100000228 to 999999904

#### Column 2
Description: Exact date of occurrence for the reported event

* **null** value: **655** rows
* Not invalid data, but
	* have **7** records on year 1015
		*  Drag out all those year 1015 record with year 2015 in **column 3**, we view those as *human error* and correct year to 2015.
	* year range from 1900 to 2015


#### Column 3
Description: Exact time of occurrence for the reported event

* **null** value: **48** rows
* "Invalid" data: **903** rows
	* all is ```24:00:00```, which can transform into ```00:00:00```, we view these data as valid data and transform into correct format ```00:00:00```. 
* Second is all ```0``` except one row recorded ```1```.

#### Column 4
Description: Ending date of occurrence for the reported event

* **null** value: **1391478** rows 
* Not invalid data, but
	* have **1** record on year 2090
		* When drag this record out and find it happens on year 2009, I think it is *human error* for this record. We decide to keep it and change year to 2009.
	* year range from 1912 to 2015

#### Column 5
Description: Ending time of occurrence for the reported event

* **null** value: **1387785** rows
* "Invalid" data: **1376** rows
	* all is ```24:00:00```, which can transform into ```00:00:00```, we view these data as valid data and transform into correct format ```00:00:00```. 
* Second is all ```0```.

#### Column 6
Description: Date event was reported to police

* **null** value: **0** rows
* Invalid data: **0** rows
* All data start from 01/01/2006 to 12/31/2015, 0 null value and invalid data might be data collection started at 2006, and all data happened before 2006 was reset to record date. **In our analysis, we dump all data happened before 2006**.

#### Column 14
Description: The name of the borough in which the incident occurred

Only five possible value: ```['BRONX', 'BROOKLYN', 'MANHATTAN', 'QUEENS', 'STATEN ISLAND']```

* **null** value:  **463** rows
* Invalid data: **0** rows, which means all data in five possible values.

#### Column 15
Description: The precinct in which the incident occurred (According to map)

* **null** value: **390** rows
* Invalid data: **0** rows, all with an **int** value in cell.
* Data range from 1 to 123