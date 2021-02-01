Welcome to Maddendeavor Website ReadME!!
----------------------------------------

Project Purpose
~~~~~~~~~~~~~~~
The purpose of this project is to migrate my current website at `www.maddendeavor.com` to a new
customizable website using Python.  Based on reading web content and watching videos, I believe
my site to be sufficiently small that using Python Flask will be the best option.  The purpose of
this update is to gain experience creating websites and hosting, as well as update my site to
include content for my new consulting business Maddendeavor, LLC.

Hosting
~~~~~~~
Currently hosting through GIT but will migrate to Bluehost server in future.  Eventually
want to migrate off of Bluehost, but have paid for this service through Aug and want to
keep my current site running.  Eventually may look at a "free" service such as Herouku t
to host the site.

Currently hosting this new website at https://maddendeavor.github.io/


Migration of Wordpress Site
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Currently hosting a Wordpress site on Bluehost, and plan to migrate to using this git repo.
First order of business was to back up website files and database in case I accidentally kill the site.
Then practice restoring those files to a staging site found under `www.staging.maddeneavor.com`.  Used
this helpful guide to perform the back up: https://blogvault.net/how-to-manually-backup-your-wordpress-site/

1.  Contacted Bluehost to enable terminal access for my account
2.  Under advanced, stored SSH Public key so could ssh into server under port 22
3.  First backed up wordpress site and database using c-Panel:  'public_html' folder into TAR archive and then production database `maddende_WPLG0`


Project Credits
~~~~~~~~~~~~~~~
Thanks to Julia Nikulski for this great starting point!
https://towardsdatascience.com/how-to-build-a-data-science-portfolio-website-335b0f253822

License
~~~~~~~
MIT license in use (see license file)
