// const stripe = Stripe("pk_test_51OjhrkFtBaQUT0WNipAlcuy2nFmBLzxKCboFhxqufitRYvpYe2gzkO0lBGvUbqd0T1fZ4FlmVvFXlwoJcyb7Rb1300YZNsnz3f");
// let elements;
// initialize();
// checkStatus();
//
// document.querySelector("#payment-form").addEventListener("submit", handleSubmit);
//
// async function initialize() {
//     const response = await fetch("http://127.0.0.1:8000/api/v1/donations/create-checkout-session/", {
//         method: "POST",
//         headers: {"Content-Type": "application/json"},
//         body: JSON.stringify({items: [{id: "prod_Pb2VzLECmiyEYk"}]}),
//     });
//     const {clientSecret} = await response.json();
//
//     const appearance = {
//         theme: 'stripe',
//     };
//     elements = stripe.elements({appearance, clientSecret});
//
//     const paymentElementOptions = {
//         layout: "tabs",
//     };
//
//     const paymentElement = elements.create("payment", paymentElementOptions);
//     paymentElement.mount("#payment-element");
// }
//
// async function handleSubmit(e) {
//     e.preventDefault();
//     setLoading(true);
//
//     const {error} = await stripe.confirmPayment({
//         elements,
//         confirmParams: {
//             // Make sure to change this to your payment completion page
//             return_url: "http://localhost:8000/api/v1/donations/success/",
//         },
//     });
//
//     if (error && (error.type === "card_error" || error.type === "validation_error")) {
//         showMessage(error.message);
//     } else {
//         showMessage("An unexpected error occurred.");
//     }
//
//     setLoading(false);
// }
//
// async function checkStatus() {
//     const clientSecret = new URLSearchParams(window.location.search).get(
//         "payment_intent_client_secret"
//     );
//
//     if (!clientSecret) {
//         return;
//     }
//
//     const {paymentIntent} = await stripe.retrievePaymentIntent(clientSecret);
//
//     switch (paymentIntent.status) {
//         case "succeeded":
//             showMessage("Payment succeeded!");
//             break;
//         case "processing":
//             showMessage("Your payment is processing.");
//             break;
//         case "requires_payment_method":
//             showMessage("Your payment was not successful, please try again.");
//             break;
//         default:
//             showMessage("Something went wrong.");
//             break;
//     }
// }
//
// function showMessage(messageText) {
//     const messageContainer = document.querySelector("#payment-message");
//
//     messageContainer.classList.remove("hidden");
//     messageContainer.textContent = messageText;
//
//     setTimeout(function () {
//         messageContainer.classList.add("hidden");
//         messageContainer.textContent = "";
//     }, 4000);
// }
//
// function setLoading(isLoading) {
//     if (isLoading) {
//         document.querySelector("#submit").disabled = true;
//         document.querySelector("#spinner").classList.remove("hidden");
//         document.querySelector("#button-text").classList.add("hidden");
//     } else {
//         document.querySelector("#submit").disabled = false;
//         document.querySelector("#spinner").classList.add("hidden");
//         document.querySelector("#button-text").classList.remove("hidden");
//     }
// }


const stripe = Stripe("pk_test_51OjhrkFtBaQUT0WNipAlcuy2nFmBLzxKCboFhxqufitRYvpYe2gzkO0lBGvUbqd0T1fZ4FlmVvFXlwoJcyb7Rb1300YZNsnz3f");
let elements;
initialize();
checkStatus();

document.querySelector("#payment-form").addEventListener("submit", handleSubmit);

async function initialize() {
    const response = await fetch("http://127.0.0.1:8000/api/v1/donations/create-checkout-session/", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({items: [{id: "prod_Pb2VzLECmiyEYk"}]}),
    });
    const {clientSecret} = await response.json();

    const appearance = {
        theme: 'stripe',
        variables: {
            borderRadius: '36px',
        }
    }
    const expressCheckoutOptions = {
        buttonHeight: '50',
        buttonTheme: {
            applePay: 'white-outline'
        }
    }
    const elements = stripe.elements({
        mode: 'payment',
        amount: 1099,
        currency: 'usd',
        appearance,
    })
    const expressCheckoutElement = elements.create('expressCheckout', expressCheckoutOptions)
    expressCheckoutElement.mount('#express-checkout-element')
}

async function handleSubmit(e) {
    e.preventDefault();
    setLoading(true);

    const {error} = await stripe.confirmPayment({
        elements,
        confirmParams: {
            // Make sure to change this to your payment completion page
            return_url: "http://localhost:8000/api/v1/donations/success/",
        },
    });

    if (error && (error.type === "card_error" || error.type === "validation_error")) {
        showMessage(error.message);
    } else {
        showMessage("An unexpected error occurred.");
    }

    setLoading(false);
}

async function checkStatus() {
    const clientSecret = new URLSearchParams(window.location.search).get(
        "payment_intent_client_secret"
    );

    if (!clientSecret) {
        return;
    }

    const {paymentIntent} = await stripe.retrievePaymentIntent(clientSecret);

    switch (paymentIntent.status) {
        case "succeeded":
            showMessage("Payment succeeded!");
            break;
        case "processing":
            showMessage("Your payment is processing.");
            break;
        case "requires_payment_method":
            showMessage("Your payment was not successful, please try again.");
            break;
        default:
            showMessage("Something went wrong.");
            break;
    }
}

function showMessage(messageText) {
    const messageContainer = document.querySelector("#payment-message");

    messageContainer.classList.remove("hidden");
    messageContainer.textContent = messageText;

    setTimeout(function () {
        messageContainer.classList.add("hidden");
        messageContainer.textContent = "";
    }, 4000);
}

function setLoading(isLoading) {
    if (isLoading) {
        document.querySelector("#submit").disabled = true;
        document.querySelector("#spinner").classList.remove("hidden");
        document.querySelector("#button-text").classList.add("hidden");
    } else {
        document.querySelector("#submit").disabled = false;
        document.querySelector("#spinner").classList.add("hidden");
        document.querySelector("#button-text").classList.remove("hidden");
    }
}