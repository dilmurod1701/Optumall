## How to install
1. Clone this project
2. Install requirements.txt
3. To install requirements.txt run on the terminal pip install -r requirements.txt

## How to use this project
1. only GET request http://127.0.0.1:8000/api/products - Returns all products
2. only GET/POST request http://127.0.0.1:8000/api/new - Endpoint to add new product
3. only PUT/PATCH request http://127.0.0.1:8000/api/id/update - Updates the data of the product with <id>
4. only GET request http://127.0.0.1:8000/api/category<product> - Returns results by product category. For example, .../category/shoes returns only shoes.
5. only GET request http://127.0.0.1:8000/api/search?product=<title> - Searches for the product by title
6. only DELETE request http://127.0.0.1:8000/api/product/id/delete - Deletes a product with <id>
7. only GET request http://127.0.0.1:8000/api/user/<username> - Any user who has logged in can go to the profile using the username
8. only PUT/PATCH request http://127.0.0.1:8000/api/user/<username>/update - Users can change information about themselves
