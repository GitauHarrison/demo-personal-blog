console.log("Sanity check!") // this is just a printout

fetch("/config")
.then((result) => { return result.json(); })
.then((data) => {
  // Initialize Stripe.js
  const stripe = Stripe(data.publicKey);
});