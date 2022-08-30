
document.addEventListener("DOMContentLoaded", function () {
    let proSection = document.getElementById('cartdrop')
    async function renderProducts() {
        console.log('here');
        let response = await fetch(`/api/cartitems/`, {
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            },
            method: "GET",
        });
        let data = await response.json()
        console.log('datadan qayidanlar :  ', data);

        let total_price = 0
        let totalItems = 0
        for (let i = 0; i < data.length; i++) {
            if (data[i]['count'] > 0 && data[i]['basket']['status'] == false) {
                totalItems += parseInt(data[i]['count'])
                // console.log(totalItems)
                let ids = data[i]['id']
                total_price += parseFloat(data[i]['count'] * data[i]['price'])
                proSection.innerHTML += `
                <div class="sin-itme clearfix">
                <i data="${data[i]['productVersion']['id']}" class="mdi mdi-close " onclick="remove(${data[i]['productVersion'].id}, ${ data[i].id }, ${ data[i].count}, ${ data[i].price } )" title="Remove this product"></i>					<a class="cart-img" href="http://127.0.0.1:8000/en/single_product/${data[i]['productVersion']['id']}/"><img src="${data[i]['productVersion']['images'][0]['image']}"
										alt="" /></a>
					<div class="menu-cart-text">
					
                    <a href="/en/products/${data[i]['productVersion']['id']}/">
					<h5>${data[i]['count']} x ${data[i]['productVersion']['title']}</h5>
					</a>
					<span>Color : ${data[i]['productVersion']['color']['title']}</span>
					<span>Size : ${data[i]['productVersion']['size']['title']}</span>
					<strong>$${(data[i]['price'] * data[i]['count']).toFixed(2)}</strong>
					</div>
				</div>
                `

            }
        };
        if (totalItems > 0) {
            document.getElementById('itemnumBer').innerHTML = totalItems;

        }
        let subTotal = document.getElementById('sub_price')
        subTotal.innerHTML = `
        <span> <strong >$ ${total_price.toFixed(2)}</strong></span>

        
        `
    }
    renderProducts();

});


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

wishlistUrl = location.origin + '/api/wishlist/'
const WishlistLogic = {
	wishlistPostManager(productId) {
		fetch(wishlistUrl, {
			method: 'POST',
			credentials: 'include',
			headers: {
				'Content-Type': 'application/json',
				'Authorization': `Bearer ${localStorage.getItem('token')}`
			},
			body: JSON.stringify({
				'product': productId,
			})
		})
			.then(response => response.json())
			.then(data => {
				try {
					wishlistManager()
				}catch{
				}
			});
            console.log('product id:',productId)

	}
}

var add_to_wishlist = document.getElementsByClassName('add_to_wishlist');
for (let i = 0; i < add_to_wishlist.length; i++) {
	add_to_wishlist[i].onclick = function () {
		const productId = this.getAttribute('data');
		WishlistLogic.wishlistPostManager(productId);
	}
}
