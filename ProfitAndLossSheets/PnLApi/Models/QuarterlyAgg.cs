namespace PnLApi.Models
{
    public class QuarterlyAgg
    {
        public int FiscalYear { get; set; }
        public int FiscalQuarter { get; set; }
        public string QuarterName { get; set; }
        public decimal QuarterlyAmount { get; set; }
    }
}
