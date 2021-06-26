## Monte Carlo Integration

* Monte Carlo integration is a technique for numerical integration using random numbers
* It is used to estimate the possible outcomes of an uncertain event

### Equation:
* Here's our equation:  
        ![MC Calc](./docs/mc_calc.PNG)  
    This is simply derived using integration by substitution <br/><br/>
        ![MC Form 1](./docs/mc_form_1.PNG) 
        ![MC Form 2](./docs/mc_form_2.PNG)  
    
    **Proof for Unbiasness:**  
        ![UB Proof](./docs/proof_unbias.PNG)  

    It can also be shown that:  
        ![ZV Proof](./docs/proof_var.PNG)  

    The law of large numbers implies:  
        ![asymp](./docs/asymp.PNG)  

### Approximate Confidence Interval:
* By Central Limit Theorem:  
    ![mc_norm](./docs/mc_norm.PNG)  
    Thus, a reasonable 100(1 − α)% confidence interval for I is:
    ![CI](./docs/CI.PNG)  

### Example of MC Integration:  
* An example of MC Integration
    ![eg_1](./docs/eg_1.PNG)  

    Confidence Interval:
    ![eg_2](./docs/eg_2.PNG)   

    We can definitely do better by increasing n! (n=4 is too small, causing a fat confidence interval)