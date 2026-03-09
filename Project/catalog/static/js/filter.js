const categoriesObj = document.getElementById("categories")
const productContainer = document.getElementById("filter_products")

async function filterProducts() {
    const response = await fetch("/catalog/filter", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            selectCategory: categoriesObj.value
        })
    })
    
    const request = await response.json()
    productContainer.innerHTML = ``
    let html = ``
    request.filtrated_products.forEach(product => {
        html += `

                <a href="/catalog/${product.id}" class="product_container">
                    <h1>${product.name}</h1>
                    <img src="/catalog/static/media/${product.image_url}" alt="">
                    <p>${product.description}</p>
                    <button class="addButton" value="${product.id}">+</button>
                    <button class="deleteButton" value="${product.id}">-</button>
                </a>
        `
    });
    productContainer.innerHTML += html
}
categoriesObj.addEventListener("change", ()=>{
    filterProducts()
})