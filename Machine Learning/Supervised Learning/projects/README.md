## Content
---

Supervised Learning

* <ins>Data Visualization and Feature Engineering</ins>
    * [Predict Titanic Passengers' Survival Rates](kaggle_titanic) - Deep dive into Kaggle's Titanic   Dataset, using pandas, matplotlib and seaborn. scikit-learn's RandomForestClassifier and XGBoost Classifier is also used, to train a supervised model

* <ins>Time Series Analysis</ins>
    * [Univariate Time Series Analysis with SARIMA and Prophet](superstore_timeseries) - Predict sales of furniture using past sales. To do so, a SARIMA model and Prophet model are trained and validated, using 1-step forward walk validation.

* <ins>Regression</ins>
    * [Predict Housing Prices](kaggle_housing_prices) - Predict prices of residential homes in Ames, Iowa, using 79 explanatory variables. LASSO, Ridge Regression, ElasticNet and XGBoostRegressor were used for supervised learning

    * [Predict Telco Customer Churn](kaggle_churn_prediction) - Assist a telco in predicting customers that are likely to churn, given demographic factors, service type and billing types. Through this notebook, I performed Exploratory Data Analysis and Feature Engineering. Then, I fitted a Logistic Regression model with a RandomForest Classifier. Interpretation of factors that are important in distinguishing customers that will churn are also provided.

* <ins>Deep Learning</ins>
    * [Digit Recognition](kaggle_digit_recognition) - Train Convolutional Neural Network (CNN) models to recognize digits in images using Tensorflow and Keras

    * [Style Transfer](pytorch_style_transfer) - Perform Image Style Transfer using CNNs, implemented in Pytorch. This was done as part of a challenge by Udacity (Favourite Memory Challenge)

    * [Image Classification](training_flower_classifier) - Using the Resnet-152 architecture, pretrained on ImageNet data, perform transfer learning and train a image classification model to classify 102 species of flowers

* <ins>Ethical AI</ins>
    * [Reducing Inherent bias using Fairlearn](fairlearn_mini_projs) Training a model that reduces inherent gender bias using Open Sources library: fairlearn

* <ins>Deploying Machine Learning Model</ins>
    * [Deploying Flower Classifier Model](https://github.com/alanchn31/Flower-App) - Deploy our trained Resnet-152 model used for flower classification, using Flask

    * [Deploying Wine Quality Regression Model](https://github.com/alanchn31/ML-Engineering-Projects/tree/master/wine-quality-elasticnet) - MLOps End-to-End, Experimentation and deployment of our trained ElasticNet model used for wine quality prediction, using MLFlow. The model is deployed to both Azure and AWS