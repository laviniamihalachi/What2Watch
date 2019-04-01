using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;

namespace What2Watch.Models
{
    public class Movie
    {
        [Key]
        public int MovieId { get; set; }
        [Required]
        public string Title { get; set; }
        [Required]
        public string Duration { get; set; }
        public string Description { get; set; }
        public string Link { get; set; }
        

        //colectii
        public virtual ICollection<MovieEmotion> MovieEmotions { get; set; }
        public virtual ICollection<Comment> Comments { get; set; }
    }
}