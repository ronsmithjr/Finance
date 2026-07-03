
CREATE TABLE AccountType (
    AccountTypeKey INT Identity(1,1) PRIMARY KEY,
    AccountTypeCode VARCHAR(20),
    AccountTypeName VARCHAR(100),
    FinancialStatement VARCHAR(50),
    SignMultiplier INT
);



Create Table Account(
    AccountKey int identity(1,1) primary key,
    AccountCode varchar(20),
    AccountName varchar(200),

    PnLSection varchar(100),
    AccountTypeKey int,

    AccountCategory varchar(100),
    AccountDescription varchar(100),

    Foreign Key AccountTypeKey References AccountType(AccountTypeKey)
);

Create Table LegalEntity(
    LegalEntityKey int identity(1,1) primary key,
    EntityCode varchar(20),
    EntityName varchar(200),
    Country varchar(50),
    RegulatoryRegion varchar(50);
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
Create Table DateTimeTable(
    DateKey  int identity(1,1) primary key,
    CalendarDate Date not null,
    FiscalYear int not null,
    FiscalQuarter int not null,
    FiscalMonth int  not null,    
    MonthName VARCHAR(20),
    QuarterName VARCHAR(10),
    YearMonth VARCHAR(7),
    MonthStartDate DATE,
    MonthEndDate DATE,
    IsMonthEnd BIT,
    IsQuarterEnd BIT,
    IsYearEnd BIT
);

Create Table FactPnL(
    FactPnLKey bigint identity(1,1) primary key,

    DateKey int,
    AccountKey int,
    LocalEntityKey int,
    BusinessUnitKey int,
    SegmentKey int,

    ActualAmount decimal(18,2),
    BudgetAmount decimal (18,2),
    ForecastAmount decimal(18,2),

    Foreign Key DateKey References DateTimeTable(DateKey),

    Foreign Key AccountKey References Account(AccountKey),
    Foreign Key LocalEntityKey References LegalEntity(LocalEntityKey),
    Foreign Key BusinessUnitKey References BusinessUnit(BusinessUnitKey),
    Foreign Key SegmentKey References ClientSegment(SegmentKey)
);