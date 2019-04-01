using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;

namespace What2Watch.Models
{
    public class Comment
    {
        [Key]
        public int CommentId { get; set; }
        [Required]
        public string Content { get; set; }
        
        public int UpVoteNumber { get; set; }
        public int DownVoteNumber { get; set; }
        [Required]
        public virtual Movie Movie { get; set; }
        [Required]
        public virtual Profile Profile { get; set; }
    }
}