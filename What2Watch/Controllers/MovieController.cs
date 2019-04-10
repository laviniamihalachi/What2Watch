using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using What2Watch.Models;

namespace What2Watch.Controllers
{
    public class MovieController : Controller
    {
        private ApplicationDbContext db = new ApplicationDbContext();

        // GET: Movie
        public ActionResult Index()
        {
            return View();
        }

        public ActionResult GetMovies()
        {
            ICollection<Movie> movies = (from movie in db.Movies
                                       select movie).ToArray();
            ViewBag.movies = movies;

            return View();
        }

        // add new movie - get method
        public ActionResult New()
        {
            return View();
        }

        [HttpPost]
        public ActionResult New(Movie movie)
        {
            
            try
            {
                db.Movies.Add(movie);
                db.SaveChanges();
                return RedirectToAction("Index", "Home"); 
            }
            catch (Exception e)
            {
                return View();
            }
        }


        public ActionResult Show(int id)
        {
            Movie movie = db.Movies.Find(id);
            ViewBag.movie = movie;

            return View();
        }
    }
}