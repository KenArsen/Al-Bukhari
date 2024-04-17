const stripe = Stripe('sk_test_51OjhrkFtBaQUT0WNQVkFceEHafIJrYqlHd5YeTiV3X7IyAuAiWvbcmPfGuevV6bmL34x4InUGc2wscMv5MazJCI500isHgFW2l');
const options = {
    mode: 'payment',
    amount: 1099,
    currency: 'usd',
    // Customizable with appearance API.
    appearance: {/*...*/},
};

// Set up Stripe.js and Elements to use in checkout form
const elements = stripe.elements(options);

const expressCheckoutElement = elements.create('expressCheckout');
expressCheckoutElement.mount('#express-checkout-element');

