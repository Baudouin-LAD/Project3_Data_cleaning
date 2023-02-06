<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Clean your data!
## Content
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Project Steps](#project-steps)
- [Deliverables](#deliverables)
- [Presentation](#presentation)

## Project Overview

The goal of this project is to combine everything you have learned about data wrangling, cleaning, and manipulation with Pandas so you can see how it all works together.


## Dataset

2 - Entrepreneurial competency in university students

The data set provides data on potential candidates to become co-founders of a business.

columns: 'education_sector', 'target_individual_project_', 'age', 'gender',
       'city', 'influenced', 'perseverance', 'desire_to_take_initiative',
       'competitiveness', 'self_reliance', 'strong_need_to_achieve',
       'self_confidence', 'good_physical_health', 'mental_disorder',
       'key_traits', 'reasons_for_lack', 'target_ent_competency',

From the data available we want to come up with a forumla for deciding who is the best candidate for co-founding a business.



## Process

- Importing
* Start a python file in Spyder
* Import the data using Pandas.


Cleaning

Reformated column headers to be snake case
Checked for null data
	- replaced missing age with mean age
	- removed rows with missing data between 'perseverance' & 'good_physical_health' since this was key to our analysis
	- replaced missing reasons for exclusion with 'no reason'

We examined the data for potential issues 
	*  naming inconsistency
	*  outliers
	*  duplicates
	*  low variance

Manipulation (Encoding)
 - columns with yes and no values were replaced with true and false
 - dummy variables created for education_sector and reasons_for_lack

Exporting to SQL
 - csv file exported from python
 - SQL alchemy used to connect python and SQL
 - SQL code run on both SQL and python

## Results

1. AVERAGE AGE OF STUDENTS IN THE STUDY

'Teaching Degree (e.g. B.Ed)','19'
'Language and Cultural Studies','19'
'Mathematics or Natural Sciences','19'
'Medicine, Health Sciences','20'
'Humanities and Social Sciences','20'
'Economic Sciences, Business Studies, Commerce and Law','20'
'Engineering Sciences','20'
'Others','20'
'Art, Music or Design','21'

2. INDIVIDUAL STUDENTS WITH HIGHEST SCORE BASED ON A SUM OF SCORES  FROM 'perseverance', 'desire_to_take_initiative', 'competitiveness', 'self_reliance', 'strong_need_to_achieve', 'self_confidence', 'good_physical_health',

'32','Engineering Sciences','35'
'34','Engineering Sciences','35'
'101','Engineering Sciences','35'
'113','Engineering Sciences','35'
'141','Teaching Degree (e.g. B.Ed)','35'
'181','Economic Sciences, Business Studies, Commerce and Law','35'


3. BEST SCORES BY EDUCATIONAL GROUP

'Teaching Degree (e.g. B.Ed)','26'
'Language and Cultural Studies','26'
'Engineering Sciences','25.785046728971963'


##Obstacles

* A lot of missing data that we had to assign values to 
* Encoding data that was concatenated in 1 single column
* SQL Alchemy - struggling to connect SQL with Python


## Deliverables

https://github.com/Baudouin-LAD/Project3_Data_cleaning.git

* **CSV file with clean data** containing the results of the data wrangling work.
* **Python file** containing all Python code and commands used in the importing, cleaning, manipulation, and exporting of the data set.
* **MySQL queries file** containing the code to obtain table of the analysis.
* **A ``README.md`` file** containing a detailed explanation of the process followed in the importing, cleaning, manipulation, and exporting of the data as well as the results, obstacles encountered, and lessons learned. 

## Presentation

https://www.canva.com/design/DAFZ0A-ilnQ/Gc_uFk1SH6BL8QSI2WtcxQ/edit






