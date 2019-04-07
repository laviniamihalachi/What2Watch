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

        //Get the current user profile
        public ActionResult Index()
        {
            var currentUserId = User.Identity.GetUserId();
            Profile profile = db.Profiles.Where(i => i.User.Id == currentUserId).FirstOrDefault();
            ViewBag.Profile = profile;
            return View();
        }


        // create profile - get method
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

        //Show a specific profile 
        public ActionResult Show(int id)
        {
            Profile profile = db.Profiles.Find(id);
            ViewBag.Profile = profile;

            return View();
        }

        //getMethod for editing the profile
        public ActionResult Edit(int id)
        {
            Profile profile = db.Profiles.Find(id);
            ViewBag.Profile = profile;
            return View();
        }

        [HttpPut]
        public ActionResult Edit(int id, Profile requestProfile)
        {
            try
            {
                Profile profile = db.Profiles.Find(id);
                if (TryUpdateModel(profile))
                {
                    //TempData["message"] = "S-a modificat " + profile.FirstName;
                    profile.FirstName = requestProfile.FirstName;
                    profile.LastName = requestProfile.LastName;
                    profile.Description = requestProfile.Description;
                    profile.Photo = requestProfile.Photo;
                    db.SaveChanges();
                    return RedirectToAction("Index", "Home");
                }
                //TempData["message"] = "NU s-a modificat " + profile.ProfileId + id;
                return RedirectToAction("Index");
            }
            catch (Exception e)
            {
                return View();
            }
        }
    }
}