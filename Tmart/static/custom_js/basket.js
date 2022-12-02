let basketButton = document.getElementById('addToBasket');
let size = document.querySelectorAll('.likeSelectButton')[0].dataset.id;
let color =document.querySelectorAll('.likeColorButton')[0].dataset.id;
let colorButton = document.querySelectorAll('.likeColorButton');
colorButton.forEach(button => button.addEventListener('click', (e) => {
    color = button.dataset.id
}));
let typeButton = document.querySelectorAll('.likeSelectButton');
typeButton.forEach(button => button.addEventListener('click', (e) => {
    size = button.dataset.id
}));

console.log(typeButton, colorButton)
accessToken = window.localStorage.getItem('access')
refreshToken = window.localStorage.getItem('refresh')
// if(accessToken || refreshToken == null){
//   deleteCookie('sessionid')
// }

basketButton.addEventListener('click', (e) => {
    e.preventDefault()
    product = basketButton.dataset.id
    quantity = document.getElementById('quantityInputSection').value
    console.log(quantity, color, size, product)
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/api/card/',
      headers: {
        Authorization: `Bearer ${accessToken}`
      },
      data: {
        product_version: product,
        color: color,
        size: size,
        quantity: quantity
      }
    }).then(res => {
      console.log(res)
    }).catch(err => {
      console.log(err)
    })
})


// function deleteCookie(c_name) {
//   document.cookie = encodeURIComponent(c_name) + "=deleted; expires=" + new Date(0).toUTCString();
// }