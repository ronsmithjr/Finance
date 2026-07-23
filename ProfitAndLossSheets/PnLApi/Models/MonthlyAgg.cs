namespace PnLApi.Models
{
    public class MonthlyAgg
    {
        public int FiscalYear { get; set; }
        public int FiscalMonth {get;set;}
        public string MonthName {get;set;}
        public decimal MonthlyAmount {get;set;}
    }
}
