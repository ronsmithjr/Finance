namespace PnLApi.Models
{
    public class QuarterlyAggPivoted
    {
        public string Category { get; set; }
        public int FiscalYear { get; set; }
        public decimal Q1 { get; set; }
        public decimal Q2 { get; set; }
        public decimal Q3 { get; set; }
        public decimal Q4 { get; set; }
    }
}
