Declare @FiscalStartMonth int = 7


SELECT
    TransactionDate,
    FiscalYear =
        CASE
            WHEN MONTH(TransactionDate) >= @FiscalStartMonth
                THEN YEAR(TransactionDate) + 1
            ELSE YEAR(TransactionDate)
        END
FROM TransactionEntry;