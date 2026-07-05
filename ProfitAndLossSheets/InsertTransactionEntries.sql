
-- Sample INSERT statements for TransactionEntry table
-- Generating entries for the last two years

BEGIN TRAN;

INSERT INTO TransactionEntry (TransactionDate, Amount, AccountKey, BusinessUnitKey, Comments) VALUES
('2024-07-15', 15000.00, 1, 1, 'Advisory fee for Q2 2024'),
('2024-07-20', -5000.00, 16, 2, 'July 2024 Salaries'),
('2024-08-05', 25000.00, 2, 2, 'Asset management fee'),
('2024-08-10', -2000.00, 21, 1, 'Software license renewal'),
('2024-09-01', 75000.00, 3, 3, 'Performance fees for client X'),
('2024-09-15', -10000.00, 11, 1, 'Advisor payout'),
('2024-10-10', 5000.00, 4, 4, 'Commission revenue'),
('2024-10-25', -3500.00, 29, 3, 'Q4 Marketing campaign'),
('2024-11-12', 120000.00, 5, 5, 'Trading revenue from equities desk'),
('2024-11-30', -15000.00, 17, 2, 'Annual bonuses payout'),
('2024-12-20', 800.00, 9, 3,  'Banking service charges'),
('2025-01-15', -7500.00, 27, 1, 'Office rent for January'),
('2025-02-03', 45000.00, 6, 4, 'Interest income from corporate loans'),
('2025-02-28', -22000.00, 18, 2, 'Payroll taxes for February'),
('2025-03-10', -5000.00, 24, 1, 'Legal fees for contract review'),
('2025-04-05', 3000.00, 7, 6, 'Custody service fees'),
('2025-04-15', -1800.00, 31, 3, 'Office supplies purchase'),
('2025-05-20', 1500.00, 8, 1, 'Financial planning session fee'),
('2025-06-10', -6000.00, 14, 5, 'Clearing fees for trades'),
('2025-07-01', 95000.00, 35, 2, 'Investment gain on sale of asset'),
('2025-07-22', -4500.00, 30, 1,  'Travel and entertainment expenses'),
('2025-08-18', -12000.00, 22, 5, 'Market data subscription renewal'),
('2025-09-05', 22000.00, 1, 1, 'Advisory fees collected'),
('2025-10-01', -8000.00, 34, 4, 'Interest expense on corporate bond'),
('2025-11-11', -25000.00, 36, 2, 'Investment loss on portfolio adjustment'),
('2025-12-15', 12000.00, 37, 5, 'Foreign exchange gain'),
('2026-01-20', -9000.00, 19, 2, 'Employee benefits contribution'),
('2026-02-10', -15000.00, 25, 1, 'Annual audit fees'),
('2026-03-15', 60000.00, 2, 2, 'Asset management fees for Q1'),
('2026-04-01', -3000.00, 38, 5, 'Foreign exchange loss'),
('2026-05-05', -40000.00, 39, 4, 'Income tax payment'),
('2026-06-10', 500.00, 10, 3, 'Other operating revenue'),
('2026-06-30', -1250.00, 32, 1, 'Depreciation for office equipment');


--COMMIT --ROLLBACK
