# Investigate a Perceptual Phenomenon Called the Stroop Effect

## Resources :

1. https://en.wikipedia.org/wiki/Stroop_effect
2. https://faculty.washington.edu/chudler/java/ready.html

## Q & A

#### What is our independent variable? What is our dependent variable?

Our Independent variable is the color of the printed word on the screen. 
The Dependent variable is the time it takes to read the color of the printed word on the screen. 

#### What is an appropriate set of hypotheses for this task? What kind of statistical test do you expect to perform? Justify your choices.

* **Null Hypothesis** : The null hypothesis will state that the times taken for a reader to read congruent letters vs the incongruent letters is the same and has no effect on the reading times

* **Alternate Hypothesis** : This hypothesis states that the times taken for a reader to read congruent letters is **DIFFERENT** from the incongruent letters. Technically, we know that it will take longer to read letters that say a color but are in different color and this would warrant an one tailed T-test in the positive direction.But in the real world, experiments rarely know which direction the test will need to be tested, so we will perform a two tailed Paired T-test here

* **Alpha Level** : 0.05

#### Now it’s your chance to try out the Stroop task for yourself. Go to this link, which has a Java-based applet for performing the Stroop task. Record the times that you received on the task (you do not need to submit your times to the site.) Now, download this dataset which contains results from a number of participants in the task. Each row of the dataset contains the performance for one participant, with the first number their results on the congruent task and the second number their performance on the incongruent task.

Congruent task: 10.053 seconds Incongruent task: 21.287 seconds

#### Report some descriptive statistics regarding this dataset. Include at least one measure of central tendency and at least one measure of variability.

* **Congruent Values** :  
  
  **Mean** : 14.051125
  **Median** : 14.3565
  **Std Dev** : 3.559357958
  
* **Incongruent Values** :  
  
  **Mean** : 22.01591667
  **Median** : 21.0175
  **Std Dev** : 4.797057122
  
  **Difference** :  
    
    **Mean** : -7.964791667
    **Median** : -7.6665
    **Standard Deviation** : 4.864

### Provide one or two visualizations that show the distribution of the sample data. Write one or two sentences noting what you observe about the plot or plots.


![Congruent Vs Incongruent](https://github.com/Suryak1986/Udacity-Data-Analyst/blob/master/CvIC.PNG)

We can clearly see from the graph above that it takes people longer to finish the incongruent words than the congruent one

### Now, perform the statistical test and report your results. What is your confidence level and your critical statistic value? Do you reject the null hypothesis or fail to reject it? Come to a conclusion in terms of the experiment task. Did the results match up with your expectations?

From the values in the difference, we can calculate the Standard Error  
  
**Standard Error** = Standard Deviation of Difference / Sqrt(Number of Observations)    
**Calculated Value** = 2.0930  
  
**T Value** = Mean Difference/Standard Error    
**Calculated Value** = -8.02071  
  
**For 23 Degrees of Freedom and for an Alpha value of 0.05** : T Critical is + or - 2.0686  
  
**Confidence Interval** = Mean of Difference + or - Margin of Error  
**Margin of Error** = tcritical * S.E  
**Calculated Value** = -24.55 to 8.62  

As we can see, the T Statistic of the difference falls in the critical zone (Higher than T-Critical), so we have enough evidence to *REJECT THE NULL HYPOTHESIS*

### CONCLUSION   
  
The Time taken for reading the congruent words is different from the time taken for reading the incongruent words. 
        

