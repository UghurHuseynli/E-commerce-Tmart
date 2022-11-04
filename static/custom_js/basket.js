basketButton = document.getElementById('addToBasket')
basketButton.addEventListener('click', (e) => {
    e.preventDefault()
    
    product = basketButton.dataset.id
    quantity = document.getElementById('quantityInputSection').value

    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/api/card/',
      headers: {
        Authorization: 'Bearer ${eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY3NTQ0NDQwLCJpYXQiOjE2Njc1NDQxNDAsImp0aSI6IjM0NGRlMzdlZGMzZjQxY2I5NjliODNiNWFhZTNhMjQyIiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJIcCJ9.m-h2LFY7Xni63coGcggQY3BmdAE0AJOTCEcWehLvIm8}'
      },
      data: {
        product_version: 1,
        quantity: 2
      }
    }).then(res => {
      console.log(res)
    }).catch(err => {
      console.log(err)
    })

    // AddBasket({'quantity': quantity, 'product_version': product})
    //   .then((data) => {
    //     console.log(data)
    //   })
    //   .catch((error) => {
    //     console.log('Error', error)
    //   })
})

// async function AddBasket(data = {}){
//     const response = await fetch('http://127.0.0.1:8000/api/card/', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//         },
//         body: JSON.stringify(data)
//     });
//     return response.json()
// }

