let requestProduct = axios.create({
    baseURL: 'http://127.0.0.1:8000/api/'
});
let productSection = document.getElementById('productSection');
let categorySection = document.getElementById('productCategorySection');

async function getProduct() {
    let response = await requestProduct.get('product/')
    productSection.innerHTML = createProduct(response.data.results)
}
getProduct()

async function getCategory(){
    let response = await requestProduct.get('category/')
    categorySection.innerHTML += await createCategory(response.data.results)
    await whichCategorySelect()
}
getCategory()

function createProduct(products) {
    return products.map(product => {
        if(product.new_price !== product.price){
            return `<div class="col-md-3 single__pro col-lg-3 cat--1 col-sm-4 col-xs-12">
            <div class="product foo">
                <div class="product__inner">
                    <div class="pro__thumb">
                        <a href="${ product.url }">
                            <img src="${ product.img }" alt="${ product.name } images">
                        </a>
                    </div>
                    <div class="product__hover__info">
                        <ul class="product__action">
                            <li><a data-toggle="modal" data-target="#productModal" data-id="${ product.id }" title="Quick View"
                                    class="quick-view modal-view detail-link myCustomDataModelSection"><span
                                        class="ti-plus"></span></a></li>
                        </ul>
                    </div>
                </div>
                <div class="product__details">
                    <h2><a href="${ product.url }">${ product.name }</a></h2>
                    <ul class="product__price">
                        <li class="old__price">$ ${ product.price }</li>
                        <li class="new__price">$ ${ product.new_price }</li>
                    </ul>
                </div>
            </div>
        </div>`
        }
        else{
            return `<div class="col-md-3 single__pro col-lg-3 cat--1 col-sm-4 col-xs-12">
            <div class="product foo">
                <div class="product__inner">
                    <div class="pro__thumb">
                        <a href="${ product.url }">
                            <img src="${ product.img }" alt="${ product.name } images">
                        </a>
                    </div>
                    <div class="product__hover__info">
                        <ul class="product__action">
                            <li><a data-toggle="modal" data-target="#productModal" data-id="${ product.id }" title="Quick View"
                                    class="quick-view modal-view detail-link myCustomDataModelSection"><span
                                        class="ti-plus"></span></a></li>
                            </li>
                        </ul>
                    </div>
                </div>
                <div class="product__details">
                    <h2><a href="${ product.url }">${ product.name }</a></h2>
                    <ul class="product__price">
                        <li class="new__price">$ ${ product.new_price }</li>
                    </ul>
                </div>
            </div>
        </div>`
        }
    }).join("");
}

async function createCategory(categories){
    return categories.map(category => {
        if(category.is_navbar){
            return `<button data-filter="${ category.id }">${ category.category_name }</button>`
        }
    }).join("")
}


function whichCategorySelect(){
    categorySection.addEventListener('click', (e) => {
        [...categorySection.children].forEach(category => {
            category.className = '';
        })
        if(e.target.type == 'submit'){
            e.target.className = 'is-checked'
            let id = e.target.dataset.filter
            getProductForCategory(id)
        }
    })
}

async function getProductForCategory(id){
    let response = await requestProduct.get(`product?category=${id}`)
    console.log(response)
    productSection.innerHTML = createProduct(response.data.results)
}

document.addEventListener('click', async (e) => {
    if(e.target.parentElement.classList.contains('myCustomDataModelSection')){
        let id = e.target.parentElement.dataset.id;
        let response = await requestProduct.get(`product/${id}/`);
        let modalSection = document.getElementById('customModalSection');
        modalSection.innerHTML = createModal(response.data)
    }
})

function createModal(data){
    if(data.new_price !== data.price){
        return `<div class="modal-product">
                    <!-- Start product images -->
                    <div class="product-images">
                        <div class="main-image images">
                            <img alt="big images" src="${ data.img }">
                        </div>
                    </div>
                    <!-- end product images -->
                    <div class="product-info">
                        <h1>${data.name}</h1>
                        <div class="price-box-3">
                            <div class="s-price-box">
                                <span class="new-price">$${ data.new_price }</span>
                                <span class="old-price">$${ data.price }</span>
                            </div>
                        </div>
                        <div class="quick-desc">
                            ${ data.detail_description }
                        </div>
                        <div class="addtocart-btn">
                            <a href="#">Add to cart</a>
                        </div>
                    </div><!-- .product-info -->
                </div>`
    }
    else{
        return `<div class="modal-product">
        <!-- Start product images -->
        <div class="product-images">
            <div class="main-image images">
                <img alt="big images" src="${ data.img }">
            </div>
        </div>
        <!-- end product images -->
        <div class="product-info">
            <h1>${data.name}</h1>
            <div class="price-box-3">
                <div class="s-price-box">
                    <span class="new-price">$${ data.new_price }</span>
                </div>
            </div>
            <div class="quick-desc">
                ${ data.detail_description }
            </div>
            </div>
            <div class="addtocart-btn">
                <a href="#">Add to cart</a>
            </div>
        </div><!-- .product-info -->
    </div>`
    }
}

let filterButton = document.getElementById('filterModalButton');
let filterForSize = document.getElementById('filterListForSize');
let filterForTags = document.getElementById('filterListForTags');
let filterForBrands = document.getElementById('filterListForBrands');
let filterForColors = document.getElementById('filterListForColor');

async function createFilterSection(){
    let responseSizes = await requestProduct.get('product-sizes/')
    let responseTags = await requestProduct.get('product-tags/')
    let responseBrands = await requestProduct.get('product-brands/')
    let responseColors = await requestProduct.get('product-colors/')

    filterForSize.innerHTML += createSizeFilters(responseSizes.data.results)
    filterForTags.innerHTML += createTagsFilters(responseTags.data.results)
    filterForBrands.innerHTML += createBrandsFilters(responseBrands.data.results)
    filterForColors.innerHTML += createColorsFilters(responseColors.data.results)
}
createFilterSection()

function createSizeFilters(data){
    return data.map(size => {
        return `<li><a class="eventListenerForSize" data-filter="${ size.id }">${ size.size }</a></li>`
    }).join("");
}

function createTagsFilters(data){
    return data.map(tag => {
        return `<li><a class="eventListenerForTags" data-filter="${ tag.id }">#${ tag.name }</a></li>`
    }).join("");
}

function createBrandsFilters(data){
    return data.map(brand => {
        return `<li><a class="eventListenerForBrands" data-filter="${ brand.id }">${ brand.name }</a></li>`
    }).join("");
}

function createColorsFilters(data){
    return data.map(color => {
        if(color.color === 'white'){
            return `<li class="${ color.color }"><a class="eventListenerForColor" data-filter="${ color.id }"><i style="padding: 0; margin-right: 1.2rem; color: ${ color.color }; border: 1px solid #d5d5d5; border-radius: 50%;" class="fa-solid fa-circle eventListenerForColorIcons"></i>${ color.color }</a></li>`
        }
        return `<li class="${ color.color }"><a class="eventListenerForColor" data-filter="${ color.id }"><i style="color: ${ color.color };" class="fa-solid fa-circle eventListenerForColorIcons"></i>${ color.color }</a></li>`
    }).join("");
}

document.addEventListener('click', async (e) => {
    if(e.target.classList.contains('eventListenerForSort')){
        let sort = e.target.dataset.filter
        let response = await requestProduct.get(`product?sort=${ sort }`)
        productSection.innerHTML = createProduct(response.data.results)
    }
    if(e.target.classList.contains('eventListenerForSize')){
        let id = e.target.dataset.filter
        let response = await requestProduct.get(`product?size=${ id }`)
        productSection.innerHTML = createProduct(response.data.results)
    }
    if(e.target.classList.contains('eventListenerForTags')){
        let id = e.target.dataset.filter
        let response = await requestProduct.get(`product?tag=${ id }`)
        productSection.innerHTML = createProduct(response.data.results)
    }
    if(e.target.classList.contains('eventListenerForBrands')){
        let id = e.target.dataset.filter
        let response = await requestProduct.get(`product?brand=${ id }`)
        productSection.innerHTML = createProduct(response.data.results)
    }
    if(e.target.classList.contains('eventListenerForPrice')){
        let id = e.target.dataset.filter
        let response = await requestProduct.get(`product?price=${ id }`)
        productSection.innerHTML = createProduct(response.data.results)
    }
    if(e.target.classList.contains('eventListenerForColor')){
        let id = e.target.dataset.filter
        let response = await requestProduct.get(`product?color=${ id }`)
        productSection.innerHTML = createProduct(response.data.results)
    }
    if(e.target.classList.contains('eventListenerForColorIcons')){
        let id = e.target.parentElement.dataset.filter
        let response = await requestProduct.get(`product?color=${ id }`)
        productSection.innerHTML = createProduct(response.data.results)
    }
})