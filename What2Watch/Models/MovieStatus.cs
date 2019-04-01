using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;

namespace What2Watch.Models
{
    public class MovieStatus
    {
        [Key]
        public int MovieStatusId { get; set; }
        [Required]
        public string Name { get; set; }
    }
}