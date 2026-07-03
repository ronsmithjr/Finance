

Create Table AccountCategory(
    CategoryId int primary key,
    CategoryName varchar(100) not null
);


Create Table Account(
    AccountId int primary key,
    AccountName varchar(150) not null,
    CategoryId int not null,
    Foreign Key (CategoryId)
        References AccountCategory(CategoryId)
);

Create Table Department(
    DepartmentId int primary key,
    DepartmentName varchar(100) not null
);

Create Table TransactionEntry(
    TransactionId bigint primary key,
    TransactionDate Date not null,
    AccountId int not null,
    DepartmentId int not null,
    Description varchar(255),
    Amount decimal(18, 2) not null

    Foreign Key (AccountId)
        References Account(AccountId)

    Foreign Key (DepartmentId)
        References Department(DepartmentId)
);

Create Table FiscalPeriod(
    PeriodId int primary key,
    StartDate Date,
    EndDate Date,
    FiscalYear int,
    FiscalMonth int
);

Create Table BusinessUnit(
    BusinessUnitId int primary key,
    BusinessUnitName varchar(100)
);

Create Table Budget(
    BudgetId BigInt Primary Key,
    PeriodId int,
    AccountId int,
    BudgetAmount decimal(18,2)
)