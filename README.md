# Selenium-Oxide
A Selenium boilerplate for automating web exploits. Use responsibly and ethically.

Selenium Oxide is a web exploitation automation framework designed 
around the needs of penetration testers and attack/defense CTF players 
alike! Whether you need to quickly make an automated
exploit for web apps, a stealthy automation tool for attack/defense, 
or a springboard for other exploit development, this is the tool for you!

The module offers a slimmer API than standard Selenium, and has 
multiple handy features, such as:

* Stealth functionality
* Builder pattern exploit writing
* Automatic browser binary configuration
* Cookie dumping and manipulation
* Proxy support
* Chrome support
* Arbitrary selector support
* Alert waiting
* User generation
* API interface
* JavaScript execution

## Why the Name?

When making this module I initially struggled with 
what to call it. I happened to look at another module,
named Selenium Wire, and decided yeah, you know what, 
using Selenium in the name is fair game. Selenium Oxide 
sounded cool, and when I looked up information on the 
chemical it read that it was at least somewhat dangerous.

A dangerous version of Selenium. Checks out for an offsec 
platform.

## Getting Started

Like regular Selenium, you're going to need a browser binary
and geckodriver. 

Selenium Oxide supports both Firefox and Chrome.

### Firefox

First, you'll want to grab a binary of Firefox. I recommend the following flow
for installing on UNIX systems. Once you've downloaded a version of firefox you 
like (for that, the official download page is usually sufficient):
```bash
    tar -xjf your_firefox_archive.tar.bz2
    sudo mv firefox /opt
```
This way, your Firefox binary will be in `/opt/firefox/firefox`, which is the
default location the module looks at. Perfect.

If you already have a Firefox binary on hand (maybe you already used Selenium),
then you can just specify the location in the exploit builder constructor. 

Then, you'll need Geckodriver. You can grab that from [here.](https://github.com/mozilla/geckodriver/releases)
```bash
    tar -xzf your_geckodriver_archive.tar.gz
    sudo mv geckodriver /usr/bin
```

So long as Geckodriver is in your path, you should be golden.

### Chrome

Installing Chrome for Seleniumis usually even easier than installing Firefox. Install Chrome normally
through your preferred package manager, then grab a copy of Chromedriver. Extract it and move 
it into /opt like so:
```bash
    sudo mv chromedriver /opt
```

Also for reference, you can find your Chrome binary with the `which` command:
```bash
    which google-chrome
```
### Final Steps

Next, just install from Pip!
```bash
    python3 -m pip install selenium-oxide
```
If that doesn't work, you may have an outdated version of Selenium (this library needs 4.1.0 or greater).
If so:
```bash
    pip install --upgrade selenium
```

That should install everythng you need.

## Using Selenium Oxide

Selenium Oxide is a builder-pattern exploit automation
framework, designed to provide a more immediately usable 
method of exploit automation before resorting 
to using the network tab. The ability to use proxies
makes the tool extremely useful as a ground layer for
API-focused exploit development as well.

### The Basics

First, import the module:

```python
from selenium_oxide.exploit_builder import ExploitBuilder
```

The ExploitBuilder constructor takes a number of arguments, two being mandatory:

```python
exploit = ExploitBuilder(
    #protocol
    "https",

    #hostname
    "juice-shop.herokuapp.com",                 

    #options (explained in docs)
    **options              
)
```

`protocol` and `hostname` correspond to the protocol (HTTP, HTTPS)
and hostname (domain, IP/port, etc) used by the web app.

Stealth mode is interesting, allowing the user to avoid alerting blue teams
with multiple rapid requests. As of 1.0.0, it uses the length of user
inputs to determine how long its sleep time is before writing text in
input boxes. There is some randomness thrown in as well, to really throw
off blue teams. However, this may be painfully slow while you're waiting
on the input to appear, so do keep an eye on your terminal for crashes.
Adjustable stealth timings may appear in a future release.

Proxy support is a 1.0.0 addition, allowing the user to use proxies (such
as ZAP or Burp Suite) to track their HTTP requests and responses. This is 
handy for mapping out APIs and finding potential additional vulnerabilities.

To start building exploits, you can chain functions together! 

```python
(
    exploit.get("/")
        .login("/#/login", "admin' OR 1=1;--", "password", '//*[@id="email"]', '//*[@id="password"]', '//*[@id="loginButton"]')
        .type_entry('//*[@id="mat-input-0"]', "<img src=\"http://url.to.file.which/not.exist\" onerror=alert(document.cookie);>")
        .send_enter('//*[@id="mat-input-0"]')
)
```

However, some functions, like `get_cookies` or `get_cookie_by_name` cannot be chained into 
other functions, and further exploitation must begin on a new line.

### Further Reading

The API documentation on [ReadtheDocs](https://selenium-oxide.readthedocs.io/) will have more information on how to use the framework to its full potential.

