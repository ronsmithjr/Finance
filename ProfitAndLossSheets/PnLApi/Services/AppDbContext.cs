using Microsoft.EntityFrameworkCore;
using PnLApi.Models;

namespace PnLApi.Services
{
    public class AppDbContext : DbContext
    {
        public AppDbContext(DbContextOptions<AppDbContext> options) : base(options)
        {

        }
        public DbSet<UserConfig> UserConfig { get; set; }
    }
}
