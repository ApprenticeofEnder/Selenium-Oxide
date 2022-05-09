API
===

Class ``ExploitBuilder``
------------------------
``selenium_oxide.exploit_builder.ExploitBuilder``

The ExploitBuilder, the bread and butter of Selenium Oxide.

Method ``click_by_class``
~~~~~~~~~~~~~~~~~~~~~~~~~
Clicks an element based on CSS class name.

Parameters:
    button_class (str): The element class name

Returns:
``exploit_builder.ExploitBuilder``

Method ``click_by_id``
~~~~~~~~~~~~~~~~~~~~~~
Clicks an element based on HTML ID.

Parameters:
    button_id (str): The element HTML ID

Returns:
``exploit_builder.ExploitBuilder``

Method ``dump_cookies``
~~~~~~~~~~~~~~~~~~~~~~~
Dumps the cookies into the terminal.

Returns:
``exploit_builder.ExploitBuilder``

Method ``get``
~~~~~~~~~~~~~~
Makes a GET request to the specified endpoint in the browser.

Parameters:
    endpoint (str): The endpoint to which the browser navigates

Returns:
``exploit_builder.ExploitBuilder``

Method ``get_contents``
~~~~~~~~~~~~~~~~~~~~~~~
Get the contents of a specified field, based on the HTML ID.

Parameters:
    field (str): The HTML ID to extract text from

Returns:
str: The text in the given field

Method ``get_cookie_by_name``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Gets a browser cookie by its name.

Parameters:
    name (str): The name of the cookie

Returns:
Optional(dict): The cookie, or None

Method ``get_cookies``
~~~~~~~~~~~~~~~~~~~~~~
Get all cookies in the browser for the current page.

Returns:
list(dict): A list of cookies in the browser

Method ``login``
~~~~~~~~~~~~~~~~
Performs a full login process for a given endpoint. Convenience function.

Parameters:
    endpoint (str): The location of the login page
    username (str): The username to use
    password (str): The password to use
    username_id (str): The HTML ID of the username field
    password_id (str): The HTML ID of the password field
    submit_id (str): The HTML ID of the submit button

Returns:
``exploit_builder.ExploitBuilder``

Method ``send_enter_by_class``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Simulates sending the enter key to a particular element selected by CSS class name.

Parameters:
    field (str): The CSS Class name of the field to send enter in

Returns:
``exploit_builder.ExploitBuilder``

Method ``send_enter_by_id``
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Simulates sending the enter key to a particular element selected by HTML ID.

Parameters:
    field (str): The HTML ID of the field to send enter in

Returns:
``exploit_builder.ExploitBuilder``

Method ``set_cookie``
~~~~~~~~~~~~~~~~~~~~~
Set a cookie in the browser.

Parameters:
    name (str): The name of the cookie
    value (str): The cookie's value
    path (str): The path to which the cookie belongs
    secure (bool): Whether or not the cookie has the Secure attribute

Returns:
``exploit_builder.ExploitBuilder``

Method ``type_by_class``
~~~~~~~~~~~~~~~~~~~~~~~~
Send text to a particular field selected by CSS class name.

Parameters:
    field (str): The CSS class name of the field
    entry (str): The text to enter into the field

Returns:
``exploit_builder.ExploitBuilder``

Method ``type_by_id``
~~~~~~~~~~~~~~~~~~~~~
Send text to a particular field selected by HTML ID.

Parameters:
    field (str): The HTML ID of the field
    entry (str): The text to enter into the field

Returns:
``exploit_builder.ExploitBuilder``

Method ``wait_for_stealth``
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Waits for a period of time based on the length of the entry.

Parameters:
    entry (str): The entry to scale by

Returns:
``exploit_builder.ExploitBuilder``