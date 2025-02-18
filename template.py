def template(title, form, func):
    return (
        """<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>"""
        + f"{title}"
        + """</title>
        <link rel="stylesheet" href="style.css" />
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
        <link
            href="https://fonts.googleapis.com/css2?family=Outfit:wght@100;400&display=swap"
            rel="stylesheet"
        />
        <style>
            /* Hide the up and down arrows on number inputs */
            input[type="number"]::-webkit-inner-spin-button,
            input[type="number"]::-webkit-outer-spin-button {
                -webkit-appearance: none;
                margin: 0;
            }
            input[type="number"] {
                -moz-appearance: textfield;
            }
            input,
            textarea,
            button,
            select,
            a {
                -webkit-tap-highlight-color: transparent;
            }
        </style>
    </head>
    <body
        class="bg-no-repeat bg-cover bg-center"
        style="background-image: url('background.jpg')"
    >
        <div
            id="banner"
            tabindex="-1"
            class="flex z-50 gap-8 justify-between py-6 w-full backdrop-blur-xl"
            style="background-color: rgba(0, 0, 0, 0.354)"
        >
            <div
                class="bg-no-repeat bg-center bg-contain py-6 mx-auto w-full z-10"
                style="background-image: url('logo.png')"
            ></div>
        </div>
        <div class="relative min-h-screen py-40 backdrop-blur-sm">
            <div class="container mx-auto relative">
                <div
                    class="flex flex-col lg:flex-row w-10/12 lg:w-8/12 rounded-2xl shadow-custom mx-auto overflow-hidden"
                >
                    <div
                        class="w-full lg:w-1/2 lg:flex flex-col items-center justify-center bg-no-repeat bg-cover bg-center"
                        style="background-image: url('background.jpg')"
                    ></div>
                    <div class="bg-boxColor w-full lg:w-1/2 lg:py-6 py-9 px-6">
                        <h2
                            class="text-white text-3xl mb-10 text-center font-bold leading-10"
                        >
                            """
        + f"{title}"
        + """
                        </h2>
                        """
        + f"{form}"
        + """
                    </div>
                </div>
            </div>
            <div
                class="absolute mb-6 left-1/2 bottom-0 transform -translate-x-1/2 md:left-auto md:transform-none md:right-0 md:bottom-0 md:mr-7"
            >
                <h3 class="text-[#B7B7B7]">Made with ❤ by tecxeon</h3>
            </div>
        </div>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
        <script>"""
        + f"{func}"
        + """
            // Select all required input elements
            const inputs = document.querySelectorAll("input[required]");

            inputs.forEach((input) => {
                // Listen for the invalid event
                input.addEventListener("invalid", function (event) {
                    // Prevent the browser's default validation UI
                    event.preventDefault();

                    // Add a red border to the input field
                    this.classList.add("border-red-500", "border"); // Add your Tailwind CSS classes here
                });

                // Listen for the input event to reset the border color when the user starts typing
                input.addEventListener("input", function (event) {
                    this.classList.remove("border-red-500", "border"); // Remove the specific CSS classes
                });
            });
        </script>
    </body>
</html>
"""
    )
