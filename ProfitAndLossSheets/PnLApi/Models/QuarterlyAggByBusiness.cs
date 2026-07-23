namespace PnLApi.Models
{
    public class QuarterlyAggByBusiness
    {
        public int FiscalYear { get; set; }
        public int FiscalQuarter { get; set; }
        public string QuarterName { get; set; }
        public string BusinessUnitName { get; set; }
        public string GlCodeName { get; set; }
        public string GlCodeCategory { get; set; }
        public string GlCodeComments { get; set; }
        public decimal QuarterlyAmount { get; set; }
    }
}
