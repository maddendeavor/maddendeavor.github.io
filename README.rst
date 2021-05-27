Welcome to Maddendeavor Website ReadME!!
----------------------------------------

Project Purpose
~~~~~~~~~~~~~~~
The purpose of this project is to migrate my current website at `www.maddendeavor.com` to a new
customizable website using Python.  Based on reading web content and watching videos, I believe
my site to be sufficiently small that using Python Flask will be the best option.  The purpose of
this update is to gain experience creating websites and hosting, as well as update my site to
include content for my new consulting business Maddendeavor, LLC. Plan is to create
two sides to the website (via 2 subdomains) so that I can have pages dedicated to travel and
a side showcasing my work as an electronics/test engineer turned burgeoning data scientist/analyst.

Migration of Wordpress Site
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Currently hosting my production Wordpress site on Bluehost `www.maddendeavor.com` is which was built
to showcase my travel blog and year long travel related details.

First order of business was to back up existing website files and database in case I accidentally kill the site.
Then practice restoring those files to a staging site found under `www.staging.maddeneavor.com`.  Used
this helpful guide to perform the back up: https://blogvault.net/how-to-manually-backup-your-wordpress-site/

1.  Contacted Bluehost to enable terminal access for my account
2.  Under advanced, stored SSH Public key so could ssh into server under port 22
3.  First backed up wordpress site and database using c-Panel:  'public_html' folder into TAR archive and
then production database `maddende_WPLG0`
4.  Created a "staging" subdomain to launch this new copy and practice backup - this all worked well
5.  In attempts to do the same for a new python implementation had to jump through hoops to get permissions
to terminal into the Bluehost server and to be able to C-compile python.
6.  Realized this will be difficult to install python packages without a good method to do so, so abandoned
this path

I am now working in the direction of starting up a completely new site, which will eventually get transferred
my URL.

New Website Hosting
~~~~~~~~~~~~~~~~~~~
This developmental version was hosted on Github initially, but now using Heroku. Plan to migrate the domain
off of Bluehost, but have paid for this service through Aug and will keep my current site running until
this one is finalized.  Eventually may look at AWS for hosting as it may have more control over the server.
For now plan to use the "free" service at Heroku as suggested by others.

Currently hosting this new website at https://maddendeavor-website.herokuapp.com/

Development
~~~~~~~~~~~
Decided to follow suggestions from various blogs and run a basic flask instance of a static style website.
For development, can run the website locally by pip installing into a .venv.  After activating can then
run the command `flask run` to check out the website design.


Project Credits
~~~~~~~~~~~~~~~
Thanks to Julia Nikulski for this great starting point!
https://towardsdatascience.com/how-to-build-a-data-science-portfolio-website-335b0f253822

License
~~~~~~~
MIT license in use (see license file)
