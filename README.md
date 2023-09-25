# Credit-RIsk
Statistical analysis and stress test for Credit risk by  using machine learning
Table of contents
Introduction	3
Finance	3
Credit Risk	4
Risk-weighted assets	4
The DRiM Game	5
CreditMetrics Model	6
Probability of default of migration	6
Transitions Matrix	6
PIT versus TTC	7
Code Implementation	8
A one-parameter representation of credit risk	10
Defining Z risk	10
Rating Migrations and macroeconomic variables	13
Objective	16
Regression Analysis	17
Linear Regression	17
Goodness of fit	19
Metrics	20
Criteria	21
Bootstrap	22
Predictors	23
A more machine Learning approach	29
Results from code implementation.	30
Bibliography	32










Introduction

Finance

Finance is a term for the management, and study of money and investments. Personal, corporate or public capital is invested through the financial markets and the flow of money begins. Money is converted to real assets, like land, estate, oil etc, or to financial assets, like bonds, securities or stocks. The objective is the returned interest, the Yield, the dividend or the profit. 
To achieve that inside a competitive system like the financial one, we have to make a better choice. The values of stocks go up and down, the influence of companies changes rapidly, and so the robustness of an investment can be easily degraded or upgraded. Then, there is always an underlying risk hidden in every investment. As an extension, the domain of Risk management was created.
Risk management is the identification, evaluation, and prioritization of risks as effect of uncertainty on objectives so as to minimize, monitor, and control the probability or impact of unfortunate events or to maximize the realisation of opportunities. 
The available archive from all the previous years’ stocks values, indicators’ values, interest rates etc.. help us realize the state of the economy and measure the impact of incidents and unexpected events. This knowledge facilitates the reduction of uncertainty and gives us a base on how to choose models and train them in order to be able to make relevant decisions and choose suitable directions. 
So, a company or a person with financial interests, consults the statistical results in order to create for example a portfolio of diversified assets that proposes an accepted combination between risk and profit. And the rule is, the higher the risk, the better the profit.
Of course, except of profit, we can calculate the possibility to fall in an economic crisis.  In the economic cycle after expansion and the peak comes the contraction. A modern economic system has mechanisms that averts the crises by adding light control and limits, like the Basel III accord, at financial institutions.
Basel III is an international regulatory accord that introduced a set of reforms designed to mitigate risk within the international banking sector by requiring banks to maintain certain leverage ratios and keep certain levels of reserve capital on hand. Begun in 2009, it is still being implemented as of 2022. It is developed by the Bank for International Settlements in order to promote stability in the international financial system.
We will not seek the details of the Basel III accord, but in simple words, it is based at the counter party risk and the Minimum Capital requirements Under Basel III. Banks always try to invest the available money they have, because a unexploited capital is considered a loss. The value of the Bank is calculated by the owned assets even if they will be returned in the longterm. But if the bank has unexpected responsibilities to cover, the money should be easily accessible. If not, the possibility of default is augmented.  Therefore, the Basel III obligates the banks to acquire minimum capital available for those case scenarios.  

Credit Risk 

Like all companies, banks are subject to different types of risks. The three most important are the credit risk, the market risk and the operational risk. Credit risk corresponds to the risk of loss for the bank, linked at the non-refund of a part or the whole amount which it granted. This is the risk that our analyse will focus on.
As an attempt to categorize the risk, ratings were created. Ratings serve as an indicator of the financial strength of worthiness of a particular credit or corporate and it is a decisive criterion regarding the investment decision of the players in financial markets. Standard and Poor’s (S&P) or Moody’s are agencies that deal with the assessment of the risk. The risk, is that the bond or the corresponding organisation will file for bankruptcy before the final bond payment is due. 
In extension of this concept, we create portfolio of bonds with the objective to construct a final package more robust and solvent. We achieve that by diversifying counter party risk bonds whose balance render profit. Furthermore, we combine high-risk and low-risk bonds, in an approach to maximize the interest rate but to keep the investment safe. It is assumed that a good rating reflects a high probability for a firm to pay its dept. Thus, the rating reflects the risk but also the cost of financing for a firm. In fact, the rating migrations and the probability of default has various implications in terms of risk and portfolio management and they should be studied before a financial activity.
In this thesis, we take the ratings as given (input) and we analyse through the probability of default and change in the rating of a particular credit. 
The rating categories, ranging from AAA to D, can assumed to be of ordinal order. The associated risk to a rating category is higher for lower states and equivalently lower for higher states. The probability of a migration from a given rating state to another is the center of our analyse so as to calculate risk. We consider that risk has two aspects, an idiosyncratic and a systematic one. Idiosyncratic risk represents the particularities of the asset, and is quite esoteric. In the other hand, the systematic risk can be assumed to be correlated with macroeconomic variables. By using the Belkin et al. model which is based as the Merton model, we will aggregate our rating bond data, create the transition matrices and calculate variables that will train our model, so as to predict future situation and assess an investment. 

Risk-weighted assets

The risk-weighted assets (RWA) represent the credit risk of a portfolio. For the financial institutions, it is a parameter that guides their activities. Risk-weighted assets are used to determine the minimum amount of capital that must be held by banks and other financial institutions in order to reduce the risk of insolvency. It is calculated by the three balaisian parameters:
Probability of default (PD) : the probability of a healthy asset to fall at default in a given period.
Exposure at default (EAD):  It can be defined as the gross exposure under a facility upon default of an obligor.
Loss given default (LGD):  is the share of an asset that is lost if a borrower defaults.
Stress tests are exercises set up by financial institutions to estimate the impacts that disastrous economic conditions could have but nevertheless plausible on the banks. The objective is to simulate a crisis situation so as to test the resistance of banks. We use two case-scenarios, the first one (baseline) where the macro-economic factors continue their present stable condition and the second one (adverse), where the macro-economic factors degrade after a crisis.
Under each of these scenarios, the necessary equities are calculated and compared, in the objective of the measurement of the impact of the bank’s solvency.
We explain the modelling of the default probability of the stress test around the Italian portfolio. The modelling of the EAD and LGD are considered identical, and they will not be furthered explained.
The DRiM Game

DRiM Game, a student competition on a problem of the banking industry, relating to the modeling of financial risks, credit risk in particular.
The Credit Risk teams of Deloitte created this competition in partnership with RCI Bank & Services and SAS. For the 4rth edition, the candidates present their solution to a problem on the modelling of credit risks in front of a jury of experts from the banking and Data industry. 
Complete data histories are made available to them. The teams apply their solution, adapt, and evaluate the performance accompanied by the experts of Deloitte. 
Within the Risk Advisory activity, the Credit Risk team is dedicated to credit risk management and operates as such across the entire credit activity value chain.
Their activities concern the optimization of the management of credit and risk management, MRM, Smart credit risk modelling, NPL, transformation of the risk function.
This thesis elaborates the same subject by using the data of the DRiM Game and implements the relevant theory and model of CreditMetrics. 
Description of the Subject:
For a credit portfolio, determine the evolution of annual credit rating migrations according to the economic situation over different time horizons. 
This amounts to proposing an approach for projecting annual rating migration matrices. The treatment is by appling a "classic" approach and by using one or more alternative methods (machine learning, etc.)
The context includes the analyse of a credit stress-test scenario, based at the Merton/Vasicek model.
The calibration of the rating migration matrix projection approach is over the period 01/201 until 12/2017. 
The data is given inside a excel file comprising 3 lists. Those lists are the identifier of the asset, the class of the rating risk and the date of this observation. Furthermore, all the provided data concerns the country of Italy. We will present the transformation of the data, using the CreditMetrics model, and afterwards, we will examine the correlation or the dependency of our asset rating class values and migration matrices possibilities with the macroeconomic variables of Italian market. The Federal Reserve Bank of St. Louis is considered a reliable source to find all the necessary economic data.
CreditMetrics Model

In the current method, the assets are grouped in different homogeneous risk classes. All the assets inside those classes are considered to have the same probability of default or migration. We will now calculate the probability of default or migration.
Probability of default of migration

In order to calculate transition probabilities from historical data, one can use the CreditMetrics method. The CreditMetrics method assigns transition probabilities to every initial rating. It does so by using the relative frequencies of migration from historical data. It simply sums up the number of ratings in a certain state at the end of a period and divide it by the number of ratings at the beginning of the period. The time is divided by month and by year. The period of one year is considered the best option, because there are many fluctuations in the monthly values, caused by seasonality, etc. 

Transitions Matrix

A Transition Matrix, also, known as a stochastic or probability matrix is a square (n x n) matrix representing the transition probabilities of a stochastic system (e.g. a Markov Chain). The size n of the matrix is linked to the cardinality of the State Space that describes the system being modelled. 
In the simplest possible setup, the stochastic system transitions from an initial state to a final state in a single step. Every position in the matrix represents the Transition Probability. In the rating state j, there are nj firms at the beginning of the period and njk migrated to state k at the end of the period. The estimated transition probability for stochastically independent migrations from initial rating j to k is     pjk = (njk/nj).


Table 1: Probability for rating migration from rating j to rating k.





PIT versus TTC

The rating systems are built as a combination of PIT (Point-in-time) and TTC (Through the cycle) philosophies.
Mesure point-in-Time (PIT), reflects the available information at a given date, and so the current economic condictions. The probabilities conditional on the state of the economy.
Mesure « Trough the Cycle » (TTC) : reflects a long term tendency, which is independent of the current economic conditions.


Image 1. Display of the PD of a portfolio depending on the rating philosophy utilized during different periods of the business cycle.

The measure PIT is considered the monthly or annual matrices and the TTC the summarized total matrix.
The construction of the reference matrix, TTC (Through-The-Cycle) matrix, is identical to those of the monthly/quarterly matrices. It is constructed taking into account the rating histories of all the latter.
Rate of migrationi,j= i=date of start of historyEnd of date historyRate of Migration(PIT)i,j,tN

With,  Rate of migrationi,j  to be the Rate of passage from rating I to rating j at the date t, and N the Number of total Matrices.


The reference matrix must meet a number of conditions, the most important of which are presented below :
Any probability of migration is strictly positive   ∀ i,j;  pi,j>0 
The probability of going into default is higher for bad ratings than for good ratings,
j<i;  pi,Def>pj,Def
The probability of moving to a close rating is higher than the probability of moving to a distant rating,
pi,i+1>pi,i+2>pi,i+3> ….pi,i+n
pi,i-1>pi,i-2>pi,i-3> ….pi,1



Code Implementation

We use python to implement and process our data. In the image above, we can see the data after some transformations. This is considered the initial form. We can observe that the index is the date and the assets Identifier. The value is the Class of every particular asset. 
The data structure used in python is the pandas’ DataFrame.


Image 2. Initial form of our data. Dataframe, indexed by date and Class identifier.

The rating transitions are assumed to be 1 to 11 (default is not present). The result of the transition matrix would be a 11 X 11 matrix. If we create a monthly transition matrix, we compare the initial position of the asset with the one of the next months. For example, if the rating value of an asset was 1 at the date 2010-01-31 and the month 2010-02-28 was 2, we add a value at the corresponding position (1,2). We sum all the similar positions, and we create the Count Migration Matrix.
If the class identifier disappears the next month, the asset is considered resolved (finished his life cycle successfully). If the class identifier appears in the next month’s table, the asset is considered a new one. 
As a result, we obtain the Number of CounterParties migration Matrix, that as his name reveals, indicates the number of assets for every possible combination of initial and terminal position.



Image 3.  the Number of CounterParties migration Matrix

The next step is to calculate the matrix of Migration Probabilities, by devising every cell of the Number of CounterParties migration Matrix by the sum of the initial class values. As indicated in the Image 4.


Image 4.  Example of monthly Migration Probabilities Matrix
 
By the fact that we are interested in the annual Rating Migration Matrices, we add up the values of all monthly Migration Probabilities Matrix in the period of one year and divided then by 12. Like this we create the annual Rating migration Matrix, which has the same form as the monthly one, but different values (more stable).

The measure PTTC is calculated by taking the total number of counterparties over all available table of dates and divide the result by the total number of dates. Those values in the matrix are independent of the date.


A one-parameter representation of credit risk

The one-parameter representation of credit risk view that ratings-transition matrices result from the ‘’binning’’ of a standard normal random variable X that measures changes in creditworthiness. We further assume that X splits into two parts: (1) an idiosyncratic component Y, and (2) a systematic component Z, shared by all borrowers. Broadly speaking, Z measures the ‘’credit cycle’’, meaning the values of default rates and of end-of-period risk ratings not predicted, using historical average transition rates. In good years Z will be positive, implying for each initial credit rating, a lower-than-average default rate and a higher-than-average ratio of upgrades to downgrades. In bad years, the reverse will be true. We describe a way of estimating Z from the separate transition matrices in our data. Conversely, we describe a method of calculating matrices conditional on an assumed value for Z. The historical pattern of Z depicts past credit conditions. For example, during the financial crisis of 2008 the values of Z were negatives.


Defining Z risk

Following the CreditMetrics approach described by Gupton, Finger, and Bhatia (1997), we assume
that ratings transitions reflect an underlying, continuous credit-change indicator X. We further assume that X has a standard normal distribution. Then, conditional on an initial credit rating G at the beginning of a year, we partition the X values into a set of disjoint bins (XgG, Xg+1G]. To simplify
references, we use the indices G and g to represent sequences of integers rather than letters or other symbols. We then define the bins such that the probability of X falling within a given interval equals the corresponding historical average transition rate (see Image 5).


Image 5, Normal Distribution of credit change indicator. Rating AAA to D.

We write the conditions defining the bons as follows:
P(G, g)  =    Φ( XGg + 1) - XGg       (1) ,
in which P(G, g) denotes the historical average G-to-g transition probability and Φ (.) represents the
standard normal cumulative distribution function. The default bin D has a lower threshold of -ꚙ. The
AAA bin has an upper threshold of +ꚙ. The remaining thresholds are fit to the observed transition
probabilities.
We illustrate the process by calculating the corresponding bins using the equation (1). Using the inverse probability function for a standard normal distribution, we compute the lower and upper values of the bins. 
In our data:

TTC Matrix

Matrix Transformation to cumulative matrix

Every line corresponds to a normal distribution whose values is the probability limits of each class. 
After we use the function ‘’ThresholdCalcutors’’ from the class TransMatrix (custom-made), we obtain the bins limits approximations by inserting the values in the inverse normal probability function.

The probability density function for norm is:

 


Rating Migrations and macroeconomic variables

The rating migrations are correlated or dependent with macroeconomic variables according to our theory model (CreditMetrics). To specify the economic or systematic influence on migration behavior, we follow the concept that the assets are standard normal distributed. The probability assets as those that we constructed before, like the example of image 8. 
The X is the estimated threshold value (bin) of the underlying standard normal distributed process that specifies the migration events. We decompose X according to:
                                                        X= Z+ 1-ρY    (2)

Here, Z represents the systematic credit risk and Y the idiosyncratic risk of a borrower. Moreover, Z and Y are assumed to be independent unit normal random variables. The parameter ρ works like a weighting coefficient of the parameters Y and Z, but it reflects the correlation between the migration risk X and the systematic credit risk. 
In order to determine the parameter of the equation (2) and so the quantitative effect they have on rating migrations, we consider the transition probability p(J, j) as:
pJ, j=Xj-1j-Xjj   (3)
Φ is the standard normal cumulative distribution function. The bin of rating 11 has a lower threshold of -ꚙ and the rating 1 has an upper threshold +ꚙ. 
Calculated Thresholds, as indicated above:
Si,j=-1(Probi,jTTC)
Furthermore, the equation (2) can be rewritten as:
Y= X- Z1-ρ     (3)

Following Belkin et al. model (1998), we will use the equation (3) but position as variable the idiosyncratic component:


Xj-1J, XjJ, Zt=Xj-1J- Zt1--XjJ- Zt1-   (4)
The equation (4) represents the transition probability from initial rating J to j for the idiosyncratic component. The threshold values of X are derived from the average transition probabilities of all the years, in our case TTC matrix.
In our attempt to find a value of Z that makes the transition probability of equation (4) to approximate the observed transition probability, we will use the least squares method. So we need a Z that minimizes the below equation:
Zt  Jjnt,J[ ptJ,j-xj-1J,  XjJ,   Zt]2xj-1J,  XjJ,   Zt(1-xj-1J, XjJ,   Zt)   (5)
nt,J  is the number of observed migrations for year t and rating class J.
pt(J, j)  is the observed transition probabilities for year t.
Regarding the calculation, and by the fact the we have two variables and a task to minimize a equation, we quantify the correlation ρ with a value close to 0 and we iterate by augmenting this value until the variance of Z values are close to 1. 

The minimization of equation (5) with respect to Z and ρ, indicates the relationship of the observed migration probabilities and those of the idiosyncratic component calculated by the average matrix. The resulting Z, reveals the comparison with the average and so the underlying economic situation. 


                           Image 6.  Impact of Z on rating transition   (Source: Kim (1999))
As already mentioned, Z is the systematic component of migrations and ρ is the correlation between X and Z. 
We obtain a value of Z for every migration matrix of each year.  A positive Z can be considered as an indicator of higher upgrades of the rating assets and a negative the opposite.

By implementing the process by using python code, we obtained the values of Z and indicated below:

Image 7. Values of Z for every year of our data.


Image 8. Bar plot of Z values.
Those values were obtained by supposing a correlation ρ between X and Z of 1%. 
All the Z values are not far from 0, which is the Z value of the TTC reference matrix. That is normal, because the probabilities are similar at the probability matrices of all years. 
By the fact that economic variations move in cycles, we should see a sinusoidal shape of the values. But our model limitations and mostly the small number of year-values makes our outcome narrow.


So we managed to calculate the Z values and the corresponding correlation. Now we can compose our Fitted Transition Matrix (using equation (4) ) and compare it with the observed Transition matrix.

Image 9. Fitted Transition Matrix 2010.


Image 10. Observed Transition Matrix 2010.

We can see that there are differences between the two tables, but it is a good approximation, and it leads us to a reliable outcome. 
Objective 

The objective of all that modelling was to predict future values of Transition Matrices. To achieve that we can predict future values of the systematic credit risk variable Z and afterworks create the fitted approximation matrix. If we implement all this, we can obtain reliable probabilities for migration ratings for future years, and so evaluate the future economical condition of our assets.
The predicted values of Z will be calculated using machine learning techniques and models like linear regression, etc.



Regression Analysis

Regression analysis starts with statistics and data collection so as to feed and construct our models. With the use of data collection science, their organization, summary and presentation, we plan, perform studies, draw conclusions and presenting the results. 
And we use statistics because the population is often too large. So, we focus on a sample that represents the population without having to know all the underlying details. 
With Descriptive statistics we can organize, picture, and summarize the data from the samples, and check all the assumptions so as afterwards to use the Inferential statistics, and draw conclusions about the whole population.
We accept that there is a level of uncertainty, which limits can be measured by statistical tools. So, the discovered association between the variables does not necessarily means causality. In other words, a statistical relationship does not implicate that a variation of a regressor variates the outcome.
Regression analysis refers to a set of statistical methods and tools that are used to estimate the relationship between dependent and independent variables. It corresponds to linear regression logistic regression and many other statistical models and techniques. 
It is the research method of analysing the association or relationship between two or more variables that called independent variables, predictors, regressors or just input, with the dependent variable, response or just outcome, and if there is a significance effect between them.


Linear Regression
Linear Regression Analysis is a way to implement Regression Analysis by using Linear Regression. This form of analysis estimates the coefficients of the linear equation involving one or more independent variables that best predict the value of the dependent variable. It fits a straight line that minimizes the discrepancies between real and predicted values. The calculation uses the least square method to discover the best fit-line for the pair of regressors-response. Thereafter, we feed the model with new regressor values and we have predictions about the response value. This is a scientifically and reliably way to predict future values. 

Simple Linear Regression:                   y=0+1x+
Multiple Linear Regression:               y=0+ 1x1+…+nxn+ = 0+ n=1nnxn+
In a Matrix form :       	   	      y=Xβ+
βₒ is the constant,  β₁ , β₂ , …, βᵥ   are the parameters that called coefficients.
In the Matrix form β is a vector of coefficients.

Model Implementation:
We try to explicate Y with the variables X.
yi=0+ 1x1+2x2+…+nxn+i
yᵢ  Observation of the dependent/endogenous variable
xn   Observation of the independent variable
εi   Residual (Difference between the real and the predicted value)
β0  Constant
βn   Parameter we search to define

So as to obtain the coefficients, we need to minimise the error, that means the residual and we do that using the least square method.
12 i=1nyi-0-j=1pjxi,j2
So, we found the estimations:
yi=0+i1 x1+i2x2+…+inxn
Residual:   i = yi - yi

Image 11. Linear model (red line) and residuals (green lines).




Goodness of fit

The goodness of fit of a statistical model describes how well it fits a set of observations.  Measures of goodness of fit typically summarize the discrepancies between observed values and the values expected under the model in question. There are various measures that help us compare the results of the models. In Linear Regression a very useful measure is the Coefficient of Determination. 
The coefficient of determination or r-squared value, denoted r2, is the regression sum of squares divided by the total sum of squares, or else the proportion of the variation in the dependent variable that is predictable from the independent variable(s).
Equation:    


Image 12. Linear model, data points and mean value.

Since r2 is a proportion, it is always a number between 0 and 1.
If r2 = 1, all of the data points fall perfectly on the regression line. The predictor x accounts for all of the variation in y!
If r2 = 0, the estimated regression line is perfectly horizontal. The predictor x accounts for none of the variation in y!

Although R-Squared seems a good measurement, it needs to be adjusted so as to be applicable. That is because every predictor add to a model increases R-squared and never decreases it. Thus, a model with more terms may seem to have a better fit just for the fact that it has more terms (overfitting), while the adjusted R-squared compensates for the addition of variables and only increases if the new term enhances the model above what would be obtained by probability and decreases when a predictor enhances the model less than what is predicted by chance.




Metrics

The objective of Linear Regression is to find among all the possible lines, one that minimizes the prediction error of all the data points.

Image 13. Linear model and errors minimization
The essential step in any machine learning model is to evaluate the accuracy of the model. The Mean Squared Error, Mean absolute error, Root Mean Squared Error, and R-Squared or Coefficient of determination metrics are used to evaluate the performance of the model in regression analysis.
Mean Squared Error represents the average of the squared difference between the original and predicted values in the data set. It measures the variance of the residuals.


Root Mean Squared Error is the square root of Mean Squared error. It measures the standard deviation of residuals.
               
The coefficient of determination or R-squared represents the proportion of the variance in the dependent variable which is explained by the linear regression model. It is a scale-free score i.e. irrespective of the values being small or large, the value of R square will be less than one.
        

Adjusted R squared is a modified version of R square, and it is adjusted for the number of independent variables in the model, and it will always be less than or equal to R².In the formula below n is the number of observations in the data and k is the number of the independent variables in the data.

  
The measure that we use as a prediction score to compare the results of the different linear regression approaches is the Adjusted R squared coefficient. It helps us to skip the outperformed approaches and reject overfitting by undermining the redundant variables.



Criteria

Here are some criteria that we need to verify in order to use a linear regression model. 
Collinearity, in statistics, correlation between predictor variables (or independent variables), such that they express a linear relationship in a regression model. When predictor variables in the same regression model are correlated, they cannot independently predict the value of the dependent variable. In other words, they explain some of the same variance in the dependent variable, which in turn reduces their statistical significance.
Biais, the mean of residuals should be close to zero, or else the model is considered underfitted.
Homoscedasticity, the variance of the residuals is constant and does not depend of the observations.
Autocorrelation, measures the relationship between a variable's current value and its past value and should be close to zero (cov(εi , εj ) = 0)
Exogeneity, tells us that the independent variables are not dependent on the dependent variables.


Bootstrap

Bootstrap and resampling are widely applicable statistical methods which relax many of the assumptions of classical statistics. Resampling methods implicitly draw on the Central Limit Theorem.
Specially bootstrap (and other resampling methods) :
Allows computation of statistics from limited data.
Allows us to compute statistics from multiple subsamples of the dataset.
Allows us to make minimal distribution assumptions.

Resampling is when you take a sample, and then you take a sample of the sample. It allows you to see how much variation there would have been, it allows you to get a different understanding of the sample that you took. By subsampling the samples, we can get a new distribution, which we will know a little bit about the uncertainty of the sample. After all, the sample itself usually embodies everything we know about the population that spawned it, so it’s often the best starting point from which we can observe the distribution of the statistic of interest.
We can compute statistics from multiple sub samples of data sets, such as the mean. We sum them up and divide them by the count by the number of items. The trick to bootstrap resampling is sampling with replacement. That means that a value can be part of subsample multiple times.

The theoretical models make many assumptions for the use of a model. Those assumptions and their underlying criteria and hypothesis tests should be fulfilled for the application of the model. 
Although real data, rarely accomplish to overcome all those terms.








Predictors

Our dependent variable is found and prepared previously. But to perform a regression we also need our dependent variables, so as to search the underlying relationship among them. By the fact that our dependent variable is a macroeconomic variable connected with the country of Italy, we search our independent variables in the field of economics associated with this country. We use the site of the ‘Federal Reserve Bank of St. Louis’. It has a large macroeconomic database for the empirical analysis of “big data”. We chose 8 economic indicators, which are essential to the country ‘s economy. The connection of these variables-indicators with our assets migrations coefficient Z is reassured because Z also represent the state of the economy. Those variables are: 
Real Gross Domestic Product
Long Term Government Bond Yields
Consumer Price Index
Inflation
Production of Total Industry in Italy
Economic Policy Uncertainty Index for Europe
Interbank Rates for Italy
Growth Rate Same Period Previous Year
Growth Rate Previous Period
Unemployment Rate
General Government Gross Debt
Working Age Population

We read our data and save them in a pandas Framework, as this is the data structure chosen for our whole project. Our variables have the form:


We will train our model with those data and afterwork we will predict some new, unknown values. The data to the test DataFrame is the values of our chosen variables for the years 2018 and 2019.


By the fact that we will use the linear Regression model to fit our data, we will test the correlation for linear connected data (Pearson).
The first step is to see the correlation with our target variable (independent variable). For correlation, the larger the value (always between 0 and 1), the better one variable explains the values of the other. We want to predict the dependent variable, and so we will take use of the appropriate predictors which are highly connected with our Z variable. 

Image 14. Correlation of the potential predictors with our target variable Z.

We reject the variable ‘Economic Policy Uncertainty Index for Europe’ from our model, because is poorly connected with the target variable. We proceed with all the variables that rest there, whose correlation with the target is sufficient.
The next step is to test the correlation of the predictors with each other. As we know, if there is a dependency between two predictors, the performance of our linear model is degraded.

Image 15. Correlation of the predictors with the target variable Z.

So, we want to achieve a low dependency, of the predictors. We will choose combinations of the predictors that create the best score of the R adjusted coefficient, which is an indicator of goodness of a model that takes into account the predictors dependency.
To create the groups of the independent variables that are not correlated, we choose a threshold of correlation, 60% in our case. We iterate for each variable (column wise) and include only the variables that have a lower correlation with this particular predictor. 
So, we create 8 groups. By the fact that for each group we tested the correlation of the resting variables only with the initial variable (the column variable) that we choose for each iteration, we risk to include in the same group, correlated variables. But, under the concept that each predictor may contain unique information, the group represents a unique combination of a partially uncorrelated state. The potential further correlation between the other variables, will eliminate using the VIF test.
In this point we will try to detect and eliminate multicollinearity. As mentioned, multicollinearity is intercorrelation between independent variables. By eliminating it, we will overcome the correlation problem in our Groups. Multicollinearity can be detected via various methods. We will focus on the most common one, the VIF (Variable Inflation Factors).
VIF determines the strength of the correlation between the independent variables. It is predicted by taking a variable and regressing it against every other variable.
We use the class variance_inflation_factor from the library statsmodels and for each group of variables we get the VIF results. The found the max values of the table with the VIF results and if the max value is greater than 5, we delete this predictor and recalculate the VIF table. 
Above we can see the initial groups and the Groups after the intervention of the VIF criterion.



Image 16. Initial Groups 



Image 17. Groups of variables for linear regression modelling with uncorrelated predictors.


In this part, we need to evaluate the performance of our groups. To achieve that, we will use the Bootstrap theory. We take samples of our data, one or multiple times, and we train our linear model. After that, we evaluate the model, with the variables that where not chosen during the sampling. The score is the RMSE. The results are shown below:


Image 18. The Rsquared adjusted indicator and the RMSE score result after a Bootstrap iteration for each group.
The R squared adjusted scores are calculated from the linear model implementation directly. The RMSE indicator is calculated by iterating over various Bootstrap subgroups and evaluating over the real values that were not part of the subgroup. The low value of the RMSE indicator satisfies the second criterion for the Biais.  
The final model will be the combination of all those models, which are weighted by their R square adjusted value.
The predicted values of Z can be shown below:

Image X. Predicted values from the cumulative linear model for the years 2018 and 2019.


Image 19. Prediction of each Group and the final cumulative prediction.




Image 20. Final Graph of all the values of Z, [2010-2017] for test and [2018,2019] for test.

The two predicted values are positive but quite close to 0. The bank can adjust their strategy based on this scenario.

Having the predicted values of Z, means that we can calculate the migration matrices for the years of 2018 and 2019. 

Image 21. Migration matrix of 2018

Image 22. Migration matrix of 2019

A more machine Learning approach

We will use a popular machine learning model, the Random Forest model. We will adjust it and implement a time Series Forecasting version.
Random forest is an ensemble of decision tree algorithms. In bagging, a number of decision trees are made where each tree is created from a different bootstrap sample of the training dataset. Bagging is an effective ensemble algorithm as each decision tree is fit on a slightly different training dataset, and in turn, has a slightly different performance. Unlike normal decision tree models, such as classification and regression trees, trees used in the ensemble are unpruned, making them slightly overfit to the training dataset. This is desirable as it helps to make each tree more different and have less correlated predictions or prediction errors.
Predictions from the trees are averaged across all decision trees, resulting in better performance than any single tree in the model.
Random forest involves constructing a large number of decision trees from bootstrap samples from the training dataset, like bagging.
Unlike bagging, random forest also involves selecting a subset of input features (columns or variables) at each split point in the construction of the trees. Typically, constructing a decision tree involves evaluating the value for each input variable in the data in order to select a split point. By reducing the features to a random subset that may be considered at each split point, it forces each decision tree in the ensemble to be more different.
Using the “sliding window” at the train dataset, we can create new samples. 
We must be careful in how to fit and evaluate the model. We must always fit the model on the past data and predict on future data, never the inverse. Because of that, we can not use the famous randomize k-fold cross-validation method. So, we use a technique called walk-forward validation. In walk-forward validation the dataset is split in train and test sets by selecting a cut point.

Results from code implementation.

The predictions obtained are:


As mentioned, we produced the predictions from a various random tree’s implementation. The average of the MAE score is:



 Image 23. Graphs of the Random Forest Predictions

Having the predicted values of Z, means that we can calculate the migration matrices for the years of 2018 and 2019.

Image 24. Migration matrix of 2018 for Random Forest.

Image 25. Migration matrix of 2019 for Random Forest













Bibliography

Malte Kleindiek Rating Migrations
A one-parameter representation of credit risk and transition matrices. (JPMorgan)
Stress tesitng des matrices de migration (M. Pierre Corre)
Wikipedia
Investopedia Academy
Statistics By Jim (Jim Frost)
Medium.com
