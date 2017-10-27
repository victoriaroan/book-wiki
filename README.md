# book-wiki
A structured wiki with markdown support.

## Setting up the dev environment

1. Install git (https://git-scm.com/), python 3.6.x (https://www.python.org/), and nodejs 8.8.x (https://nodejs.org/)
2. Install less css via node (http://lesscss.org)
3. Clone the project (`git clone https://github.com/victoriaroan/book-wiki.git`)
4. Move to server folder and set up a virtualenv (https://virtualenv.pypa.io/en/stable/)
5. Install requirements (`pip install -r requirements.txt`)
6. Copy bookwiki.settings.local_example to bookwiki.settings.local and update as needed.
7. Migrate database (`python manage.py migrate`)
8. Run development server (`python manage.py runserver`)
