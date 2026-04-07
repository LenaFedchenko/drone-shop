const select = document.getElementById("warehouse")
const cityInput = document.getElementById("cityName")

async function getWarehouses(city_name) {
    const response = await fetch(`/order/${city_name}`)
    const result = await response.json()
    return result.warehouses
}

cityInput.addEventListener("change", async (event)=>{
    const warehouses = await getWarehouses(event.target.value)
    warehouses.forEach((warehouse) => {
        const option = document.createElement("option")
        option.textContent = warehouse
        option.value = warehouse
        select.appendChild(option)
    });
})