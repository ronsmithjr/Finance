USE [Finance]
GO

INSERT INTO [dbo].[UserConfig]
           ([SystemName] ,[PropertyKey] ,[ConfigKey] ,[ConfigValue] ,[UpdatedDate] ,[UpdatedBy])
     VALUES
           ('PnLSheet', 'RevenuesAndExpenses','QuarterlyAggregation'
		   ,'SELECT
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
    dt.FiscalQuarter'
           ,GetDate()
           ,'Admin'),
           ('PnLSheet', 'RevenuesAndExpenses','QuarterlyAggregationPivoted'
		   ,'SELECT
    FiscalYear,
    isnull ([Q1],0) as Q1,
    isnull ([Q2],0) as Q2,
    isnull ([Q3],0) as Q3,
    isnull ([Q4],0) as Q4
From 
(
SELECT
	a.AccountType,
    dt.FiscalYear,
    dt.QuarterName,
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
	a.AccountType  IN (''Revenue'', ''Expense'')
) as sourceTable
PIVOT
(
    Sum(Amount)
    FOR QuarterName in ([Q1],[Q2],[Q3],[Q4])
) as PivotTable
Order by FiscalYear asc, Accounttype desc'
           ,GetDate()
           ,'Admin'),
           ('PnLSheet', 'RevenuesAndExpenses','QuarterlyAggregationByBusinessUnit'
		   ,'SELECT
    dt.FiscalYear,
    dt.FiscalQuarter,
    dt.QuarterName,
    bu.BusinessUnitName,
    a.AccountName,
    a.AccountType,
    a.AccountCategory,
    SUM(t.Amount) AS QuarterlyAmount
FROM
    TransactionEntry t
JOIN
    DateTimeTable dt ON t.TransactionDate = dt.CalendarDate
JOIN
	Account a on t.AccountKey = a.AccountKey
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
    a.AccountName,
    a.AccountType,
    a.AccountCategory
ORDER BY
	bu.BusinessUnitName,
    dt.FiscalYear,
    dt.FiscalQuarter'
           ,GetDate()
           ,'Admin')
GO


