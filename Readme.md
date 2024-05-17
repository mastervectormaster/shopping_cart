#### API request types for each functionality using Postman.

### 1. **User Signup**

**Http Method Type**: POST  
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

**Http Method Type**: POST  
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

**Http Method Type**: POST  
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

**Http Method Type**: POST  
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

**Http Method Type**: POST  
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

**Http Method Type**: PUT  
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

**Http Method Type**: POST  
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

**Http Method Type**: POST  
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

**Http Method Type**: POST  
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

**Http Method Type**: POST  
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

**Http Method Type**: POST  
**URL**: `http://127.0.0.1:8000/api/orders/{order_id}/cancel/`  
**Headers**:

- `Authorization: Bearer your_jwt_token`

### 12. **Initiate Payment**

**Http Method Type**: POST  
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

**Http Method Type**: POST  
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

#### Detailed description about the whole development process

### 1. Designing the Data Model:

- **Identified Main Entities:**

  - Recognized the core entities necessary for an e-commerce platform, including Products, Orders, Payments, and Users, based on the requirements.

- **Determined Relationships:**

  - Established the relationships between entities, such as a many-to-many relationship between Products and Orders to allow multiple products in one order, and a one-to-one relationship between Orders and Payments to ensure each order has a corresponding payment.

- **Defined Fields:**

  - Specified the fields and attributes for each entity, considering the information needed to support the business requirements. For example, for Products, fields like Name, Price, and Amount were defined.

- **Leveraged Django ORM:**
  - Utilized Django's Object-Relational Mapping (ORM) to define the data model, taking advantage of Django's built-in features for managing database relationships, ensuring data integrity, and simplifying database operations.

### 2. Integrating Business Logic:

- **Implemented Logic:**

  - Developed the necessary business logic to support key operations such as creating orders, updating product quantities, and processing payments. This logic was designed to meet the functional requirements of the e-commerce platform and ensure smooth operation.

- **Ensured Data Consistency:**

  - Implemented checks and constraints within the business logic to ensure data consistency and validation. For example, when creating an order, checks were performed to verify the availability of products and update their quantities accordingly.

- **Authentication and Access Control:**
  - Integrated Django's authentication system to authenticate users and control access to various parts of the application based on user roles and permissions. This included restricting access to certain endpoints and operations to authenticated users only.

### 3. Implementing the API:

- **Designed CRUD Endpoints:**

  - Defined API endpoints for performing CRUD (Create, Read, Update, Delete) operations on resources such as Products, Orders, and Payments using Django REST Framework (DRF).

- **Serialization and Deserialization:**

  - Utilized DRF serializers to convert data between JSON format and Python objects, ensuring smooth data exchange between the client and the server.

- **Viewsets and Routers:**

  - Used DRF's viewsets and routers to automatically generate URL patterns for CRUD operations on resources, reducing boilerplate code and simplifying API development.

- **Authentication and Permissions:**
  - Configured authentication and permissions settings within the API to enforce access control and ensure that only authorized users can access certain endpoints or perform specific actions.

### 4. Challenges Faced and Decisions Made:

- **Complex Relationships:**

  - Faced challenges in managing complex relationships between entities, such as many-to-many and one-to-one relationships. Decisions were made to leverage Django's ORM capabilities and DRF serializers to handle these relationships effectively.

- **Data Integrity and Security:**

  - Addressed challenges related to ensuring data integrity and security, particularly when handling sensitive information such as user authentication tokens and payment details. Decisions were made to implement best practices, including encryption, token-based authentication, and role-based access control.

- **Performance Optimization:**

  - Focused on optimizing the performance of the API, especially in scenarios involving large datasets or high concurrency. This involved implementing caching mechanisms, pagination, and optimizing database queries to improve response times and scalability.
