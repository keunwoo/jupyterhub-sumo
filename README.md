# jupyterhub-sumo : a big, batteries-included JupyterHub

VERY ROUGH WIP - use at your own risk

These scripts automate the creation of an jupyterhub installation with
the following features:

* GitHub OAuth login
* Full anaconda2 and anaconda3 release kernels included
* Cooperates with letsencrypt.org SSL cert serving
* Use sudospawner to reduce setuid root surface area
* Easy setup under vagrant for local development
* Easy setup under a remote VM environment

In the parlance of our times, this is an "opinionated" stack.


## Quick Start

### Remote VM setup

Step 1. Set up a GitHub application.

Step 2. Create a VM with a fresh Ubuntu 15.10 (Wily) install.

Step 3. ssh into the machine and run the following commands:

    $ git clone PATH_TO_REPO
    $ cd path_to_cloned_repo
    $ mkdir -p run
    $ cp examples/letsencrypt-config.json run/config.json
    $ sudo ./provision.sh
    $ sudo service nginx start

Edit run/config.json to taste.

    $ sudo su jupterhub -c 'script /dev/null'
    $ screen -S jupyterhub jupyterhub

As usual, use `CTRL-a CTRL-d` to detach the screen and `screen -r
jupyterhub` to reattach.  Read `man screen` for more info about how to
use screen.


### Vagrant setup

This is suitable for locally developing jupyterhub-sumo itself.

Step 1. Set up a GitHub application.

Step 2. Bring up the box:

    vagrant up

Step 3. Edit run/config.json to have the proper values:

* `__SERVER_NAME__`
* `__OAUTH_CALLBACK_URL__`
* `__OAUTH_CLIENT_ID__`
* `__OAUTH_CLIENT_SECRET__`

Step 4. ssh into the box and

    $ vagrant ssh
    $ sudo service nginx start
    $ sudo su jupyterhub
    $ cd
    $ jupyterhub


## TODO

- Config:
    - Consider switching to a format that can contain embedded comments
    - Document config format
    - Load config dynamically rather than statically where possible
- Ubuntu's pip is ancient; switch to a modern one
- Consider a real provisioning framework (chef, ansible, ...)
- Containerize and make a Docker image
- Start nginx system service persistently by default
- Setup jupyterhub as a system service instead of running the script
  under screen as su jupyterhub
- Linkify these docs


## Q & A

Q: Why sumo?

A: The name is derived from the old XEmacs "emacs-sumo" distributions,
which included not just the base emacs and a minimal package set, but
a wide array of convenient third party elisp packages, enough that you
rarely had to go get your own.  emacs-sumo was a band-aid over the
relatively primitive elisp packaging and distribution systems
available at the time.  Perhaps someday JupyterHub will be a
one-click-install sandstorm.io application that can install its own
third party kernels and manage auth, SSL, and sandboxing, and nobody
will want a monolithic "sumo" sized package anymore.  We can hope!

Q: This pile of hacky scripts is a joke.  Bro, do you even devops?

A: See the first line of this README and the TODO section.
