/* Monthly aggregation for a fiscal year */
DECLARE @FiscalYear INT = 2025; -- Set the fiscal year you want to query

SELECT
    dt.FiscalYear,
    dt.FiscalMonth,
    dt.MonthName,
    SUM(t.Amount) AS MonthlyAmount
FROM
    TransactionEntry t
JOIN
    DateTimeTable dt ON t.TransactionDate = dt.CalendarDate
WHERE
    dt.FiscalYear = @FiscalYear
GROUP BY
    dt.FiscalYear,
    dt.FiscalMonth,
    dt.MonthName
ORDER BY
    dt.FiscalYear,
    dt.FiscalMonth;

/* Pivoted monthly aggregation for a fiscal year */
DECLARE @PivotFiscalYear INT = 2025; -- Set the fiscal year for the pivot

SELECT
    FiscalYear,
    ISNULL([January], 0) AS January,
    ISNULL([February], 0) AS February,
    ISNULL([March], 0) AS March,
    ISNULL([April], 0) AS April,
    ISNULL([May], 0) AS May,
    ISNULL([June], 0) AS June,
    ISNULL([July], 0) AS July,
    ISNULL([August], 0) AS August,
    ISNULL([September], 0) AS September,
    ISNULL([October], 0) AS October,
    ISNULL([November], 0) AS November,
    ISNULL([December], 0) AS December
FROM
(
    SELECT
        dt.FiscalYear,
        dt.MonthName,
        t.Amount
    FROM
        TransactionEntry t
    JOIN
        DateTimeTable dt ON t.TransactionDate = dt.CalendarDate
    WHERE
        dt.FiscalYear = @PivotFiscalYear
) AS SourceTable
PIVOT
(
    SUM(Amount)
    FOR MonthName IN ([January], [February], [March], [April], [May], [June], [July], [August], [September], [October], [November], [December])
) AS PivotTable;/* Pivoted monthly aggregation for a fiscal year */


/* Monthly aggregation for a fiscal year */
DECLARE @FiscalYear INT = 2025; -- Set the fiscal year you want to query
DECLARE @BusinessUnitName varchar(100) = 'Private Wealth'

SELECT
    dt.FiscalYear,
    dt.FiscalMonth,
    dt.MonthName,
    bu.BusinessUnitName,
    IsNull(SUM(t.Amount),0) AS MonthlyAmount
FROM
    TransactionEntry t
JOIN
    DateTimeTable dt ON t.TransactionDate = dt.CalendarDate
JOIN
    BusinessUnit bu on t.BusinessUnitKey = bu.BusinessUnitKey
WHERE
    dt.FiscalYear = @FiscalYear
AND
    bu.businessunitname = @businessUnitName
GROUP BY
    dt.FiscalYear,
    dt.FiscalMonth,
    dt.MonthName,
    bu.BusinessUnitName
ORDER BY
    dt.FiscalYear,
    dt.FiscalMonth;
