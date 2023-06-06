# Fansub Workbench
A web-based workbench for fansub groups.

Coded by Huluyou, since May 8, 2023.

v0.0.0.0. Still in development (as of May 2023).

### Frontend

`./client` is the frontend, in Vue.

Dependencies:
* Node.js
* Vue
* axios
* Element UI
* js-md5

Run (on dev):
```
cd client
npm install
npm run dev
```

Build (In production, build the fronten and then run the backend, and no need to run the frontend manually):
```
cd client
npm install
npm build
```

### Backend

`./server` is the backend, in Python with Flask.

Dependencies:
* Python
* Flask
* SQLite

Build:
```
cd server
python -m venv venv
./venv/Scripts/activate
python init.py

```

Run:
```
cd server
./venv/Scripts/activate
flask run
```

Stop:
```
Ctrl + C
deactivate
```

## Todos

* Login. Create new account. Change the password. User name. Quit the group. Kick out of the group.
* User group. User rights. Leader, translator, checker, others.
* Tasks. Timeline. Deadline.
  * Task assignment, reassignment, handover. Accept task.
  * Message. Report. Ping user. Checked.
  * Tag. Category. Category tree.
* File. Upload and download. Diff.
* Schedule.
* Shared database. Lyrics. Corpus. Dictionary. Norms.
  * Auto-detection and remind. Auto-correction.
* Notification.
* User page.
