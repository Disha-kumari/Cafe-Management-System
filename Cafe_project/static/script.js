let cart = []
let total = 0

window.onload = loadMenu

function loadMenu(){

fetch("/menu")
.then(res => res.json())
.then(data => {

let container = document.getElementById("menu")

container.innerHTML = ""

data.forEach(item => {

let card = document.createElement("div")
card.className = "food-card"

card.innerHTML = `
<img src="${item.image}">
<h3>${item.name}</h3>
<p>₹${item.price}</p>
<button onclick="addToCart(${item.id},'${item.name}',${item.price})">
Add to Cart
</button>
`

container.appendChild(card)

})

})

}


function addToCart(id,name,price){

let qty = 1

let itemTotal = price * qty

cart.push({
id:id,
price:price,
quantity:qty
})

total += itemTotal

let table = document.getElementById("cart")

let row = table.insertRow()

row.insertCell(0).innerHTML = name
row.insertCell(1).innerHTML = price
row.insertCell(2).innerHTML = qty
row.insertCell(3).innerHTML = itemTotal

document.getElementById("total").innerHTML = total

}


function placeOrder(){

let payment = document.getElementById("payment").value

fetch("/place_order",{

method:"POST",
headers:{'Content-Type':'application/json'},
body:JSON.stringify({
items:cart,
payment:payment
})

})
.then(res => res.json())
.then(data => {

alert("Order Placed Successfully")
location.reload()

})

}