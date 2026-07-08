
CREATE TABLE AccountType (
    AccountTypeKey INT Identity(1,1) PRIMARY KEY,
    AccountTypeCode VARCHAR(20),
    AccountTypeName VARCHAR(100),
    FinancialStatement VARCHAR(50),
    SignMultiplier INT
);


DROP TABLE IF EXISTS  finance.dbo.account 
Create Table Account(
    AccountKey int identity(1,1) primary key,
    AccountCode varchar(20),
    AccountName varchar(200),

    PnLSection varchar(100),
    AccountType varchar(100),

    AccountCategory varchar(100),
    AccountDescription varchar(100)
);


Drop Table if Exists Finance.dbo.GLCodes
Create Table Finance.dbo.GLCodes(
    GlCodeKey int identity(1,1) primary key,
    GlCode varchar(20),
    GlCodeName varchar(200),

    PnLSection varchar(100),
    GlCodeType varchar(100),

    GlCodeCategory varchar(100),
    GlCodeDescription varchar(100)
);

Create Table LegalEntity(
    LegalEntityKey int identity(1,1) primary key,
    EntityCode varchar(20),
    EntityName varchar(200),
    Country varchar(50),
    RegulatoryRegion varchar(50)
);

Create Table BusinessUnit(
    BusinessUnitKey int  identity(1,1) primary key,
    BusinessUnitName varchar(100)
);

Create Table ClientSegment(
    SegmentKey int identity primary key,
    SegmentName varchar(100)
)
/*Can the DateTimeTable be prefilled*/
/*Since we have different types of holidays, we will not put holidays here*/
DROP TABLE IF EXISTS dbo.DateTimeTable;
Create Table DateTimeTable(
    DateKey  int identity(1,1) primary key,
    CalendarDate Date not null,
    FiscalYear int not null,
    FiscalQuarter int not null,
    FiscalMonth int not null,    
    "MonthName" VARCHAR(20) not null,
    QuarterName VARCHAR(10) not null,
    YearMonth VARCHAR(7) not null,
    MonthStartDate DATE not null,
    MonthEndDate DATE not null,
    IsMonthEnd BIT not null,
    IsQuarterStart BIT not null,
    IsQuarterEnd BIT not null,
    IsYearEnd BIT not null
);

Create unique nonclustered index UIX_DateTimeTable_CalendarDate
    on DateTimeTable (CalendarDate);

Drop Table if exists dbo.FactPnL;
Create Table FactPnL(
    FactPnLKey bigint identity(1,1) primary key,
	--Foreign Keys
    DateKey int,	-- Points to Date Slices
    AccountKey int,  -- Points to Revenue or Expense
    LegalEntityKey int, -- Points to Legal Entity
    BusinessUnitKey int, -- Points to 
    SegmentKey int,

	--Measures
    ActualAmount decimal(18,2), -- Measure
    BudgetAmount decimal (18,2), --Measure
    ForecastAmount decimal(18,2), -- Measure

    Foreign Key (DateKey) References DateTimeTable(DateKey),
    Foreign Key (AccountKey) References Account(AccountKey),
    Foreign Key (LegalEntityKey) References LegalEntity(LegalEntityKey),
    Foreign Key (BusinessUnitKey) References BusinessUnit(BusinessUnitKey),
    Foreign Key (SegmentKey) References ClientSegment(SegmentKey),
);

Drop Table if exists dbo.TransactionEntry;
Create Table TransactionEntry(
    TransactionId bigint identity(1, 1) primary key,
    TransactionDate Date not null,
    Amount decimal(18, 2) not null,
    AccountKey int not null,
    BusinessUnitKey int not null,
    Comments varchar(255),   

    Foreign Key (AccountKey)
        References Account(AccountKey),
    Foreign Key (BusinessUnitKey)
        References BusinessUnit(BusinessUnitKey)
);