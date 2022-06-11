import paho.mqtt.client as mqtt

#Publisher
client = mqtt.Client()
client.connect("localhost",1883,60)
client.publish("colombia/valle/cali", "{temperatura:26, estado:'ok'}");
client.disconnect();