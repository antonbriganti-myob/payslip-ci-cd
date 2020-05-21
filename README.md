# Payslip Calculator
[![Build Status](https://travis-ci.org/antonbriganti-myob/payslip-ci-cd.svg?branch=master)](https://travis-ci.org/antonbriganti-myob/payslip-ci-cd)

At MYOB we rock at payroll, the most important part of payroll is getting your payslip!

## Contact Us
we can't get you jobs but we can answer questions you have
`anton.briganti@myob.com`
`bianca.carnevale@myob.com`

## Feedback Appreciated
https://forms.office.com/Pages/ResponsePage.aspx?id=__VH7LjHSEiGWRHCxCTRIEYw3kqR8YdOnczwtGBbCw1UMVAyVE84OVJTMDBXTVE2VUEzV0lYRVRQVC4u

## The Problem
### Payslip definition and rules
* Gross income = annual salary / 12 months   
* Income tax = based on the tax table provided below    
* Net income = gross income - income tax    
* Super = gross income x super rate    
* All calculation results should be rounded to the whole dollar. If >= 50 cents round up to the next dollar increment, otherwise round down.

#### Tax Table 
The following rates for 2017-18 apply from 1 July 2017:

| Taxable Income     | Tax on this Income                         |
|--------------------|--------------------------------------------|
| $0 - $18,200       | Nil                                        |
| $18,201 - $37,000  | 19c for each $1 over $18,200               |
| $37,001 - $87,000  | $3,572 plus 32.5c for each $1 over $37,000 |
| $87,001 - $180,000 | $19,822 plus 37c for each $1 over $87,000  |
| $180,001 and over  | $54,232 plus 45c for each $1 over $180,000 |


### Example
Payslip for an employee with an annual salary of $60,050 and a super rate of 9% is:

* gross income = 60,050 / 12 = 5,004.16666667 (round down) = 5,004  
* income tax = (3,572 + (60,050 - 37,000) x 0.325) / 12 = 921.9375 (round up) = 922  
* net income = 5,004 - 922 = 4,082  
* super = 5,004 x 9% = 450.36 (round down) = 450  

```
Name: John Smith
Gross Income: 5004
Income Tax: 922
Net income: 4082
Super Earned: 450
```

