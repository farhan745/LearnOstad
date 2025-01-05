// Selecting necessary elements
let listProductHTML = document.querySelector(".listProduct");
let listCartHTML = document.querySelector(".listCart");
let iconCart = document.querySelector(".icon-cart");
let iconCartSpan = document.querySelector(".icon-cart span");
let body = document.querySelector("body");
let closeCart = document.querySelector(".close");

// Initialize products and cart arrays
let products = [];
let cart = [];

// Toggle cart visibility on icon click
iconCart.addEventListener("click", () => {
  body.classList.toggle("showCart");
});

// Close cart on button click
closeCart.addEventListener("click", () => {
  body.classList.toggle("showCart");
});

// Function to add product data to HTML
const addDataToHTML = () => {
  listProductHTML.innerHTML = ""; // Clear previous product data
  if (products.length > 0) {
    products.forEach((product) => {
      let newProduct = document.createElement("div");
      newProduct.dataset.id = product.id;
      newProduct.classList.add("item");
      newProduct.innerHTML = `
        <img src="${product.image}" alt="">
        <h2>${product.name}</h2>
        <div class="price">$${product.price}</div>
        <button class="addCart">Add To Cart</button>`;
      listProductHTML.appendChild(newProduct);
    });
  }
};

// Add product to cart on button click
listProductHTML.addEventListener("click", (event) => {
  let positionClick = event.target;
  if (positionClick.classList.contains("addCart")) {
    let id_product = positionClick.parentElement.dataset.id;
    addToCart(id_product);
  }
});

// Function to add product to cart
const addToCart = (product_id) => {
  let positionThisProductInCart = cart.findIndex(
    (value) => value.product_id == product_id
  );
  if (cart.length <= 0) {
    cart = [
      {
        product_id: product_id,
        quantity: 1,
      },
    ];
  } else if (positionThisProductInCart < 0) {
    cart.push({
      product_id: product_id,
      quantity: 1,
    });
  } else {
    cart[positionThisProductInCart].quantity += 1;
  }
  addCartToHTML();
  addCartToMemory();
};

// Function to save cart to local storage
const addCartToMemory = () => {
  localStorage.setItem("cart", JSON.stringify(cart));
};

// Function to render cart items to HTML
const addCartToHTML = () => {
  listCartHTML.innerHTML = ""; // Clear previous cart data
  let totalQuantity = 0;
  if (cart.length > 0) {
    cart.forEach((item) => {
      totalQuantity += item.quantity;
      let newItem = document.createElement("div");
      newItem.classList.add("item");
      newItem.dataset.id = item.product_id;
      
      let positionProduct = products.findIndex(
        (value) => value.id == item.product_id
      );
      let info = products[positionProduct];
      listCartHTML.appendChild(newItem);
      newItem.innerHTML = `
        <div class="image">
          <img src="${info.image}">
        </div>
        <div class="name">
          ${info.name}
        </div>
        <div class="totalPrice">$${info.price * item.quantity}</div>
        <div class="quantity">
          <span class="minus">&lt;</span>
          <span>${item.quantity}</span>
          <span class="plus">&gt;</span>
        </div>`;
    });
  }
  iconCartSpan.innerText = totalQuantity;
};

// Update cart item quantity on button click
listCartHTML.addEventListener("click", (event) => {
  let positionClick = event.target;
  if (
    positionClick.classList.contains("minus") ||
    positionClick.classList.contains("plus")
  ) {
    let product_id = positionClick.parentElement.parentElement.dataset.id;
    let type = positionClick.classList.contains("plus") ? "plus" : "minus";
    changeQuantityCart(product_id, type);
  }
});

// Function to change cart item quantity
const changeQuantityCart = (product_id, type) => {
  let positionItemInCart = cart.findIndex(
    (value) => value.product_id == product_id
  );
  if (positionItemInCart >= 0) {
    let item = cart[positionItemInCart];
    if (type === "plus") {
      item.quantity += 1;
    } else if (item.quantity > 1) {
      item.quantity -= 1;
    } else {
      cart.splice(positionItemInCart, 1);
    }
  }
  addCartToHTML();
  addCartToMemory();
};

// Function to initialize the app
const initApp = () => {
  fetch("products.json")
    .then((response) => response.json())
    .then((data) => {
      products = data;
      addDataToHTML();
      if (localStorage.getItem("cart")) {
        cart = JSON.parse(localStorage.getItem("cart"));
        addCartToHTML();
      }
    });
};

// Function to clear the cart
function clearCart() {
  cart = []; // Clear the cart array
  listCartHTML.innerHTML = ""; // Clear the cart display
  iconCartSpan.innerText = 0; // Reset the cart count in the icon
  addCartToMemory(); // Update the local storage
}

// Initialize the app
initApp();
