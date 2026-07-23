namespace PnLApi.Models
{
    public class MonthlyAggByBusiness
    {
        public int FiscalYear { get; set; }
        public int FiscalMonth { get; set; }
        public string MonthName { get; set; }
        public string BusinessUnitName { get; set; }
        public string GlCodeName {get;set;}
        public string GlCodeCategory {get;set; }
        public string GlCodeComments { get; set; }
        public decimal MonthlyAmount { get; set; }
    }
}
