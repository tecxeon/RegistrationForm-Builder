import re
import os
import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from template import template


def sanitize_name(label):
    # Remove all special characters, spaces, and convert to lowercase
    return re.sub(r"[^a-zA-Z0-9]", "", label).lower()


def fetch_data(url):
    options = webdriver.EdgeOptions()
    options.add_argument("--headless")
    driver = webdriver.Edge(options=options)
    driver.get(url)
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name^='entry']"))
        )
    except:
        raise Exception("failed to get element")
    elements = driver.find_elements(By.CSS_SELECTOR, "input[name^='entry']")
    class_elements = driver.find_elements(By.CLASS_NAME, "M7eMe")
    name = [element.text.strip() for element in class_elements]
    ids = [element.get_attribute("name") for element in elements]
    name_id = dict(zip(name, ids))
    heading_container = driver.find_element(By.CLASS_NAME, "ahS2Le")
    heading_element = heading_container.find_element(
        By.CSS_SELECTOR, "div[role='heading']"
    )
    base_url = url.rsplit("/", 1)[0]
    final_data = (name_id, heading_element.text, base_url)
    driver.quit()
    return final_data


def generate_form(data, base_url):
    form_html = """
    <form action="post">
        <div class="mb-6">
            <div class="grid grid-cols-2 gap-5">
                <input
                    type="text"
                    placeholder="First Name"
                    class="bg-lbox outline-none placeholder-labelColor text-white py-2 px-3 rounded"
                    required
                    id="fname"
                />
                <input
                    type="text"
                    placeholder="Last Name"
                    class="bg-lbox outline-none placeholder-labelColor text-white py-2 px-3 rounded"
                    required
                    id="lname"
                />
            </div>
        </div>
    """

    for label in data:
        name = sanitize_name(label)
        if name == "fullname" or name == "name":
            continue
        form_html += f'''
        <div class="mb-6">
            <input
                type="text"
                placeholder="{label}"
                class="bg-lbox outline-none placeholder-labelColor text-white py-2 px-3 w-full rounded"
                required
                id="{name}"
                name="{name}"
            />
        </div>
        '''

    form_html += """
        <button
            class="w-full bg-button py-5 text-center text-white active:bg-white active:text-black rounded"
            id="submit"
        >
            Register Now
        </button>
    </form>"""

    func = """
        $(function () {
            $("form").on("submit", function (e) {
                e.preventDefault();
                // data
                let fname = $("#fname").val();
                let lname = $("#lname").val();
                let fullname = fname + " " + lname;
    """

    for key in data:
        name = sanitize_name(key)
        if name == "fullname" or name == "name":
            continue
        else:
            func += f"""
                    let {name}=$("#{name}").val();
        """

    func += """let data = {"""

    for key, ids in data.items():
        name = sanitize_name(key)
        if name == "fullname" or name == "name":
            func += f'''"{ids}": fullname,'''
        else:
            func += f'''"{ids}": {name},'''

    func += (
        """
                };

                // url
                """
        + f'const url ="{base_url}/formResponse;"'
        + """

                // post
                    $.ajax({
                        type: "POST",
                        url: url,
                        data: data,
                        contentType: "application/json",
                        dataType: "jsonp",
                        complete: function () {
                            // Clear the input fields
                            $("form")[0].reset();

                            // Redirect to google.com
                            window.location.href = "../thankyou";
                        },
                    });
            });
        });
    """
    )

    return form_html, func


def main(url, pagename):
    print("creating page folder")
    if not os.path.exists(pagename):
        os.makedirs(pagename)
    path = os.path.join(pagename, "index.html")
    print("fectching data from url")
    name_id, heading, base_url = fetch_data(url)
    print("data fetched: ", name_id, heading, base_url)
    form, func = generate_form(name_id, base_url)
    print("generating template")
    page = template(heading, form, func)
    print("writing to file")
    with open(path, "w", encoding="utf-8") as f:
        f.write(page)
    print("copying necessary files")
    shutil.copy2("data/style.css", os.path.join(pagename, "style.css"))
    shutil.copy2("data/background.jpg", os.path.join(pagename, "background.jpg"))
    shutil.copy2("data/logo.png", os.path.join(pagename, "logo.png"))


# main(googleformurl, pagename)
