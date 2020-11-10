url=tcp://127.0.0.1:40899
./pubSub server $url server & server=$! && sleep 1
./pubSub client $url client0 & client0=$!
./pubSub client $url client1 & client1=$!
./pubSub client $url client2 & client2=$!
sleep 10
kill $server $client0 $client1 $client2
