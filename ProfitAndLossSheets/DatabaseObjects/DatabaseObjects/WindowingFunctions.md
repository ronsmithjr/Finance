# Windowing Functions

## Why they matter
Window functions matter because they let you calculate analytics across rows without collapsing them, something regular SQL aggregates simply cannot do. The concise takeaway: we need window functions to perform running totals, rankings, moving averages, and “look around” calculations while still keeping each row intact.

## 🧠 What window functions solve (the core idea)
A normal aggregate like SUM() or AVG() forces you to use GROUP BY, which reduces your result set. Window functions let you compute those same aggregates over a “window” of rows while still returning every row.

This single difference unlocks a huge amount of analytical power.


Row-level analytics — You can compute totals, averages, counts, ranks, and percentiles per row without grouping.

Running totals — Calculate cumulative sums like “sales up to this day.”

Moving averages — Smooth trends over time without writing complex subqueries.

Ranking — ROW_NUMBER(), RANK(), DENSE_RANK() let you rank items inside partitions.

Lag/lead comparisons — Compare a row to the previous or next row (e.g., “difference from last month”).

Percentiles — NTILE(), PERCENT_RANK(), CUME_DIST() give distribution insights.

Top-N per group — Without messy correlated subqueries.