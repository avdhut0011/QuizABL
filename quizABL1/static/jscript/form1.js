document.addEventListener("DOMContentLoaded", function () {
    document.querySelector('.toggle-link a[href="#registration"]').addEventListener('click', function () {
        document.getElementById('registration-container').style.display = 'block';
        document.getElementById('login-container').style.display = 'none';
    });

    document.querySelector('.toggle-link a[href="#login"]').addEventListener('click', function () {
        document.getElementById('login-container').style.display = 'block';
        document.getElementById('registration-container').style.display = 'none';
    });
});
