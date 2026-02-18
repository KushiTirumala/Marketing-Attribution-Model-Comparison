import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv("marketing_data.csv")
first_touch = data.sort_values("touchpoint_order") \
                  .groupby("customer_id") \
                  .first()

first_touch_revenue = first_touch.groupby("channel")["conversion_value"].sum()
last_touch = data.sort_values("touchpoint_order") \
                 .groupby("customer_id") \
                 .last()

last_touch_revenue = last_touch.groupby("channel")["conversion_value"].sum()
data["touch_count"] = data.groupby("customer_id")["customer_id"].transform("count")
data["linear_credit"] = data["conversion_value"] / data["touch_count"]
linear_revenue = data.groupby("channel")["linear_credit"].sum()
attribution_df = pd.DataFrame({
    "First Touch": first_touch_revenue,
    "Last Touch": last_touch_revenue,
    "Linear": linear_revenue
}).fillna(0)
print("\n Attribution Model Comparison:")
print(attribution_df)
plt.figure()
attribution_df.plot(kind="bar")
plt.title("Marketing Attribution Model Comparison")
plt.xlabel("Channel")
plt.ylabel("Revenue Attribution")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
