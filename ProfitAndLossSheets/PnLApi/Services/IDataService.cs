using Microsoft.AspNetCore.Mvc;
using PnLApi.Models;

namespace PnLApi.Services
{
    public interface IDataService
    {
        List<MonthlyAgg> GetMonthlyAgg(int? startFiscalYear, int? endFiscalYear);
        List<MontlhyAggPivoted> GetMonthlyAggPivoted(int? startFiscalYear, int? endFiscalYear);
        List<MonthlyAggByBusiness> GetMonthlyAggByBusiness(int? startFiscalYear, int? endFiscalYear);
        List<QuarterlyAgg> GetQuarterlyAgg(int? startFiscalYear, int? endFiscalYear);
        List<QuarterlyAggPivoted> GetQuarterlyAggPivoted(int? startFiscalYear, int? endFiscalYear);
        List<QuarterlyAggByBusiness> GetQuarterlyAggByBusiness(int? startFiscalYear, int? endFiscalYear);

        List<UserConfig> GetConfigsAdmin();
        List<UserConfig> GetConfigs();
        //List<UserConfig> DbConfigs { get; }
    }
}
