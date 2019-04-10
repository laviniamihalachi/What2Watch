using System;
using System.Collections.Generic;
using System.Data;
using System.Data.Entity;
using System.Data.Entity.Infrastructure;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;
using System.Web.Http.Description;
using What2Watch.Models;

namespace What2Watch.Controllers
{
    public class EmotionsController : ApiController
    {
        private ApplicationDbContext db = new ApplicationDbContext();

        // GET: api/Emotions
        public IQueryable<Emotion> GetEmotions()
        {
            return db.Emotions;
        }

        // GET: api/Emotions/5
        [ResponseType(typeof(Emotion))]
        public IHttpActionResult GetEmotion(int id)
        {
            Emotion emotion = db.Emotions.Find(id);
            if (emotion == null)
            {
                return NotFound();
            }

            return Ok(emotion);
        }

        // PUT: api/Emotions/5
        [ResponseType(typeof(void))]
        public IHttpActionResult PutEmotion(int id, Emotion emotion)
        {
            if (!ModelState.IsValid)
            {
                return BadRequest(ModelState);
            }

            if (id != emotion.EmotionId)
            {
                return BadRequest();
            }

            db.Entry(emotion).State = EntityState.Modified;

            try
            {
                db.SaveChanges();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!EmotionExists(id))
                {
                    return NotFound();
                }
                else
                {
                    throw;
                }
            }

            return StatusCode(HttpStatusCode.NoContent);
        }

        // POST: api/Emotions
        [ResponseType(typeof(Emotion))]
        public IHttpActionResult PostEmotion(Emotion emotion)
        {
            if (!ModelState.IsValid)
            {
                return BadRequest(ModelState);
            }

            db.Emotions.Add(emotion);
            db.SaveChanges();

            return CreatedAtRoute("DefaultApi", new { id = emotion.EmotionId }, emotion);
        }

        // DELETE: api/Emotions/5
        [ResponseType(typeof(Emotion))]
        public IHttpActionResult DeleteEmotion(int id)
        {
            Emotion emotion = db.Emotions.Find(id);
            if (emotion == null)
            {
                return NotFound();
            }

            db.Emotions.Remove(emotion);
            db.SaveChanges();

            return Ok(emotion);
        }

        protected override void Dispose(bool disposing)
        {
            if (disposing)
            {
                db.Dispose();
            }
            base.Dispose(disposing);
        }

        private bool EmotionExists(int id)
        {
            return db.Emotions.Count(e => e.EmotionId == id) > 0;
        }
    }
}