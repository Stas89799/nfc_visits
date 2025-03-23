document.addEventListener('DOMContentLoaded', function() {
    const formOpenBtn = document.getElementById('form-open');
    const formContainer = document.querySelector('.form_container');
    const formCloseBtn = document.querySelector('.form_close');
    const loginForm = document.querySelector('.login_form');
    const signupForm = document.querySelector('.signup_form');
    const signupBtn = document.getElementById('signup');
    const loginBtn = document.getElementById('login');

    formOpenBtn.addEventListener('click', () => {
        formContainer.style.display = 'flex';
        loginForm.style.display = 'block';
        signupForm.style.display = 'none';
    });

    formCloseBtn.addEventListener('click', () => {
        formContainer.style.display = 'none';
    });

    signupBtn.addEventListener('click', () => {
        loginForm.style.display = 'none';
        signupForm.style.display = 'block';
    });

    loginBtn.addEventListener('click', () => {
        signupForm.style.display = 'none';
        loginForm.style.display = 'block';
    });
});