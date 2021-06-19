##  Types of Missing Data

* In order to impute missing data meaningfully, we need to consider why the data is missing and characteristics of its missingness. Below are 4 main types of missing data:

    1. Missing completely at random - A variable is missing completely at random if the probability of missingness is the same for all units. In this case, dropping the observations with missing data will not bias model training.

    2. Missing at random - The probability a variable is missing depends only on available information. For eg,  if sex, race, education, and age are recorded for all the people in the survey, then “earnings” is missing at random if the probability of nonresponse to this question depends only on these other, fully recorded variables.  It is often reasonable to model this process, using the other variables to predict missing values

    3. Missingness that depends on unobserved predictors - depends on information that has not been recorded and this information also predicts the missing values. If missingness is not at random, it must be explicitly modeled, or else you must accept some bias in your inferences.

    4. Missingness that depends on the missing value itself - The probability of missingness depends on the (potentially missing) variable itself. For example, people with higher earnings are less likely to reveal them. This can be somewhat mitigated by including more predictors in the missing-data model and thus bringing it closer to missing at random.

## Methods of Imputation

1. Discard all missing data
    * This approach may lead to biased estimates and estimates with larger standard errors due to reduced sample size

2. Imputation
    * Mean Imputation -  replace each missing value with the mean of the observed values for that variable. This can severely distort the distribution for this variable, leading to complications with summary measures including, notably, underestimates of the standard deviation. Moreover, mean imputation distorts relationships between variables by “pulling” estimates of the correlation toward zero.

    * Using information from related observations - For instance, we can use another measurement from another data source to proxy values for missing data in the dataset with missing values. These imputations may propagate measurement error. Also we must consider whether there is any incentive for the reporting person to misrepresent the measurement for the
    person about whom he or she is providing information.

    * Indicator variables for missingness of categorical predictors - Add an additional category for missing values, for categorical variables

    * Build a model using remaining variables to predict variable with missing data - Adds a layer of complexity to the modelling process and can lead to results that are bias if missingness at random assumption is not satisfied.

The summarized information above is derived from: http://www.stat.columbia.edu/~gelman/arm/missing.pdf. Refer to it for more details.