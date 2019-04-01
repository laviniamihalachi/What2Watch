using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;

namespace What2Watch.Models
{
    public class MovieCollection
    {
        [Key]
        public int MovieCollectionId { get; set; }
        [Required]
        public virtual Movie Movie { get; set; }
        [Required]
        public virtual Profile Profile { get; set; }
        [Required]
        public virtual MovieStatus MovieStatus { get; set; }
    }
}