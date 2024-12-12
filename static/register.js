
document.getElementById('register-form').addEventListener('submit', function(event) {
    let formIsValid = true;

    const username = document.getElementById('username').value;
    if (username.length < 3 || username.length > 20) {
        document.getElementById('username-error').textContent = "Username must be between 3 and 20 characters.";
        formIsValid = false;
    } else {
        document.getElementById('username-error').textContent = "";
    }

    const password = document.getElementById('password').value;
    if (password.length < 8) {
        document.getElementById('password-error').textContent = "Password must be at least 8 characters.";
        formIsValid = false;
    } else {
        document.getElementById('password-error').textContent = "";
    }

    const confirmPassword = document.getElementById('confirm-password').value;
    if (confirmPassword !== password) {
        document.getElementById('confirm-password-error').textContent = "Passwords do not match.";
        formIsValid = false;
    } else {
        document.getElementById('confirm-password-error').textContent = "";
    }

    const termsAccepted = document.getElementById('terms').checked;
    if (!termsAccepted) {
        document.getElementById('terms-error').textContent = "You must agree to the terms and conditions.";
        formIsValid = false;
    } else {
        document.getElementById('terms-error').textContent = "";
    }

    if (!formIsValid) {
        event.preventDefault();
    }
});
