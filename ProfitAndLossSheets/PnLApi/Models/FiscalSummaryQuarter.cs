namespace PnLApi.Models
{
    public class FiscalSummaryQuarter
    {
        public string GlCodeCategory { get; set; }
        public string FiscalYear { get; set; }
        public decimal Q1{get;set;}
        public decimal Q2{get;set;}
        public decimal Q3{get;set;}
        public decimal Q4 { get; set; }
    }
}
