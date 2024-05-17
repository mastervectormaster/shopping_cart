# Django App Models Explanation

## Models Overview

This Django app consists of the following models:

1. User
2. Product
3. Order
4. OrderProduct
5. Payment

Additionally, it includes two enumerations for status management:

- OrderStatus
- PaymentStatus

### User

- This is Django's built-in User model.

### Product

- Fields:
  - name: The name of the product (CharField, max length 100).
  - price: The price of the product (DecimalField, max digits 10, decimal places 2).
  - amount: The amount of the product available (DecimalField, max digits 10, decimal places 2, default 0.00).
  

### Order

- Fields:
  - user: A foreign key linking to the User model (ForeignKey, CASCADE).
  - products: A many-to-many relationship with Product through the OrderProduct model.
  - created_at: The date and time when the order was created (DateTimeField, auto_now_add=True).
  - status: The status of the order (CharField, max length 20, default 'pending', choices derived from OrderStatus).



### OrderProduct

- Fields:
  - order: A foreign key linking to the Order model (ForeignKey, CASCADE).
  - product: A foreign key linking to the Product model (ForeignKey, CASCADE).
  - amount: The amount of the product in the order (DecimalField, max digits 10, decimal places 2).

### Payment

- Fields:
  - order: A one-to-one relationship with the Order model (OneToOneField, CASCADE).
  - payment_date: The date and time when the payment was made (DateTimeField, auto_now_add=True).
  - created_at: The date and time when the payment record was created (DateTimeField, default=timezone.now).
  - updated_at: The date and time when the payment record was last updated (DateTimeField, default=timezone.now).
  - status: The status of the payment (CharField, max length 20, default 'initiated', choices derived from PaymentStatus).



## Enums

### OrderStatus (models.TextChoices)
- Choices:
  - INITIATED: Represents the initiated state of an order.
  - PENDING: Represents the pending state of an order.
  - COMPLETED: Represents the completed state of an order.
  - CANCELLED: Represents the cancelled state of an order.

### PaymentStatus (models.TextChoices)
- Choices:
  - INITIATED: Represents the initiated state of a payment.
  - SUCCESS: Represents a successful payment.
  - FAILED: Represents a failed payment.

## Model Relationships

1. Product and Order:
   - A many-to-many relationship facilitated by the OrderProduct model.
   - An order can contain multiple products, and a product can belong to multiple orders.

2. Order and User:
   - A many-to-one relationship with the User model.
   - An order is placed by a single user.

3. Order and OrderProduct:
   - A one-to-many relationship.
   - An order can have multiple entries in the OrderProduct model, each linking to a product.

4. Order and Payment:
   - A one-to-one relationship with the Payment model.
   - Each order can have only one associated payment.

## Behavior and Workflow

1. Placing an Order:
   - When a user places an order, an entry is created in the Order model linking the user to the order.
   - Products are added to the order through the OrderProduct model.

2. Making a Payment:
   - When a payment is initiated, a Payment entry is created linked to the respective Order.
   - The status of the payment is updated based on the payment process outcome.

3. Order Status Management:
   - The status of an order is managed using the OrderStatus enumeration, allowing it to be updated as the order progresses through different stages (initiated, pending, completed, cancelled).
4. Payment Status Management:
   - The status of a payment is managed using the PaymentStatus enumeration, reflecting the current state of the payment (initiated, success, failed).

By structuring the models and relationships this way, the app provides a clear and organized way to manage products, orders, and payments, ensuring data integrity and ease of access.