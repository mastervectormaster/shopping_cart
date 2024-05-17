#### API request types for each functionality using Postman.

### 1. **User Signup**

**Request Type**: POST  
**URL**: `http://127.0.0.1:8000/api/users/signup/`  
**Headers**: None  
**Body**:

```json
{
  "username": "newuser",
  "password": "password123",
  "email": "newuser@example.com"
}
```

### 2. **User Login**

**Request Type**: POST  
**URL**: `http://127.0.0.1:8000/api/token/`  
**Headers**: None  
**Body**:

```json
{
  "username": "newuser",
  "password": "password123"
}
```

**Response**:

```json
{
  "access": "your_jwt_token",
  "refresh": "your_refresh_token"
}
```

### 3. **Change Email**

**Request Type**: POST  
**URL**: `http://127.0.0.1:8000/api/users/change_email/`  
**Headers**:

- `Authorization: Bearer your_jwt_token`
  **Body**:

```json
{
  "email": "newemail@example.com"
}
```

### 4. **Change Password**

**Request Type**: POST  
**URL**: `http://127.0.0.1:8000/api/users/change_password/`  
**Headers**:

- `Authorization: Bearer your_jwt_token`
  **Body**:

```json
{
  "password": "newpassword123"
}
```

### 5. **Add Product (Admin Only)**

**Request Type**: POST  
**URL**: `http://127.0.0.1:8000/api/products/`  
**Headers**:

- `Authorization: Bearer your_jwt_token`
  **Body**:

```json
{
  "name": "Product1",
  "price": "19.99",
  "amount": 10
}
```

### 6. **Update Product (Admin Only)**

**Request Type**: PUT  
**URL**: `http://127.0.0.1:8000/api/products/{product_id}/`  
**Headers**:

- `Authorization: Bearer your_jwt_token`
  **Body**:

```json
{
  "name": "Updated Product1",
  "price": "29.99",
  "amount": 20
}
```

### 7. **Increase Product Amount (Admin Only)**

**Request Type**: POST  
**URL**: `http://127.0.0.1:8000/api/products/{product_id}/increase_amount/`  
**Headers**:

- `Authorization: Bearer your_jwt_token`
  **Body**:

```json
{
  "amount": 5
}
```

### 8. **Create Order**

**Request Type**: POST  
**URL**: `http://127.0.0.1:8000/api/orders/`  
**Headers**:

- `Authorization: Bearer your_jwt_token`
  **Body**:

```json
{
  "products": [1, 2]
}
```

### 9. **Add Product to Order**

**Request Type**: POST  
**URL**: `http://127.0.0.1:8000/api/orders/{order_id}/add_product/`  
**Headers**:

- `Authorization: Bearer your_jwt_token`
  **Body**:

```json
{
  "product_id": 3
}
```

### 10. **Remove Product from Order**

**Request Type**: POST  
**URL**: `http://127.0.0.1:8000/api/orders/{order_id}/remove_product/`  
**Headers**:

- `Authorization: Bearer your_jwt_token`
  **Body**:

```json
{
  "product_id": 2
}
```

### 11. **Cancel Order**

**Request Type**: POST  
**URL**: `http://127.0.0.1:8000/api/orders/{order_id}/cancel/`  
**Headers**:

- `Authorization: Bearer your_jwt_token`

### 12. **Initiate Payment**

**Request Type**: POST  
**URL**: `http://127.0.0.1:8000/api/payments/`  
**Headers**:

- `Authorization: Bearer your_jwt_token`
  **Body**:

```json
{
  "order": 1,
  "amount": "49.98"
}
```

### 13. **Finalize Payment**

**Request Type**: POST  
**URL**: `http://127.0.0.1:8000/api/payments/{payment_id}/finalize/`  
**Headers**:

- `Authorization: Bearer your_jwt_token`

### Summary

1. **User Signup**:

   - `POST /api/users/signup/`

2. **User Login**:

   - `POST /api/token/`

3. **Change Email**:

   - `POST /api/users/change_email/`

4. **Change Password**:

   - `POST /api/users/change_password/`

5. **Add Product (Admin Only)**:

   - `POST /api/products/`

6. **Update Product (Admin Only)**:

   - `PUT /api/products/{product_id}/`

7. **Increase Product Amount (Admin Only)**:

   - `POST /api/products/{product_id}/increase_amount/`

8. **Create Order**:

   - `POST /api/orders/`

9. **Add Product to Order**:

   - `POST /api/orders/{order_id}/add_product/`

10. **Remove Product from Order**:

    - `POST /api/orders/{order_id}/remove_product/`

11. **Cancel Order**:

    - `POST /api/orders/{order_id}/cancel/`

12. **Initiate Payment**:

    - `POST /api/payments/`

13. **Finalize Payment**:
    - `POST /api/payments/{payment_id}/finalize/`

Make sure to replace `{product_id}`, `{order_id}`, and `{payment_id}` with the actual IDs of the products, orders, and payments you're working with. Also, ensure that the `Authorization` header contains a valid JWT token obtained from the login request.

#### Tables

### Product Table

- **Fields**:

  - `name` (CharField): Represents the name of the product. It has a maximum length of 100 characters.
  - `price` (DecimalField): Represents the price of the product, stored as a decimal number with a maximum of 10 digits, including up to 2 decimal places.
  - `amount` (IntegerField): Represents the quantity or stock of the product. It has a default value of 0.

- **Description**:
  - The `Product` table stores information about individual products available for purchase.
  - Each product has a unique name and price.
  - The `amount` field represents the quantity or stock of the product available for purchase.

---

### Order Table

- **Fields**:

  - `user` (ForeignKey to User): Represents the user who placed the order.
  - `products` (ManyToManyField to Product): Represents the products included in the order. Many products can be associated with many orders, and vice versa.
  - `created_at` (DateTimeField): Represents the date and time when the order was created.
  - `status` (CharField): Represents the status of the order. It has a default value of 'pending'.

- **Description**:
  - The `Order` table stores information about orders placed by users.
  - Each order is associated with a single user and can contain multiple products.
  - The `status` field indicates the current status of the order, with a default value of 'pending'.

---

### Payment Table

- **Fields**:

  - `order` (OneToOneField to Order): Represents the order for which the payment is made. Each payment is associated with a single order.
  - `amount` (DecimalField): Represents the amount paid for the order, stored as a decimal number with a maximum of 10 digits, including up to 2 decimal places.
  - `payment_date` (DateTimeField): Represents the date and time when the payment was made.
  - `status` (CharField): Represents the status of the payment. It has a default value of 'initiated'.

- **Description**:
  - The `Payment` table stores information about payments made for orders.
  - Each payment is associated with a single order, indicated by the `order` field.
  - The `amount` field represents the total amount paid for the order.
  - The `status` field indicates the current status of the payment, with a default value of 'initiated'.
