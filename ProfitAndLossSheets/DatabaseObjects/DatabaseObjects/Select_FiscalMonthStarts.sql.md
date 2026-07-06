
# Fiscal Start Date Queries


## Fiscal Month Starting in July

```sql
Select
	TransactionDate,
	FiscalYear = Case
		When month(TransactionDate) >= 7 then Year(TransactionDate) + 1
		else Year(TransactionDate)
	End
From
	transactionEntry;
```

## Generic Formula for any Fiscal Month Start

```sql
Declare @FiscalStartMonth int = 7;

Select
	Case
		When Month(TransactionDate) >= @FiscalStartMonth then Year(TransactionDate) + 1
		else Year(TransactionDate)
	End As FiscalYear
From
	TransactionEntry;
```