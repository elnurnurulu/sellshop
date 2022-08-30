//add to cart

document.addEventListener("DOMContentLoaded", function AddtoCartLogic() {
    let button = document.getElementsByClassName('cartButton');
    for (let i = 0; i < button.length; i++) {
        button[i].addEventListener('click', async (event) => {
            event.preventDefault();
            var countItem,
                element = document.getElementById('quantity');
            if (element != null) {
                countItem = element.value;
            } else {
                countItem = 1;
            }
            let price = document.getElementsByClassName('priceItem')
            let priceItem = price[i].getAttribute('data-value')
            let findItem = document.getElementsByClassName('Idpro')
            let valueId = findItem[i].value

            // console.log('value-id: ', valueId);
            // console.log('count', countItem)
            // console.log('price', price)
            // console.log('priceitem', priceItem)
            // console.log('finditem', findItem)
            async function getProducts() {
                let postData = {

                    "productVersion": parseInt(valueId),
                    "price": parseFloat(priceItem),
                    "sub_total": parseFloat(priceItem),
                    "count": parseInt(countItem),

                }
                let response = await fetch('/api/cartitems/', {
                    credentials: 'include',
                    headers: {
                        'Content-Type': 'application/json',
                        "X-Requested-With": "XMLHttpRequest",
                        'Authorization': `Bearer ${localStorage.getItem('token')}`,
                        // 'X-CSRF-TOKEN': "FETCH"
                    },

                    method: "POST",

                    body: JSON.stringify(postData)
                });
                console.log(JSON.stringify(postData))
                // window.location.reload()    
            }
            console.log('i of button:', i);
            getProducts();
           
        });

    }
});