function loadProduct() {
  let minPrice = $("#minPrice").val();
  let maxPrice = $("#maxPrice").val();
  let sorting = $("#sorting").val();
  let brand = $(".brandInputBox:checked");
  let category = $(".categoryInputBox:checked");
  let productType = $(".productTypeInputBox:checked");
  let seller = $(".sellerInputBox:checked");
  let warranty = $(".warrantyInputBox:checked");
  if (minPrice == "") {
    minPrice = $("#minHiddenPrice").val();
  }
  if (maxPrice == "") {
    maxPrice = $("#maxHiddenPrice").val();
  }

  let brand_ids = make_list(brand);
  let category_ids = make_list(category);
  let productType_ids = make_list(productType);
  let seller_ids = make_list(seller);
  let warranty_ids = make_list(warranty);

  let data = {
    min_price: minPrice,
    max_price: maxPrice,
    brand: brand_ids,
    category: category_ids,
    product_type: productType_ids,
    sellers: seller_ids,
    warranty: warranty_ids,
    sorting: sorting,
  };
  send_request(data);
}

function make_list(element) {
  let items = [];
  if (element.length > 0) {
    for (let i = 0; i < element.length; i++) {
      items.push(element[i].value);
    }
  }
  return items;
}
$(document).on("submit", "#rangeForm", function (e) {
  e.preventDefault();
  loadProduct();
});
$(document).on("click", ".filterItem", function () {
  loadProduct();
});

$("#sorting").on("change", function () {
  loadProduct();
});
let spinner = `
<div class="row">
    <div class="col-md-8 mx-auto" style="margin-top:100px">
        <div class="spinner-border" role="status">
                 <span class="visually-hidden">Loading...</span>
         </div>
  
     </div>
</div>`;

let not_found=`<div class="row">
<div class="col-md-12 mx-auto">
       <p class="text-muted ml-3"> Product not found </p>
   
</div>
</div>`

function send_request(data) {
  let productListBox = $(".productListBox").html("");
  productListBox.html(spinner);
  let url = "/products/filter/";
  $.ajax({
    url: url,
    method: "GET",
    data: data,
    success: function (res) {
      let data = res.data;
      productListBox.html(null)
      if(data.length==0){
        productListBox.html(not_found)
      }else{
        data.forEach((element) => {
            productListBox.append(productCard(element));
          });
      }
      $(".showCount").html(res.count)

    },
  });
}

function productCard(data) {
  let element = `
    <div class="col-md-3 mb-2">
    <div class="card cardOverride">
        <img src="${data.image}" class="${data.title} loading..." alt="...">
        <div class="card-body">
        <p class="p-0 m-0">${data.title} 
        </p>
       <div>
        <span  style="font-size:10px;font-weight: bold;" class="text-muted"> Category:
          <span  class="text-muted text-uppercase" style="font-weight: normal;">(${data.category})</span>
      </span>
       </div>
       <div>
       <span  style="font-size:10px;font-weight: bold;" class="text-muted"> Brand:
         <span  class="text-muted text-uppercase" style="font-weight: normal;">(${data.brand})</span>
     </span>
      </div>
          <div class="d-flex">
            ${
              data.discount_price
                ? `
            <p style="color:orangered">BDT-${data.discount_price}</p>
            <p style="color:gray;margin-left:10px;font-weight: 300;"><strike>BDT-${data.price}</strike></p>
            `
                : ` <p style="color:orangered">BDT-${data.price}</p>`
            }
           
          </div>
          <div class="d-flex" style="justify-content: space-between;">
            <button class="btn text-uppercase" style="font-size:9px;background:orangered;color:white">
                 buy now
            </button>
            <button class="btn btn-dark text-uppercase" style="font-size:9px">
                add To card
           </button>
          </div>
        </div>
      </div>
 </div>
    `;
  return element;
}
