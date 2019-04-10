using Microsoft.AspNet.Identity;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using What2Watch.Models;

namespace What2Watch.Controllers
{
    public class MyCollectionController : Controller
    {
        private ApplicationDbContext db = new ApplicationDbContext();

        // GET: Friend
        public ActionResult Index()
        {
            return View();
        }

        public ActionResult GetMovieCollection()
        {
            var currentUserId = User.Identity.GetUserId();
            Profile currentProfile = db.Profiles.Where(i => i.User.Id == currentUserId).FirstOrDefault();

            List<MovieCollection> movieCollection = currentProfile.MovieCollections.ToList();
            if (movieCollection.Count() != 0)
            {
                ViewBag.movieCollection = movieCollection;
            }
            return View();
        }

        [HttpPost]
        public ActionResult AddMovieInCollection(MovieCollection movie)
        {
            var currentUserId = User.Identity.GetUserId();
            Profile currentProfile = db.Profiles.Where(i => i.User.Id == currentUserId).FirstOrDefault();

            try
            {
                currentProfile.MovieCollections.Add(movie);
                db.SaveChanges();
            }
            catch (Exception e)
            {
            }

            return View("Index");
        }

        [HttpPost]
        public ActionResult DeleteMovieFromCollection(MovieCollection movie)
        {
            var currentUserId = User.Identity.GetUserId();
            Profile currentProfile = db.Profiles.Where(i => i.User.Id == currentUserId).FirstOrDefault();

            try
            {
                currentProfile.MovieCollections.Remove(movie);
                db.SaveChanges();
            }
            catch (Exception e)
            {
            }

            return View("Index");
        }

        [HttpPost]
        public ActionResult UpdateMovieCollection(MovieCollection movie, String movieStatus)
        {
            MovieCollection movieToBeUpdated = db.MovieCollections.Where(x => x.MovieCollectionId == movie.MovieCollectionId).FirstOrDefault();
            MovieStatus newStatus = db.MovieStatuses.Where(x => x.Name == movieStatus).FirstOrDefault();
            try
            {
                movieToBeUpdated.MovieStatus = newStatus;
                db.SaveChanges();
            }
            catch (Exception e)
            {
            }
            return View("Index");
        }
    }
}