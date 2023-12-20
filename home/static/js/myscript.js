
$('.plus-cart').click(function () {
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]
    // console.log(id)
    $.ajax({
        type: "GET",
        url: "/pluscart",
        data: {
            prod_id: id
        },
        success: function (data) {
            eml.innerText = data.quantity
            document.getElementById("amount").innerText = data.amount
            document.getElementById("totalamount").innerText = data.totalamount
            
        }
    })
})

$('.minus-cart').click(function () {
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]
    // console.log(id)
    $.ajax({
        type: "GET",
        url: "/minuscart",
        data: {
            prod_id: id
        },
        success: function (data) {
            eml.innerText = data.quantity
            document.getElementById("amount").innerText = data.amount
            document.getElementById("totalamount").innerText = data.totalamount
            
        }
    })
})

$('.remove-cart').click(function () {
    var id = $(this).attr("pid").toString();
    var eml = this
    // console.log(id)
    $.ajax({
        type: "GET",
        url: "/removecart",
        data: {
            prod_id: id
        },
        success: function (data) {
            
            document.getElementById("amount").innerText = data.amount
            document.getElementById("totalamount").innerText = data.totalamount
            eml.parentNode.parentNode.parentNode.parentNode.remove()
            
        }
    })
})


// Function to show the cart info div on hover
function showCartInfo() {
    const cartInfo = document.getElementById('cart-info');
    cartInfo.style.display = 'block';
}

// Function to hide the cart info div when not hovered
function hideCartInfo() {
    const cartInfo = document.getElementById('cart-info');
    cartInfo.style.display = 'none';
}
