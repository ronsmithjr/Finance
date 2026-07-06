/*Basic Data Pull*/

SELECT
    t.TransactionId,
    t.TransactionDate,
    t.Amount,
	a.AccountKey,
    a.AccountCode,
    b.BusinessUnitName
    Comments
FROM
    TransactionEntry t
    Join Account a on t.accountKey = a.accountKey
    join businessUnit b on t.businessUnitKey = b.BusinessUnitKey;



