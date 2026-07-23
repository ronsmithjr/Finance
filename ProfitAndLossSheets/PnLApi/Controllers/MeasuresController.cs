using Microsoft.AspNetCore.Mvc;
using PnLApi.Models;
using PnLApi.Services;

namespace PnLApi.Controllers
{
    [ApiController]
    [Route("[controller]/[action]")]
    public class MeasuresController : Controller
    {
        private IDataService dataService;
        public MeasuresController(IDataService _dataService) 
        {
            dataService = _dataService;
        }

        [HttpGet]
        public IActionResult GetMonthlyAgg([FromQuery] int? startFiscalYear, [FromQuery] int? endFiscalYear)
        {
            
            var retVal = dataService.GetMonthlyAgg(startFiscalYear, endFiscalYear);

            return Ok(retVal);
        }

        [HttpGet]
        public IActionResult GetMonthlyAggPivoted([FromQuery] int? startFiscalYear, [FromQuery] int? endFiscalYear)
        {
            var retVal = dataService.GetMonthlyAggPivoted(startFiscalYear, endFiscalYear);
            return Ok(retVal);
        }

        [HttpGet]
        public IActionResult GetMonthlyByKey([FromQuery] int? startFiscalYear, [FromQuery] int? endFiscalYear)
        {
            var retVal = dataService.GetMonthlyAggByBusiness(startFiscalYear, endFiscalYear);
            return Ok(retVal);
        }

        [HttpGet]
        public IActionResult GetQuarterlyAgg([FromQuery] int? startFiscalYear, [FromQuery] int? endFiscalYear)
        {
            var retVal = dataService.GetQuarterlyAgg(startFiscalYear, endFiscalYear);
            return Ok(retVal);
        }

        [HttpGet]
        public IActionResult GetQuarterlyAggPivoted([FromQuery] int? startFiscalYear, [FromQuery] int? endFiscalYear)
        {
            var retVal = dataService.GetQuarterlyAggPivoted(startFiscalYear, endFiscalYear);
            return Ok(retVal);
        }

        [HttpGet]
        public IActionResult GetQuarterlyAggByKey([FromQuery] int? startFiscalYear, [FromQuery] int? endFiscalYear)
        {
            var retVal = dataService.GetQuarterlyAggByBusiness(startFiscalYear, endFiscalYear);
            return Ok(retVal);
        }
    }
}
