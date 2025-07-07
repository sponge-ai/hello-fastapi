export BASE=http://127.0.0.1:8000

curl "$BASE/users?name=amy"
echo

curl "$BASE/users/3"
echo

curl "$BASE/users?name=zach"
echo

curl "$BASE/users/100"
echo

curl $BASE/users
echo

curl -X POST $BASE/users \
    -H "Content-Type: application/json" \
    -d '{ "id": 4, "name": "dre" }'
echo

curl -X POST $BASE/users \
    -H "Content-Type: application/json" \
    -d '{ "id": 5, "name": "eve" }'
echo

curl $BASE/users
echo