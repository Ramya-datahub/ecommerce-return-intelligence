# E-Commerce Return Intelligence & Customer Risk Analytics

An end-to-end data analytics project focused on understanding e-commerce return patterns, customer behavior, product factors, and higher-risk customer segments using Python, SQL, and Power BI.

## Project Overview

Product returns can affect revenue, inventory planning, customer experience, and business operations.

In this project, I analyzed 200,000 e-commerce orders to understand:

* Which product categories have higher return rates
* How product price is associated with returns
* How customer experience relates to return behavior
* Whether browsing and session behavior show different return patterns
* How delivery, payment, shipping, and coupon usage relate to returns
* Which combinations of product category, price, and customer experience show elevated return rates

The analysis focuses on identifying **observed patterns and associations**, rather than assuming that one factor directly causes a return.

## Tools Used

* Python
* Pandas
* NumPy
* MySQL
* Power BI

## Project Workflow

```text
Kaggle Dataset
      ↓
Data Understanding
      ↓
Data Quality Checking & Cleaning
      ↓
Exploratory Data Analysis
      ↓
Feature Engineering
      ↓
Return-Risk Segmentation
      ↓
SQL Business Analysis
      ↓
Power BI Dashboard
      ↓
Business Recommendations
```

## Dataset

The dataset contains 200,000 e-commerce orders and includes information about:

* Customer age
* Previous purchases
* Previous return rate
* Product price
* Discount
* Product rating
* Session length
* Product views
* Device type
* Product category
* Shipping method
* Payment method
* Coupon usage
* Delivery delay
* Return status

The raw dataset is not included in this repository.

## Data Cleaning

During data-quality checking, I found several logically invalid values.

Examples included:

* Negative product prices
* Negative discount percentages
* Negative session lengths
* Negative product views
* Negative past return rates
* Product ratings outside the 1–5 range

These invalid numeric values were converted to `NaN` instead of replacing them with zero.

I also found some customer ages below 18. These values were kept because there was not enough evidence to consider them invalid.

## Feature Engineering

I created additional groups to make the analysis easier to understand:

* Age Group
* Return History Group
* Delivery Time
* Discount Group
* Price Group
* Session Length Group
* Product View Group
* Customer Experience Group

## Key Findings

### Overall Return Rate

* Total orders: **200,000**
* Returned orders: **94,919**
* Not returned orders: **105,081**
* Overall return rate: **47.46%**

### Product Category

The observed return rates varied across product categories:

| Product Category | Return Rate |
| ---------------- | ----------: |
| Clothing         |      53.05% |
| Toys             |      50.31% |
| Beauty           |      49.72% |
| Sports           |      45.04% |
| Home             |      44.54% |
| Electronics      |      41.73% |

Clothing had the highest observed return rate, while Electronics had the lowest.

### Customer Experience

The customer experience groups showed different return rates:

* Low experience: **50.68%**
* Medium experience: **45.61%**
* High experience: **47.16%**

This shows an observed association between customer experience level and return behavior.

### Product Price

Return rates increased across the price groups:

* Low price: **46.20%**
* Medium price: **47.86%**
* High price: **50.24%**

### Return-Risk Segmentation

I combined:

* Product category
* Price group
* Customer experience group

This created **54 segments** for comparison against the overall return-rate baseline of **47.46%**.

The highest observed segment was:

**Clothing + High Price + Low Customer Experience**

* Orders: **1,628**
* Return rate: **60.57%**
* Gap from overall baseline: **+13.11 percentage points**

I classified segments as:

* **Elevated:** at least 5 percentage points above the baseline
* **Near baseline:** within 5 percentage points of the baseline
* **Lower:** at least 5 percentage points below the baseline

The ±5 percentage-point threshold was used as a practical analytical threshold for this project.

## SQL Analysis

SQL was used to analyze:

* Total orders
* Returned orders
* Overall return rate
* Category-level return rates
* Shipping methods
* Payment methods
* Coupon usage
* Delivery conditions
* Product prices
* Customer purchase history
* Different product categories

The SQL analysis is available in:

`sql/ecommerce_analysis.sql`

## Power BI Dashboard

The Power BI dashboard contains three pages.

### 1. Executive Overview

Provides an overall view of:

* Total orders
* Returned orders
* Not returned orders
* Overall return rate
* Product category return rates
* Delivery conditions

### 2. Customer & Product Analysis

Analyzes return patterns across:

* Customer experience
* Price
* Session length
* Payment method
* Discount level
* Product views
* Shipping method
* Coupon usage

It also includes a matrix comparing price group and customer experience.

### 3. Return Risk Segmentation

Focuses on the combined return-risk analysis using:

* Product category
* Price group
* Customer experience
* Return rate
* Overall baseline
* Risk gap
* Highest-risk segment

Dashboard screenshots are available in:

`powerbi/dashboard_screenshots/`

## Business Recommendations

Based on the observed patterns, some areas that could be prioritized for further investigation are:

1. Focus on higher-return clothing segments, especially higher-priced clothing with lower customer experience.
2. Improve product information for higher-priced products.
3. Investigate customer experience patterns associated with higher returns.
4. Review clothing-specific product information and customer expectations.
5. Monitor delivery patterns and investigate why early and on-time orders show different return rates.
6. Improve product information for customers with fewer product views.
7. Review whether shorter sessions indicate insufficient product information.
8. Treat discounts as a lower-priority factor because the observed difference between discount groups was very small.
9. Prioritize elevated return-risk segments instead of treating all customers and products equally.
10. Use lower-return segments as comparison benchmarks.
11. Focus business attention on category, price, customer experience, and their combinations.
12. Monitor these segments regularly to identify whether the patterns remain consistent over time.

These recommendations are based on observed patterns in the dataset and should be validated with additional business or operational data before making major decisions.

## Project Structure

```text
ecommerce-return-intelligence/
│
├── python/
│   ├── README.md
│   └── ecommerce_return.py
│
├── sql/
│   ├── README.md
│   └── ecommerce_analysis.sql
│
├── powerbi/
│   └── dashboard_screenshots/
│       ├── README.md
│       ├── 01_Executive_Overview.png
│       ├── 02_Customer_Product_Analysis.png
│       └── 03_Return_Risk_Segmentation.png
│
└── README.md
```

## Conclusion

This project helped me work through an end-to-end analytics workflow, from data cleaning and exploratory analysis to SQL analysis, risk segmentation, Power BI visualization, and business recommendations.

The main objective was not just to calculate return rates, but to identify meaningful patterns that could help a business understand where return risk appears to be higher and where further investigation could be focused.
