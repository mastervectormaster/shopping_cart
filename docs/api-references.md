# API References.

### 1. **User Signup**

**Http Method**: POST  
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

**Http Method**: POST  
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

**Http Method**: POST  
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

**Http Method**: POST  
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

**Http Method**: POST  
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

**Http Method**: PUT  
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

**Http Method**: POST  
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

**Http Method**: POST  
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

**Http Method**: POST  
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

**Http Method**: POST  
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

**Http Method**: POST  
**URL**: `http://127.0.0.1:8000/api/orders/{order_id}/cancel/`  
**Headers**:

- `Authorization: Bearer your_jwt_token`

### 12. **Initiate Payment**

**Http Method**: POST  
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

**Http Method**: POST  
**URL**: `http://127.0.0.1:8000/api/payments/{payment_id}/finalize/`  
**Headers**: None

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
