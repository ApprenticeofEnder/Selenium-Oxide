API
===

Class ``ExploitBuilder``
------------------------
``selenium_oxide.exploit_builder.ExploitBuilder``

The ExploitBuilder, the bread and butter of Selenium Oxide.

``ExploitBuilder(protocol, hostname, **options)``

Parameters:
    * protocol (str): The protocol to use (either "http" or "https" in most cases)
    * hostname (str): The hostname of the application to access
    * \*\*options

Options:
    * stealth (bool): Whether or not to engage stealth mode (Default: False)
    * browser (str): Which browser to use ("firefox" or "chrome", default: "firefox")
    * use_proxy (bool): Whether or not to use a proxy (Default: False)
    * proxy_address (str): Which proxy address to use (Default: "127.0.0.1:8080")

Methods
#######

Methods for ``selenium_oxide.exploit_builder.ExploitBuilder``

``click``
~~~~~~~~~~~~~~~~
Clicks an element.

Parameters:
    * button (str): The selector for the element to click
    * by (SelectBy): The selector type to use (default: SelectBy.XPATH)

Returns:
``exploit_builder.ExploitBuilder``

``click_by_class``
~~~~~~~~~~~~~~~~~~~~~~~~~
Clicks an element based on CSS class name.

Parameters:
    * button_class (str): The element class name

Returns:
``exploit_builder.ExploitBuilder``

``click_by_id``
~~~~~~~~~~~~~~~~~~~~~~
Clicks an element based on HTML ID.

Parameters:
    * button_id (str): The element HTML ID

Returns:
``exploit_builder.ExploitBuilder``

``click_by_xpath``
~~~~~~~~~~~~~~~~~~~~~~~~~
Clicks an element based on XPath.

Parameters:
    * xpath (str): The element XPath

Returns:
``exploit_builder.ExploitBuilder``

``dump_cookies``
~~~~~~~~~~~~~~~~~~~~~~~
Dumps the cookies into the terminal.

Returns:
``exploit_builder.ExploitBuilder``

``get``
~~~~~~~~~~~~~~
Makes a GET request to the specified endpoint in the browser.

Parameters:
    * endpoint (str): The endpoint to which the browser navigates

Returns:
``exploit_builder.ExploitBuilder``

``get_contents``
~~~~~~~~~~~~~~~~~~~~~~~
Get the contents of a specified field.

Parameters:
    * field (str): The selector to extract text from
    * by (SelectBy): The type of selector to use (default: SelectBy.XPATH)

Returns:
str: The text in the given field

``get_contents_by_id``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Get the contents of a specified field, based on the HTML ID

Parameters:
    * field (str): The HTML ID to extract text from

Returns:
str: The text in the given field

``get_contents_by_class``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Get the contents of a specified field, based on the CSS class name

Parameters:
    * field (str): The CSS class name to extract text from

Returns:
str: The text in the given field

``get_contents_by_xpath``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Get the contents of a specified field, based on the XPath

Parameters:
    * xpath (str): The XPath to extract text from

Returns:
str: The text in the given field

``get_cookie_by_name``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Gets a browser cookie by its name.

Parameters:
    * name (str): The name of the cookie

Returns:
Optional(dict): The cookie, or None

``get_cookies``
~~~~~~~~~~~~~~~~~~~~~~
Get all cookies in the browser for the current page.

Returns:
list(dict): A list of cookies in the browser

``login``
~~~~~~~~~~~~~~~~
Performs a full login process for a given endpoint. Convenience function.

Parameters:
    * endpoint (str): The location of the login page
    * username (str): The username to use
    * password (str): The password to use
    * username_xpath (str): The XPath of the username field
    * password_xpath (str): The XPath of the password field
    * submit_xpath (str): The XPath of the submit button

Returns:
``exploit_builder.ExploitBuilder``

``send_enter``
~~~~~~~~~~~~~~~~~~~~~
Simulates sending the enter key to a particular element.

Parameters:
    * field (str): The selector of the field
    * by (SelectBy): The selector type to use (default: SelectBy.XPATH)

Returns:
``exploit_builder.ExploitBuilder``

``send_enter_by_class``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Simulates sending the enter key to a particular element selected by CSS class name.

Parameters:
    * field (str): The CSS Class name of the field to send enter in

Returns:
``exploit_builder.ExploitBuilder``

``send_enter_by_id``
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Simulates sending the enter key to a particular element selected by HTML ID.

Parameters:
    * field (str): The HTML ID of the field to send enter in

Returns:
``exploit_builder.ExploitBuilder``

``send_enter_by_xpath``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Simulates sending the enter key to a particular element selected by XPath.

Parameters:
    * field (str): The XPath of the field to send enter in

Returns:
``exploit_builder.ExploitBuilder``

``set_cookie``
~~~~~~~~~~~~~~~~~~~~~
Set a cookie in the browser.

Parameters:
    * name (str): The name of the cookie
    * value (str): The cookie's value
    * path (str): The path to which the cookie belongs
    * secure (bool): Whether or not the cookie has the Secure attribute

Returns:
``exploit_builder.ExploitBuilder``

``type_entry``
~~~~~~~~~~~~~~~~~~~~~
Send text to a particular field.

Parameters:
    * field (str): The selector of the field
    * entry (str): The text to enter into the field
    * by (SelectBy): The selector type to use (default: SelectBy.XPATH)

Returns:
``exploit_builder.ExploitBuilder``

``type_by_class``
~~~~~~~~~~~~~~~~~~~~~~~~
Send text to a particular field selected by CSS class name.

Parameters:
    * field (str): The CSS class name of the field
    * entry (str): The text to enter into the field

Returns:
``exploit_builder.ExploitBuilder``

``type_by_id``
~~~~~~~~~~~~~~~~~~~~~
Send text to a particular field selected by HTML ID.

Parameters:
    * field (str): The HTML ID of the field
    * entry (str): The text to enter into the field

Returns:
``exploit_builder.ExploitBuilder``

``type_by_xpath``
~~~~~~~~~~~~~~~~~~~~~~~~
Send text to a particular field selected by XPath.

Parameters:
    * field (str): The XPath of the field
    * entry (str): The text to enter into the field

Returns:
``exploit_builder.ExploitBuilder``

``wait_for_alert``
~~~~~~~~~~~~~~~~~~~~~~~~~
Waits for an alert to fire, looking for an optional marker.

Parameters:
    * timeout (int): The amount of time to wait for an alert
    * marker (Optional[str]): A known marker, used to detect XSS attacks

Returns:
bool: whether or not the alert fired

``wait_for_stealth``
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Waits for a period of time based on the length of the entry.

Parameters:
    * entry (str): The entry to scale by

Returns:
``exploit_builder.ExploitBuilder``