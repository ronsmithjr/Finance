/* Monthly aggregation for a fiscal year */
DECLARE @StartFiscalYear INT = 2023;
DECLARE @EndFiscalYear   INT = 2030;

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
    dt.FiscalYear >= @StartFiscalYear AND dt.FiscalYear <= @EndFiscalYear
GROUP BY
    dt.FiscalYear,
    dt.FiscalMonth,
    dt.MonthName
ORDER BY
    dt.FiscalYear,
    dt.FiscalMonth;

/* Pivoted monthly aggregation for a fiscal year */

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
		a.AccountType,
        dt.FiscalYear,
        dt.MonthName,
        t.Amount
    FROM
        TransactionEntry t
    JOIN
        DateTimeTable dt ON t.TransactionDate = dt.CalendarDate
	JOIN 
		Account a on t.AccountKey = a.AccountKey
    WHERE
        dt.FiscalYear >= @StartFiscalYear AND dt.FiscalYear <= @EndFiscalYear
	AND
		a.AccountType  IN ('Revenue', 'Expense')
) AS SourceTable
PIVOT
(
    SUM(Amount)
    FOR MonthName IN ([January], [February], [March], [April], [May], [June], [July], [August], [September], [October], [November], [December])
) AS PivotTable
Order by FiscalYear asc, Accounttype desc
;




/* Monthly aggregation for a fiscal year  */

SELECT
    dt.FiscalYear,
    dt.FiscalMonth,
    dt.MonthName,
    bu.BusinessUnitName,
    a.AccountName,
    a.AccountType,
    a.AccountCategory,
    IsNull(SUM(t.Amount),0) AS MonthlyAmount
FROM
    TransactionEntry t
JOIN
    DateTimeTable dt ON t.TransactionDate = dt.CalendarDate
JOIN
    BusinessUnit bu on t.BusinessUnitKey = bu.BusinessUnitKey
JOIN
    Account a on t.AccountKey = a.AccountKey
WHERE
    dt.FiscalYear  >= @StartFiscalYear AND dt.FiscalYear <= @EndFiscalYear
AND
    --bu.businessunitkey = @BusinessUnitKey
	bu.BusinessUnitKey in (Select BusinessUnitKey from businessunit)
GROUP BY
    dt.FiscalYear,
    dt.FiscalMonth,
    dt.MonthName,
    bu.BusinessUnitName,
    a.AccountName,
    a.AccountType,
    a.AccountCategory
ORDER BY
	bu.BusinessUnitName,
    dt.FiscalYear,
    dt.FiscalMonth;
