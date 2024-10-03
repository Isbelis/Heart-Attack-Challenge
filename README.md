# Heart Attack Prediction and Dashboard Project

## Introduccion

This project focuses on heart attack prediction using machine learning models and Tableau dashboards. The topic was chosen due to the alarming statistics reported by the CDC: heart disease is the leading cause of death for men, women, and most racial/ethnic groups in the United States, including African Americans, Hispanics, and whites. Approximately 660,000 people die from heart disease each year in the U.S., equating to 1 in every 4 deaths or one person every 40 seconds. This project addresses the need for accurate, data-driven healthcare solutions to predict heart attack risks.

Machine learning allows for the analysis of complex clinical and demographic data, uncovering patterns that improve early prediction and intervention. By integrating these models with Tableau, we can create interactive visualizations, making insights accessible to healthcare providers and decision-makers. This combined approach aims to enhance heart disease prevention and improve patient outcomes.
## Analysis:

This analysis included the following:

### 1. Cleaning Process**:
The dataset `heart_2022_no_nans` was updated by adding latitude and longitude columns. It was merged with `US_GeoCode.csv`, with data for Guam and the Virgin Islands added manually. This dataset was prepared for creating visualizations and a story dashboard in Tableau. The `heart_2020_cleaned` dataset was used directly for the machine learning experiment without needing further cleaning.

### 3. Design Considerations
For the visual components of the project, consistency in design was key. We employed an `autumn color palette` (featuring shades of orange, red, and brown) and used the `Bootswatch 4.5.2 United theme` to ensure that the exploratory data analysis, dashboards, and webpage all maintained a cohesive look and feel.
  
### 4. Machine Learning Experiment

#### Model Creation:
Given the pre-cleaned data, the focus was encoding categorical variables and scaling numerical data. Notably:
    **Age categories**: Averaged between ranges, then added to the numerical features.
    **General Health (GenHealth)**: Encoded on a 5-category scale (poor to very good).
    **Race**: Encoded into 6 numbers representing different race options.

After testing various models, the **Decision Tree Classifier** was chosen for its highest accuracy in predicting positive results. Despite a modest 25% accuracy, the model helps identify high-risk individuals, focusing more on positive predictive values over negative ones.

#### Web Integration:
A user-friendly website was created to interact with the model. Users can input their data, which is then processed and run through the trained machine learning model. Results are displayed interactively on the website.
![prediction](https://github.com/user-attachments/assets/9d78af6e-bcf7-4ebc-8e2b-286aed74d037)

### 5. Dashboards 
This project includes two story dashboards, each displaying descriptive statistics and relationships between variables relevant to heart attack prediction. Both stories contain four dashboards, providing insights into various factors contributing to heart attacks. 

**Dashboard 1**: 

![dashboard_1jpg](https://github.com/user-attachments/assets/899ce58f-25f2-4fd9-8b4b-d575770e52ed)

**link**: https://public.tableau.com/views/Project_4_Group_12/HeartDiseases?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

**Dashboard 2**
![Dashboard_2](https://github.com/user-attachments/assets/d55cfcfc-0c36-4b3f-a033-7aa39ef13bb3)

**link**: https://public.tableau.com/shared/PW9DM2MWS?:display_count=n&:origin=viz_share_link

## Folders:

### 1. EDA Folder (Exploratory Data Analysis):

  **Resources**: Contains reference files like geographical data `US_GeoCode.csv`, `world_country_and_usa_states_latitude_and_longitude_values.csv`, dataset `heart_2022_no_nans.csv`, and images were used for visualizations in the dashboard.
  
  **Files**:
            **1. heart_attack_2022_cleaning.ipynb**: A Jupyter notebook that handles the cleaning of the `heart_2022_no_nans.csv` dataset.
            **2. heart_attack_2022_location.csv**: The cleaned dataset, saved as a CSV file for further analysis and visualization.
            **3. heart_attack_2022_viz.ipynb**: A notebook focused on visualizing heart disease data using various charts and plots.

### 2. ML Folder (Machine Learning):
  **Files**:
    **- modelHelper.py**: A Python script with helper functions used for building machine learning models.
    **- model_creation.ipynb**: A Jupyter notebook for creating machine learning models based on the cleaned heart disease dataset.
    **- heart_2020_cleaned.csv**
    
### 3. Resources: 
Contains the original datasets `heart_2020_cleaned.csv` and `heart_attack_2022_location.csv`.

## Files:

### Heart Diseases Analysis.pptx: The final presentation summarizing the project's analysis, results, and conclusions.
### Project 4 Proposal – Group 12.docx.pdf: A PDF document containing the initial project proposal.
### Write-up-project-4-group-12.pdf: The final report on the project, detailing methods, analysis, and findings.

  
## Web Version:
  
Explore the project online through the following link:
  https://isbelis.pythonanywhere.com/

This README provides an overview of the project's goals, the machine learning and visualization tools used, and the project structure, offering users insight into heart attack prediction and prevention strategies.


## Reference

 https://public.tableau.com/app/search/vizzes/heart%20attack
 
 https://public.tableau.com/app/profile/adrian.tan2691/viz/HeartAttackDistributions/Demographics
 
 https://www.quantizeanalytics.co.uk/tableau-healthcare-dashboard-examples/
 
 https://www.analyticsvidhya.com/blog/2022/06/machine-learning-for-heart-disease-prediction/
 
 https://www.analyticsvidhya.com/blog/2022/02/heart-disease-prediction-using-machine-learning-2/
 
 https://www.analyticsvidhya.com/blog/2022/02/heart-disease-prediction-using-machine-learning/
 
 https://github.com/g-shreekant/Heart-Disease-Prediction-using-Machine-Learning/blob/master/Heart_disease_prediction.ipynb
 
 https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10378171/







