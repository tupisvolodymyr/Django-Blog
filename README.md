## System Design — Journalistic Blog Platform 
A minimalist, brutalist-inspired web platform for publishing articles, built with Django. The project focuses on clean typography, a monochrome aesthetic, and a high-quality reading experience.

### 🖋 Design Philosophy
* __Monochrome Aesthetic:__ Exclusively uses black, white, and shades of gray to maintain a professional look.

* __Typography:__ Powered by the Inter font family, focusing on bold headings and generous line spacing.

* __Grid System:__ A layout inspired by modern architecture and design magazines, utilizing hard borders and structured cells.

### 🛠 Tech Stack
* __Backend:__ Django 4.x / 5.x

* __Frontend:__ HTML5, CSS3 (Custom Brutalist CSS), Bootstrap 5 (for base grid)

* __Database:__ SQLite (default for development)

* __Media:__ Pillow (for image processing and monochrome filters)

# 🚀 Quick Start

### __1. Clone and Prepare__ ###
Ensure you have Python 3.10+ installed on your system.
```bash
# Clone the repository
git clone https://github.com/yourusername/system-design-blog.git
cd system-design-blog

# Create a virtual environment
python -m venv venv

# Activate it
# For Windows:
venv\Scripts\activate
# For macOS/Linux:
source venv/bin/activate
```

### __2. Install Dependencies__ ###
The project includes a __requirements.txt__ file containing all necessary libraries (Django, Pillow, etc.).
```bash
pip install -r requirements.txt
```

### __3. Setup the Database__ ###
Run migrations to create the database schema.
```bash
python manage.py migrate
```

### __4. Create an Admin Account__ ###
To access the dashboard and create categories/posts, set up a superuser:
```bash
python manage.py createsuperuser
```
### __5. Launch the Server__ ###
```bash
python manage.py runserver
```
The project will be available at: __http://127.0.0.1:8000/__

# 📁 Template Structure #
### The project uses a hierarchical template system: ###

* __base.html:__ The core framework containing the navigation and global styles.

* __blog/post_list.html:__ The homepage featuring the post grid with author and date metadata.

* __blog/post_detail.html:__ Detailed view for individual articles.

* __blog/user_dashboard.html:__ A private management panel for authors to manage their content.

* __registration/:__ Contains the login, registration, and deletion confirmation pages.

# 🛡 Security & Permissions #
* __Authorization:__ Post creation and editing are restricted to authenticated users via the @login_required decorator.

* __Author Tracking:__ Every post is automatically linked to the user account that created it.

* __Destructive Actions:__ A custom confirmation page is implemented for deletions to prevent accidental data loss, featuring dark red warning accents.

# 📄 License #
This project was developed for educational and creative purposes.

Developed in 2026. system design • architecture • content.
