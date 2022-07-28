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

``api``
~~~~~~~
``api(self, req_method: Callable, endpoint: str, api_protocol: str = None, api_hostname: str = None, **kwargs)``

Wrapper for Python's Requests library, enabling automatic proxy usage and cookie sharing when interfacing with APIs. 
kwargs supports same options as Requests.

Parameters:
    * req_method (Callable): requests function to use (requests.get, requests.posts, etc.)
    * endpoint (str): the API endpoint to request
    * api_protocol (str): the protocol to use for the API. Effectively defaults to the same protocol used in the ExploitBuilder
    * api_hostname (str): the hostname to use for the API. Effectively defaults to the same hostname used in the ExploitBuilder
    * \*\*kwargs: interoperable with Python Requests (e.g. headers parameter will be passed into the requests call)

Returns:
requests.Response

``api_get``
~~~~~~~~~~~
``api_get(self, endpoint: str, api_protocol: str = None, api_hostname: str = None, **kwargs)``

Wrapper for ExploitBuilder.api(requests.get, ...).

Parameters:
    * endpoint (str): the API endpoint to request
    * api_protocol (str): the protocol to use for the API. Effectively defaults to the same protocol used in the ExploitBuilder
    * api_hostname (str): the hostname to use for the API. Effectively defaults to the same hostname used in the ExploitBuilder
    * \*\*kwargs: interoperable with Python Requests (e.g. headers parameter will be passed into the requests call)

Returns:
requests.Response

``api_post``
~~~~~~~~~~~~
``api_post(self, endpoint: str, api_protocol: str = None, api_hostname: str = None, **kwargs)``

Wrapper for ExploitBuilder.api(requests.post, ...).

Parameters:
    * endpoint (str): the API endpoint to request
    * api_protocol (str): the protocol to use for the API. Effectively defaults to the same protocol used in the ExploitBuilder
    * api_hostname (str): the hostname to use for the API. Effectively defaults to the same hostname used in the ExploitBuilder
    * \*\*kwargs: interoperable with Python Requests (e.g. headers parameter will be passed into the requests call)

Returns:
requests.Response

``api_put``
~~~~~~~~~~~
``api_put(self, endpoint: str, api_protocol: str = None, api_hostname: str = None, **kwargs)``

Wrapper for ExploitBuilder.api(requests.put, ...).

Parameters:
    * endpoint (str): the API endpoint to request
    * api_protocol (str): the protocol to use for the API. Effectively defaults to the same protocol used in the ExploitBuilder
    * api_hostname (str): the hostname to use for the API. Effectively defaults to the same hostname used in the ExploitBuilder
    * \*\*kwargs: interoperable with Python Requests (e.g. headers parameter will be passed into the requests call)

Returns:
requests.Response

``api_delete``
~~~~~~~~~~~~~~
``api_delete(self, endpoint: str, api_protocol: str = None, api_hostname: str = None, **kwargs)``

Wrapper for ExploitBuilder.api(requests.delete, ...).

Parameters:
    * endpoint (str): the API endpoint to request
    * api_protocol (str): the protocol to use for the API. Effectively defaults to the same protocol used in the ExploitBuilder
    * api_hostname (str): the hostname to use for the API. Effectively defaults to the same hostname used in the ExploitBuilder
    * \*\*kwargs: interoperable with Python Requests (e.g. headers parameter will be passed into the requests call)

Returns:
requests.Response

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

Class ``SeO2User``
------------------------
``selenium_oxide.user_generator.SeO2User``

Generates an individual user for use with Selenium Oxide. Uses Faker.

``SeO2User(self, gen: Faker = None, locale: str = "en_US", **data)``

Parameters:
    * gen (faker.Faker): a Faker generator to use for the user. Defaults to an individually made generator.
    * locale (str): a locale to use for Faker. Defaults to "en_US".
    * \*\*data

Data:
All provided data is optional and overrides Faker profile generation.
    * name (str): The user's name
    * sex (str): The user's sex (usually "M" or "F") determines name gender in lieu of a provided name. Feel free to put "X" for a nonbinary name 
    * username (str): The user's username
    * email (str): The user's email
    * address (str): The user's address
    * birthdate (datetime.date): The user's date of birth

Methods
#######

Methods for ``selenium_oxide.user_generator.SeO2User``

``get_generator``
~~~~~~~~~~~~~~~~~
``get_generator(self)``

Getter method for the user's generator.

Returns:
``faker.Faker``