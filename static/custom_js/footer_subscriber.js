// subs_modal = document.getElementById('subs_form_modal');
// document.getElementById('mc-embedded-subscribe-form').addEventListener('submit', (e) => {
//   e.preventDefault()
//   const data = {'email': document.getElementById('mce-EMAIL').value };
//   fetch('http://127.0.0.1:8000/api/subscribe/', {
//     method: 'POST', // or 'PUT'
//     headers: {
//       'Content-Type': 'application/json',
//     },
//     body: JSON.stringify(data),
//   })
//     .then((response) => response.json())
//     .then((data) => {
//       document.getElementById('mce-EMAIL').value = '';
//       subs_modal.innerHTML = data['email'];
//     })
//     .catch((error) => {
//       console.error('Error:', error);
//     });
// })


subs_modal = document.getElementById('subs_form_modal');
document.getElementById('mc-embedded-subscribe-form').addEventListener('submit', (e) => {
  e.preventDefault()
  const email = document.getElementById('mce-EMAIL') ;
  axios({
    method: 'post',
    url: 'http://127.0.0.1:8000/api/subscribe/',
    data: {
      email: email.value,
    }
  }).then(res => {
    subs_modal.innerHTML = 'Your coupon sended your email';
    subs_modal.className = 'alert alert-success text-center';
    email.innerHTML = '';
  }).catch(err => {
    subs_modal.className = 'alert alert-danger text-center';
    subs_modal.innerHTML = err.response.data.email;
    email.innerHTML = '';
  })
})
