# Smart Crop Recommendation Model
## Project Objective:
To predict the most suitable crop to grow based on environmental and soil conditions using Machine Learning and Deep Learning models.
## How can run model 
For running the script you should have python-3 installed on your machine along with the libraries mentioned in requirements.txt. For installing Python you can refer any blog or Tutorial online. For installing requirements.txt just execute the below command in the command prompt or terminal. 

**pip install -r requirements.txt**

After Installing the required libraries you are good to go with the  script. You can clone or download zip file of this repository 
offline in your machine. after downloading the repository, go to the folder where the repository is downloaded and open a command prompt from 
that location. And then enter the following command. 

 **streamlit run App.py

 
##  Feature Summary
| Feature           | Data Type    | Description                                                                 |
| :---------------: |:-----------: |:--------------------------------------------------------------------------: |
| **N**           | Integer     | Nitrogen content in the soil (promotes leafy growth and chlorophyll)       |
| **P**           | Integer     | Phosphorus content in the soil (supports root development and flowering)   |
| **K**           | Integer     | Potassium content in the soil (improves crop health and stress resistance) |
| **temperature** | Float       | Environmental temperature in Celsius (affects growth and germination)      |
| **humidity**    | Float       | Relative humidity in % (influences transpiration and plant respiration)    |
| **ph**          | Float       | Acidity or alkalinity of the soil (affects nutrient absorption efficiency) |
| **rainfall**    | Float       | Rainfall amount in mm (critical for hydration and root health)             |
| **label**       | Categorical | Recommended crop name (target variable – e.g., rice, coconut, banana)      |


Step-by-Step Workflow:

#### 1. Library Imports

Essential libraries for ML, DL, visualization, and evaluation were imported.

#### 2. Dataset Load & Overview

* Dataset loaded successfully
* No missing values
* Balanced target distribution

3. Data Preprocessing

* Features (`X`) and target (`y`) separated
* Features scaled using `StandardScaler`
* Dataset split into 75% train, 25% test (with stratification)

####  4. Advanced EDA (15+ Visualizations)

* Crop distribution barplot
* Histograms for each numerical feature
* Boxplots grouped by crop type
* Correlation heatmap
* Skewness analysis for numerical features

####  5. Feature Engineering

* Correlation analysis showed **no multicollinearity**
* Detected skewed features: `K`, `P`, `rainfall`

####  6. Label Encoding & Re-Splitting

* Target `label` column encoded with `LabelEncoder`
* Data re-scaled and split again

---

###  7. Machine Learning Models

Trained and evaluated the following 8 models:

* Logistic Regression
* Decision Tree
* Random Forest
* Naive Bayes
* K-Nearest Neighbors
* Support Vector Machine (SVM)
* Gradient Boosting
* XGBoost

All models evaluated using accuracy score.

---

###  8. Deep Learning (ANN)

* Built a 1-layer fully connected Artificial Neural Network
* Hidden layers used **ReLU** activation
* Final layer used **Softmax** for multiclass classification
* Regularized using **Dropout**
* Achieved \~98% accuracy on test set

---

9. Model Evaluation

**Random Forest**  which gives accuracy of 99.55 selected for confusion matrix and classification report

