# Smart Crop Recommendation Model
## Project Objective:
To predict the most suitable crop to grow based on environmental and soil conditions using Machine Learning and Deep Learning models.

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
