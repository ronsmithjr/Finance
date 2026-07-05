CREATE TABLE Holiday (
    HolidayKey INT IDENTITY(1,1) PRIMARY KEY,
    HolidayDate DATE NOT NULL,
    HolidayName VARCHAR(100) NOT NULL,
    MarketCode VARCHAR(20) NOT NULL,
    CountryCode VARCHAR(10) NOT NULL,
    IsTradingHoliday BIT NOT NULL,
    IsSettlementHoliday BIT NOT NULL,
    IsEarlyClose BIT NOT NULL,
    Notes NVARCHAR(255) NULL
);

INSERT INTO Holiday
(
    HolidayDate,
    HolidayName,
    MarketCode,
    CountryCode,
    IsTradingHoliday,
    IsSettlementHoliday,
    IsEarlyClose,
    Notes
)
VALUES

('2026-01-01', 'New Year''s Day',
 'NYSE', 'US', 1, 1, 0,
 'Market Closed'),

('2026-01-19', 'Martin Luther King Jr. Day',
 'NYSE', 'US', 1, 1, 0,
 'Market Closed'),

('2026-02-16', 'Presidents Day',
 'NYSE', 'US', 1, 1, 0,
 'Market Closed'),

('2026-04-03', 'Good Friday',
 'NYSE', 'US', 1, 1, 0,
 'Market Closed'),

('2026-05-25', 'Memorial Day',
 'NYSE', 'US', 1, 1, 0,
 'Market Closed'),

('2026-06-19', 'Juneteenth',
 'NYSE', 'US', 1, 1, 0,
 'Market Closed'),

('2026-07-03', 'Independence Day Observed',
 'NYSE', 'US', 1, 1, 0,
 'Market Closed'),

('2026-09-07', 'Labor Day',
 'NYSE', 'US', 1, 1, 0,
 'Market Closed'),

('2026-11-26', 'Thanksgiving Day',
 'NYSE', 'US', 1, 1, 0,
 'Market Closed'),

('2026-11-27', 'Day After Thanksgiving',
 'NYSE', 'US', 0, 0, 1,
 'Early Close 1:00 PM ET'),

('2026-12-24', 'Christmas Eve',
 'NYSE', 'US', 0, 0, 1,
 'Early Close 1:00 PM ET'),

('2026-12-25', 'Christmas Day',
 'NYSE', 'US', 1, 1, 0,
 'Market Closed'); 




 WITH DateRange AS (
    SELECT CAST('2023-01-01' AS DATE) AS CalendarDate
    UNION ALL
    SELECT DATEADD(day, 1, CalendarDate)
    FROM DateRange
    WHERE CalendarDate < '2029-12-31'
)
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
    IsQuarterStart,
    IsQuarterEnd,
    IsYearEnd
)
SELECT
    CalendarDate,
    YEAR(CalendarDate) AS FiscalYear,
    DATEPART(quarter, CalendarDate) AS FiscalQuarter,
    MONTH(CalendarDate) AS FiscalMonth,
    DATENAME(month, CalendarDate) AS MonthName,
    'Q' + CAST(DATEPART(quarter, CalendarDate) AS VARCHAR(1)) AS QuarterName,
    FORMAT(CalendarDate, 'yyyy-MM') AS YearMonth,
    DATEFROMPARTS(YEAR(CalendarDate), MONTH(CalendarDate), 1) AS MonthStartDate,
    EOMONTH(CalendarDate) AS MonthEndDate,
    CASE WHEN CalendarDate = EOMONTH(CalendarDate) THEN 1 ELSE 0 END AS IsMonthEnd,
    CASE WHEN DAY(CalendarDate) = 1 AND MONTH(CalendarDate) IN (1, 4, 7, 10) THEN 1 ELSE 0 END AS IsQuarterStart,
    CASE WHEN CalendarDate = EOMONTH(CalendarDate) AND MONTH(CalendarDate) IN (3, 6, 9, 12) THEN 1 ELSE 0 END AS IsQuarterEnd,
    CASE WHEN CalendarDate = EOMONTH(CalendarDate) AND MONTH(CalendarDate) = 12 THEN 1 ELSE 0 END AS IsYearEnd
FROM DateRange
OPTION (MAXRECURSION 0);