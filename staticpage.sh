#!/bin/sh
lxterminal --command='./ngrokstart.sh'
sleep 3
curl 127.0.0.1:4040/inspect/http -o web.txt
rm index.html
python CNAME.py

git add --all
git commit -m 'updating cname'
git push