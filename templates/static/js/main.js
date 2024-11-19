document.addEventListener("DOMContentLoaded", function () {
    // Handle the login form submission
    const loginForm = document.getElementById("loginForm");
    const flashMessage = document.getElementById("flashMessage");

    loginForm.addEventListener("submit", function (e) {
        e.preventDefault(); // Prevent the default form submission

        const formData = new FormData(loginForm);

        // Make the POST request to the Flask app
        fetch("/login", {
            method: "POST",
            body: formData,
        })
        .then(response => {
            if (response.redirected) {
                window.location.href = response.url; // Redirect on successful login
            } else if (response.status === 500) {
                flashMessage.textContent = "Incorrect username or password. Please try again.";
            }
        })
        .catch(error => {
            console.error('Error:', error);
            flashMessage.textContent = "An error occurred. Please try again.";
        });
    });
});
