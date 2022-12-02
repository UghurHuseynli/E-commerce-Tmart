let cartSection = document.getElementById('cartSection');
let accessToken = window.localStorage.getItem('access');
let totalPrice = document.getElementById('totalPriceInCart');
let totalPriceWithShipping = document.getElementById('TotalPriceForShopping');

let cardRequst = axios.create({
    baseURL: 'http://127.0.0.1:8000/api/card/',
    headers: {
        Authorization: `Bearer ${accessToken}`
    }
});

async function showCardItem(){
    let data = await cardRequst.get()
    let sum = 0
    data.data.forEach(item => {
        sum += item.price
        cartSection.innerHTML += createCardItem(item)
    });
    totalPrice.innerHTML = `$${sum}`
    if(sum === 0){
        totalPriceWithShipping.innerHTML = '$0'
    } else{
        totalPriceWithShipping.innerHTML = `$${parseFloat(sum) + parseFloat(document.getElementById('shippingAmount').innerHTML.split(' ')[1])}`
    }
};
showCardItem()


document.addEventListener('click', async (e) => {
    if(e.target.parentElement.className.includes('deleteCardItem')){
        const buttonId = e.target.parentElement.dataset.id
        await cardRequst.delete(`${buttonId}`)
        const response = await cardRequst.get()
        const data = await response.data
        getCartElementForCartModal()
        cartSection.innerHTML = ''
        let sum = 0
        data.forEach(item => {
            cartSection.innerHTML += createCardItem(item)
            sum += item.price
        })
        totalPrice.innerHTML = `$${sum}`
        totalPriceWithShipping.innerHTML = `$${parseFloat(sum) + parseFloat(document.getElementById('shippingAmount').innerHTML.split(' ')[1])}`
    }
})


function createCardItem(item){
    if(item.color[0] === 'white'){
        return `<tr>
            <td class="product-thumbnail"><a href="${item.url}"><img src="${item.image}" alt="${item.product_version_name}" /></a></td>
            <td class="product-name"><a href="${item.url}">${item.product_version_name}</a></td>
            <td class="product-price"><span class="amount">$${item.price}</span></td>
            <td class="product-color"><span style="white-space: nowrap;" class="amount"><i style="color: ${item.color}; margin-right: 1rem; border: 1px solid #d5d5d5; border-radius: 50%" class="fa-solid fa-circle"></i>${item.color}</span></td>
            <td class="product-size"><span class="amount">${item.size}</span></td>
            <td class="product-quantity"><input type="number" readonly value="${item.quantity}" /></td>
            <td class="product-subtotal">$${parseInt(item.quantity) * parseInt(item.price)}</td>
            <td class="product-remove"><a data-id="${item.id}" class="deleteCardItem"><i class="fa-solid fa-xmark"></i></a></td>
        </tr>
        `
    }
    return `<tr>
            <td class="product-thumbnail"><a href="${item.url}"><img src="${item.image}" alt="${item.product_version_name}" /></a></td>
            <td class="product-name"><a href="${item.url}">${item.product_version_name}</a></td>
            <td class="product-price"><span class="amount">$${item.price}</span></td>
            <td class="product-color"><span style="white-space: nowrap;" class="amount"><i style="color: ${item.color}; margin-right: 1rem;" class="fa-solid fa-circle"></i>${item.color}</span></td>
            <td class="product-size"><span class="amount">${item.size}</span></td>
            <td class="product-quantity"><input type="number" readonly value="${item.quantity}" /></td>
            <td class="product-subtotal">$${parseInt(item.quantity) * parseInt(item.price)}</td>
            <td class="product-remove"><a data-id="${item.id}" class="deleteCardItem"><i class="fa-solid fa-xmark"></i></a></td>
        </tr>
        `
}