
INSERT INTO LegalEntity
(
    EntityCode,
    EntityName,
    Country,
    RegulatoryRegion
)
VALUES

('USBD', 'ABC Financial Broker Dealer LLC',
 'United States', 'SEC/FINRA'),

('USWM', 'ABC Wealth Management LLC',
 'United States', 'SEC'),

('USIA', 'ABC Investment Advisors LLC',
 'United States', 'SEC'),

('USBK', 'ABC Private Bank NA',
 'United States', 'OCC'),

('UKWM', 'ABC Wealth Management UK Ltd',
 'United Kingdom', 'FCA'),

('UKAM', 'ABC Asset Management UK Ltd',
 'United Kingdom', 'FCA'),

('CAWM', 'ABC Wealth Management Canada Inc',
 'Canada', 'CIRO'),

('SGAM', 'ABC Asset Management Singapore Pte Ltd',
 'Singapore', 'MAS'),

('HKAM', 'ABC Asset Management Hong Kong Ltd',
 'Hong Kong', 'SFC'),

('AUWM', 'ABC Wealth Management Australia Pty Ltd',
 'Australia', 'ASIC');


INSERT INTO ClientSegment (
    SegmentName
)
VALUES
('Retail'),
('Mass Affluent'),
('High Net Worth'),
('Ultra High Net Worth'),
('Institutional'),
('Corporate');

INSERT INTO BusinessUnit(
    BusinessUnitName
)
VALUES
('Private Wealth'),
('Institutional Asset Management'),
('Retail Banking'),
('Corporate Banking'),
('Capital Markets'),
('Insurance Services');


INSERT INTO Account
(
    AccountCode,
    AccountName,
    PnLSection,
    AccountType,
    AccountCategory,
    AccountDescription
)
VALUES

-- REVENUE
('REV001','Advisory Fee Revenue',
 'Revenue','Revenue',
 'Fee Revenue','Advisory Fees'),

('REV002','Asset Management Fees',
 'Revenue','Revenue',
 'Fee Revenue','AUM Fees'),

('REV003','Performance Fees',
 'Revenue','Revenue',
 'Fee Revenue','Performance Fees'),

('REV004','Commission Revenue',
 'Revenue','Revenue',
 'Transaction Revenue','Commissions'),

('REV005','Trading Revenue',
 'Revenue','Revenue',
 'Trading Revenue','Securities Trading'),

('REV006','Interest Income',
 'Revenue','Revenue',
 'Net Interest Income','Interest Income'),

('REV007','Custody Service Fees',
 'Revenue','Revenue',
 'Service Revenue','Custody Fees'),

('REV008','Financial Planning Fees',
 'Revenue','Revenue',
 'Fee Revenue','Planning Fees'),

('REV009','Banking Service Charges',
 'Revenue','Revenue',
 'Service Revenue','Banking Fees'),

('REV010','Other Operating Revenue',
 'Revenue','Revenue',
 'Other Revenue','Miscellaneous Revenue'),

-- REVENUE COSTS
('COS001','Advisor Payouts',
 'Revenue Costs','Expense',
 'Revenue Sharing','Advisor Compensation'),

('COS002','Client Acquisition Costs',
 'Revenue Costs','Expense',
 'Sales Costs','Acquisition Costs'),

('COS003','Custody Expenses',
 'Revenue Costs','Expense',
 'Service Delivery','Custody Costs'),

('COS004','Clearing Fees',
 'Revenue Costs','Expense',
 'Transaction Costs','Clearing Fees'),

('COS005','Transaction Processing Fees',
 'Revenue Costs','Expense',
 'Transaction Costs','Processing Fees'),

-- OPERATING EXPENSES
('EXP001','Salaries',
 'Operating Expenses','Expense',
'Compensation','Base Salary'),

('EXP002','Bonuses',
 'Operating Expenses','Expense',
 'Compensation','Annual Bonus'),

('EXP003','Payroll Taxes',
 'Operating Expenses','Expense',
 ,'Compensation','Payroll Taxes'),

('EXP004','Employee Benefits',
 'Operating Expenses','Expense',
 'Compensation','Benefits'),

('EXP005','Technology Infrastructure',
 'Operating Expenses','Expense',
 'Technology','Infrastructure'),

('EXP006','Software Licenses',
 'Operating Expenses','Expense',
'Technology','Applications'),

('EXP007','Market Data Services',
 'Operating Expenses','Expense',
 'Technology','Market Data'),

('EXP008','Professional Services',
 'Operating Expenses','Expense',
 ,'Professional Fees','Consulting'),

('EXP009','Legal Fees',
 'Operating Expenses','Expense',
 'Professional Fees','Legal'),

('EXP010','Audit Fees',
 'Operating Expenses','Expense',
 'Professional Fees','Audit'),

('EXP011','Compliance Costs',
 'Operating Expenses','Expense',
 'Risk & Compliance','Compliance'),

('EXP012','Rent Expense',
 'Operating Expenses','Expense',
 'Facilities','Rent'),

('EXP013','Insurance Expense',
 'Operating Expenses','Expense',
'Facilities','Insurance'),

('EXP014','Marketing Expense',
 'Operating Expenses','Expense',
 'Marketing','Advertising'),

('EXP015','Travel and Entertainment',
 'Operating Expenses','Expense',
 'General & Administrative','Travel'),

('EXP016','Office Supplies',
 'Operating Expenses','Expense',
'General & Administrative','Office Supplies'),

('EXP017','Depreciation Expense',
 'Operating Expenses','Expense',
'Non-Cash Expenses','Depreciation'),

('EXP018','Amortization Expense',
 'Operating Expenses','Expense',
 'Non-Cash Expenses','Amortization'),

-- NON-OPERATING
('NON001','Interest Expense',
 'Non-Operating Items','Expense',
 'Financing Costs','Interest'),

('NON002','Investment Gain',
 'Non-Operating Items','Revenue',
 'Investment Activity','Investment Gains'),

('NON003','Investment Loss',
 'Non-Operating Items','Expense',
'Investment Activity','Investment Losses'),

('NON004','Foreign Exchange Gain',
 'Non-Operating Items','Revenue',
 'Foreign Exchange','FX Gain'),

('NON005','Foreign Exchange Loss',
 'Non-Operating Items','Expense',
 'Foreign Exchange','FX Loss'),

-- TAXES
('TAX001','Income Tax Expense',
 'Taxes','Expense',
 'Federal & State Taxes','Income Tax');

INSERT INTO AccountType
(
    AccountTypeCode,
    AccountTypeName,
    FinancialStatement,
    SignMultiplier
)
VALUES

('REV', 'Revenue',
 'Profit & Loss', 1),

('DIRCOST', 'Revenue Cost',
 'Profit & Loss', -1),

('OPEX', 'Operating Expense',
 'Profit & Loss', -1),

('NONOP_INC', 'Non-Operating Income',
 'Profit & Loss', 1),

('NONOP_EXP', 'Non-Operating Expense',
 'Profit & Loss', -1),

('TAX', 'Income Tax',
 'Profit & Loss', -1),

('ASSET', 'Asset',
 'Balance Sheet', 1),

('LIAB', 'Liability',
 'Balance Sheet', -1),

('EQUITY', 'Equity',
 'Balance Sheet', 1),

('CONTRA_REV', 'Contra Revenue',
 'Profit & Loss', -1);

 INSERT INTO DateTimeTable
(
    CalendarDate,
    FiscalYear,
    FiscalQuarter,
    FiscalMonth,
    MonthName,
    QuarterName,
    YearMonth,
    MonthStartDate,
    MonthEndDate,
    IsMonthEnd,
    IsQuarterEnd,
    IsYearEnd
)
VALUES
(
    '2026-01-31',
    2026,
    1,
    1,
    'January',
    'Q1',
    '2026-01',
    '2026-01-01',
    '2026-01-31',
    1,
    0,
    0
),
(
    '2026-03-31',
    2026,
    1,
    3,
    'March',
    'Q1',
    '2026-03',
    '2026-03-01',
    '2026-03-31',
    1,
    1,
    0
),
(
    '2026-12-31',
    2026,
    4,
    12,
    'December',
    'Q4',
    '2026-12',
    '2026-12-01',
    '2026-12-31',
    1,
    1,
    1
);


