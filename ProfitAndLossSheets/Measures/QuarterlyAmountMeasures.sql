
/* Quarterly aggregation for a fiscal year */
DECLARE @FiscalYear_Q INT = 2025; -- Set the fiscal year you want to query

SELECT
    dt.FiscalYear,
    dt.FiscalQuarter,
    dt.QuarterName,
    SUM(t.Amount) AS QuarterlyAmount
FROM
    TransactionEntry t
JOIN
    DateTimeTable dt ON t.TransactionDate = dt.CalendarDate
WHERE
    dt.FiscalYear = @FiscalYear_Q
GROUP BY
    dt.FiscalYear,
    dt.FiscalQuarter,
    dt.QuarterName
ORDER BY
    dt.FiscalYear,
    dt.FiscalQuarter;

/* Pivoted for quarterly aggregation for a fiscal year*/
DECLARE @FiscalYear_Q INT = 2025; -- Set the fiscal year you want to query
SELECT
    FiscalYear,
    isnull ([Q1],0) as Q1,
    isnull ([Q2],0) as Q2,
    isnull ([Q3],0) as Q3,
    isnull ([Q4],0) as Q4
From 
(
SELECT
    dt.FiscalYear,
    dt.QuarterName,
	t.Amount
FROM
    TransactionEntry t
JOIN
    DateTimeTable dt ON t.TransactionDate = dt.CalendarDate
WHERE
    dt.FiscalYear = @FiscalYear_Q
) as sourceTable
PIVOT
(
    Sum(Amount)
    FOR QuarterName in ([Q1],[Q2],[Q3],[Q4])
) as PivotTable; 