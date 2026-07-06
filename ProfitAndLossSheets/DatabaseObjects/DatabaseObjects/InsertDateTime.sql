
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