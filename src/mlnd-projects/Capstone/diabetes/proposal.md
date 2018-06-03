# Machine Learning Engineer Nanodegree
## Capstone Proposal

Manas Mukherjee
May 29th, 2018

## Proposal

### Domain Background

Diabetes is a leading chronic disease that affects more than 30 million people in the United States.
The economic impact of diabetes is estimated at $105 billion, according to a study published in 2016 and led by researchers from Imperial College London,
Harvard T.H. Chan School of Public Health and the World Health Organization.

It is a chronic disease that occurs either when the pancreas does not produce enough insulin or when the body cannot effectively use the insulin it produces.
Insulin is a hormone that regulates blood sugar. Hyperglycaemia, or raised blood sugar, is a common effect of uncontrolled diabetes and
over time leads to serious damage to many of the body's systems, especially the nerves and blood vessels.

Leading compnaies as well as startups are actively working on this specific healthcare domain and coming up with AI powered applications on use-cases like
Glucose Monitoring Systems, Nutrition Coaching, Early Diagnosis Tools etc.

#### Motivation

In the last two yearly health check, my blood-sugar(glucose) level and BMI were above the normal range.
Note -

* Glucose : Reference Range: 65-99 mg/dL
* BMI : Reference Range: 18.5-24.9 (calc)  

Since these two factors indicate a pre-diabetes tendency, I would like to take some proactive measures to prevent any future suffering.
The motivation behind working on this important domains is to increase self-awareness and apply my newly learned ML skills in a real-world problem.

References -
1. Worldwide trends in diabetes since 1980:  https://www.thelancet.com/pdfs/journals/lancet/PIIS0140-6736(16)00618-8.pdf
2. Machine Learning for Managing Diabetes: 5 Current Use Cases: https://www.techemergence.com/machine-learning-managing-diabetes-5-current-use-cases/
3. How Machine Learning Is Helping Us Predict Heart Disease and Diabetes: https://hbr.org/2017/05/how-machine-learning-is-helping-us-predict-heart-disease-and-diabetes
4. ML and Data Mining Methods in Diabetes Research: https://www.sciencedirect.com/science/article/pii/S2001037016300733

### Problem Statement

The goal of this project is to build a machine learning model to predict the onset of diabetes based on some diagnostic measures.
The expected outcome of this project is to contribute in the clinical research study related to diabetes.

* Main Objective:
Build a mathematical model to predict whether or not a patient has diabetes, based on certain diagnostic measurements.

* Secondary Objective:
Identify important indicateors or a cluster of features that cause diabetes.

### Datasets and Inputs

In this section, the dataset(s) and/or input(s) being considered for the project should be thoroughly described,
such as how they relate to the problem and why they should be used. Information such as how the dataset or input is (was) obtained,
and the characteristics of the dataset or input, should be included with relevant references and citations as necessary.
 It should be clear how the dataset(s) or input(s) will be used in the project and whether their use is appropriate given the context of the problem.

* Source
https://www.kaggle.com/uciml/pima-indians-diabetes-database
This dataset is originally from the National Institute of Diabetes and Digestive and Kidney Diseases.

* Content
The datasets consists of **8 medical predictor** variables and **one target variable** - Outcome corresponding to the **768 persons**.
Here is the list of predictor variables with their brief description.

|Feature Name| Description |Datetype |
|:-------------|:-------------|:-----|
|Pregnancies | Number of times pregnant |Numeric|
|Glucose | Plasma glucose concentration a 2 hours in an oral glucose tolerance test|Numeric|
|BloodPressure|Diastolic blood pressure (mm Hg)|Numeric|
|SkinThickness|Triceps skin fold thickness (mm)|Numeric|
|Insulin|2-Hour serum insulin (mu U/ml)|Numeric|
|BMI|Body mass index (weight in kg/(height in m)^2)|Numeric|
|DiabetesPedigreeFunction|Diabetes pedigree function|Numeric|
|Age|Age (years)|Numeric|
|**Outcome**|Class variable (0 or 1)|Numeric|

#### Constraint
Several constraints were placed on the selection of these instances from a larger database.
In particular, all patients here are females at least 21 years old of **Pima Indian** heritage.

#### Background details and important characteristics of Pima people
The Pima are a group of Native Americans living in an area consisting of what is now central and southern Arizona.
The majority population of the surviving two bands of the Akimel O'odham are based in two reservations:
the Keli Akimel O'otham on the Gila River Indian Community (GRIC) and the On'k Akimel O'odham on the Salt River Pima-Maricopa Indian Community (SRPMIC).

The Keli Akimel O'odham and the Onk Akimel O'odham have various environmentally based health issues related to the decline of their traditional economy and farming.
**They have the highest prevalence of type 2 diabetes in the world, much more than is observed in other U.S. populations.**
While they do not have a greater risk than other tribes, **the Pima people have been the subject of intensive study of diabetes, in part because they form a homogeneous group.**

Source -
1. Wikipedia - https://en.wikipedia.org/wiki/Pima_people
2. Smith-Morris, Carolyn. "Diabetes Among the Pima: Stories of Survival". Tucson: University of Arizona Press, 2006. ISBN 978-0816527328.
Summary of the above book - https://muse.jhu.edu/article/450458/summary

### Solution Statement
_(approx. 1 paragraph)_

In this section, clearly describe a solution to the problem. The solution should be applicable to the project domain and appropriate for the dataset(s) or input(s) given. Additionally, describe the solution thoroughly such that it is clear that the solution is quantifiable (the solution can be expressed in mathematical or logical terms) , measurable (the solution can be measured by some metric and clearly observed), and replicable (the solution can be reproduced and occurs more than once).

### Benchmark Model
_(approximately 1-2 paragraphs)_

In this section, provide the details for a benchmark model or result that relates to the domain, problem statement, and intended solution. Ideally, the benchmark model or result contextualizes existing methods or known information in the domain and problem given, which could then be objectively compared to the solution. Describe how the benchmark model or result is measurable (can be measured by some metric and clearly observed) with thorough detail.

### Evaluation Metrics
_(approx. 1-2 paragraphs)_

In this section, propose at least one evaluation metric that can be used to quantify the performance of both the benchmark model and the solution model. The evaluation metric(s) you propose should be appropriate given the context of the data, the problem statement, and the intended solution. Describe how the evaluation metric(s) are derived and provide an example of their mathematical representations (if applicable). Complex evaluation metrics should be clearly defined and quantifiable (can be expressed in mathematical or logical terms).

### Project Design
_(approx. 1 page)_

In this final section, summarize a theoretical workflow for approaching a solution given the problem. Provide thorough discussion for what strategies you may consider employing, what analysis of the data might be required before being used, or which algorithms will be considered for your implementation. The workflow and discussion that you provide should align with the qualities of the previous sections. Additionally, you are encouraged to include small visualizations, pseudocode, or diagrams to aid in describing the project design, but it is not required. The discussion should clearly outline your intended workflow of the capstone project.

-----------

**Before submitting your proposal, ask yourself. . .**

- Does the proposal you have written follow a well-organized structure similar to that of the project template?
- Is each section (particularly **Solution Statement** and **Project Design**) written in a clear, concise and specific fashion? Are there any ambiguous terms or phrases that need clarification?
- Would the intended audience of your project be able to understand your proposal?
- Have you properly proofread your proposal to assure there are minimal grammatical and spelling mistakes?
- Are all the resources used for this project correctly cited and referenced?
