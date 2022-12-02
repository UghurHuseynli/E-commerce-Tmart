getProductVersion = axios.create({
    baseURL: 'http://127.0.0.1:8000/api/'
});
let imageSection = document.querySelector('.product__big__images');
let priceSection = document.querySelector('.pro__dtl__prize');
let colorSection = document.querySelector('.pro__choose__color');
let sizeSection = document.querySelector('.pro__choose__size');
let productVersionId = document.getElementById('addToBasket').dataset.id;
let productId = document.getElementById('productIdElement').dataset.id;

let accessToken = window.localStorage.getItem('access')
let refreshToken = window.localStorage.getItem('refresh')

let modal = document.getElementById("myModalForAddToWishListModal");

let btn = document.getElementById("addToWishlist");

let span = document.getElementsByClassName("close-custom-detail-page")[0];

async function getProductDetails(){
    let response = await getProductVersion.get(`product-versions?product=${ productId }`);
    sizeSection.innerHTML = createSize(response.data)
    colorSection.innerHTML = createColor(response.data, response.data)  
}
getProductDetails()

async function getProductDetail(id) {
    let response = await getProductVersion.get(`product-versions/${id}/`);
    imageSection.innerHTML = createImage(response.data.images)
    priceSection.innerHTML = createPrice(response.data.price, response.data.discount, response.data.is_percent)
    $(".xzoom, .xzoom-gallery").xzoom({
        tint: '#333',
        Xoffset: 15,
    });

    $(document).ready(function () {
        $('.center').slick({
            centerPadding: '60px',
            slidesToShow: 4,
            infinite: false,
            dots: false,
            arrows: true,
            responsive: [{
                    breakpoint: 768,
                    settings: {
                        arrows: true,
                        centerMode: true,
                        centerPadding: '40px',
                        slidesToShow: 4
                    }
                },
                {
                    breakpoint: 480,
                    settings: {
                        arrows: true,
                        centerMode: true,
                        centerPadding: '40px',
                        slidesToShow: 1
                    }
                }
            ]
        });
    });
}
getProductDetail(productVersionId)

function createImage(images) {
     return `
        <img class="xzoom" src="${ images[0] }" xoriginal="${ images[0] }" />
        <div class="xzoom-thumbs D-flex div center">
        ${images.map(image => {
            return `
                <div class="item">
                    <a href="${ image }">
                        <img class="xzoom-gallery" style="object-fit: scale-down;" height="72" width="100" src="${ image }"  xpreview="${ image }">
                    </a>
                </div>
            `
        }).join('')}
        </div>
    `
}

function createPrice(price, discount, is_percent) {
    if(discount){
        if(is_percent){
            return `
                <li class="old__prize">$${ price }</li>
                <li>$${ price - (price * discount / 100) }</li>
            `
        }
            return `
                <li class="old__prize">$${ price }</li>
                <li>$${ price - discount }</li>
            `
    }
    return `<li>$${ price }</li>`
}

function createColor(product, products) {
    let allColors = removeDuplicates(products, 'colors')
    let uniqueColor = removeDuplicates(product, 'colors')
    return  Object.entries(allColors).map(([color, id]) => {
        if(color in uniqueColor){
            if(color !== 'white'){
                return `
                    <li><a class="likeColorButton" data-id="${ id }" title="${ color }"><i style="color: ${ color }; " class="fa-solid fa-circle"></i></a></li>
                `  
            }else{
                return `
                    <li><a class="likeColorButton" data-id="${ id }" title="${ color }"><i style="color: ${ color }; border: 1px solid #d5d5d5; border-radius: 50%" class="fa-solid fa-circle"></i></a></li>
                `
            }
        }else{
            if(color !== 'white'){
                return `
                    <li><a class="likeColorButton" data-id="${ id }" data-disabled='disabled' title="${ color }"><i style="color: ${ color }; cursor: not-allowed;" class="fa-solid fa-circle-xmark"></i></a></li>
                `
            }else{
                return `
                    <li><a class="likeColorButton" data-id="${ id }" data-disabled='disabled' title="${ color }"><i style="color: ${ color }; background-color: black; cursor: not-allowed; border: 1px solid #d5d5d5; border-radius: 50%" class="fa-solid fa-circle-xmark"></i></a></li>
                `
            }
        }
    }).join('')
}

function createSize(products) {
    let uniqueSize = removeDuplicates(products, 'sizes')
    return Object.entries(uniqueSize).map(([productType, productId]) => {
        return `
            <li><a class="likeSelectButton" data-id = "${ productId }">${ productType }</a></li>
        `
    }).join('')
}

function removeDuplicates(products, name){
    let unique = []
    for (let i = 0; i < products.length; i++) {
        let obj = products[i];
        if (!unique[obj[`${name}`]]) {
            unique[obj[`${name}`]] = [];
        }
        unique[obj[`${name}`]].push(obj.id);
    }
    return unique
}

let colorForApi
let sizeForApi
document.addEventListener('click', async (e) => {
    if(e.target.className === 'likeSelectButton'){

        let typeId = (e.target.dataset.id).split(',');
        sizeForApi = typeId;
        response = await getProductVersion.get('product-versions/');
        let data = []
        response.data.forEach(element => {
            if(typeId.includes(String(element.id))){
                data.push(element)
            }
        })
        priceSection.innerHTML = createPrice(data[0].price, data[0].discount, data[0].is_percent)
        colorSection.innerHTML = createColor(data, response.data)
    }
    if(e.target.parentElement.className === 'likeColorButton' && e.target.parentElement.dataset.disabled !== 'disabled'){
        let colorId = (e.target.parentElement.dataset.id).split(',');
        colorForApi = colorId
        let response;
        for (const id of colorId) {
            response = await getProductVersion.get(`product-versions/${id}/`)
            if(response.data.images.length !== 0){
                break;
            }
        }
        
        imageSection.innerHTML = createImage(response.data.images) 
        $(".xzoom, .xzoom-gallery").xzoom({
            tint: '#333',
            Xoffset: 15,
        });
    
        $(document).ready(function () {
            $('.center').slick({
                centerPadding: '60px',
                slidesToShow: 4,
                infinite: false,
                dots: false,
                arrows: true,
                responsive: [{
                        breakpoint: 768,
                        settings: {
                            arrows: true,
                            centerMode: true,
                            centerPadding: '40px',
                            slidesToShow: 4
                        }
                    },
                    {
                        breakpoint: 480,
                        settings: {
                            arrows: true,
                            centerMode: true,
                            centerPadding: '40px',
                            slidesToShow: 1
                        }
                    }
                ]
            });
        });
    }
    if(e.target.id === 'addToBasket'){
        e.preventDefault()
        let quantity = document.getElementById('quantityInputSection').value;
        let id = sizeForApi.filter(value => colorForApi.includes(value))[0];
        axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/api/card/',
        headers: {
            Authorization: `Bearer ${accessToken}`
        },
        data: {
            product_version: id,
            quantity: quantity
        }
        })
        await getCartElementForCartModal()
        await document.getElementById('cartModalButton').click()
    }
    if(e.target.id === 'addToWishlist' | e.target.className === 'ti-heart'){
        let id = sizeForApi.filter(value => colorForApi.includes(value))[0];
        let res = await axios({
            method: 'post',
            url: 'http://127.0.0.1:8000/api/wishlist/',
            headers: {
                Authorization: `Bearer ${accessToken}`
            },
            data: {
                product_version: id
            }
        })
        if(res.status === 200){
            document.getElementById('AddToWishlistModalInnerHtml').innerHTML = res.data.message
        }
        else if(res.status === 201){
            document.getElementById('AddToWishlistModalInnerHtml').innerHTML = 'The product has been added to your wishlist'
        }
    }
})

btn.onclick = function() {
    modal.style.display = "block";
  }
  
  span.onclick = function() {
    modal.style.display = "none";
  }
  
  window.onclick = function(event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  }