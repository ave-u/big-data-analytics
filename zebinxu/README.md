##Data Summary

| Column | Base Type | Semantic Type | Label count | Summary
|:---:|:---:|:---:|:---:|:---:|
| KY\_CD              | INT  | Three digit code | VALID: 5101231 INVALID: 0 NULL: 0     | Three digits values
| OFNS\_DESC          | TEXT | Description      | VALID: 5082391 INVALID: 0 NULL: 18840 | Text description, contains null values
| PD\_CD              | INT  | Three digit code | VALID: 5096657 INVALID: 0 NULL: 4574  | Three digits values
| PD\_DESC            | TEXT | Description      | VALID: 5096657 INVALID: 0 NULL: 4574  | Text description, contains null values with the size same as its corresponding code
| CRM\_ATPT\_CPTD\_CD | TEXT | Indicator        | VALID: 5101224 INVALID: 0 NULL: 7     | Two possible values: "COMPLETED", "ATTEMPTED"; contains null values
| LAW\_CAT\_CD        | TEXT | Offense level    | VALID: 5101231 INVALID: 0 NULL: 0     | Three possible values: "VIOLATION", "FELONY", and "MISDEMEANOR"
| JURIS\_DESC         | TEXT | Jurisdiction     | VALID: 5101231 INVALID: 0 NULL: 0     | 25 possible values


## Aggregated Values and Count
Aggregate each column and count their frequency. The script used to produce the result: [get\_values\_count.py](https://github.com/ave-u/big-data-analytics/blob/master/zebinxu/get_values_count.py)

[Column 7: KY\_CD](https://raw.githubusercontent.com/ave-u/big-data-analytics/master/zebinxu/result/values_count/col7.csv)

[Column 8: OFNS\_DESC](https://raw.githubusercontent.com/ave-u/big-data-analytics/master/zebinxu/result/values_count/col8.csv)

[Column 9: PD\_CD](https://raw.githubusercontent.com/ave-u/big-data-analytics/master/zebinxu/result/values_count/col9.csv)

[Column 10: PD\_DESC](https://raw.githubusercontent.com/ave-u/big-data-analytics/master/zebinxu/result/values_count/col10.csv)

[Column 11: CRM\_ATPT\_CPTD\_CD](https://raw.githubusercontent.com/ave-u/big-data-analytics/master/zebinxu/result/values_count/col11.csv)

[Column 12: LAW\_CAT\_CD](https://raw.githubusercontent.com/ave-u/big-data-analytics/master/zebinxu/result/values_count/col12.csv)

[Column 13: JURIS\_DESC](https://raw.githubusercontent.com/ave-u/big-data-analytics/master/zebinxu/result/values_count/col13.csv)


## Base type, Semantic data type, Label
Assign each value a base type, a semantic data type, and a label (VALID/INVALID/NULL). The script used to produce the result: [get\_label.py](https://github.com/ave-u/big-data-analytics/blob/master/zebinxu/get_label.py)

## Label Count
Count label for each column. The script used to produce the result: [get\_label\_count.py](https://github.com/ave-u/big-data-analytics/blob/master/zebinxu/get_label_count.py)


