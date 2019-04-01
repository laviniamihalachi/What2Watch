using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;

namespace What2Watch.Models
{
    public class MovieEmotion
    {
        [Key]
        public int MovieEmotionId { get; set; }
        [Required]
        public double Percentage  { get; set; }
        [Required]
        public virtual Movie Movie { get; set; }
        [Required]
        public virtual Emotion Emotion { get; set; }
    }
}