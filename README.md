# Data Science consumer_complaints
Given the consumer complaints data, task is to identify the number of complaints filed and how they're spread across different companies. https://github.com/InsightDataScience/consumer_complaints

## Dataset
Consumer.csv (Smaller version uploaded): Consult the Consumer Finance Protection Bureau's technical documentation for a description of each field.

## Implementation
Implemented using python by using only default data structures (Not pandas or external libraries) with the objective of understanding basic data structure building blocks needed in data science.

## Results
The analysis output is written to report.csv where each line in the output file corresponds to :
- product (name should be written in all lowercase)
- year
- total number of complaints received for that product and year
- total number of companies receiving at least one complaint for that product and year
- highest percentage (rounded to the nearest whole number) of total complaints filed against one company for that product and year. Use standard rounding conventions (i.e., Any percentage between 0.5% and 1%, inclusive, should round to 1% and anything less than 0.5% should round to 0%)
