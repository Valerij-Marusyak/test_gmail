Test task

Write a test plan (script) for the login form in gmail. Cover script with selenium (java/gradle or python/pip). 
Push to git. The repository should have a README.md that will contain startup instructions.

Scenario

Check login with correct address and password
Check login with wrong password
Check input with wrong address
Check "Forgot password" functionality
Check "Forgot address" functionality

I have implemented the basic test cases, imho :). 
There are many more cases. For example, 
    
- Verify that there is limit on the total number of unsuccessful attempts
- Use the tab to navigate from username textbox to password textbox and then to the login button.
- Verify the login page and all its controls in different browsers
- Verify the login page by pressing ‘Back button’ of the browser.
  It should not allow you to enter into the system once you log out.
  

To check if the tests work:

Python 3.10 and higher is required.

""" shell
cd <project_folder>
git clone https://github.com/Valerij-Marusyak/test_gmail.git .
pip install -r requirements.txt
"""
Create run configuration for file <test_login_pageobject.py> and create there environment variables
SELENIUM_DRIVER_KIND=chrome;WINDOW_RESOLUTION=DESKTOP_1024X768
