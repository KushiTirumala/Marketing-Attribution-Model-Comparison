Marketing Attribution Model Comparison

This project evaluates the effectiveness of different marketing attribution models to determine how revenue should be credited across customer touchpoints.

The analysis compares:

First-Touch Attribution

Last-Touch Attribution

Linear Attribution

The goal is to understand which marketing channels truly drive revenue.

Business Problem

Companies invest in multiple marketing channels (Google Ads, Email, Social Media, Direct Traffic).

However, leadership needs clarity on:

Which channel drives conversions?

Are we over-crediting the last interaction?

How should revenue be fairly distributed?

This project answers these questions using data-driven attribution models.

Dataset

The dataset includes:

customer_id – Unique customer

touchpoint_order – Order of interaction

channel – Marketing channel

conversion_value – Revenue generated

Each customer may interact with multiple channels before conversion.

Tools Used

Python

Pandas

NumPy

Matplotlib

Attribution Models Implemented
First-Touch Attribution

Credits 100% of revenue to the first interaction channel.

Last-Touch Attribution

Credits 100% of revenue to the final interaction channel.

Linear Attribution

Distributes revenue equally across all touchpoints.

Output

Revenue credited per channel under each model

Visual comparison of attribution impact

Identification of over- or under-valued channels

Key Insights

Last-touch may overvalue bottom-funnel channels.

First-touch highlights awareness drivers.

Linear provides balanced credit distribution.

Business Impact

Helps marketing teams:

Optimize budget allocation

Avoid misleading attribution bias

Improve ROI measurement

Make data-backed channel investment decisions
