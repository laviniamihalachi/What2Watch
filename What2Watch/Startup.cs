using Microsoft.Owin;
using Owin;

[assembly: OwinStartupAttribute(typeof(What2Watch.Startup))]
namespace What2Watch
{
    public partial class Startup
    {
        public void Configuration(IAppBuilder app)
        {
            ConfigureAuth(app);
        }
    }
}
