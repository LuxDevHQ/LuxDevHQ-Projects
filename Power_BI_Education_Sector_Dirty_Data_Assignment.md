### **Power BI End-to-End Project: Education Sector Dirty Data**

### **Project Overview**

You have been provided with a dirty flat dataset named **“[Student's Dirty Data.xlsx](https://github.com/LuxDevHQ/LuxDevHQ-Projects/blob/main/Student's%20Dirty%20Data.xlsx)”**.

This dataset contains education-related records covering students, schools, teachers, subjects, locations, academic performance, payments, and other related details.

Your task is to work on this dataset from start to finish using **Power BI**. This project is meant to test your ability to clean messy data, create a proper data model, write DAX measures, analyze the data, and build a useful dashboard.

You are expected to apply the skills you have already learned in **Power Query, data cleaning, data modeling, relationships, DAX, dashboard design, data analysis, and insight communication**.

This is not only a dashboarding task. It is a full **end-to-end Power BI project**.

---

### **Part 1: Data Understanding and Cleaning**

Start by loading the **“Student's Dirty Data.xlsx”** file into Power BI.

Before cleaning, carefully inspect the dataset and understand what each column represents. Some columns may not be clearly named, so you are expected to rename columns appropriately based on the values they contain.

Clean the dataset properly and ensure that the final data is ready for analysis.

Pay attention to issues such as:

* Inconsistent category names
* Mixed uppercase and lowercase values
* Wrong spellings
* Short forms and abbreviations
* Null values
* Error values
* Incorrect data types
* Invalid numeric values
* Dates stored in the wrong format
* Duplicate or repeated records
* Inconsistent location names
* Inconsistent school, teacher, and student details
* Incorrect or unclear values in revenue, performance, attendance, and payment-related fields

Your goal is to make the cleaned data consistent, reliable, and ready for modeling.

Do not remove data blindly. Make reasonable cleaning decisions and document the assumptions you make.

---

### **Part 2: Data Modeling**

After cleaning the dataset, create a proper data model from the flat table.

The dataset should **not remain as one flat table**. You are expected to normalize it into meaningful tables where necessary.

Think carefully about which columns belong together.

You may need to create tables such as:

* Student table
* Teacher table
* School table
* Subject table
* Location table
* Academic performance or assessment table
* Payment or revenue table

Also think carefully about the location hierarchy:

**Country → Region → County → Sub-county**

The location table should be reusable where possible. For example, both students and teachers may belong to locations, so avoid unnecessary duplication if a shared location structure makes sense.

Your final model should clearly define:

* Primary keys
* Foreign keys
* Fact table
* Dimension tables
* Correct relationships
* Cardinality
* Filter direction

You may use a **star schema** or **snowflake schema** where appropriate, but your final model should be logical, clean, and easy to explain.

---

### **Part 3: Measures and Calculations**

Create the necessary DAX measures to support your analysis.

Your measures should help answer important education and business questions from the dataset.

You may need measures related to:

* Number of students
* Number of schools
* Number of teachers
* Total revenue collected
* Average score
* Pass rate
* Failure rate
* Attendance rate
* Average fee paid
* Outstanding balance
* Subject performance
* School performance
* County or region performance

Create clean and reusable measures. Avoid creating unnecessary calculated columns where a measure would be more appropriate.

---

### **Part 4: Analysis Questions**

Use your cleaned and modeled data to answer the following questions.

### **Student and School Analysis**

1. Which school has the highest number of students?
2. Which county has the highest number of students?
3. Which region has the highest student population?
4. How many students are enrolled in each school?
5. What is the gender distribution of students across schools?
6. Which sub-county has the lowest number of students?
7. Which school has the most diverse student population by county or region?

### **Teacher Analysis**

8. How many teachers are available in the dataset?
9. Which teacher is assigned to the highest number of students?
10. Which school has the highest teacher-to-student ratio?
11. Which county or region has the highest number of teachers?
12. Are teachers and students distributed evenly across locations?

### **Academic Performance Analysis**

13. What is the average score across all students?
14. Which school has the highest average score?
15. Which subject has the highest average score?
16. Which subject has the lowest average score?
17. Which teacher’s students have the highest average performance?
18. Which county has the best average performance?
19. Which students are performing below the expected pass mark?
20. What is the overall pass rate?
21. What is the failure rate by subject?
22. Which schools need academic support based on performance?

### **Revenue and Payment Analysis**

23. What was the total revenue collected?
24. Which school generated the highest revenue?
25. Which county generated the highest revenue?
26. What is the total outstanding balance?
27. Which students have pending balances?
28. What is the average fee paid per student?
29. Which payment method is used most frequently?
30. Which school has the highest unpaid balance?

### **Location-Based Analysis**

31. Which county performs best academically?
32. Which region generates the highest revenue?
33. Which sub-county has the highest average student score?
34. Which locations have high student numbers but low performance?
35. Which locations have high revenue but low attendance or performance?

---

### **Part 5: Dashboard Requirements**

Create a Power BI dashboard that presents the cleaned and modeled data clearly.

Your dashboard should include pages or sections for:

* Key Performance Indicators
* Student analysis
* School analysis
* Teacher analysis
* Academic performance analysis
* Revenue analysis
* Location-based analysis

Your dashboard should allow users to filter by:

* School
* County
* Region
* Sub-county
* Teacher
* Subject
* Gender
* Payment status
* Term or academic period, where applicable

Use suitable visuals such as:

* KPI cards
* Bar charts
* Column charts
* Line charts
* Donut charts
* Matrix tables
* Maps, where useful
* Slicers
* Tooltips

The dashboard should be clean, professional, interactive, and easy to understand.

---

### **Part 6: Final Deliverables**

Each group should submit the following:

1. Names and emails of all group members
2. Cleaned Power BI file
3. Properly modeled data with relationships
4. DAX measures used in the report
5. Dashboard pages
6. A short explanation of your data model
7. A short summary of the insights discovered
8. A brief note explaining the major cleaning decisions made

---

### **Important Reminder**

This project is meant to test your ability to work through a real-world messy dataset.

You are expected to demonstrate your ability to:

* Understand dirty data
* Clean and prepare data
* Normalize a flat table
* Build a good schema
* Create relationships
* Write useful DAX measures
* Analyze the data
* Build an interactive dashboard
* Communicate insights clearly

Submit a professional Power BI report that shows both technical understanding and clear business insight.
