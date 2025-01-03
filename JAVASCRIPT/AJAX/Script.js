
//GET
async function getProducts(){
  let URL =  'https://crud.teamrabbil.com/api/v1/ReadProduct';
  let response = await axios.get(URL);
  let products = response.data['data'];
  products.forEach(item => {
    document.getElementById('productList').innerHTML+=`
    <tr>
        <td>${item['ProductName']}</td>
        <td>${item['ProductCode']}</td>
        <td>${item['UnitPrice']}</td>
        <td>${item['Qty']}</td>
        <td>${item['TotalPrice']}</td>
        <td> <button onclick="deleteProduct('${item['_id']}')">Delete</button></td>
        <td> <button onclick="goToUpdate('${item['_id']}')">Edit</button></td>
    </tr>
    `
  });
  
}
getProducts();

//Delete products

async function deleteProduct(id){
  let URL = `https://crud.teamrabbil.com/api/v1/DeleteProduct/${id}`;
  let response = await axios.get(URL);
  document.getElementById('productList').innerHTML = 'Deleted this product';
  getProducts();
}
function goToUpdate(id) {
  window.location.href = `update.html?id=${id}`;
  
}