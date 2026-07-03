
Create Table FactBusinessMetrics(
    MetricFactKey bigint identity(1,1) primary key,
    DateKey int,
    BusinessUnitKey int,

    AUM Decimal (20, 2),
    ClientCount int,
    AdvisorCount int,
    AccountsOpened int, 
    TradeVolume decimal(20,2)
);