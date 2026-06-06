let register_btn = document.querySelector('#register-btn');
register_btn.addEventListener('click', function() { 
    // Registration logic here
    let name = document.querySelector('#name').value;
    let mobile = document.querySelector('#mobile').value;
    let email = document.querySelector('#email').value;
    let password = document.querySelector('#password').value;
    // For demonstration, we'll just log the values to the console
    console.log('Name:', name);
    console.log('Mobile:', mobile);
    console.log('Email:', email);
    console.log('Password:', password);
    // You can add your registration logic here, such as sending the data to a server
    if (name && mobile && email && password ) {
        // Proceed with registration
        alert('Registration successful!\nPlease check the console for details.\n\nProceeding to login page...');
    } else {
        alert('Please fill in all fields.');
    }
});