# Configuration Table

```sql
Drop Table if exists Finance.dbo.UserConfig;

Create Table Finance.dbo.UserConfig
(
    ConfigId int identity(1,1) not null primary key,
    SystemName nvarchar(100) not null,
    PropertyKey nvarchar(100) not null,
    ConfigKey nvarchar(100) not null,
    ConfigValue nvarchar(max),
    UpdatedDate Date not null,
    UpdatedBy nvarchar(100) not null
)

Create unique nonclustered index UIDX_UserConfig on Finance.dbo.UserConfig
(
    SystemName,
    PropertyKey,
    ConfigKey
);
```