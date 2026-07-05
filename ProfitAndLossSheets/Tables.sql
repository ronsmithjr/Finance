

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


/*We need a transaction table to be linked to the following
1. Account Table
2. Business Unit
3. Client Segment
4. Legal Entity
    We can join the Transaction Date to the DateTimeTable Calendar Date
*/
Create Table TransactionEntry(
    TransactionId bigint primary key,
    TransactionDate Date not null,
    Amount decimal(18, 2) not null,
    AccountCode varchar(20) not null
    BusinessUnitKey int not null,
    LegalEntityKey int not null


    Comments varchar(255),
    

    Foreign Key (AccountCode)
        References Account(AccountCode)
    Foreign Key (BusinessUnitKey)
        References BusinessUnit(BusinessUnitKey)
    Foreign Key (LegalEntityKey)
        References LegalEntity(LegalEntityKey)

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