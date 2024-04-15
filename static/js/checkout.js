document.addEventListener('DOMContentLoaded', function () {
    var stripe = Stripe('pk_test_51OjhrkFtBaQUT0WNipAlcuy2nFmBLzxKCboFhxqufitRYvpYe2gzkO0lBGvUbqd0T1fZ4FlmVvFXlwoJcyb7Rb1300YZNsnz3f');
    var elements = stripe.elements();
    // var cardElement = elements.create('card');
    var style = {
        base: {
            fontSize: '16px',
            color: '#32325d',
            fontFamily: 'Arial, sans-serif',
        },
    };

    var cardElement = elements.create('card', {
        style: style,
        hidePostalCode: true, // Скрыть поле для ввода почтового индекса
    });

    cardElement.mount('#card-element');

    var form = document.getElementById('donation-form');
    var submitButton = document.getElementById('submit-donation');
    var errorElement = document.getElementById('card-errors');

    form.addEventListener('submit', function (event) {
        event.preventDefault();
        stripe.createPaymentMethod({
            type: 'card',
            card: cardElement,
            billing_details: {
                name: document.getElementById('first_name').value + ' ' + document.getElementById('last_name').value
            }
        }).then(function (result) {
            if (result.error) {
                errorElement.textContent = result.error.message;
            } else {
                var formData = new FormData(form);
                formData.set('payment_method_id', result.paymentMethod.id);

                fetch('https://albukhari.inclusivetec.com/api/v1/donations/create/', {
                    method: 'POST',
                    body: formData
                }).then(function (response) {
                    return response.json();
                }).then(function (data) {
                    console.log(data);
                    if (data.success) {
                        alert('Payment successful!');
                    } else {
                        alert('Payment failed: ' + data.message);
                    }
                }).catch(function (error) {
                    console.error('Error:', error);
                });
            }
        });
    });
});