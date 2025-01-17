# RegistrationForm-Builder
tecxeon registration form builder

### pre-requisites:
- python
- Microsoft edge browser
- selenium

### How to run:
1. Clone the repository
2. Install selenium 
    ```bash 
    pip install selenium
    ```
2. Edit script.py set the google form link(url) and page name (should not contain spaces)
3. Run the script.py 
    ```py
    python script.py
    ```
### Google Form Format:
- The first column/question in the Google Form should be "Name" or "Full Name". Avoid using variations like "First Name", "Last Name" columns or "Name of Participant", "Participant 1" etc.
- All columns/questions should be in the "Short Answer" format (text field). Multiple choices and other formats are not supported.
