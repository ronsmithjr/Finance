
/* Quarterly aggregation for a fiscal year */

DECLARE @StartFiscalYear INT = 2023;
DECLARE @EndFiscalYear   INT = 2030;

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
    dt.FiscalYear >= @StartFiscalYear AND dt.FiscalYear <= @EndFiscalYear
GROUP BY
    dt.FiscalYear,
    dt.FiscalQuarter,
    dt.QuarterName
ORDER BY
    dt.FiscalYear,
    dt.FiscalQuarter;

/* Pivoted for quarterly aggregation for a fiscal year*/



SELECT
    FiscalYear,
    isnull ([Q1],0) as Q1,
    isnull ([Q2],0) as Q2,
    isnull ([Q3],0) as Q3,
    isnull ([Q4],0) as Q4
From 
(
SELECT
	g.GlCodeCategory,
    dt.FiscalYear,
    dt.QuarterName,
	t.Amount
FROM
    TransactionEntry t
JOIN
    DateTimeTable dt ON t.TransactionDate = dt.CalendarDate
JOIN
	GLCodes g on t.GlCodeKey = g.GlCodeKey
WHERE
	dt.FiscalYear >= @StartFiscalYear AND dt.FiscalYear <= @EndFiscalYear
AND
	g.GlCodeCategory  IN ('Revenue', 'Expense')
) as sourceTable
PIVOT
(
    Sum(Amount)
    FOR QuarterName in ([Q1],[Q2],[Q3],[Q4])
) as PivotTable
Order by FiscalYear asc, GlCodeCategory desc;



SELECT
    dt.FiscalYear,
    dt.FiscalQuarter,
    dt.QuarterName,
    bu.BusinessUnitName,
    g.GlCodeName,
    g.GlCodeCategory,
    SUM(t.Amount) AS QuarterlyAmount
FROM
    TransactionEntry t
JOIN
    DateTimeTable dt ON t.TransactionDate = dt.CalendarDate
JOIN
	GLCodes g on t.GlCodeKey = g.GlCodeKey
JOIN
	BusinessUnit bu on t.BusinessUnitKey = bu.BusinessUnitKey
WHERE
    dt.FiscalYear >= @StartFiscalYear AND dt.FiscalYear <= @EndFiscalYear
AND		
	t.BusinessUnitKey in (Select BusinessUnitKey from BusinessUnit)
GROUP BY
    dt.FiscalYear,
    dt.FiscalQuarter,
    dt.QuarterName,
    bu.BusinessUnitName,
    g.GlCodeName,
    g.GlCodeCategory
ORDER BY
	bu.BusinessUnitName,
    dt.FiscalYear,
    dt.FiscalQuarter;