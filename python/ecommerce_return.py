import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("ecommerce_data.csv")

print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)

# Check missing values
print(df.isnull().sum())

# Check duplicate rows
print(df.duplicated().sum())

# Return distribution
print(df["returned"].value_counts())
print(df["returned"].value_counts(normalize=True) * 100)


# Data quality checks

print("Negative product prices:",
      (df["product_price"] < 0).sum())

print("Negative discount values:",
      (df["discount_percent"] < 0).sum())

print("Negative session length:",
      (df["session_length_minutes"] < 0).sum())

print("Negative product views:",
      (df["num_product_views"] < 0).sum())

print("Negative past return rate:",
      (df["past_return_rate"] < 0).sum())

print("Invalid product ratings:",
      ((df["product_rating"] < 1) |
       (df["product_rating"] > 5)).sum())


# Cleaning invalid values

df.loc[df["past_return_rate"] < 0, "past_return_rate"] = np.nan
df.loc[df["product_price"] < 0, "product_price"] = np.nan
df.loc[df["discount_percent"] < 0, "discount_percent"] = np.nan
df.loc[df["session_length_minutes"] < 0, "session_length_minutes"] = np.nan
df.loc[df["num_product_views"] < 0, "num_product_views"] = np.nan

df.loc[
    (df["product_rating"] < 1) |
    (df["product_rating"] > 5),
    "product_rating"
] = np.nan


# Feature engineering

df["age_group"] = pd.cut(
    df["customer_age"],
    bins=[0, 17, 25, 35, 45, 55, 100],
    labels=[
        "under 18",
        "18-25",
        "26-35",
        "36-45",
        "46-55",
        "55+"
    ]
)

df["return_history_group"] = pd.cut(
    df["past_return_rate"],
    bins=[0, 0.20, 0.50, 1],
    labels=["low", "medium", "high"],
    include_lowest=True
)

df["delivery_time"] = np.select(
    [
        df["delivery_delay_days"] < 0,
        df["delivery_delay_days"] == 0,
        df["delivery_delay_days"] > 0
    ],
    [
        "early_delivery",
        "on_time",
        "late_delivery"
    ],
    default="unknown"
)

df["discount_group"] = pd.cut(
    df["discount_percent"],
    bins=[0, 50, 100],
    labels=["low_discounts", "high_discounts"],
    include_lowest=True
)

df["price_group"] = pd.cut(
    df["product_price"],
    bins=[0, 13.395740, 61.116620, 855.078645],
    labels=["low_price", "medium_price", "high_price"],
    include_lowest=True
)

df["session_length_group"] = pd.cut(
    df["session_length_minutes"],
    bins=[0, 49.760188, 81.966057, 137.652911],
    labels=["low", "medium", "high"],
    include_lowest=True
)

df["product_view_group"] = pd.cut(
    df["num_product_views"],
    bins=[0, 6, 27, 44],
    labels=["low", "medium", "high"],
    include_lowest=True
)

df["customer_experience_group"] = pd.cut(
    df["past_purchase_count"],
    bins=[0, 8, 10, 26],
    labels=["low", "medium", "high"],
    include_lowest=True
)


# Exploratory analysis

print("\nReturn rate by product category")

category_return_rate = (
    df.groupby("product_category")["returned"]
    .mean()
    .mul(100)
    .round(2)
    .sort_values(ascending=False)
)

print(category_return_rate)


print("\nReturn rate by customer experience")

experience_return_rate = (
    df.groupby("customer_experience_group", observed=True)["returned"]
    .mean()
    .mul(100)
    .round(2)
)

print(experience_return_rate)


print("\nReturn rate by price group")

price_return_rate = (
    df.groupby("price_group", observed=True)["returned"]
    .mean()
    .mul(100)
    .round(2)
)

print(price_return_rate)


# Advanced analysis

category_price_experience_analysis = (
    df.groupby(
        [
            "product_category",
            "price_group",
            "customer_experience_group"
        ],
        observed=True
    )["returned"]
    .agg(["count", "mean"])
)

category_price_experience_analysis["return_rate"] = (
    category_price_experience_analysis["mean"] * 100
)

overall_return_rate = df["returned"].mean() * 100

category_price_experience_analysis["return_rate_gap"] = (
    category_price_experience_analysis["return_rate"]
    - overall_return_rate
)

conditions = [
    category_price_experience_analysis["return_rate_gap"] >= 5,
    category_price_experience_analysis["return_rate_gap"] <= -5
]

choices = ["elevated", "lower"]

category_price_experience_analysis["return_pattern"] = np.select(
    conditions,
    choices,
    default="near_baseline"
)

print("\nReturn risk segmentation")
print(category_price_experience_analysis)


# Save cleaned dataset

df.to_csv(
    "ecommerce_final_cleaned.csv",
    index=False
)

print("\nFinal cleaned dataset saved successfully.")