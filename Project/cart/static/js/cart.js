import { addToCart } from "./countProducts.js"
import { deleteInCart } from "./countProducts.js"

(
    async () => {
        await countSum()
    }
)()

async function countSum() {
    const response = await fetch("/count_sum/")
    const data = await response.json()
    document.getElementById("total_price").textContent = data.totalPrice
}
const addButtons = document.querySelectorAll(".addButton")
addButtons.forEach((button) => {
    button.addEventListener("click", async ()=>{
        const result = await addToCart(button.value)
        const container = button.closest(".product_container")
        const countProduct = container.querySelector(".renderCount")
        countProduct.textContent = result
        countSum()
    })
})

const deleteButtons = document.querySelectorAll(".deleteButton")
deleteButtons.forEach((button) => {
    button.addEventListener("click", async ()=>{
        const result = await deleteInCart(button.value)
        const container = button.closest(".product_container")
        const countProduct = container.querySelector(".renderCount")
        countProduct.textContent = result
        countSum()
    })
})