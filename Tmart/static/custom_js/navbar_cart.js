let accessTokenForCartModalSection = window.localStorage.getItem('access');
let shopModalSection = document.getElementById('shpCartWrap');
let totalPriceForModalCart = document.getElementById('totalPriceForCardModal');

let getCardDataForModal = axios.create({
                            baseURL: 'http://127.0.0.1:8000/api/card/',
                            headers: {
                                Authorization: `Bearer ${accessTokenForCartModalSection}`
                            },     
                        })


let cartSectionInNavbar = document.getElementById('cartSection');
let totalPriceForNavbarSection = document.getElementById('totalPriceInCart');
let totalPriceWithShippingInNavbar = document.getElementById('TotalPriceForShopping');

async function showCardItemForModalJS(){
    let data = await getCardDataForModal.get()
    let sum = 0
    data.data.forEach(item => {
        sum += item.price
        cartSectionInNavbar.innerHTML += createCardItemInModalCard(item)
    });
    totalPriceForNavbarSection.innerHTML = `$${sum}`
    totalPriceWithShippingInNavbar.innerHTML = `$${parseFloat(sum) + parseFloat(document.getElementById('shippingAmount').innerHTML.split(' ')[1])}`
};

function createCardItemInModalCard(item){
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



async function getCartElementForCartModal(){
    if(accessTokenForCartModalSection){
        let response = await getCardDataForModal.get() 
        shopModalSection.innerHTML = createCartElementForCartModelSection(response.data)
        let sum = 0
        response.data.forEach(data => sum += data.price)
        totalPriceForModalCart.innerHTML = `$${sum}`
    }
}
getCartElementForCartModal()

function createCartElementForCartModelSection(data){
    return data.map(element => {
        return `<div class="shp__single__product">
                    <div class="shp__pro__thumb">
                        <a href="#">
                            <img src="${ element.image }" alt="${ element.product_version_name } images">
                        </a>
                    </div>
                    <div class="shp__pro__details">
                        <h2><a href="${ element.url }">${ element.product_version_name }</a></h2>
                        <span class="quantity">QTY: ${ element.quantity }</span>
                        <span class="shp__price">$${ element.price }</span>
                    </div>
                    <div class="remove__btn">
                        <a title="Remove this item"><i data-id="${ element.id }" class="zmdi zmdi-close RemoveElementFromCartModal"></i></a>
                    </div>
                </div>`
    }).join("")
}

document.addEventListener('click', async (e) => {
    if(e.target.classList.contains('RemoveElementFromCartModal')){
        await getCardDataForModal.delete(`${ e.target.dataset.id }`)
        await getCartElementForCartModal()
        cartSectionInNavbar.innerHTML = ''
        await showCardItemForModalJS()
    }
})
