using System.ComponentModel.DataAnnotations;

namespace PnLApi.Models
{
    public class UserConfig
    {
        [Key]
        public int ConfigId { get; set; }
        [Required]
        public string SystemName { get; set; }
        [Required]
        public string PropertyKey { get; set; }
        [Required]
        public string ConfigKey { get; set; }
        [Required]
        public string ConfigValue { get; set; }
        [Required]
        public DateTime UpdatedDate { get; set; }
        [Required]
        public string UpdatedBy { get; set; }
    }
}
