form = document.getElementById('login_form_custom')
button = document.getElementById('loginButtonForToken')
button.addEventListener('click', (e) => {
    data = {'username': form.username.value, 'password': form.password.value}
    fetch('http://127.0.0.1:8000/api/token/',{
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    })
    .then((response) => response.json())
    .then((data) => {
        window.localStorage.setItem('access', data.access)
        window.localStorage.setItem('refresh', data.refresh)
    })
    form.submit()
})