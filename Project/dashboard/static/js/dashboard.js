const contactPage = document.getElementById("contact-page")
const ordersPage = document.getElementById("orders-page")
const deliveryPage = document.getElementById("delivery-page")

const contactBtn = document.getElementById("contact")
const ordersBtn = document.getElementById("orders")
const deliveryBtn = document.getElementById("delivery")

function showDelivery(){
    deliveryPage.style.display = "flex"
    ordersPage.style.display = "none"
    contactPage.style.display = "none"
}
function showOrders(){
    deliveryPage.style.display = "none"
    ordersPage.style.display = "flex"
    contactPage.style.display = "none"
}
function showContact(){
    deliveryPage.style.display = "none"
    ordersPage.style.display = "none"
    contactPage.style.display = "flex"
}
contactBtn.addEventListener("click", ()=>{
    showContact()
})
ordersBtn.addEventListener("click", ()=>{
    showOrders()
})
deliveryBtn.addEventListener("click", ()=>{
    showDelivery()
})