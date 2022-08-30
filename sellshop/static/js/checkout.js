let product_table = document.getElementById("product_table")


function checkoutManager() {
    fetch(`http://127.0.0.1:8000/api/cartitems/`, {
        method: 'GET',
        credentials: 'include',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem('token')}`
        }
    })
        .then(response => response.json())
        .then(data => {
            let subtotal = 0
            let html = ''
            if (product_table) {
                
                product_table.innerHTML = `
                <thead>
                <tr>
                <th>Product</th>
                <td>Total</td>
                </tr>
                </thead>
                `
            }
            console.log('data:',data[0])

            if (data.length > 0 && data[0]['basket']['status'] == false) {
                for (let i = 0; i < data.length; i++) {
                    html += `
                    <tr>
                    ${data[i]['count'] == 0 ? `
                    <th><span style="text-decoration: line-through">${data[i]['count']} x ${data[i]['productVersion']['title']}</span> Expired </th>` : `<th>${data[i]['count']} x ${data[i]['productVersion']['title']}</th>`}
                    <td>$${parseFloat(data[i]['count'] * data[i]['price']).toFixed(2)}</td>
                    </tr>`
                    subtotal += parseFloat(data[i]['count'] * data[i]['price'])
                }
                product_table.innerHTML += html
                let totall = (subtotal + 15).toFixed(2)
                console.log('total',totall)
                product_table.innerHTML += `
                <tr>
                <th>Cart Subtotal</th>
                <td>$${subtotal.toFixed(2)}</td>
                </tr>
                <tr>
                <th>Shipping and Handing</th>
                <td>$15.00</td>
                </tr>
                <tfoot>
                <tr>
                <th>Order total</th>
                <td class="totalprice" data-total="${totall}">$${totall}</td>
                </tr>
                </tfoot>
                `
            }
        });
}

window.addEventListener('DOMContentLoaded', (event) => {
    checkoutManager()
});


paypal.Buttons({
    // Sets up the transaction when a payment button is clicked
    style: {
      color: 'blue',
      shape: 'pill',
      label: 'pay',
      height: 40
    },
    createOrder: (data, actions) => {
        console.log('payment',document.querySelector('.totalprice').getAttribute('data-total'))
      return actions.order.create({
        purchase_units: [{
          amount: {
            value: document.querySelector('.totalprice').getAttribute('data-total') // Can also reference a variable or function
          }
        }]
      });
    },
    // Finalize the transaction after payer approval
    onApprove: (data, actions) => {
      return actions.order.capture().then(function(orderData) {
        // Successful capture! For dev/demo purposes:
        console.log('Capture result', orderData, JSON.stringify(orderData, null, 2));
        const transaction = orderData.purchase_units[0].payments.captures[0];
        alert(`Transaction ${transaction.status}: ${transaction.id}\n\nSee console for all available details`);
        // When ready to go live, remove the alert and show a success message within this page. For example:
        // const element = document.getElementById('paypal-button-container');
        // element.innerHTML = '<h3>Thank you for your payment!</h3>';
        // Or go to another URL:  actions.redirect('thank_you.html');
      });
    }
  }).render('#paypal-button-container');