using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;

namespace What2Watch.Models
{
    public class Profile
    {
        [Key]
        public int ProfileId { get; set; }
        [Required]
        public string FirstName { get; set; }
        [Required]
        public string LastName { get; set; }
        public string Description { get; set; }
        public string Photo { get; set; }
        public virtual ApplicationUser User { get; set; }

        //colectie albume
        public virtual ICollection<MovieCollection> MovieCollections { get; set; }
        
    }
}