function validateForm() {
    let valid = true;

    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const phone = document.getElementById("phone").value.trim();
    const message = document.getElementById("message").value.trim();

    document.getElementById("nameError").innerText = "";
    document.getElementById("emailError").innerText = "";
    document.getElementById("phoneError").innerText = "";
    document.getElementById("messageError").innerText = "";

    if (name === "") {
        document.getElementById("nameError").innerText = "Name is required";
        valid = false;
    }

    const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
    if (!email.match(emailPattern)) {
        document.getElementById("emailError").innerText = "Invalid email format";
        valid = false;
    }

    if (!phone.match(/^[0-9]{10}$/)) {
        document.getElementById("phoneError").innerText = "Enter 10-digit phone number";
        valid = false;
    }

    if (message === "") {
        document.getElementById("messageError").innerText = "Message required";
        valid = false;
    }

    return valid;
}
