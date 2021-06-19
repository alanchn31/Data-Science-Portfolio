## Feature Engineering

### Definition
* Feature engineering is the process of transforming raw data into features that better represent the underlying problem to the predictive models, resulting in improved model accuracy on unseen data.

### Techniques for feature engineering
1. Handling Outliers 
    * There are 2 main methods of detecting outliers, visualizing the data (boxplot or scatterplot for eg) or statistical methods
        * Outlier Detection with Standard Deviation - drop observations that are higher than x * standard deviation where x is between 2 and 4 in practice
        *  Interquartile Range (IQR) - Calculate IQR by taking the 3rd quantile - 1st quantile. Presume ```values < (Q1 - 1.5 * IQR)) |(values > (Q3 + 1.5 * IQR))``` as outliers

    * Once we have detected outliers, we have to make a decision on how to handle them, whether to clip the outliers to a value or drop them. This is a tradeoff as clipping the outliers could lead to a distortion of distribution of values while dropping the outliers could lead to loss of information.

2. Binning
    * The main motivation of binning is to make the model more robust and prevent overfitting, however, it has a cost to the performance. 
    
    * Every time binning happens, information is sacrificed and data becomes more regularized. For numerical columns, binning might be kind of redundant due to its effect on model performance. For categorical columns, the labels with low frequencies probably affect the robustness of statistical models negatively. Assigning a general category to these less frequent values helps to keep the robustness of the model.

3. Log Transform
    * Helps to handle skewed data and after transformation, the distribution becomes more approximate to normal.
    * Decreases the effect of the outliers, due to the normalization of magnitude differences and the model become more robust
    * Usually used for transforming target variables in regression, when normality assumption is violated and distribution seems skewed towards large values

4. Generate Polynomial features from existing features - for eg, square/cube of the variable.

5. Feature split
    * Split 1 feature into multiple features. Especially useful for string columns, for eg, splitting address into postal code, district number, country etc.

6. Scaling
    * Min-max normalization - Take ```(x - x_min)/(x_max - x_min)```. This has an advantage over standard scaling when the distribution of the feature (or any transformations of the feature) isn’t Gaussian and the feature falls within a bounded interval (for example, pixel intensities fit within a 0–255 range). Howvever, due to the decreased standard deviations, the effects of the outliers increases.

    * Standardization - Take ```(x-mu)/sd```. This helps to reduce the effect of outliers. Suitable when distribution of variable is Gaussian/approximately Gaussian.

7. Date Features - extract year, month, dayofyear, weekofyear, dayofmonth, dayofweek etc. We can also extract days/months passed since a certain date as a feature.

8. Generate statistical features - mean, standard deviation, kurtosis, skew, min, max, percentiles

9. Aggregation based on a key - for eg, grouping by customer id, to engineer features for a specific customer, such as mean, median, standard deviation, average, min, max. Especially useful when dealing with time series data, for eg, finding sum of sales for last 6 month, last 3 months, last 2 months, last 1 month, last 2 weeks, last 1 week etc.

10. Generate ratios of different features - for eg, finding average sales of transactions by taking total sales of store divide by number of transactions. Another example is momentum ratios - for eg, finding sales generated in the last 2 weeks and divide it by sales generated in the last 6 months, to get short term sales momentum of a store.

11. Time series features - see https://tsfresh.readthedocs.io/en/latest/text/list_of_features.html for more details.