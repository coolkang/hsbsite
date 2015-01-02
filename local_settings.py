
DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "c69c2ab2-9c58-4013-94a6-004052f2583d40029806-a510-4c48-a874-20e9245f55f70394cbad-48b5-4945-9499-96c303d771e6"
NEVERCACHE_KEY = "9fb86bbb-51a2-494d-b6ca-1065c0f1f58ee6d757ec-85b0-4f66-9003-ff57c8a3d9d8b37a8b11-19a9-4c03-8596-ba129af542ed"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.mysql",
        # DB name or path to database file if using sqlite3.
        "NAME": "hsbsite",
        # Not used with sqlite3.
        "USER": "dbuser",
        # Not used with sqlite3.
        "PASSWORD": "dbuser",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
