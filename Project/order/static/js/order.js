const select = document.getElementById("warehouse")
const cityInput = document.getElementById("cityName")
const modalForDelivery = document.getElementById("modal_for_delivery")
const radioBtns = document.getElementsByName("delivery")


radioBtns.forEach((btn)=>{
    btn.addEventListener("change", async ()=>{
        modalForDelivery.style.display = "block"
        await updateWarehouses()
        
    })
})

async function getWarehouses(city_name, type) {
    const response = await fetch(`/order/${city_name}?type=${type}`)
    const result = await response.json()
    return result.warehouses
}

cityInput.addEventListener("change", async (event)=>{
    await updateWarehouses()
})

async function updateWarehouses() {
    const city = cityInput.value
    const deliveryType = document.querySelector("input[name='delivery']:checked")?.value
    const warehouses = await getWarehouses(city, deliveryType)
    select.options.length = 0
    warehouses.forEach((warehouse)=>{
        const option = document.createElement("option")
        option.textContent = warehouse
        option.value = warehouse
        select.appendChild(option)
        
    })
}