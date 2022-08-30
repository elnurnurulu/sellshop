let cart_body = document.getElementById("cart_body")

url = location.origin + '/api/cartitems/';
console.log(url)

function cartItemManager() {
    fetch(url, {
            method: 'GET',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            }
        })
        .then(response => response.json())
        .then(data => {
            // let html = ''
            total_price = 0
            total_products = document.getElementById("total_products")
            for (let i = 0; i < data.length; i++) {
                if (data[i]['count'] > 0 && data[i]['basket']['status'] == false) {
                    total_price += parseFloat(data[i]['count'] * data[i]['price'])
                    console.log(data[i]['productVersion']['color']['title'])
                    cart_body.innerHTML += `
            <tr>
            <td class="td-img text-left">
            <a href="#"><img style="height: 7rem;" src="${data[i]['productVersion']['images'][0]['image']}" alt="Add Product" /></a>
            <div class="items-dsc">
            <h5><a href="#">${data[i]['productVersion']['title']}</a></h5>
            <p class="itemcolor">Color : <span>${data[i]['productVersion']['color']['title']}</span></p>
            <p class="itemcolor">Size   : <span>${data[i]['productVersion']['size']['title']}</span></p>
            </div>
            </td>
            <td>$${parseFloat(data[i]['productVersion']['new_price']).toFixed(2)}</td>
            <td>
            

            <div class="plus-minus" >
            <button class="dec qtybutton" onclick="minus(${data[i]['productVersion'].id}, ${ data[i].id }, ${ data[i].count}, ${ data[i].price } )" id="minus">-</button>
            <input type="number"  data="${data[i]['productVersion']['id']}" min="1" max="${data[i]['productVersion']['quantity']}" value="${data[i]['count']}" name="qtybutton" class="plus-minus-box">
            <button class="inc qtybutton" onclick="plus(${data[i]['productVersion'].id}, ${ data[i].id }, ${ data[i].count}, ${ data[i].price } )" id="plus">+</button>
            </div>
            
            </td>
            <td>
            <strong>$${parseFloat(data[i]['productVersion']['new_price'] * data[i]['count']).toFixed(2)}</strong>
            </td>
            <td><i data="${data[i]['productVersion']['id']}" class="mdi mdi-close " onclick="remove(${data[i]['productVersion'].id}, ${ data[i].id }, ${ data[i].count}, ${ data[i].price } )" title="Remove this product"></i></td>
            </tr>
			`
                }
            }
            // cart_body.innerHTML = html
            total_products.children[0].innerHTML = `
                        <tr>
                            <th>Shipping and Handing</th>
                            <td>$15.00</td>
                        </tr>
                        <tr>
                            <th>Cart Subtotal</th>
                            <td>$${total_price.toFixed(2)}</td>
                        </tr>
                        `
            total_products.children[1].innerHTML = `
                <tr>
                    <th class="tfoot-padd">Order total</th>
                    <td class="tfoot-padd">$${(total_price + 15).toFixed(2)}</td>
                </tr>`
            if (data.length == 0) {
                total_products.style.display = 'none'
            }

        });
}

window.addEventListener('DOMContentLoaded', (event) => {
    cartItemManager()
});


async function minus(productVersion, valueId, countItem, priceItem) {
    console.log('mius bura');

    let postData = {
        "productVersion": productVersion,
        "price": parseFloat(priceItem),
        "sub_total": parseFloat(priceItem),
        "count": parseInt(--countItem),
    }
    async function removeProducts() {
        console.log('here');
        let response = await fetch(`http://127.0.0.1:8000/api/cartitems/${valueId}/`, {
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            },
            method: "PUT",
            body: JSON.stringify(postData)
        });


        window.location.reload()
    }
    removeProducts();
    // }


};

async function plus(productVersion, valueId, countItem, priceItem) {

    let postData = {
        "productVersion": productVersion,
        "price": parseFloat(priceItem),
        "sub_total": parseFloat(priceItem),
        "count": parseInt(++countItem),
    }

    async function addProducts() {
        console.log('here');
        let response = await fetch(`http://127.0.0.1:8000/api/cartitems/${valueId}/`, {
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            },
            method: "PUT",
            body: JSON.stringify(postData)
        });

        window.location.reload()
    }
    addProducts();
};

async function remove(productVersion, valueId, countItem, priceItem) {

    let postData = {
        "productVersion": productVersion,
        "price": parseFloat(priceItem),
        "sub_total": parseFloat(priceItem),
        "count": parseInt(countItem),
    }

    async function removeProducts() {
        console.log('here');
        let response = await fetch(`http://127.0.0.1:8000/api/cartitems/${valueId}/`, {
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            },
            method: "DELETE",
            body: JSON.stringify(postData)
        });
        console.log('remove')
        window.location.reload()
    }
    removeProducts();
};