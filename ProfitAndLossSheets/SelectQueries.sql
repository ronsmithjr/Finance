Declare @TransYear int = 2026;

Select ac.CategoryName, a.AccountName, Sum(t.Amount) as TotalAmount from transactionEntry t
join Account a on t.AccountId = a.AccountId
join AccountCategory ac on a.CategoryId = ac.CategoryId
where year(t.TransactionDate) == @TransYear
Group by 
    ac.CategoryName,
    a.AccountName
Order by 
    ac.CategoryName,
    a.AccountName;


SELECT
    le.EntityName,
    SUM(fp.ActualAmount) AS Revenue
FROM FactPnL fp
JOIN LegalEntity le
    ON fp.LegalEntityKey = le.LegalEntityKey
JOIN Account da
    ON fp.AccountKey = da.AccountKey
WHERE da.PnLSection = 'Revenue'
GROUP BY le.EntityName;

SELECT
    da.PnLSection,
    SUM(fp.ActualAmount * dat.SignMultiplier) AS Amount
FROM FactPnL fp
JOIN Account da
    ON fp.AccountKey = da.AccountKey
JOIN AccountType dat
    ON da.AccountTypeKey = dat.AccountTypeKey
GROUP BY da.PnLSection;