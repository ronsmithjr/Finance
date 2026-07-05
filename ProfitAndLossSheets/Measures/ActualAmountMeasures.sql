/*Basic Data Pull*/

SELECT
    t.TransactionId,
    t.TransactionDate,
    t.Amount,
    a.AccountCode,
    b.BusinessUnitName,
    l.EntityName,
    Comments
FROM
    TransactionEntry t
    Join Account a on t.accountKey = a.accountKey
    join businessUnit b on t.businessUnitKey = b.BusinessUnitKey
    join LegalEntity l on t.LegalEntityKey = l.LegalEntityKey;



