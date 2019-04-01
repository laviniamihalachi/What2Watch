using Microsoft.AspNet.Identity;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using What2Watch.Models;

namespace What2Watch.Controllers
{
    public class ProfileController : Controller
    {

        private ApplicationDbContext db = new ApplicationDbContext();

        public ActionResult Index()
        {
            return View();
        }

        public ActionResult New()
        {
            var currentUserId = User.Identity.GetUserId();
            ViewBag.user = db.Users.Find(currentUserId);
            return View();
        }

        [HttpPost]
        public ActionResult New(Profile profile)
        {
            var currentUserId = User.Identity.GetUserId();
            try
            {

                profile.User = db.Users.Find(currentUserId);
                db.Profiles.Add(profile);
                db.SaveChanges();
                return RedirectToAction("Index", "Home"); ;
            }
            catch (Exception e)
            {
                return View();
            }
        }


    }
}