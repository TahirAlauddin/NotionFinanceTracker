
# Notion-Based Personal Finance Tracker

A web application for managing personal finances by syncing data with a Notion database. The app provides financial insights and visualizations, and supports CRUD operations for financial records, budget management, and category-wise expense tracking.

## Table of Contents
1. [Project Scope](#project-scope)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Getting Started](#getting-started)
5. [Usage](#usage)
6. [Contributing](#contributing)
7. [License](#license)

## Project Scope
The Notion-Based Personal Finance Tracker allows users to:
- Synchronize financial data from a Notion database.
- Manage financial records with create, read, update, and delete (CRUD) operations.
- View category-wise expense breakdowns and monthly financial summaries.
- Set budget limits and receive notifications when limits are exceeded.

This project aims to integrate Notion into personal finance tracking to provide a flexible, cloud-based solution.

## Features
- **User Authentication**: Secure login and registration system.
- **Notion API Integration**: Syncs data with a Notion database.
- **Financial Data Management**: Manage records directly in the app.
- **Visualizations**: Displays charts for expense tracking.
- **Budget Management**: Allows users to set budget limits and receive notifications.
- **Responsive Design**: Bootstrap-powered, mobile-friendly interface.

## Technologies Used
- **Backend**: Django
- **Frontend**: Django Templates, Bootstrap, Chart.js
- **Database**: SQLite (for development), PostgreSQL (optional for production)
- **APIs**: Notion API
- **Deployment**: [Platform of your choice, e.g., Heroku, AWS, or DigitalOcean]

## Getting Started

### Prerequisites
- Python 3.7+
- Notion account and integration set up ([How to set up Notion Integration](https://www.notion.so/my-integrations))

### Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/TahirAlauddin/NotionFinanceTracker.git
   cd NotionFinanceTracker
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Create a `.env` file in the project root with the following variables:
     ```plaintext
     NOTION_API_KEY=your_notion_integration_token
     NOTION_DATABASE_ID=your_database_id
     ```

5. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser** for admin access:
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

8. Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser to access the app.

## Usage
1. **Sign up** for an account or log in as an admin.
2. **Sync data** from Notion by navigating to `/sync/`.
3. **Manage financial records** through the dashboard.
4. **View visualizations** for insights on spending habits.

### Developer Guide
To make changes or add features, please fork the repository and create a pull request.

1. **Fork the repository** and clone your fork.
2. Create a new branch for your changes:
   ```bash
   git checkout -b feature/new-feature
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/new-feature
   ```
5. **Open a Pull Request** on the original repository.

## Contributing
We welcome contributions! Please check out the [issues](https://github.com/your-username/notion-finance-tracker/issues) and open a pull request to add features, fix bugs, or improve documentation.

### Code of Conduct
Please follow the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/0/code_of_conduct/).

## License
This project is licensed under the MIT License. See [LICENSE](./LICENSE) for more information.


**Happy coding!**

