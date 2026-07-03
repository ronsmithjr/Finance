Create Table Revenue(
    RevenueId int identity(1,1) primary key,
    AccountKey int not null,
    
    Amount decimal(18,2) not null,
    Foreign Key AccountKey References Account(AccountKey)
);

Create Table RevenueCost(
    CostId int identity(1,1) primary key,
    RevenueId int not null,
    AccountKey int not null,
    Amount decimal(18,2),
    Foreign Key RevenueId References RevenueCost(RevenueId)
    Foreign Key AccountKey References Account(AccountKey)

    Foreign Key RevenueId References Revenue (RevenueId)
);
