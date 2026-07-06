-- This script dynamically generates sample transaction data for the last two years,
-- ensuring at least one revenue and one expense transaction for each month.

-- Temp table to hold revenue accounts
DECLARE @RevenueAccounts TABLE (AccountKey INT);
INSERT INTO @RevenueAccounts (AccountKey) VALUES
(1), (2), (3), (4), (5), (6), (7), (8), (9), (10), (35), (37);

-- Temp table to hold expense accounts
DECLARE @ExpenseAccounts TABLE (AccountKey INT);
INSERT INTO @ExpenseAccounts (AccountKey) VALUES
(11), (12), (13), (14), (15), (16), (17), (18), (19), (20), (21), (22), (23), (24), (25), (26), (27), (28), (29), (30), (31), (32), (33), (34), (36), (38), (39);

-- Clear existing data to avoid duplicates if script is run multiple times
-- TRUNCATE TABLE TransactionEntry;

DECLARE @StartDate DATE = DATEADD(year, -2, GETDATE());
DECLARE @EndDate DATE = GETDATE();
DECLARE @CurrentMonthStart DATE = DATEFROMPARTS(YEAR(@StartDate), MONTH(@StartDate), 1);
DECLARE @TransactionIdCounter BIGINT = 1;

WHILE @CurrentMonthStart <= @EndDate
BEGIN
    DECLARE @TransactionDate DATE = @CurrentMonthStart;

    -- 1. Add a Revenue Transaction for the month
    INSERT INTO TransactionEntry (TransactionDate, Amount, AccountKey, BusinessUnitKey, Comments)
    SELECT
        @TransactionDate,
        (ABS(CHECKSUM(NEWID())) % 50000) + 1000.00, -- Random positive amount
        (SELECT TOP 1 AccountKey FROM @RevenueAccounts ORDER BY NEWID()), -- Random Revenue Account
        (ABS(CHECKSUM(NEWID())) % 6) + 1, -- Random Business Unit (1-6)
        'Monthly generated revenue';

    -- 2. Add an Expense Transaction for the month
    INSERT INTO TransactionEntry (TransactionDate, Amount, AccountKey, BusinessUnitKey, Comments)
    SELECT
        @TransactionDate,
        -1 * ((ABS(CHECKSUM(NEWID())) % 10000) + 500.00), -- Random negative amount
        (SELECT TOP 1 AccountKey FROM @ExpenseAccounts ORDER BY NEWID()), -- Random Expense Account
        (ABS(CHECKSUM(NEWID())) % 6) + 1, -- Random Business Unit (1-6)
        'Monthly generated expense';

    -- Move to the next month
    SET @CurrentMonthStart = DATEADD(month, 1, @CurrentMonthStart);
END;
