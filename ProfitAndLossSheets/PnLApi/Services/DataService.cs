using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using PnLApi.Models;

namespace PnLApi.Services
{
    public class DataService : IDataService
    {
        private string MonthlyAggQuery;
        private string MonthlyAggPivotedQuery;
        private string MonthlyAggByBusinessQuery;

        private string QuarterlyAggQuery;
        private string QuarterlyAggByBusinessQuery;
        private string QuarterlyAggPivotedQuery;

        private readonly AppDbContext context;

        public DataService(AppDbContext context)
        {
            this.context = context;
            GetConfigs();

        }
        public List<MonthlyAgg> GetMonthlyAgg(int? startFiscalYear, int? endFiscalYear)
        {
            var query = MonthlyAggQuery;
            string startDate, endDate;
            GetStartAndEndDates(startFiscalYear, endFiscalYear, out startDate, out endDate);

            if (string.IsNullOrWhiteSpace(query))
            {
                return new List<MonthlyAgg>();
            }

            var sql = $@"
            {startDate};
            {endDate};
            
            {query}";

            return context.Database.SqlQueryRaw<MonthlyAgg>(sql).ToList();
        }

      

        public List<MonthlyAggByBusiness> GetMonthlyAggByBusiness(int? startFiscalYear, int? endFiscalYear)
        {
            var query = MonthlyAggByBusinessQuery;
            string startDate, endDate;
            GetStartAndEndDates(startFiscalYear, endFiscalYear, out startDate, out endDate);

            if (string.IsNullOrWhiteSpace(query))
            {
                return new List<MonthlyAggByBusiness>();
            }

            var sql = $@"
            {startDate};
            {endDate};
            
            {query}";

            return context.Database.SqlQueryRaw<MonthlyAggByBusiness>(sql).ToList();
        }

        public List<MontlhyAggPivoted> GetMonthlyAggPivoted(int? startFiscalYear, int? endFiscalYear)
        {
            var query = MonthlyAggPivotedQuery;
            string startDate, endDate;
            GetStartAndEndDates(startFiscalYear, endFiscalYear, out startDate, out endDate);

            if (string.IsNullOrWhiteSpace(query))
            {
                return new List<MontlhyAggPivoted>();
            }

            var sql = $@"
            {startDate};
            {endDate};
            
            {query}";

            return context.Database.SqlQueryRaw<MontlhyAggPivoted>(sql).ToList();
        }

        public List<QuarterlyAgg> GetQuarterlyAgg(int? startFiscalYear, int? endFiscalYear)
        {
            var query = QuarterlyAggQuery;
            string startDate, endDate;
            GetStartAndEndDates(startFiscalYear, endFiscalYear, out startDate, out endDate);

            if (string.IsNullOrWhiteSpace(query))
            {
                return new List<QuarterlyAgg>();
            }

            var sql = $@"
            {startDate};
            {endDate};
            
            {query}";

            return context.Database.SqlQueryRaw<QuarterlyAgg>(sql).ToList();
        }

        public List<QuarterlyAggByBusiness> GetQuarterlyAggByBusiness(int? startFiscalYear, int? endFiscalYear)
        {
            var query = QuarterlyAggByBusinessQuery;
            string startDate, endDate;
            GetStartAndEndDates(startFiscalYear, endFiscalYear, out startDate, out endDate);

            if (string.IsNullOrWhiteSpace(query))
            {
                return new List<QuarterlyAggByBusiness>();
            }

            var sql = $@"
            {startDate};
            {endDate};
            
            {query}";

            return context.Database.SqlQueryRaw<QuarterlyAggByBusiness>(sql).ToList();
        }

        public List<QuarterlyAggPivoted> GetQuarterlyAggPivoted(int? startFiscalYear, int? endFiscalYear)
        {
            var query = QuarterlyAggPivotedQuery;
            string startDate, endDate;
            GetStartAndEndDates(startFiscalYear, endFiscalYear, out startDate, out endDate);

            if (string.IsNullOrWhiteSpace(query))
            {
                return new List<QuarterlyAggPivoted>();
            }

            var sql = $@"
            {startDate};
            {endDate};
            
            {query}";

            return context.Database.SqlQueryRaw<QuarterlyAggPivoted>(sql).ToList();
        }

        public List<UserConfig> GetConfigsAdmin()
        {

            var data = context.UserConfig.ToList();
            List<UserConfig> configs = new List<UserConfig>();
            foreach (var config in data)
            {
                UserConfig c = new UserConfig
                {
                    ConfigId = config.ConfigId,
                    PropertyKey = config.PropertyKey,
                    SystemName = config.SystemName,
                    ConfigKey = config.ConfigKey,
                    ConfigValue = config.ConfigValue,
                    UpdatedDate = config.UpdatedDate,
                    UpdatedBy = config.UpdatedBy
                };
                configs.Add(c);
            }
            return configs;
        }

        public List<UserConfig> GetConfigs()
        {

            var data = context.UserConfig.ToList();
            List<UserConfig> configs = new List<UserConfig>();
            foreach (var config in data)
            {
                UserConfig c = new UserConfig
                {
                    ConfigId = config.ConfigId,
                    ConfigKey = config.ConfigKey,
                    ConfigValue = config.ConfigValue,
                };
                configs.Add(c);
            }

            MonthlyAggQuery = configs.FirstOrDefault(s => s.ConfigKey == "MonthlyAggregation")?.ConfigValue;
            MonthlyAggPivotedQuery = configs.FirstOrDefault(s => s.ConfigKey == "MonthlyAggregationPivoted")?.ConfigValue;
            MonthlyAggByBusinessQuery = configs.FirstOrDefault(s => s.ConfigKey == "MonthlyAggregationByBusinessUnit").ConfigValue;

            QuarterlyAggQuery = configs.FirstOrDefault(s => s.ConfigKey == "QuarterlyAggregation")?.ConfigValue;
            QuarterlyAggByBusinessQuery = configs.FirstOrDefault(s => s.ConfigKey == "QuarterlyAggregationByBusinessUnit")?.ConfigValue;
            QuarterlyAggPivotedQuery = configs.FirstOrDefault(s => s.ConfigKey == "QuarterlyAggregationPivoted")?.ConfigValue;

            return configs;
        }

        private static void GetStartAndEndDates(int? startFiscalYear, int? endFiscalYear, out string startDate, out string endDate)
        {
            if (startFiscalYear.HasValue && endFiscalYear.HasValue)
            {
                startDate = startFiscalYear.Value.ToString();
                endDate = endFiscalYear.Value.ToString();
            }

            if (startFiscalYear.HasValue)
            {
                startDate = $@"DECLARE @StartFiscalYear INT = {startFiscalYear.Value}";
            }
            else
            {
                startDate = $@"DECLARE @StartFiscalYear INT = (SELECT MIN(FiscalYear) FROM DateTimeTable)";
            }

            if (endFiscalYear.HasValue)
            {
                endDate = $@"DECLARE @EndFiscalYear INT = {endFiscalYear.Value}";
            }
            else
            {
                endDate = $@"DECLARE @EndFiscalYear INT = (SELECT MAX(FiscalYear) FROM DateTimeTable)";
            }
        }
    }
}
