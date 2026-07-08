/*Basic Data Pull*/

SELECT
    t.TransactionId,
    t.TransactionDate,
    t.Amount,
	g.GlCodeKey,
    g.GlCode,
    b.BusinessUnitName
    Comments
FROM
    TransactionEntry t
    Join GLCodes g on t.GlCodeKey = g.GlCodeKey
    join businessUnit b on t.businessUnitKey = b.BusinessUnitKey;



