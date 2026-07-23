using Microsoft.AspNetCore.Mvc;
using PnLApi.Models;
using PnLApi.Services;

namespace PnLApi.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class UserConfigsController : Controller
    {
        private IDataService dataService;
        public UserConfigsController(IDataService _dataService)
        {
            dataService = _dataService;
        }
        [HttpGet]
        public IActionResult GetUserConfigs()
        {
            var configs = dataService.GetConfigsAdmin();
            return Ok(configs);
        }

        [HttpGet("{id}")]
        public IActionResult GetUserConfigs(int id)
        {
            var configs = dataService.GetConfigsAdmin();

            var retVal = configs.FirstOrDefault(c => c.ConfigId == id);           
            return Ok(retVal);
        }
    }
}
