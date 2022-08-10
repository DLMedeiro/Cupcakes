// baseHtml = "http://127.0.0.1:5000"

function cupcakeHtml(cupcake) {

    return `
        <div data-cupcake-id = ${cupcake.id}> 
            <li>
                ${cupcake.flavor} | ${cupcake.size} | ${cupcake.rating}
                <button class = "delete-button">X</button>
            </li>
            <img class = "Cupcake-img" src = "${cupcake.image}">
        </div>
    `;

}

async function getCupcakes() {
    const response = await axios.get("http://127.0.0.1:5000/api/cupcakes");

    for (let cupcake of response.data.cupcakes) {
        let lineItem = $(cupcakeHtml(cupcake));
        $("#cupcake-list").append(lineItem);
    }
    // console.log("getCupcake resp= ", response); $("#cupcake-list").html(response.data.cupcakes);
}

// $("#getlist").on("click", getCupcakes);

$("#newCupcakeForm").on("submit", async function (e){
    e.preventDefault();
    let flavor = $("#flavor").val();
    let size = $("#size").val();
    let rating = $("#rating").val();
    let image = $("#image").val();
    
    const newCupcakeResponse = await axios.post("http://127.0.0.1:5000/api/cupcakes", {flavor, size, rating, image});
    
    let newCupcake = $(cupcakeHtml(newCupcakeResponse.data.cupcake));
    $("#cupcake-list").append(newCupcake);
    $("#submitNewCupcake").trigger("reset");
});

$("#cupcake-list").on("click", ".delete-button", async function (e){
    e.preventDefault();
    let $cupcake = $(e.target).closest("div");
    let cupcakeId = $cupcake.attr("data-cupcake-id");

    await axios.delete(`http://127.0.0.1:5000/api/cupcakes/${cupcakeId}`)
    $cupcake.remove();
});

$(getCupcakes);