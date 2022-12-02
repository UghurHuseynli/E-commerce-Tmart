let productSection = document.getElementById('productSection');
let accessToken = window.localStorage.getItem('access');
let productRequest = axios.create({
    baseURL: 'http://127.0.0.1:8000/api/wishlist/',
    headers: {
        Authorization: `Bearer ${accessToken}`
    }
});


async function getProduct(){
    let response = await productRequest.get()
    productSection.innerHTML = createWishlist(response.data.results)
}
getProduct()

function createWishlist(data){
    return data.map(ele => {
        if(ele.is_stock){
            return `<tr>
                        <td class="product-remove"><a class="remove-wishlist-item" data-id="${ ele.id }">×</a></td>
                        <td class="product-thumbnail"><a href="${ ele.url }"><img src="${ ele.image }"
                                    alt="${ ele.product_name } picture" /></a></td>
                        <td class="product-name"><a href="${ ele.url }">${ ele.product_name }</a></td>
                        <td class="product-price"><span class="amount">$${ ele.price }</span></td>
                        <td class="product-stock-status"><span class="wishlist-in-stock">In Stock</span>
                        </td>
                        <td class="product-add-to-cart"><a class="productAddToCart" data-id="${ele.product_version}"> Add to Cart</a></td>
                    </tr>`
        } 
        else{
            return `<tr>
                        <td class="product-remove"><a class="remove-wishlist-item" data-id="${ ele.id }">×</a></td>
                        <td class="product-thumbnail"><a href="${ ele.url }"><img src="${ ele.image }"
                                    alt="${ ele.product_name } picture" /></a></td>
                        <td class="product-name"><a href="${ ele.url }">${ ele.product_name }</a></td>
                        <td class="product-price"><span class="amount">$${ ele.price }</span></td>
                        <td class="product-stock-status"><span class="wishlist-in-stock">Out of Stock</span>
                        </td>
                        <td class="product-add-to-cart"><a class="productAddToCart" data-id="${ele.product_version}"> Add to Cart</a></td>
                    </tr>`
        }
    }).join('');

}


document.addEventListener('click', async (e) => {
    if(e.target.className === 'remove-wishlist-item'){
        await productRequest.delete(`${e.target.dataset.id}`)
        await getProduct()
    }
    if(e.target.className === 'productAddToCart'){
        let id = e.target.dataset.id;
        await axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/api/card/',
        headers: {
            Authorization: `Bearer ${accessToken}`
        },
        data: {
            product_version: id,
            quantity: 1
        }
        })
    }
})