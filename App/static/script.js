const products = [];

function render_products(data) {
    console.log(`Rendering ${data}`)
    const p_list = document.getElementById("product_list");
    const p_row = document.getElementById("row");
    console.log(`My list: ${p_list}`)
    for (i in data) {
        products[i] = data[i];
        [id, pName, description, price, picture] = data[i];

        const cloned_row = p_row.cloneNode(true);
        cloned_row.id = id;

        const p_title = cloned_row.querySelector(".card-title");
        p_title.innerHTML = id.toString() + ". Name: " + pName;

        const p_img = cloned_row.querySelector(".card-img");
        p_img.src = picture;

        const p_desc = cloned_row.querySelector(".card-description");
        p_desc.innerHTML = description;

        const p_price = cloned_row.querySelector(".card-price");
        p_price.innerHTML = price;

        // Rederect on click
        //var p_btn = cloned_row.querySelector(".btn");
        //_btn.onclick =

        console.log(`ID: ${id}, Name: ${pName}, Description: ${description}, Price: ${price}, Picture: ${picture}`);
        p_list.appendChild(cloned_row);
    }
    p_row.remove();
}

fetch("./", {
    headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
})
    .then(response => response.json())
    .then(data => render_products(data));

console.log("Fetching in progress...")


// const findDiv = document.querySelector("#product_list")
//
// function showOneProduct(product) {
//     const newElement = document.createElement("div")
//     newElement.className = "content"
//     newElement.innerHTML = `
//     <div class="item-card">
//         <div class="center">
//             <img src="${product.image_url}" class="image">
//             <h2>${product.name}</h2>
//             <p>Price: $${product.price}</p>
//             <button class="add-item">Add to Cart</button>
//         </div>
//     </div>
//     `
//     findDiv.append(newElement)
// }
//
// function showAllProducts(productsList) {
//     productsList.forEach(product => showOneProduct(product))
// }
//
// fetch("./products")
//     .then(response => response.json())
//     .then(productsList => showAllProducts(productsList))
//
// const findListOfItems = document.querySelector(".items-list")
//
// function showCartItem(cartItem) {
//     const newLi = document.createElement("li")
//     newLi.innerHTML = `
//     <p id="pTag"> ${cartItem.product.name}: $${cartItem.product.price}
//         <button class="delete-button">
//             <span>remove</span>
//         </button>
//
//     </p>
// `
//     findListOfItems.append(newLi)
// }
//
// function showAllCartItems(cartItems) {
//     cartItems.forEach(cartItem => showCartItem(cartItem))
// }
//
// fetch("./cart_items")
//     .then(response => response.json())
//     .then(cartItems => {
//         cartList = cartItems;
//         showAllCartItems(cartList)
//     })
//
// const addButton = newElement.querySelector(".add-product")
// addButton.addEventListener("click", event => {
//     findListOfItems.innerText = ""
//
//     fetch("./cart_items", {
//         method: "POST",
//         headers: {
//             "Content-Type": "application/json",
//             "Accept": "application/json"
//         },
//         body: JSON.stringify({
//             cart_id: 1,
//             product_id: product.id
//         })
//     })
//         .then(response => response.json())
//         .then(newCartItem => {
//             cartList.push(newCartItem);
//             showAllCartItems(cartList)
//         })
// })
//
// const removeButton = newLi.querySelector(".delete-button")
// removeButton.addEventListener("click", event => {
//     newLi.remove()
//     fetch(`./cart_items/${cartItem.id}`, {
//         method: "DELETE"
//     })
//         .then(response => response.json())
//         .then(results => {
//             cartList = results
//             findListOfItems.innerHTML = ""
//             showAllCartItems(cartList)
//         })
// })
//
// const checkOut = document.querySelector("#checkout")
// const newDiv = document.createElement("div")
// subTotoal = cartList.map(item => item.product.price)
// const subFloat = subTotoal.map(num => parseFloat(num))
// let sum = subFloat.reduce(function (accumulator, currentValue) {
//     return accumulator + currentValue
// }, 0)
// checkOut.innerHTML = ""
// newDiv.innerHTML = `
// <hr>
// <p id="subtotal"> Subtotal: $${sum.toFixed(2)}</p>
// <p id="total"> Total: $${((sum).toFixed(2))}</p>
// <button id="check-out">Check Out</button>
// `
// checkOut.append(newDiv)


