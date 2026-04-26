sudo apt update
sudo apt install couchdb -y
sudo service couchdb start
curl -X PUT http://127.0.0.1:5984/studentdb

curl -X POST http://127.0.0.1:5984/studentdb -H "Content-Type: application/json" -d '{"SRN":"1","Sname":"Rahul","Degree":"BCA","Sem":5,"CGPA":7.2}'
curl -X POST http://127.0.0.1:5984/studentdb -H "Content-Type: application/json" -d '{"SRN":"2","Sname":"Anita","Degree":"BCA","Sem":3,"CGPA":6.8}'
curl -X POST http://127.0.0.1:5984/studentdb -H "Content-Type: application/json" -d '{"SRN":"3","Sname":"Vikram","Degree":"BSc","Sem":2,"CGPA":8.1}'
curl -X POST http://127.0.0.1:5984/studentdb -H "Content-Type: application/json" -d '{"SRN":"4","Sname":"Priya","Degree":"BCA","Sem":6,"CGPA":7.4}'
curl -X POST http://127.0.0.1:5984/studentdb -H "Content-Type: application/json" -d '{"SRN":"5","Sname":"Kiran","Degree":"BCom","Sem":4,"CGPA":6.2}'
curl -X POST http://127.0.0.1:5984/studentdb -H "Content-Type: application/json" -d '{"SRN":"6","Sname":"Sneha","Degree":"BCA","Sem":1,"CGPA":7.0}'
curl -X POST http://127.0.0.1:5984/studentdb -H "Content-Type: application/json" -d '{"SRN":"7","Sname":"Arjun","Degree":"BCA","Sem":5,"CGPA":6.5}'

curl -X GET http://127.0.0.1:5984/studentdb/_all_docs?include_docs=true

curl -X POST http://127.0.0.1:5984/studentdb/_find -H "Content-Type: application/json" -d '{"selector":{"Degree":"BCA"}}'

curl -X POST http://127.0.0.1:5984/studentdb/_find -H "Content-Type: application/json" -d '{"selector":{},"sort":[{"Sname":"asc"}]}'

curl -X POST http://127.0.0.1:5984/studentdb/_find -H "Content-Type: application/json" -d '{"selector":{},"limit":5}'

curl -X POST http://127.0.0.1:5984/studentdb/_find -H "Content-Type: application/json" -d '{"selector":{},"skip":4,"limit":3}'

curl -X POST http://127.0.0.1:5984/studentdb/_find -H "Content-Type: application/json" -d '{"selector":{"Sname":"Rahul"},"fields":["Degree"]}'

curl -X POST http://127.0.0.1:5984/studentdb/_find -H "Content-Type: application/json" -d '{"selector":{},"sort":[{"CGPA":"desc"}],"skip":4,"limit":3}'

curl -X POST http://127.0.0.1:5984/studentdb/_find -H "Content-Type: application/json" -d '{"selector":{"Degree":"BCA","CGPA":{"$gt":6,"$lt":7.5}}}'
