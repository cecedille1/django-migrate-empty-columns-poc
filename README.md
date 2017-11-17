When migrating a table in sqlite, a temp table may be created and values from
the source table are inserted into the new table. This transfert may have no
column if there is only a manual primary key. (Happends with pointer tables)

```
pip install django
django-admin migrate --pythonpath=. --settings=app.settings

Operations to perform:
  Apply all migrations: app
Running migrations:
  Applying app.0002_auto_20171117_1131...Traceback (most recent call last):
  File ".envs/py3/lib/python3.6/site-packages/django/db/backends/utils.py", line 65, in execute
    return self.cursor.execute(sql, params)
  File ".envs/py3/lib/python3.6/site-packages/django/db/backends/sqlite3/base.py", line 328, in execute
    return Database.Cursor.execute(self, query, params)
sqlite3.OperationalError: near ")": syntax error
```

The SQL is generated with an empty `()` in the INSERT clause.

```
BEGIN;
--
-- Remove field f1 from poc
--
ALTER TABLE "app_poc" RENAME TO "app_poc__old";
CREATE TABLE "app_poc" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT);
INSERT INTO "app_poc" () SELECT  FROM "app_poc__old";
DROP TABLE "app_poc__old";
--
-- Add field f2 to poc
--
ALTER TABLE "app_poc" RENAME TO "app_poc__old";
CREATE TABLE "app_poc" ("f2" integer NOT NULL PRIMARY KEY);
INSERT INTO "app_poc" ("f2") SELECT 1 FROM "app_poc__old";
DROP TABLE "app_poc__old";
COMMIT;
```
