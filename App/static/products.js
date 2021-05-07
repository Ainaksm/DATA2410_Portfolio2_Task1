console.log("Products frontend loaded");

var images = [
    "/App/static/images/breezy-hanson-AXOF4dPcg2g-unsplash.jpg",
    "/App/static/images/curtis-hystad-twClBGWNo-g-unsplash.jpg",
    "/App/static/images/lucas-van-oort-LVJRzXqbJ1s-unsplash.jpg",
    "/App/static/images/mateusz-butkiewicz-jNk0_Bpd_xw-unsplash.jpg",
    "/App/static/images/przemyslaw-zientala-54bRSFZkSGg-unsplash.jpg",
    "/App/static/images/rachael-gorjestani-XlA2994Txhw-unsplash.jpg",
    "/App/static/images/robert-wiedemann-d9yOg5zP-oQ-unsplash.jpg"
]

var products = []

function render_products(data){
    console.log(`Rendering ${data}`)
    var p_list = document.getElementById("product_list");
    var p_row = document.getElementById("first_row");
    console.log(`My list: ${p_list}`)
    for (i in data){
        products[i] = data[i];
        [id, name, description, price, picture] = data[i];

        var cloned_row = p_row.cloneNode(true);
        cloned_row.id = id;

        var p_title = cloned_row.querySelector(".card-title");
        p_title.innerHTML = id.toString() + ". Name: " + name;

        var p_img = cloned_row.querySelector(".card-image");
        p_img.src = picture;

        // Rederect on click
        //var p_btn = cloned_row.querySelector(".btn");
        //_btn.onclick =

        console.log('ID: ${id}, Name: ${name}, Description: ${description}, Price: ${price}, Picture: ${picture}');
        p_list.appendChild(cloned_row);
    }
    p_row.remove();
}

fetch("./products")
    .then(response => response.json())
    .then(data => render_products(data));

console.log("Fetching in progress...")
