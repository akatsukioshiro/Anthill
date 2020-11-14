#include "WiFi.h"
#include "ESPAsyncWebServer.h"
#include <HTTPClient.h>

String aray[100]={},aray2[100]={};

/*Put your SSID & Password*/
const char* ssid = "Aswathy";  // Enter SSID here
const char* password = "viju@1967";  //Enter Password here

#define ONBOARD_LED  2

AsyncWebServer server(80);

void notFound(AsyncWebServerRequest *request) {
    request->send(404, "text/plain", "Not found");
}

String jsoner(String aray[100], String aray2[100])
{
String json_d="{";
json_d+="'wifi_names':['";
for(int i=0; i<=99;i++)
{
  json_d+=(aray[i]);
  json_d+="','";
}
json_d+="'],'wifi_ids':['";
for(int i=0; i<=99;i++)
{
  json_d+=(aray2[i]);
  json_d+="','";
}
json_d+="']}";

return json_d;
}


void setup()
{
  Serial.begin(115200);
  WiFi.mode(WIFI_AP_STA);
  pinMode(ONBOARD_LED,OUTPUT);
  
  // Connect to Wi-Fi network with SSID and password
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  // Print local IP address and start web server
  Serial.println("");
  Serial.println("WiFi connected.");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  int n = WiFi.scanNetworks();
    Serial.println("scan done");
    if (n == 0) {
        Serial.println("no networks found");
    } else {
        Serial.print(n);
        Serial.println(" networks found");
        for (int i = 0; i < n; ++i) {
            // Print SSID and RSSI for each network found
            Serial.print(i + 1);
            Serial.print(": ");
            Serial.print(WiFi.SSID(i));
            Serial.print(" (");
            Serial.print(WiFi.RSSI(i));
            Serial.print(")");
            Serial.println((WiFi.encryptionType(i) == WIFI_AUTH_OPEN)?" ":"*");
            
            delay(10);
            aray[i]=(WiFi.SSID(i));
            aray2[i]=(WiFi.RSSI(i));
          //  if((WiFi.RSSI(i))<(-90)){
              //digitalWrite(ONBOARD_LED,HIGH);}
//              else{
           //digitalWrite(ONBOARD_LED,LOW);  }
        }
    }
  server.on("/", HTTP_GET, [](AsyncWebServerRequest *request){
    request->send_P(200, "text/html", jsoner(aray, aray2).c_str());
  });
  server.onNotFound(notFound);
  server.begin();
  HTTPClient http;
  http.begin("http://192.168.1.10:5001/begin_loop?device=esp32");
  int httpCode = http.GET();                                        //Make the request
 
    if (httpCode > 0) { //Check for the returning code
 
        //String payload = http.getString();
        Serial.println(httpCode);
        Serial.println("Triggered");
      }
 
    else {
      Serial.println("Error on HTTP request");
    }
 
    http.end();
}

String light(uint8_t Volt,String msg)
{
  digitalWrite(ONBOARD_LED,Volt); 
  return msg;
}

void test()
{
  int n = WiFi.scanNetworks();
  Serial.println("scan done");
  if (n == 0) 
  {
    Serial.println("no networks found");
  } 
  else 
  {
     Serial.print(n);
     Serial.println(" networks found");
     for (int i = 0; i < n; ++i) 
     {
       // Print SSID and RSSI for each network found
       delay(10);
       aray[i]=(WiFi.SSID(i));
       aray2[i]=(WiFi.RSSI(i));
            
      }
   }
  server.on("/", HTTP_GET, [](AsyncWebServerRequest *request){
    request->send_P(200, "text/html", jsoner(aray, aray2).c_str());
  });
  server.on("/OFF", HTTP_GET, [](AsyncWebServerRequest *request){
    request->send_P(200, "text/html", light(LOW,"Light is Switched OFF").c_str());
  });
  server.on("/ON", HTTP_GET, [](AsyncWebServerRequest *request){
    request->send_P(200, "text/html", light(HIGH,"Light is Switched ON").c_str());
  });
  server.onNotFound(notFound);
}

void loop()
{
  test();
  delay(50000);
}
