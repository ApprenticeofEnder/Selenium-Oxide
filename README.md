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

Planned features include:

* Payload generation
* Chrome support
* Web crawl functionality
* More as suggested or encountered in field testing

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
and geckodriver. As of right now, Selenium Oxide only supports
Firefox.

To install Firefox and Geckodriver:

```bash
    # With Firefox BZ2 archive obtained
    tar -xjf your_firefox_archive.tar.bz2
    sudo mv firefox /opt
    
    # With Geckodriver gzip archive obtained
    tar -xzf your_geckodriver_archive.tar.gz
    sudo mv geckodriver /usr/bin
```

If you have an existing binary of Firefox you'd like to use, you can simply pass
that into the Exploit Builder Constructor.

Once you have the prerequisite binaries installed, you 
can simply type:

```bash
python3 -m pip install --upgrade selenium-oxide
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
from selenium_oxide.payload_builder import PayloadBuilder # Future Release
```

The ExploitBuilder constructor takes a number of arguments, two being mandatory:

```python
exploit = ExploitBuilder(
    #protocol
    "https",

    #hostname
    "juice-shop.herokuapp.com",                 

    #stealth mode (default False)
    stealth=True,

    #firefox binary location (default /opt/firefox/firefox)
    firefox_binary_path="/opt/firefox/firefox",

    #use a proxy (default False)
    useProxy=True,           

    #proxy address (default 127.0.0.1:8080)
    proxyAddress="127.0.0.1:8080"               
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
        .login("/login", "admin' OR 1=1;--", "admin", "username", "password", "login-btn")
        .type_by_id("search-field", "<img src=\"http://url.to.file.which/not.exist\" onerror=alert(document.cookie);>")
        .click_by_id("search-btn")
)
```

However, some functions, like `get_cookies` or `get_cookie_by_name` cannot be chained into 
other functions, and further exploitation must begin on a new line.

### Further Reading

The API documentation on [ReadtheDocs](https://selenium-oxide.readthedocs.io/en/latest/) will have more information on how to use the framework to its full potential.