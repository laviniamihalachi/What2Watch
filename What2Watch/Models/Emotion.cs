using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;

namespace What2Watch.Models
{
    public class Emotion
    {
        [Key]
        public int EmotionId { get; set; }
        [Required]
        public string Name { get; set; }
    }
}