(function () {
    let form = document.querySelector('#subscribe-form');
    form.addEventListener('submit', async (event) => {
        event.preventDefault();
        console.log('here');

        let postData = {
            "email": form.email.value
        }
        let response = await fetch('http://127.0.0.1:8000/api/subscribers/', {
            headers: {
                'Content-Type': 'application/json',
            },
            method: "POST",
            body: JSON.stringify(postData)

        });
        console.log(postData)
        form.email.value = '';
        let responseData = await response.json();
        console.log('BACK END RESPONSE AS JSON: ', responseData);
        // if (response.ok) {
        //     alert('Ugurla subscribe oldunuz')
        // } else {
        //     alert(responseData.email);
        // }


    });

})();