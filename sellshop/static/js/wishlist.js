url = location.origin + '/api/wishlist/';

function wishlistManager() {
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
			wishlist_tbody = document.getElementById('wishlist_tbody');
			if (wishlist_tbody) {
				wishlist_tbody.innerHTML = '';
			}

			id_arr = []
			for (let i = 0; i < data['product'].length; i++) {
				id_arr.push(data['product'][i]['id'])
				if (wishlist_tbody) {
					wishlist_tbody.innerHTML += `
						<tr>
					<td class="td-img text-left">
					<a href="#"><img style="width: 83px; height: 108px;" src="${data['product'][i]['images'][0]['image']}" alt="Add Product" /></a>
					<div class="items-dsc">
					<h5><a href="#">${data['product'][i]['title']}</a></h5>
					<p class="itemcolor">Color : <span>${data['product'][i]['color']['title']}</span></p>
					<p class="itemcolor">Size   : <span>${data['product'][i]['size']['title']}</span></p>
					</div>
					</td>
					<td>$ ${data['product'][i]['new_price']}</td>
					<td>${data['product'][i]['quantity'] > 0 ? `In Stock` : 'Expired'}</td>
					<td>
					<div class="submit-text">
					<a data="${data['product'][i]['id']}"  class="cartButton">add to cart</a>
					</div>
					</td>
					<td><i class="mdi mdi-close removeFromWishlist" data="${data['product'][i]['id']}" onmouseover="removeFromWishlist()"  title="Remove this product"></i></td>
					</tr>
					`;
				}
			}


		});
}

window.addEventListener('DOMContentLoaded', (event) => {
	wishlistManager()
});

//add to cart
function addtoCartFromWishlist() {
	const addToBasket = document.querySelectorAll('.cartButton');
	console.log(addToBasket)
	addToBasket.forEach(item => {
		item.onclick = function () {

			const valueId = this.getAttribute('data');

			console.log(valueId)
			try {
				count = document.getElementById('quantity').value;
			} catch {
				count = 1
			}
			AddtoCartLogic.getProducts(valueId, priceItem, priceItem, countItem);



		}
	})
}



function removeFromWishlist() {
	var removeFromWishlist = document.querySelectorAll('.removeFromWishlist');
	for (let i = 0; i < removeFromWishlist.length; i++) {
		removeFromWishlist[i].onclick = function () {
			const productId = this.getAttribute('data');
			WishlistLogic.wishlistPostManager(productId);
		}
	}
}