
# 🛒 Terminal-Based E-Commerce System

A Python-based terminal application that allows users to register, log in, browse products, manage a shopping cart, place orders, and view their order history — all within a terminal interface. User data and product information are securely stored using JSON files, with encrypted passwords for authentication.

---

## 🚀 Features

- **User Registration & Login**
  - Secure user registration with encrypted passwords.
  - Authentication system to restrict access to registered users.

- **View Products**
  - Browse available products with pricing and stock information.

- **Shopping Cart**
  - Add items to a cart with stock validation.
  - Place orders and automatically update stock.

- **Order History**
  - View past orders with purchase details.

- **Product Management**
  - Products stored and managed in a JSON file.
  - Easily update product details like stock or price.

- **Secure Storage**
  - User passwords encrypted using `cryptography.fernet`.
  - Key stored separately in a secure storage directory.

---

## 📁 Project Structure

```
.
├── main.py                # Main script to run the system
├── users.json             # Stores user data (encrypted passwords)
├── secure_storage/
│   └── key.key            # Encryption key for password security
├── utils/
│   ├── products.json      # Product data
│   └── helper.py          # Helper functions (e.g., encryption/decryption)
└── README.md              # Project documentation
```

---

## ⚙️ Getting Started

### Prerequisites

- Python 3.6+
- `pip` for package installation

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/<your-username>/Terminal-Based-E-Commerce-System.git
   cd Terminal-Based-E-Commerce-System
   ```

2. **Install Required Packages**
   ```bash
   pip install cryptography
   ```

3. **Run the Application**
   ```bash
   python main.py
   ```

4. **Follow On-Screen Instructions**
   - Register or log in
   - Browse products, manage your cart, and view orders

---

## 🤝 Contributing

We welcome contributions! Follow these steps to contribute:

### Method 1: GitHub UI

```mermaid
flowchart LR
    Fork[Fork the repository] --> Branch[Create a new branch]
    Branch --> Edit[Make changes]
    Edit --> Commit[Commit changes]
    Commit --> PR[Create Pull Request]
```

### Method 2: Local Git

1. **Fork the Repository**
2. **Clone It Locally**
   ```bash
   git clone https://github.com/<your-username>/Terminal-Based-E-Commerce-System.git
   cd Terminal-Based-E-Commerce-System
   ```

3. **Create a Branch**
   ```bash
   git checkout -b your-branch-name
   ```

4. **Make Changes and Commit**
   ```bash
   git add .
   git commit -m "Your descriptive message"
   ```

5. **Push and Create PR**
   ```bash
   git push origin your-branch-name
   ```

   Go to GitHub and create a Pull Request.

---

## ❗ Troubleshooting Merge Conflicts

Conflicts happen when multiple changes occur in the same file. Learn more here:

- [GitHub Docs - About Merge Conflicts](https://docs.github.com/en/github/collaborating-with-pull-requests/addressing-merge-conflicts/about-merge-conflicts)
- [GitHub Docs - Resolve Merge Conflict](https://docs.github.com/en/github/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-on-github)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

> Made with ❤️ for educational and practical learning.
