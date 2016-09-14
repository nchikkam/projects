package snippets;

import com.sun.org.apache.xerces.internal.parsers.DOMParser;
import org.xml.sax.InputSource;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.URL;
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.ZoneOffset;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;

import org.w3c.dom.*;

public class LatLongCityFinder {
    private String urlTemplate =
            "https://maps.googleapis.com/maps/api/timezone/xml?location=%s&timestamp=1&sensor=false";

    public String [] getCityAndTimeZoneInfo(String latlon) throws Exception{
        String location ="",
                timezone= "";
        try {
            URL url = new URL(String.format(urlTemplate, latlon));
            BufferedReader br = new BufferedReader(new InputStreamReader(url.openStream()));
            String resp = "";
            String strTemp = "";
            while (null != (strTemp = br.readLine())) {
                resp += strTemp;
            }

            DOMParser parser = new DOMParser();
            try {
                parser.parse(new InputSource(new java.io.StringReader(resp)));
                Document doc = parser.getDocument();
                String message = doc.getDocumentElement().getTextContent();
                location = doc.getElementsByTagName("time_zone_id").item(0).getFirstChild().getNodeValue();
                timezone = doc.getElementsByTagName("time_zone_name").item(0).getFirstChild().getNodeValue();
            } catch (Exception e) {}
        } catch (Exception ex) {
            ex.printStackTrace();
        }
        return new String[] {
                location,
                timezone
        };
    }

    public static void main(String[] args) throws Exception{
        LatLongCityFinder d = new LatLongCityFinder();

        String [] inputs = {
                "2016-09-06 00:15:49,52.507629,13.1459606",
                "2016-09-07 02:20:49,15.8766919,80.7769585",
        };

        for (String input: inputs) {
            String[] p = input.split(",");
            String date = p[0];
            String latlon = p[1] + "," + p[2];

            String[] info = d.getCityAndTimeZoneInfo(latlon);

            DateTimeFormatter UTCTimeFormat = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss").withZone(ZoneOffset.UTC);
            ZonedDateTime zonedDateTime = ZonedDateTime.parse(date, UTCTimeFormat);
            String output = input + "," +
                    info[0] + "," +
                    LocalDateTime.ofInstant(zonedDateTime.toInstant(), ZoneId.of(info[0]));

            System.out.println(
                    output
            );
        }
    }
}